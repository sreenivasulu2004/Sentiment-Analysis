import pickle
import os
import re
import numpy
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem.snowball import PorterStemmer
import string

class SentimentAnalyser:

    def __init__(
            self,
            model_path: str= "classifier.pkl",
            vectorizer_path: str ="vectorizer.pkl",
            encoder_path: str ="encoder.pkl"
    ):

        self.model_ = self.load_model(model_path)
        self.vectorizer_ = self.load_vectorizer(vectorizer_path)
        self.encoder = self.load_encoder(encoder_path)
        self.stop_words_ = set(stopwords.words('english'))
        self.stemmer = PorterStemmer()

    def load_model(self, filepath: str):
        """
        This function loads the model from a pickle file.
        :param filepath:
        :return:
        """
        if not os.path.isfile(filepath):
            raise FileNotFoundError(f"File {filepath} not found")

        with open(filepath, "rb") as file:
            model = pickle.load(file)

        return model

    def load_encoder(self, filepath: str):
        if not os.path.isfile(filepath):
            raise FileNotFoundError(f"File {filepath} not found")

        with open(filepath, "rb") as file:
            encoder = pickle.load(file)

        return encoder

    def load_vectorizer(self, filepath: str):
        """
        This function loads the vectorizer from a pickle file.
        :param filepath:
        :return:
        """
        if not os.path.isfile(filepath):
            raise FileNotFoundError(f"File {filepath} not found")

        with open(filepath, "rb") as file:
            vectorizer = pickle.load(file)

        return vectorizer

    def clean_text(self, text: str) -> str:
        """
        This function cleans and stems the text.
        :param text:
        :return:
        """
        text = re.sub(f'[{string.punctuation}]', "", text.lower())
        words = word_tokenize(text)
        words = [word for word in words if word not in self.stop_words_]
        stemmed_words = [self.stemmer.stem(word) for word in words]
        return ' '.join(stemmed_words)

    def vectorize_text(self, text: str):
        """
        This function vectorizes the text.
        :param text: 
        :return: 
        """
        return self.vectorizer_.transform([text])

    def predict(self, input)-> numpy.ndarray:
        """
        This function predicts the sentiment.
        :param input:
        :return:
        """
        return self.model_.predict(input)

    def decode_sentiment(self, sentiment: numpy.ndarray)-> str:
        """
        This function decodes the sentiment.
        :param sentiment:
        :return:
        """
        return self.encoder.inverse_transform(sentiment)

    def predict_sentiment(self, text: str) -> str:
        """
        This function predicts the sentiment.
        :param text:
        :return:
        """
        cleaned_text = self.clean_text(text)
        vectorized_text = self.vectorize_text(cleaned_text)
        prediction = self.predict(vectorized_text)
        decoded_prediction = self.decode_sentiment(prediction)

        return decoded_prediction[0]
