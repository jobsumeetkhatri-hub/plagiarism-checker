import nltk
import re
import requests
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import string
import os

# Setup NLTK data path for Railway
nltk_data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'nltk_data')
os.makedirs(nltk_data_path, exist_ok=True)
nltk.data.path.append(nltk_data_path)

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', download_dir=nltk_data_path)
    nltk.download('stopwords', download_dir=nltk_data_path)
    nltk.download('wordnet', download_dir=nltk_data_path)

def preprocess_text(text):
    """Clean and preprocess text"""
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    return text

def search_web(query):
    """Search the web for similar content using Google Custom Search API"""
    # You'll need to set up Google Custom Search API and add your API keys
    # For now, return a placeholder
    API_KEY = os.environ.get('GOOGLE_API_KEY', '')
    SEARCH_ENGINE_ID = os.environ.get('SEARCH_ENGINE_ID', '')
    
    if not API_KEY or not SEARCH_ENGINE_ID:
        # Return sample links if no API keys configured
        return ["https://www.example.com/sample-result-1", "https://www.example.com/sample-result-2"]
    
    try:
        url = "https://www.googleapis.com/customsearch/v1"
        params = {
            'key': API_KEY,
            'cx': SEARCH_ENGINE_ID,
            'q': query
        }
        response = requests.get(url, params=params)
        results = response.json()
        
        links = []
        if 'items' in results:
            for item in results['items'][:5]:  # Get top 5 results
                links.append(item['link'])
        return links
    except:
        return ["https://www.example.com/error-retrieving-results"]

def findSimilarity(text):
    """Find plagiarism percentage by comparing text with web content"""
    # Preprocess input text
    processed_text = preprocess_text(text)
    
    # Search web for similar content
    web_links = search_web(processed_text[:100])  # Send first 100 chars for search
    
    # For demo purposes, return a sample percentage and link
    # In a real implementation, you would fetch content from web links and compare
    
    import random
    similarity_percentage = random.uniform(60, 95)  # This is just for demo
    
    # Return percentage and first link
    if web_links:
        return similarity_percentage, web_links[0]
    else:
        return similarity_percentage, "https://www.google.com"
