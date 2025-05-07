# Kurdish Dialect Classifier

A lightweight web app that automatically classifies Kurdish text (in Perso-Arabic script) as either **Sorani** or **Kurmanji (Badini)** dialect.

[![Demo on Hugging Face Spaces](https://img.shields.io/badge/Live%20Demo-Hugging%20Face%20Spaces-blue)](https://huggingface.co/spaces/akam-ot/kurdish-dialect-classifier)

## 🚀 Quickstart

1. **Clone** the repo:

   ```bash
   git clone https://github.com/akam-ot/kurdish-dialect-classifier.git
   cd kurdish-dialect-classifier
   ```
2. **Install** dependencies (create a virtualenv first if you like):

   ```bash
   pip install -r requirements.txt
   ```
3. **Run** the app locally:

   ```bash
   python app.py
   ```

## 🧠 How It Works

* **Data**: A labeled dataset of Kurdish sentences in Perso-Arabic script, with dialect tags.
* **Preprocessing**: Normalizes Arabic-script variations (e.g. `ك`→`ک`, `ي`→`ی`), lowercases, and trims whitespace.
* **Vectorization**: TF–IDF on character n‑grams (1–3), up to 5k features.
* **Model**: Logistic Regression trained on the vectorized text.

## 🛠️ Project Structure

```
├── app.py               # Gradio application
├── models/              # Pre-trained model & vectorizer
│   ├── ku_vectorizer.pkl
│   └── ku_dialect_model.pkl
├── requirements.txt     # Python dependencies
```

## 📄 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.
