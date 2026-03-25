# Financial Data Tracker & AI Analyzer 

A lightweight automated Python ETL pipeline that extracts real-time currency exchange rates, stores them in a local relational database, and leverages an LLM to generate instant financial insights. The project is fully containerized using Docker for seamless deployment.

This project demonstrates core Data Engineering, Backend Development, and DevOps principles.

## Features
- **ETL Pipeline & API Integration:** Fetches real-time exchange rates (USD to PLN and EUR) via the [Frankfurter API](https://www.frankfurter.app/).
- **AI Financial Analysis:** Integrates the `OpenAI API` to generate automated, short-form financial summaries based on the extracted currency data.
- **Data Persistence:** Uses `sqlite3` to securely store historical exchange rates using parameterized SQL queries to prevent injections.
- **Containerization:** Fully Dockerized application, ensuring consistent execution across different environments (e.g., local machines, Azure, AWS).

## Technologies Used
- **Language:** Python 3.11
- **Libraries:** `requests`, `sqlite3`, `openai`
- **Infrastructure:** Docker

## Setup & Execution

### Option 1: Run via Docker (Recommended)
1. Clone the repository.
2. Build the Docker image:
   ```bash
   docker build -t finance-tracker .