import matplotlib.pyplot as plt
import pandas as pd

def compare_data(minimizing_lateness_python, minimizing_lateness_c):
    pd.DataFrame(minimizing_lateness_python).plot(kind='line')
    plt.title('Grafico Tempo(s) x Processos: Python')
    plt.ylabel('Tempo(s)')
    plt.xlabel('Processos')
    pd.DataFrame(minimizing_lateness_c).plot(kind='line')
    plt.title('Grafico Tempo(s) x Processos: C')
    plt.ylabel('Tempo(s)')
    plt.xlabel('Processos')
    plt.show()