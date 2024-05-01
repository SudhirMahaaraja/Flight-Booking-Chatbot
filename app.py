from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# Rasa server URL
RASA_SERVER_URL = "http://localhost:5005/webhooks/rest/webhook"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    user_message = request.json['message']
    print("User Message:", user_message)

    # Send user message to Rasa and get bot's response
    rasa_response = requests.post(RASA_SERVER_URL, json={'message': user_message})
    rasa_response_json = rasa_response.json()
    print("Rasa Response:", rasa_response_json)

    bot_response = rasa_response_json[0]['text'] if rasa_response_json else 'Sorry, I didn\'t understand that.'

    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
