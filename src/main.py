import openai
import gradio as gr
import markdown
import config

# API_KEY
openai.api_key = config.API_KEY


messages = [
    {"role": "system",
     "content": "You are a helpful and kind AI Assistant"
     },
]


def chat_bot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )
        reply = chat["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": reply})
        reply_markdown = markdown.markdown(reply)

        return reply_markdown


if __name__ == '__main__':
    inputs = gr.components.Textbox(lines=6, label="Chat with AI")
    outputs = gr.components.HTML(label="Reply")
    iface = gr.Interface(fn=chat_bot,
                         outputs=outputs,
                         inputs=inputs,
                         title="XChat",
                         description="Ask anything you want",
                         theme="default").launch(share=False)
