# Chap02-03/twitter_term_frequency_graph.py
import sys
import string
import json
from collections import Counter
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
import os
import matplotlib as mpl
mpl.use('Agg')
#if os.environ.get('DISPLAY','') == '':
#    print('no display found. Using non-interactive Agg backend')
#    mpl.use('Agg')
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import random

def process(text, tokenizer=TweetTokenizer(), stopwords=[]):
    """Process the text of a tweet:
    - Lowercase
    - Tokenize
    - Stopword removal
    - Digits removal

    Return: list of strings
    """
    text = text.lower()
    tokens = tokenizer.tokenize(text)
    return [tok for tok in tokens if tok not in stopwords and not tok.isdigit() and not tok.startswith(('#', '@', 'https')) and not tok.endswith(('am', 'pm'))]

def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

if __name__ == '__main__':
    tweet_tokenizer = TweetTokenizer()
    punct = list(string.punctuation)
    stopword_list = stopwords.words('english') + punct + ['rt', 'via', '...', '’']

    fname = sys.argv[1]
    tf = Counter()
    with open(fname, 'r') as f:
        words=[]
        for line in f:
            tweet = json.loads(line)
            
            tokens = process(text=tweet.get('text', ''),
                             tokenizer=tweet_tokenizer,
                             stopwords=stopword_list)
            words.extend(tokens)
           
            tf.update(tokens)
            
        text= ' '.join(words)
        
        # Generate Word Cloud
        wordcloud = WordCloud(background_color='white',
            max_words=500,
            width=2400,
            height=1800
            ).generate(text)

        plt.figure( figsize=(20,10), facecolor='k' )
        plt.imshow(wordcloud.recolor(color_func=None, random_state=3))
        plt.axis('off')
        plt.savefig('./TwitterWordCloud.png', dpi=300)
#        plt.show()
