import base64


def process_audio_file(path):
    with open(path, 'rb') as file:
        audio = file.read()
    return base64.b64encode(audio).decode('utf-8')