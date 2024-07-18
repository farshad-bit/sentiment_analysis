# src/models/trend_analyzer.py
# این فایل برای تحلیل روندهای موجود در داده‌ها استفاده می‌شود

import pandas as pd
import numpy as np
from src.services.database_service import DatabaseService

class TrendAnalyzer:
    def __init__(self):
        self.db_service = DatabaseService()

    def analyze_trends(self, data):
        try:
            # تبدیل داده‌ها به دیتافریم
            df = pd.DataFrame(data)
            
            # تحلیل روندها
            trends = df.groupby('category').size().reset_index(name='counts')
            trends['trend'] = trends['counts'].pct_change().fillna(0)
            
            # ذخیره نتیجه در دیتابیس
            self.db_service.insert_trends(trends.to_dict('records'))

            return trends.to_dict('records')
        except Exception as e:
            print(f"Error: {e}")
            return str(e)
