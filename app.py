import streamlit as st
from transformers import pipeline

# Tiny model for faster inference
classifier = pipeline("text-classification", model="mrm8488/bert-tiny-finetuned-sms-spam-detection")

st.set_page_config(page_title="Email Spam Detector", layout="centered")

st.title("📧 Email Spam Detector")
st.write("Paste your email content and check if it's **Spam** or **Not Spam**.")

email_text = st.text_area("Enter email text:")

if st.button("Check"):
    if email_text.strip() != "":
        result = classifier(email_text)[0]

        # Map labels to human-readable form
        label_map = {"LABEL_0": "Not Spam", "LABEL_1": "Spam"}
        label = label_map.get(result['label'], result['label'])
        
        st.subheader("Result:")
        st.write(f"**Prediction:** {label}")
        st.write(f"**Confidence:** {result['score']:.2f}")
    else:
        st.warning("Please enter an email!")
