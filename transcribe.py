import os
import openai
import logging


logger = logging.getLogger(__name__)
openai.api_key = os.getenv('OPENAI_API_KEY')


def transcribe_from_audio_file(path):
    logger.debug('opening %s', path)
    audio_file = open(path, 'rb')
    logger.debug('transcribing %s', path)
    transcription = openai.Audio.transcribe('whisper-1', audio_file)
    logger.debug(transcription)
    return transcription['text']
