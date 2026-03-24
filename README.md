# Financial Data Tracker 📈

A lightweight automated Python pipeline that extracts real-time currency exchange rates using a RESTful API and loads the data into a local relational database for historical tracking. 

This project demonstrates core Data Engineering and Backend Development principles, including API integration, data extraction, and data persistence.

## Features
- **REST API Integration:** Fetches real-time exchange rates (USD to PLN and EUR) via the [Frankfurter API](https://www.frankfurter.app/).
- **Data Parsing:** Processes JSON responses to extract specific financial metrics.
- **Data Persistence:** Uses `sqlite3` to securely store historical exchange rates in a local SQLite database using parameterized SQL queries to prevent injections.

## Technologies Used
- **Python 3**
- **Libraries:** `requests`, `sqlite3`
- **Database:** SQLite

## Setup & Execution
1. Clone the repository.
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate