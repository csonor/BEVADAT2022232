import pandas as pd
import numpy as np


class NJCleaner:
    def __init__(self, csv_path):
        self.data = pd.read_csv(csv_path)

    def order_by_scheduled_time(self):
        df = self.data.sort_values(by=['scheduled_time'])
        return df

    def drop_columns_and_nan(self):
        df = self.data.drop(columns=['from', 'to'])
        df = df.dropna()
        return df

    def convert_date_to_day(self):
        df = self.data.copy()
        df['day'] = pd.to_datetime(df['date']).dt.day_name()
        df = df.drop(columns=['date'])
        return df

    def convert_scheduled_time_to_part_of_the_day(self):
        df = self.data.copy()
        df['scheduled_time'] = pd.to_datetime(
            df['scheduled_time'])
        df['part_of_the_day'] = df['scheduled_time'].apply(
            lambda x: 'late_night' if x.hour < 4
            else 'early_morning' if x.hour < 8
            else 'morning' if x.hour < 12
            else 'afternoon' if x.hour < 16
            else 'evening' if x.hour < 20
            else 'night')
        df = df.drop(columns=['scheduled_time'])
        return df

    def convert_delay(self):
        df = self.data.copy()
        df['delay'] = df['delay_minutes'].apply(
            lambda x: 1 if x >= 5 else 0)
        return df

    def drop_unnecessary_columns(self):
        df = self.data.copy()
        df = df.drop(
            columns=['train_id', 'actual_time', 'delay_minutes'])
        return df

    def save_first_60k(self, path):
        self.data.iloc[:60000].to_csv(path, index=False)

    def prep_df(self, path='data/NJ.csv'):
        self.data = self.order_by_scheduled_time()
        self.data = self.drop_columns_and_nan()
        self.data = self.convert_date_to_day()
        self.data = self.convert_scheduled_time_to_part_of_the_day()
        self.data = self.convert_delay()
        self.data = self.drop_unnecessary_columns()
        self.save_first_60k(path)
