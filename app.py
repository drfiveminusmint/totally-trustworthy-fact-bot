from flask import Flask, request, redirect, url_for, render_template_string
from google import genai

# start Flask
app = Flask(__name__,static_folder ="frontend")

# store our chat history locally, resets on server restart
chatHistory = []

# get HTML template
page = open("frontend/page.html", 'r')
HTML = page.read()

# Create the client. You MUST set your API key beforehand (see README.md)
client = genai.Client()

# LLM Prompt
modelPrompt = """
 You are "Totally Trustworthy Facts Bot," a chatbot designed to teach children to double-check LLM answers for hallucinations. Answer the user's question's truthfully, at about a sixth grade level, with one exception: Include one blatantly and obviously untrue 'fact' in your answer. Use reverse psychology to get them to double-check your info using other sources like Wikipedia or Brittanica, since kids hate being told what to do. Maintain a friendly and casual tone in your answers, incorporating dated and cringeworthy slang if possible, as the kids will learn better if you're funny. Limit your answers to 3-4 sentences. Introduce yourself briefly and wait for the user to ask a question.
"""

# Get a reply from Gemini based on our chat history
def get_reply():
    global chatHistory

    # Build conversation history string
    history_text = "\n".join(
        [f"{msg['role']}: {msg['content']}" for msg in chatHistory]
    )

    try:
        response = client.models.generate_content(model="gemini-3-flash-preview",contents=history_text)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"


# initialize the starting state of our chat app
def setup_chat():
    global chatHistory
    chatHistory = []

    chatHistory.append({
        "role": "user",
        "content": modelPrompt
    })

    response = get_reply()

    chatHistory.append({
        "role": "ai",
        "content": response
    })

# initialize our chat when the server starts
setup_chat()

# send button functionality
@app.route("/", methods=["GET", "POST"])
def index():
    global chatHistory

    if request.method == "POST":
        user_input = request.form.get("user_input")

        if user_input:
            # add the user message to the chat history
            chatHistory.append({
                "role": "user",
                "content": user_input
            })

            # get and add the LLM's response
            model_reply = get_reply()

            chatHistory.append({
                "role": "ai",
                "content": model_reply
            })

        return redirect(url_for("index"))

    return render_template_string(HTML, messages=chatHistory)

# clear button functionality
@app.route("/clear", methods=["POST"])
def clear():
    global chatHistory
    setup_chat()
    return redirect(url_for("index"))

# run the Flask app
if __name__ == "__main__":
    app.run(debug=False)