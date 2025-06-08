# 🎭 Sentiment Analysis Project

> A powerful sentiment analysis application that understands emotions in text using machine learning

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-Web%20Framework-green.svg)](https://flask.palletsprojects.com)
[![Machine Learning](https://img.shields.io/badge/ML-Sentiment%20Analysis-orange.svg)](https://scikit-learn.org)

---

## ✨ What This Project Does

Transform raw text into meaningful emotional insights! This application analyzes the sentiment behind any piece of text, helping you understand whether the tone is positive, negative, or neutral.

Perfect for:
- 📝 **Social Media Monitoring** - Track brand sentiment across platforms
- 🏨 **Review Analysis** - Understand customer feedback at scale
- 📊 **Market Research** - Gauge public opinion on products or services
- 🤖 **Content Moderation** - Automatically filter content by emotional tone

---

## 🚀 Quick Start

### Prerequisites
Make sure you have Python 3.8+ installed on your system.

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/sreenivasulu2004/Sentiment-Analysis.git
   cd sentiment-analysis-project
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:5000` and start analyzing!

---

## 📁 Project Structure


📦 sentiment-analysis-project

    ├── 🚀 app.py # Flask web application
    ├── 🧠 SentimentAnalyser.py # Core sentiment analysis engine 
    ├── 📊 Models/ # Pre-trained machine learning models 
    │ ├── classifier.pkl
    │ ├── label_encoder.pkl 
    │ └── tfidf_vectorizer.pkl 
    ├── 📁 Dataset/ # Training data 
    │ └── tripadvisor_hotel_reviews.csv 
    ├── 📓 Notebooks/ # Jupyter notebooks for exploration 
    │ └── test.ipynb 
    ├── 📋 requirements.txt # Python dependencies 
    └── ⚙️ pyproject.toml # Project configuration

---

## 🎯 Features

### 🔍 **Intelligent Text Analysis**
- Real-time sentiment detection
- Support for multiple text lengths
### 🌐 **Web Interface**
- Clean, intuitive user interface
- Instant results display
- Mobile-responsive design

### 🧪 **Research & Development**
- Jupyter notebooks for experimentation
- Pre-trained models ready to use
- Extensible architecture for improvements

---

## 🛠️ How It Works

1. **Text Preprocessing** - Clean and prepare your input text
2. **Feature Extraction** - Convert text to numerical features using TF-IDF
3. **Model Prediction** - Apply machine learning classifier
4. **Result Interpretation** - Present human-readable sentiment analysis

---

## 📊 Dataset

The project uses TripAdvisor hotel reviews dataset, providing:
- ✅ Real-world text samples
- ✅ Diverse sentiment expressions
- ✅ High-quality labeled data for training

---

<div align="center">

**Made with ❤️**

*Happy analyzing! 🎉*

</div>
