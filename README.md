# E-Library Project

This project sets up a digital library system using PostgreSQL. It includes scripts to create the database schema, generate dummy data, and insert it into the database.

# Project Structure

        project_elibrary/
        ├── main_elibrary.py             # Main script to run all steps
        └── code_elibrary/
            ├── e-library.sql            # SQL script to create database structure
            ├── elibrary_dummy_gen.py    # Python script to generate dummy data (CSV)
            ├── insert_data_library.sh   # Shell script to insert CSV data into the database
            └── dummy_elibrary/          # Folder containing generated CSV files
                ├── users.csv
                ├── addresses.csv
                └── ...

# Requirements

Ensure the following are installed on your system:

-- Python 3.x
-- PostgreSQL
-- psql (PostgreSQL CLI tool)
-- Access to a PostgreSQL database named e_library with user postgres

    Note: You must create the e_library database before running the scripts.

# ▶ How to Run

  Navigate to the project directory:

  cd project_elibrary

  (Optional) Make the shell script executable:
  
  chmod +x code_elibrary/insert_data_library.sh
  
  Run the main script:
  
  python main_elibrary.py

This will:

  1. Execute e-library.sql to create the database schema.
  
  2. Run elibrary_dummy_gen.py to generate dummy CSV data.
  
  3. Run insert_data_library.sh to load the data into PostgreSQL.

# 🛠 Database Configuration

  Ensure that the postgres user can run psql commands without being prompted for a password. You can achieve this by using a .pgpass file or configuring pg_hba.conf to allow trusted connections.
  
  Example database access in the scripts:
  
  psql -U postgres -d e_library


