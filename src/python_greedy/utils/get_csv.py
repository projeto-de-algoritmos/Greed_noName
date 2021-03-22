import csv

def get_csv_data(minimizing_lateness, type_language):
    df = pd.DataFrame(tempo_ordenacao)
    filename = 'results_' + type_language + '.csv'
    df.to_csv(filename)

