from flask import Flask, request
import gradio as gr
from zari_bot_voice import ask_zari

app = Flask(__name__)

def chat_with_zari(question):
    return ask_zari(question)

@app.route('/')
def index():
    return "ZARI Agent is running."

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    question = data.get("question", "")
    return {"answer": ask_zari(question)}

demo = gr.Interface(fn=chat_with_zari,
                    inputs=gr.Textbox(lines=2, placeholder="Ask ZARI Agent anything..."),
                    outputs="text",
                    title="ZARI Agent",
                    description="Ask ZARI Agent questions about your business, ops, or automation strategy.")

app = demo.launch(inline=False, share=False)
