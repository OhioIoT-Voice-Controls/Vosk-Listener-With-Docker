

FROM python:3.11-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    curl unzip libportaudio2 libatomic1 \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir vosk sounddevice

WORKDIR /app

ARG MODEL=vosk-model-small-en-us-0.15

RUN curl -sL -o /tmp/model.zip \
    "https://alphacephei.com/vosk/models/${MODEL}.zip" \
    && unzip -q /tmp/model.zip -d /app \
    && rm /tmp/model.zip

COPY listener.py .

CMD ["python", "-u", "listener.py"]