import requests
from flask import Flask, request, jsonify
import json

api_key = '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' # you need to use your own chatgpt apikey for testing

app = Flask(__name__)

@app.route('/check', methods = ['POST'])
def check_question():
    record = json.loads(request.data)
    question = ""
    print(record)
    for i in record:
        question += f"{i}: {record[i]}\n"
    print(question)
    try:
        response = requests.post(
            'https://api.openai.com/v1/completions',
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {api_key}'
            },
            json = {
                'model': 'text-davinci-003',
                'prompt': f'Help me to solve the following multiple choice question."{record}"',
                'temperature': 0.4,
                'max_tokens': 300,
                'n': 1
            }
        )

        chatgpt = response.json()
        for item in chatgpt['choices']:
            print(f"{item['index']}{item['text']}")

        return chatgpt['choices'][0]['text']
    except:
        return "Failed to access checking service. Please wait for a while"

app.run(host='0.0.0.0', debug=True)