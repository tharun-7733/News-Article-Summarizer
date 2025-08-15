📰 News Article Summarizer

A Flask-based web application that uses Natural Language Processing (NLP) to automatically summarize news articles from URLs. The app extracts the main text from an online article and provides a concise summary for quick reading.

🚀 Features

Extracts full text from a news article URL.

Generates a short, clear summary using facebook/bart-large-cnn NLP model.

Simple web interface built with Flask.

Handles common scraping and parsing errors.

🛠️ Tech Stack

Python 3

Flask – Web framework

Hugging Face Transformers – Summarization model

Newspaper3k – Article extraction

BeautifulSoup – HTML parsing

📦 Installation

Clone the repository

git clone https://github.com/tharun-7733/News-Article-Summarizer.git
cd News-Article-Summarizer


Create a virtual environment & activate it

python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows


Install dependencies

pip install -r requirements.txt

▶️ Usage

Run the Flask app

python app.py


Open your browser and go to:

http://127.0.0.1:5000/


Paste any news article URL to get an instant summary.

📌 Example

Input:
https://example.com/news/article

Output:
A short paragraph summarizing the main points of the article with images.
