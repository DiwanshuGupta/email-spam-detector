# email-spam-detector
The Email Spam Detector is a lightweight AI-powered web app that classifies emails as Spam or Not Spam using a fine-tuned BERT model from Hugging Face.
Users can paste the content of any email into the app, and the system analyzes it in real-time, providing:

**Prediction**: Spam / Not Spam


**Confidence Score**: How confident the model is in its decision

The app is built with Streamlit for an interactive UI and integrates Hugging Face’s pre-trained spam detection models for fast, accurate results.

 **Tech Stack**

Frontend/UI: Streamlit

Backend/AI: Hugging Face Transformers (bert-tiny-finetuned-sms-spam-detection)

Language: Python

**How to Run**

**1.Clone the repository**:

git clone https://github.com/your-username/email-spam-detector.git

cd email-spam-detector

**2.Create a virtual environment (optional but recommended)**:
python -m venv venv

venv\Scripts\activate      # On Windows

**3.Install dependencies**:
pip install -r requirements.txt

**4.Run the app**:
streamlit run app.py

**5.Open in browser**
Go to  http://localhost:8501

**Requirements**

streamlit

transformers

torch

Pillow


