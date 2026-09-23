
# --- process lifecycle -----------------------------
import signal
import sys

# --- audio capture ---------------------------------
import queue
import sounddevice as sd

# --- speech recognition ----------------------------
import json
from vosk import Model, KaldiRecognizer, SetLogLevel

########################
COMMANDS = [
    "lights on",
    "lights off",
    "turn the temperature up",
    "turn the temperature down"
]
########################

# --- process lifecycle ----------------------------
signal.signal(signal.SIGTERM, lambda *_: sys.exit(0))

# --- audio capture --------------------------------
mic_rate = int(sd.query_devices(kind="input")["default_samplerate"])
audio = queue.Queue()
def on_audio(data, frames, time, status):
    audio.put(bytes(data))

# --- speech recognition ---------------------------
SetLogLevel(-1)
model = Model("vosk-model-small-en-us-0.15")
grammar = json.dumps(COMMANDS + ["[unk]"])
recognizer = KaldiRecognizer(model, mic_rate, grammar)

# --- listener -------------------------------------
with sd.RawInputStream(samplerate=mic_rate,
                       blocksize=mic_rate // 2,
                       dtype="int16", channels=1,
                       callback=on_audio):
    while True:
        chunk = audio.get()
        if not recognizer.AcceptWaveform(chunk):
            continue
        text = json.loads(recognizer.Result())["text"]
        text = text.replace("[unk]", "").strip()
        if not text:
            continue
        print("heard:", text)
        for phrase in COMMANDS:
            if phrase in text:
                print("WE GOT A COMMAND:", phrase)
                
                break