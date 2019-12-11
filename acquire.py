import z_acquire
from os import path
import pandas as pd

def get_github_data(from_cache = True):
    if from_cache == True and path.exists('data.json'):
        df = pd.read_json('data.json')
        return df
    else: 
        z_acquire.scrape_github_data()
        df = pd.read_csv('data.json')
        return df
