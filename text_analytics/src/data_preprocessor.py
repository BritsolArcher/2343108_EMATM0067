import re
import emoji
import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


class DataPreprocessor:
    def __init__(self):
        nltk.download('stopwords')
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        
    # Cleaning
    def remove_non_printable(self,text):
        def has_non_printable(text):
            non_printable_pattern = re.compile(r'[\x00-\x1F\x7F-\x9F]')
            match = re.search(non_printable_pattern, text)
            return bool(match)

        while True:
            non_printable_pattern = re.compile(r'[\x00-\x1F\x7F-\x9F]')
            text = re.sub(non_printable_pattern, '', text)
            if not has_non_printable(text):
                break   
        cleaned_text = text
        return cleaned_text
    
    def emoji_to_text(self,emoji_str):
        text = emoji.demojize(emoji_str)
        return text
    
    def remove_urls(self,text):
        url_pattern = re.compile(r'https?://\S+|www\.\S+')
        return url_pattern.sub('', text)
    
    def remove_mentions(self,text):
        mention_pattern = re.compile(r'@[\w_]+')
        return mention_pattern.sub('', text)
    
    def remove_hashtag_symbol(self, text):
        hashtag_pattern = re.compile(r'#(\w+)')
        return hashtag_pattern.sub(r'\1', text)
    
    # Tokenisation
    def text_tokenisation(self, text):
        tokens = nltk.word_tokenize(text)
        
        pattern = re.compile(r'[a-zA-Z]')
        filtered_tokens = []
        for token in tokens:
            if re.search(pattern, token):
                filtered_tokens.append(token)
        
        return filtered_tokens
    
    def remove_non_english_words(self, tokens):
        def is_English_word(word):
            return len(wordnet.synsets(word)) > 0
        
        filtered_tokens = []
        for token in tokens:
            if is_English_word(token):
                filtered_tokens.append(token)
        return filtered_tokens
    
    def remove_stop_words(self, tokens):
        filtered_tokens = [word for word in tokens if word.lower() not in self.stop_words and len(word)>2] 
        return filtered_tokens
    
    # Lemmatisation
    def lemmatise_tokens(self, tokens):
        lemmatised_tokens = []
        lemmatizer = self.lemmatizer
        for token in tokens:
            token = lemmatizer.lemmatize(token.lower(), pos='r')
            token = lemmatizer.lemmatize(token.lower(), pos='a')
            token = lemmatizer.lemmatize(token.lower(), pos='v')
            token = lemmatizer.lemmatize(token.lower(), pos='n')
            lemmatised_tokens.append(token)
        return lemmatised_tokens
    
    def __call__(self, sent):
        sent = self.emoji_to_text(sent)
        sent = self.remove_non_printable(sent)
        sent = self.remove_urls(sent)
        sent = self.remove_mentions(sent)
        sent = self.remove_hashtag_symbol(sent)
        # Tokenisation
        tokens = self.text_tokenisation(sent)
        tokens = self.remove_stop_words(tokens)
        tokens = self.remove_non_english_words(tokens)
        tokens = self.lemmatise_tokens(tokens)
        self.cleaned_sent = ' '.join(tokens)
        return self.cleaned_sent




