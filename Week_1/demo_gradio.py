import gradio as gr
from transformers import pipeline

# ✅ Model is defined here
model = pipeline("text-generation", model="gpt2")

def generate(prompt, temperature):
    response = model(
        prompt,
        temperature=temperature,
        max_new_tokens=200,
        do_sample=True      # Required when using temperature
    )
    return response[0]["generated_text"]

gr.Interface(
    fn=generate,
    inputs=[
        gr.Textbox(label="Prompt", placeholder="Enter your prompt here..."),
        gr.Slider(minimum=0.0, maximum=1.0, value=0.7, step=0.1, label="Temperature")
    ],
    outputs=gr.Textbox(label="Output"),
    title="Text Generator",
    description="Adjust temperature to control creativity"
).launch(share=True)