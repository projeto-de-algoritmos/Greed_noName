import matplotlib.pyplot as plt
import pandas as pd

def plot_graph(csvFile):
    try:
        data = pd.read_csv(csvFile)

        plt.figure(figsize=(6.8, 4.2))
        x = range(len(data['shortest_processing_first']))
        plt.plot(data['shortest_processing_first'])
        plt.plot(data['earliest_deadline_first'])
        plt.plot(data['smallest_slack'])
        plt.xlabel('Quantidade')
        plt.ylabel('Tempo(ns)')
        plt.show()
    except Exception:
        print('Necessario gerar csv primeiro')