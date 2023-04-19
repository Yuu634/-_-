import os
import openai
import requests

openai.api_key = os.getenv("yuki1234")
messages = []
print("今どんな気分ですか？")
musicstyle = input()
# 指定できるroleはassistant, system, userの3種類
messages.append({"role": "system", "content": "あなたはChatGPTです。Userからの質問に答えてください。"})
messages.append({"role": "user", "content": musicstyle + "時に聞きたい曲に含まれているジャンル、曲の長さ、テンポ、楽器、キーを教えてください。"})
# userはユーザからのセリフ
# assistantはChatGPT自身のセリフ
# systemとassistantの違いはよくわからない
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
)
answer = response["choices"][0]["message"]["content"]
print(answer)
genre = answer.find('ジャンル')
musictime = answer.find('曲の長さ')
tempo = answer.find('テンポ')
instrument = answer.find('楽器')
key = answer.find('キー')
print(answer[genre:musictime])
print(answer[musictime:tempo])
print(answer[tempo:instrument])
print(answer[instrument:key])
print(answer[key:])