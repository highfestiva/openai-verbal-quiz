import os
import openai


openai.api_key = os.getenv('OPENAI_API_KEY')


def transcribe_from_audio_file(path):
    audio_file = open(path, 'rb')
    transcription = openai.Audio.transcribe('whisper-1', audio_file)
    return transcription['text']
