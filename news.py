from transformers import pipeline
from newspaper import Article
from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
app = Flask(__name__)

summarizer = pipeline("summarization", model = "sshleifer/distilbart-cnn-12-6") // facebook/bart-large-cnn

def extract_text_from_url(url):
        
        try:
            article = Article(url)
            article.download()
            article.parse()
            article_text = article.text

            if not article_text.strip():
                response = requests.get(url, timeout=20)
                response.raise_for_status()
                soup = BeautifulSoup(response.text, 'html.parser')
                paragraph = [p.get_text() for p in soup.find_all("p") if p.get_text().strip()]
                article_text =  ' '.join(paragraph)

            else:
                response = requests.get(url, timeout=20)
                soup = BeautifulSoup(article.html, 'html.parser')
                
            image_urls = []
            for img in soup.find_all("img"):
                src = img.get("src")
                if src and not src.startswith("data:"):
                    src = urljoin(url, src)
                    image_urls.append(src)

            return article_text, image_urls
        except Exception as e:
                return "", []

@app.route("/", methods=["GET", "POST"])
def summarize_article():
    summary_text = ""
    images = []
    error = None
    if request.method == "POST":
        url = request.form.get("article_url")
        if not url:
            error = "No URL provided."
        else:    
            try:
                article_text, images = extract_text_from_url(url)
                if len(article_text.strip()) > 100:
                    summary = summarizer(article_text,max_length=150, min_length=30, do_sample=False)
                    summary_text = summary[0]['summary_text']
                else:
                    error = "Article text is too short to summarize."
            except Exception as e:
                error = f"Error processing URL: {str(e)}"
    return render_template('index.html', summary=summary_text, images=images,error=error)  




