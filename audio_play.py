import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
from gtts import gTTS
import pygame as pg


def say(text, tmp_filename='speech.mp3'):
    text2mp3(text, tmp_filename)
    play_mp3(tmp_filename)


def text2mp3(text, path):
    tts = gTTS(text=text, lang='en')
    tts.save(path)


def play_mp3(path):
    pg.mixer.init()
    pg.mixer.music.load(path)
    pg.mixer.music.play()
    while pg.mixer.music.get_busy(): 
        pg.time.Clock().tick(10)
    pg.mixer.quit()
