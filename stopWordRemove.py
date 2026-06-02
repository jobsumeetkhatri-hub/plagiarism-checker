import nltk
import os

# Set a writable directory for NLTK data
nltk_data_dir = os.path.join(os.getcwd(), 'nltk_data')
os.makedirs(nltk_data_dir, exist_ok=True)
nltk.data.path.append(nltk_data_dir)

# Download required packages
print("Downloading NLTK data...")
nltk.download('stopwords', download_dir=nltk_data_dir)
nltk.download('punkt', download_dir=nltk_data_dir)
nltk.download('wordnet', download_dir=nltk_data_dir)
nltk.download('pros_cons', download_dir=nltk_data_dir)
nltk.download('reuters', download_dir=nltk_data_dir)
print("NLTK data downloaded successfully!")
