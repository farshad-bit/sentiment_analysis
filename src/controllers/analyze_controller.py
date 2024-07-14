from flask import Blueprint, request, render_template
from src.models.sentiment_analyzer import SentimentAnalyzer
from src.utils.chart_utils import create_chart

analyze_blueprint = Blueprint('analyze', __name__, template_folder='../views/templates')

analyzer = SentimentAnalyzer()

@analyze_blueprint.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    sentiment = analyzer.analyze_sentiment(text)
    results = analyzer.get_results()
    
    # Generate chart
    chart = create_chart(results)

    return render_template('index.html', text=text, sentiment=sentiment, chart=chart)
