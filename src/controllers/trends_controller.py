from flask import Blueprint, render_template
import pandas as pd
from src.services.database_service import DatabaseService
from src.utils.chart_utils import create_trend_chart

trends_blueprint = Blueprint('trends', __name__, template_folder='../views/templates')

db_service = DatabaseService()

@trends_blueprint.route('/trends')
def trends():
    rows = db_service.fetch_all_sentiments()
    df = pd.DataFrame(rows, columns=['id', 'text', 'sentiment', 'date'])
    
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)

    # Generate trend chart
    chart = create_trend_chart(df)

    return render_template('trends.html', chart=chart)
