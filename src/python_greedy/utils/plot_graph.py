import matplotlib.pyplot as plt
import pandas as pd

def plot_graph(minimizing_lateness, type_language):
    pd.DataFrame(minimizing_lateness).plot(kind='line')
    graph_title = 'Grafico Tempo(s) x Processo em ' + type_language
    plt.title(graph_title)
    plt.ylabel('Tempo(s)')
    plt.xlabel('Processo')
    plt.show()