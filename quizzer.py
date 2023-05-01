import os
import openai
from random import choice


openai.api_key = os.getenv('OPENAI_API_KEY')
if not openai.api_key:
    print('ERROR: you need to a) create an OpenAI account, b) create API keys, and c) set the OPENAI_API_KEY system variable')
    os.exit(1)


prompt1 = '''An AI is asking very difficult quiz questions in music, history, physics and many other topics. After the human gives an answer the AI responds with the correct one and immediately asks a new question.
'''
prompt2 = '''
Human: '''
prompt3 = '''
AI: '''
prompt4 = ' Next time please give me a question on %s. Is %s correct?'
prompt = prompt1 + prompt3
last_question = ''
topics = 'ancient_history modern_history geography architecture technology social_science languages chemistry biology physics maths countries culture music dance'
last_topics = ['geography']


def start():
    global last_question, prompt
    last_question = quiz(prompt)
    return last_question


def answer(ans):
    global last_question, prompt
    ans = ans.strip()
    ans = answer_fix(ans)
    text = f'{prompt}{last_question}{prompt2}{ans}{prompt3}'
    prompt = text
    last_question = quiz(prompt)
    return last_question


def quiz(text):
    # print(text, ' <-----------', end='\n\n')
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=text,
      temperature=0.9,
      max_tokens=150,
      top_p=1,
      frequency_penalty=0.0,
      presence_penalty=0.6,
      stop=[' AI:', ' Human:']
    )
    resp = response['choices'][0]['text'].split('\n\n')[0].strip()
    return resp


def get_topic():
    topic = last_topics[0]
    while topic in last_topics:
        topic = choice(topics.split()).replace('_',' ')
    last_topics.insert(0, topic)
    if len(last_topics) > 5:
        last_topics.pop()
    return topic


def answer_fix(ans):
    topic = get_topic()
    return prompt4 % (topic, ans)
