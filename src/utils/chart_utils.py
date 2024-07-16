# src/utils/chart_utils.py
import matplotlib.pyplot as plt
import io
import base64

def create_sentiment_chart(sentiments):
    # تعیین رنگ‌ها و برچسب‌ها برای نمودار
    labels = ['Positive', 'Negative', 'Neutral']
    sizes = [sentiments.get(label.lower(), 0) for label in labels]
    colors = ['#00ff00', '#ff0000', '#0000ff']

    # ایجاد نمودار پای
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    ax.axis('equal')  # برابر نگه داشتن نسبت‌ها

    # تبدیل نمودار به تصویر پایه 64
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    chart_url = base64.b64encode(img.getvalue()).decode('utf8')
    plt.close()

    return f'data:image/png;base64,{chart_url}'
