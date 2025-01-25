# Week1-SQL: Database Design and Querying for Library Management System

## Objective
To design, implement, and optimize a relational database for a library system using industry best practices. This project involves creating a robust database, generating synthetic data, and executing complex SQL queries to derive business insights.

## Project Overview
This assignment covers the following tasks:

1. Database Design:
   - Logical and conceptual data model design.
   - Creation of an ER Diagram for a library management system.
2. Database Implementation:
   - Setup of PostgreSQL database (`lms_db`) with tables, primary/foreign keys, and constraints.
   - Use of `NOT NULL`, `UNIQUE`, and `ON DELETE CASCADE` constraints.
3. Data Generation:
   - Python script to generate synthetic data.
   - Ingestion of data into the PostgreSQL database.
4. SQL Querying:
   - Business insights derived using SQL queries.
   - Query optimization with appropriate indexing.
   - Execution plan analysis using `EXPLAIN`.
5. Reporting:
   - Final report created in PDF format to summarize the project.

## Folder Structure
```plaintext
Week1-SQL/
├── ER_Diagram/
│   ├── library_system_er_diagram.drawio       # Editable ER diagram file
│   └── library_system_er_diagram.pdf         # PDF version of the ER diagram
├── Schema/
│   ├── schema_design.sql                     # SQL script to create the database schema
│   ├── data_insertion_script.sql             # SQL script to populate the database with sample data
├── Python_Scripts/
│   ├── generate_synthetic_data.py            # Python script to generate synthetic data
├── SQL_Queries/
│   ├── queries.sql                 # SQL queries to derive business insights
├── Reports/
│   ├── library_management_system_report.pdf  # Final project report
├── README.md                                 # This file
├── requirements.txt                          # Dependencies and setup requirements 
```

# Project Setup and Execution Guide

## Requirements

### Prerequisites

- Database: PostgreSQL
- Database Tool: pgAdmin
- Python: Version 3.8 or above

### Python Libraries

The following Python libraries are required for the project:

- `psycopg2`
- `faker`
- `dotenv`

To install the required Python libraries, run the following command:

```bash
pip install -r requirements.txt
```



## Step 1: Repository Setup

1. Clone the repository from GitHub:

    ```bash
    git clone <https://github.com/Bhoomikak18/Agenix-Training>
    ```

2. Navigate to the `Week1-SQL` directory:

    ```bash
    cd Week1-SQL
    ```

---

## Step 2: PostgreSQL Setup

1. Install PostgreSQL and pgAdmin if they are not already installed on your system.

2. Open pgAdmin and set up a new database named `lms_db`.

3. Run the `schema_design.sql` script from the `Schema` folder to create the required database schema.

4. Populate the database by running the `data_insertion_script.sql` file to insert initial data into the database.

---

## Step 3: Generate Synthetic Data

1. Navigate to the `Python_Scripts` folder.

2. Run the Python script to generate synthetic data:

    ```bash
    python generate_synthetic_data.py
    ```

3. The generated data will then be ingested into the PostgreSQL database.

---

## Step 4: Run SQL Queries

1. Open the `queries.sql` file in your SQL client (e.g., pgAdmin).

2. Execute the queries to derive business insights and generate reports based on the data in the database.

---

## Step 5: Analyze Query Execution Plans

1. Use the `EXPLAIN` command in PostgreSQL to analyze the query execution plans for at least two queries from the `business_insights.sql` file.

2. Document your findings and any optimization opportunities you observe in the query execution plans.

---

### Business Insights Queries

1. Retrieve the top 5 most-issued books with their issue count.
2. List books and authors in the "Fantasy" genre, sorted by publication year.
3. Identify the top 3 customers who borrowed the most books.
4. List customers with overdue books (ReturnDate is null and IssueDate > 30 days).
5. Find authors with more than 3 books.
6. Retrieve authors with books issued in the last 6 months.
7. Calculate total books issued and percentage issued vs. available.
8. Generate a monthly report of issued books (month, book count, unique customer count).
9. Add appropriate indexes to optimize queries.
10. Analyze query execution plans for two queries using `EXPLAIN`.

---

### Outputs

- ER Diagram: Visual representation of the database.
- SQL Queries: Business insights and reporting.
- Reports: Final PDF summarizing the assignment.

---

## Additional Notes

- Ensure that your PostgreSQL server is running and accessible when executing SQL queries.
- The `dotenv` library should be used to manage any environment variables that may be needed for connecting to the database.

---

### License

This project is part of the Agenix Training program and is intended for educational purposes only.


