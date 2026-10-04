from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# OpenAI API key (environment variable recommended)
openai.api_key = "YOUR_OPENAI_API_KEY"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful AI chatbot."},
                {"role": "user", "content": user_msg},
            ],
        )
        bot_reply = response["choices"][0]["message"]["content"]
    except Exception as e:
        bot_reply = "Sorry, AI service not available right now."

    return jsonify({"reply": bot_reply})


if __name__ == "__main__":
    app.run(debug=True)
