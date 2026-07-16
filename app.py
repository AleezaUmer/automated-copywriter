import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("Groq API Key not found!")
    st.stop()

client = Groq(api_key=api_key)

# Page Configuration
st.set_page_config(
    page_title="Automated Copywriting & Tone Transformer",
    page_icon="✍️",
    layout="centered"
)

st.title("✍️ Automated Copywriting & Tone Transformer")
st.write("Generate AI-powered marketing copy for different platforms.")

# Product Name
product_name = st.text_input("Product Name")

# Product Description
product_description = st.text_area("Product Description")

# Platform
platform = st.selectbox(
    "Select Platform",
    ["LinkedIn", "Instagram", "Email"]
)

# Tone
tone = st.selectbox(
    "Select Tone",
    ["Professional", "Friendly", "Casual", "Formal", "Persuasive", "Excited"]
)

# Temperature
temperature = st.slider(
    "Temperature",
    min_value=0.0,
    max_value=1.0,
    value=0.7,
    step=0.1
)

# Top P
top_p = st.slider(
    "Top P",
    min_value=0.0,
    max_value=1.0,
    value=0.9,
    step=0.1
)

# Generate Button
generate = st.button("Generate Copy")

if generate:

    # Input Validation
    if not product_name or not product_description:
        st.warning("Please enter Product Name and Product Description.")
        st.stop()

    # Prompt
    prompt = f"""
You are an expert marketing copywriter.

Create high-quality marketing content.

Product Name: {product_name}

Product Description:
{product_description}

Platform:
{platform}

Tone:
{tone}

Instructions:
- Match the writing style to the selected platform.
- Use the selected tone consistently.
- Keep the content engaging.
- Add hashtags only for Instagram and LinkedIn.
- For Email, include a Subject line and Body.
"""

    # Spinner
    with st.spinner("Generating marketing copy..."):

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            top_p=top_p,
        )

    # Success Message
    st.success("Marketing copy generated successfully!")

    # Output Title
    st.subheader(f"{platform} Marketing Copy")

    # Display Output
    st.write(response.choices[0].message.content)