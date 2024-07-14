import matplotlib
matplotlib.use('Agg')  # Use Agg backend for matplotlib

import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

def create_chart(results):
    labels = list(results.keys())
    values = list(results.values())

    plt.figure(figsize=(10, 5))
    sns.barplot(x=labels, y=values)
    plt.title('Sentiment Analysis Results')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')

    # Save the plot to a PNG image in memory
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    chart = base64.b64encode(buf.getvalue()).decode('utf8')
    buf.close()
    plt.close()

    return chart

def create_trend_chart(df):
    sentiment_counts = df.resample('D').size()

    plt.figure(figsize=(10, 5))
    sentiment_counts.plot()
    plt.title('Sentiment Analysis Trends Over Time')
    plt.xlabel('Date')
    plt.ylabel('Count')

    # Save the plot to a PNG image in memory
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    chart = base64.b64encode(buf.getvalue()).decode('utf8')
    buf.close()
    plt.close()

    return chart
