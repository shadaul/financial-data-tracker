import requests
import sqlite3

def get_exchange_rates():
    url = "https://api.frankfurter.app/latest?from=USD&to=PLN,EUR"

    response = requests.get(url)
    data = response.json()

    date = data["date"]
    usd_to_pln = data["rates"]["PLN"]
    usd_to_eur = data["rates"]["EUR"]

    print(f"Market update for {date}:")
    print(f"1 USD = {usd_to_pln} PLN")
    print(f"1 USD = {usd_to_eur} EUR")
    save_to_database(date, usd_to_pln, usd_to_eur)




def save_to_database(date,pln,eur):
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS rates (date TEXT, pln REAL, eur REAL)")
    cursor.execute("INSERT INTO rates VALUES (?, ? ,?)", (date, pln, eur))
    conn.commit()
    conn.close()

get_exchange_rates()
