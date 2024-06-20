import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

def plot_produttivita_totale_nazionale():
    conn = sqlite3.connect('pesca.db')
    query = "SELECT * FROM produttivita_totale_nazionale"
    df = pd.read_sql_query(query, conn)
    conn.close()

    plt.figure(figsize=(10, 6))
    plt.plot(df['anno'], df['produttivita_totale'], marker='o')
    plt.title('Produttività Totale Nazionale')
    plt.xlabel('Anno')
    plt.ylabel('Produttività (migliaia di euro)')
    plt.grid(True)
    plt.savefig('produttivita_totale_nazionale.png')

plot_produttivita_totale_nazionale()
