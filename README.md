# 📊 ETL Pipeline - Sales Data

## 📌 Overview
This project implements a simple **ETL (Extract, Transform, Load) pipeline** for processing sales data.

The pipeline performs the following steps:
1. **Extract** sales data from an external API  
2. **Transform** the data by cleaning, removing duplicates, and standardizing formats  
3. **Load** the processed data into a MySQL database  

---

## ⚙️ Tech Stack
- **Python** – Core programming language  
- **SQL** – Data querying and storage  
- **MySQL** – Relational database for data persistence  
- **FakeAPI** - API to extract data

---

## 🔄 Pipeline Flow

### 1. Extract
- Fetch sales data from a REST API  
- Convert JSON response into a structured format (Pandas DataFrame)

### 2. Transform
- Remove duplicate records  
- Normalize column names and data types  

### 3. Load
- Connect to MySQL database  
- Insert cleaned data into target tables  
- Ensure data integrity and consistency  

---
## 🗂️ Project Structure

```
etl-sales-pipeline/
│
├── extract.py # Handles API data extraction
├── transform.py # Data cleaning and transformation logic
├── load.py # Database connection and data insertion
├── main.py # Pipeline orchestration
├── config.py # Configuration (API URL, DB credentials)
├── requirements.txt # Project dependencies
└── README.md # Project documentation
```

---

💡 Purpose

This project is designed as a beginner-friendly data engineering pipeline, demonstrating core ETL concepts and best practices using modern tools.
