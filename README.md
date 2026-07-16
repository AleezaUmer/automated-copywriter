# ✍️ Automated Copywriting & Tone Transformer

An AI-powered marketing copy generator built with **Streamlit** and **Groq Llama 3.3**. This application generates engaging marketing content for different platforms such as **LinkedIn, Instagram, and Email** based on the selected tone.

---

## 🚀 Features

- Generate AI-powered marketing copy
- Support for multiple platforms:
  - LinkedIn
  - Instagram
  - Email
- Multiple writing tones:
  - Professional
  - Friendly
  - Casual
  - Formal
  - Persuasive
  - Excited
- Adjustable AI creativity using:
  - Temperature
  - Top P
- User-friendly Streamlit interface
- Input validation
- Loading spinner while generating content
- Success notification after generation

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Groq API
- Llama 3.3 70B Versatile
- Python Dotenv

---

## 📂 Project Structure

```text
automated-copywriter/
│── app.py
│── requirements.txt
│── .env
│── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/automated-copywriter.git
```

### 2. Navigate to the project folder

```bash
cd automated-copywriter
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your Groq API Key

Create a `.env` file and add:

```env
GROQ_API_KEY=your_api_key_here
```

### 5. Run the application

```bash
streamlit run app.py
```

---

## 💡 How It Works

1. Enter the Product Name.
2. Enter the Product Description.
3. Select the Platform.
4. Choose the Tone.
5. Adjust Temperature and Top P.
6. Click **Generate Copy**.
7. The AI generates platform-specific marketing content.

---

## 📸 Example Output

### Instagram

> 📱 Meet the all-new iPhone 17!
>
> Experience next-generation AI, an advanced camera, and all-day battery life.
>
> #iPhone17 #Innovation #AI

---

## 🔮 Future Improvements

- Copy to Clipboard button
- Download generated copy
- AI content history
- Dark mode
- More platform options (Facebook, X, Threads)

---

## 👩‍💻 Author

**Aleeza Umer**

GitHub: https://github.com/AleezaUmer

---

## 📄 License

This project is created for educational purposes as part of the DecodeLabs Generative AI Training Program.