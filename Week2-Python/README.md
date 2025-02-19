# Week2-Python Project

This repository contains two main scenarios:
1. API Extraction - Fetching and storing cat facts using an API and PostgreSQL.
2. Log Parser - Parsing Apache logs and analyzing data using SQL queries.

## Project Structure

```
Week2-Python/
├── API_Extraction/            
│   ├── extract_api.py       # Fetches cat facts and stores them in PostgreSQL
│   ├── api_config.py        # API configuration details
│   ├── database.py          # Database connection and operations
│   ├── .env                 # Database details for Scenario 1 (ignored in Git)
├── Log_Parser/                
│   ├── log_parser.py       # Parses Apache log files
│   ├── database.py        # Database connection and log insertion
│   ├── sql_queries.sql    # SQL queries for log analysis
│   ├── apache_logs.txt    # Sample Apache logs
│   ├── .env               # Database details for Scenario 2 (ignored in Git)
├── .gitignore               # Ignoring both .env files
├── README.md                # Project documentation
├── requirements.txt         # Python dependencies
```

## Setup Instructions

1. Clone the Repository
   ```sh
   git clone <repository-url>
   cd Week2-Python
   ```

2. Install Dependencies
   ```sh
   pip install -r requirements.txt
   ```

3. Set Up Environment Variables
   - Create a `.env` file inside `API_Extraction/` and `Log_Parser/` with the following details:
     ```ini
     DB_NAME=your_database_name
     DB_USER=your_database_user
     DB_PASSWORD=your_database_password
     DB_HOST=your_database_host
     DB_PORT=your_database_port
     ```

4. Run API Extraction
   ```sh
   python API_Extraction/extract_api.py
   ```

5. Run Log Parser
   ```sh
   python Log_Parser/log_parser.py
   ```

## SQL Queries
The `sql_queries.sql` file contains useful queries for analyzing logs, such as:
- Total number of requests
- Unique IP addresses
- Top requested URLs
- Busiest hour of the day

## Notes
- Ensure PostgreSQL is running and accessible before executing scripts.

---