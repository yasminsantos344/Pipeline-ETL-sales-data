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
- **Pandas** – Data manipulation and transformation  
- **SQL** – Data querying and storage  
- **MySQL** – Relational database for data persistence  

---

## 🔄 Pipeline Flow

### 1. Extract
- Fetch sales data from a REST API  
- Convert JSON response into a structured format (Pandas DataFrame)

### 2. Transform
- Remove duplicate records  
- Handle missing or inconsistent values  
- Standardize date formats (e.g., `YYYY-MM-DD`)  
- Normalize column names and data types  

### 3. Load
- Connect to MySQL database  
- Insert cleaned data into target tables  
- Ensure data integrity and consistency  

---

💡 Purpose

This project is designed as a beginner-friendly data engineering pipeline, demonstrating core ETL concepts and best practices using modern tools.
