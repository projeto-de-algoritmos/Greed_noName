import csv
import pandas as pd
import os

def get_csv_data(minimizing_lateness, type_language):
    df = pd.DataFrame(minimizing_lateness)
    filename = 'results_' + type_language + '.csv'
    df.to_csv(filename)

