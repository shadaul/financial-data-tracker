import requests
import sqlite3
from openai import OpenAI


def get_ai_analysis(date, pln, eur):
    client = OpenAI(api_key="openai_api_key")

    prompt = f"act as a financial analyst. On {date}, 1 USD = {pln} PLN and 1 EUR = {eur} EUR. Write a short 1-sentence summary for an investor."

    try:
        response = client.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful financial expert."},
                {"role": "user", "content": prompt}
            ]
        )

        ai_message = response.choices[0].message.content
        print(f"AI report: {ai_message}\n")

    except Exception as e:
        print("⚠️ AI Integration is ready, but a valid API Key is required to fetch the report.\n")


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
    get_ai_analysis(date, usd_to_pln, usd_to_eur)




def save_to_database(date,pln,eur):
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS rates (date TEXT, pln REAL, eur REAL)")
    cursor.execute("INSERT INTO rates VALUES (?, ? ,?)", (date, pln, eur))
    conn.commit()
    conn.close()

get_exchange_rates()


