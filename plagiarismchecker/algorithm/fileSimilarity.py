import nltk
import re
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
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
    """Clean and preprocess text for similarity comparison"""
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    return text

def findFileSimilarity(text1, text2):
    """Calculate cosine similarity between two texts"""
    # Preprocess both texts
    processed_text1 = preprocess_text(text1)
    processed_text2 = preprocess_text(text2)
    
    # If either text is empty, return 0
    if not processed_text1 or not processed_text2:
        return 0.0
    
    # Create TF-IDF vectors
    vectorizer = TfidfVectorizer()
    
    try:
        # Fit and transform the texts
        tfidf_matrix = vectorizer.fit_transform([processed_text1, processed_text2])
        
        # Calculate cosine similarity
        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
        
        # Return similarity percentage (0-100)
        return similarity[0][0] * 100
    except:
        # If error occurs (e.g., no meaningful words), return 0
        return 0.0
