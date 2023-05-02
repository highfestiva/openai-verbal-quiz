#!/usr/bin/env python3

from argparse import ArgumentParser
from audio_play import say
from audio_record import record_to_file
import logging
import quizzer
from transcribe import transcribe_from_audio_file


logger = logging.getLogger(__name__)


def output(text, prefix=''):
    logger.info(prefix+text)
    say(text, 'ai-output.mp3')


parser = ArgumentParser()
parser.add_argument('-v','--verbose', action='store_true')
options = parser.parse_args()

if options.verbose:
    logging.basicConfig(format='%(asctime)-15s %(name)-24s %(levelname)-7s %(message)s', level=logging.DEBUG)
else:
    logging.basicConfig(format='%(message)s', level=logging.INFO)

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
