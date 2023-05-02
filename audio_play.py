import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
from gtts import gTTS
import logging
import pygame as pg


logger = logging.getLogger(__name__)


def say(text, tmp_filename='speech.mp3'):
    text2mp3(text, tmp_filename)
    play_mp3(tmp_filename)


def text2mp3(text, path):
    logger.debug('converting "%s" to speech', text)
    tts = gTTS(text=text, lang='en')
    logger.debug('saving speech to "%s"', path)
    tts.save(path)


def play_mp3(path):
    logger.debug('playing speech in %s', path)
    pg.mixer.init()
    pg.mixer.music.load(path)
    pg.mixer.music.play()
    logger.debug('waiting for speech to finish playing')
    while pg.mixer.music.get_busy(): 
        pg.time.Clock().tick(10)
    pg.mixer.quit()
    logger.debug('speech finished, mixer closed')
