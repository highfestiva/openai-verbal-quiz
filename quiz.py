#!/usr/bin/env python3

from audio_play import say
from audio_record import record_to_file
import quizzer
from transcribe import transcribe_from_audio_file


def output(text, prefix=''):
    print(prefix+text)
    say(text, 'ai-output.mp3')


output('Welcome to The Quiz! Speak clearly into the mic to answer. Get ready!')
first_question = quizzer.start()
output('First question: ' + first_question)
i = 0
while True:
    fn = 'human-input.wav'
    record_to_file(fn)
    player_answer_txt = transcribe_from_audio_file(fn)
    if not player_answer_txt:
        output(prefix="I couldn't quite catch that. ", text='Please repeat.')
        continue
    output(prefix='Your answer: ', text=player_answer_txt)
    next_question = quizzer.answer(player_answer_txt)
    output(prefix='Quiz AI: ', text=next_question)
