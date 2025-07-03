from flask import Flask, request, render_template
import openai

app = Flask(__name__)
openai.api_key = "your-api-key-here"  # Replace this with your actual API key

def generate_poem(topic):
    prompt = f"Write a creative poem about {topic}. Use rich language, vivid imagery, and emotion."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message["content"]

@app.route("/", methods=["GET", "POST"])
def home():
    poem = ""
    if request.method == "POST":
        topic = request.form["topic"]
        poem = generate_poem(topic)
    return render_template("index.html", poem=poem)

if __name__ == "__main__":
    app.run(debug=True)