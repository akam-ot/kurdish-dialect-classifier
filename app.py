import gradio as gr
import joblib
import os

# Load model and vectorizer
model = joblib.load("models/ku_dialect_model.pkl")
vectorizer = joblib.load("models/ku_vectorizer.pkl")

# Normalize function
def normalize(text):
    return text.replace("ك", "ک").replace("ي", "ی").replace("ى", "ی").lower().strip()

# Prediction logic
def predict_dialect(text):
    if not text.strip():
        return "⚠️ Please enter some text"
    normalized = normalize(text)
    vec = vectorizer.transform([normalized])
    prediction = model.predict(vec)[0]
    return prediction

# Gradio UI
with gr.Blocks(theme=gr.themes.Soft(primary_hue="blue")) as demo:
    gr.Markdown("## 🌍 Kurdish Dialect Classifier")

    with gr.Row():
        input_text = gr.Textbox(
            label="Input Text",
            placeholder="Enter Sorani or Kurmanji (Badini) text in Arabic script...",
            lines=4
        )
        output_text = gr.Textbox(label="Predicted Dialect", interactive=False)

    with gr.Row():
        submit_btn = gr.Button("🔍 Submit")
        clear_btn = gr.ClearButton([input_text, output_text], value="🧹 Clear")

    submit_btn.click(fn=predict_dialect, inputs=input_text, outputs=output_text)

if __name__ == "__main__":
    demo.launch()