import matplotlib.pyplot as plt
import pandas as pd

def plot_graph(csvFile):
    try:
        data = pd.read_csv(csvFile)

        plt.figure(figsize=(6.8, 4.2))
        x = range(len(data['shortest_processing_first']))
        plt.plot(x, data['shortest_processing_first'], label='shortest_processing_first')
        plt.plot(x, data['earliest_deadline_first'], label='earliest_deadline_first')
        plt.plot(x, data['smallest_slack'], label='smallest_slack')
        plt.legend(loc='upper left')
        plt.xlabel('Quantidade')
        plt.ylabel('Tempo(ns)')
        plt.show()

    except Exception:
        print('Necessario gerar csv primeiro')