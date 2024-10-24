
from flask import Flask, render_template, request
from nltk.sentiment import SentimentIntensityAnalyzer
from datetime import datetime

app = Flask(__name__)

# Initialize sentiment intensity analyzer
sia = SentimentIntensityAnalyzer()

# Store previous comments and their sentiments
previous_comments = []

# Function to analyze sentiment
def analyze_sentiment(comment):
    sentiment_scores = sia.polarity_scores(comment)
    if sentiment_scores['compound'] >= 0.05:
        return "Positive"
    elif sentiment_scores['compound'] <= -0.05:
        return "Negative"
    else:
        return "Neutral"

@app.route('/', methods=['GET', 'POST'])
def index():
    comment = ''
    sentiment = ''
    if request.method == 'POST':
        comment = request.form['comment']
        sentiment = analyze_sentiment(comment)
        
        # Store comment with timestamp and sentiment
        previous_comments.append({
            'comment': comment,
            'sentiment': sentiment,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
        
    return render_template('index.html', comment=comment, sentiment=sentiment, previous_comments=previous_comments)

if __name__ == '__main__':
    app.run(debug=True)
    """
from flask import Flask, render_template, request
from nltk.sentiment import SentimentIntensityAnalyzer
from datetime import datetime

app = Flask(__name__)

# Initialize sentiment intensity analyzer
sia = SentimentIntensityAnalyzer()

# Store previous comments and their sentiments
previous_comments = []

# Function to analyze sentiment
def analyze_sentiment(comment):
    sentiment_scores = sia.polarity_scores(comment)
    if sentiment_scores['compound'] >= 0.05:
        return "Positive"
    elif sentiment_scores['compound'] <= -0.05:
        return "Negative"
    else:
        return "Neutral"

@app.route('/', methods=['GET', 'POST'])
def index():
    comment = ''
    sentiment = ''
    if request.method == 'POST':
        comment = request.form['comment']
        sentiment = analyze_sentiment(comment)
        
        # Store comment with timestamp and sentiment
        previous_comments.append({
            'comment': comment,
            'sentiment': sentiment,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
        
    # Reverse previous comments to show the latest on top
    previous_comments.reverse()
    
    return render_template('index.html', comment=comment, sentiment=sentiment, previous_comments=previous_comments)

if __name__ == '__main__':
    app.run(debug=True)
"""
