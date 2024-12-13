from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Replace YOUR_API_KEY with your OpenAI API key
openai.api_key = "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"

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )
    bot_reply = response["choices"][0]["message"]["content"]
    return jsonify({"response": bot_reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
