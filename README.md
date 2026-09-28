# Vosk Listener (with Docker)<a href="https://www.ohioiot.com"><img src="https://www.ohioiot.com/logo_150.jpg" width="40" ></a>
#### [(back to the Voice Controls organization page)](https://github.com/OhioIoT-Voice-Controls)

This code was generated in the linked YouTube video about making a speech-to-text listener on a Raspberry Pi with a USB mic.  See more at: [Offline Voice Control](https://youtu.be/oKQ9xvL7ptM)

When I made the video, I manually downloaded the Vosk library and then used it with this line: 
```
model = Model("vosk-model-small-en-us-0.15")
```
It turns out that if you use the following line instead, the library will download automatically:
```
model = Model(model_name="vosk-model-small-en-us-0.15")
```
Either make the change above in your code before you run, or do something like:
```
wget https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
unzip vosk-model-small-en-us-0.15.zip
```

Installation Steps (works on Git Bash on Windows):
```
git clone https://github.com/OhioIoT-Voice-Controls/Vosk-Listener.git vosk-listener
cd vosk-listener
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
./+run
```

For the same version of this code, but without the Docker files, check out out [Vosk Listener](https://github.com/OhioIoT-Voice-Controls/Vosk-Listener).

## About
<a href="https://www.ohioiot.com"><img src="https://www.ohioiot.com/logo_150.jpg" width="40" ></a>

*OhioIoT is an IoT platform designed for small-scale IoT projects.  For more, check out our website at [www.OhioIoT.com](https://www.ohioiot.com).*
