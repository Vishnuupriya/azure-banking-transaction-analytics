````markdown
# Azure Banking Transaction Analytics Lakehouse

An end-to-end Azure Data Engineering project that implements a modern banking analytics lakehouse using Azure Data Lake Storage Gen2, Azure Data Factory, Azure Databricks, PySpark, Spark SQL, and Delta Lake.

The project demonstrates data ingestion, transformation, data quality validation, Slowly Changing Dimension Type 2 (SCD Type 2), analytical data modeling, and pipeline orchestration.

---

## 🏗️ Architecture

```text
Synthetic Banking CSV Files
            |
            v
   Azure Data Lake Storage Gen2
          Raw Layer
            |
            v
    Azure Data Factory
      Orchestration
            |
            v
      Azure Databricks
            |
            v
       Bronze Layer
            |
            v
       Silver Layer
            |
      +-----+-----+
      |           |
      v           v
 Data Quality   SCD Type 2
      |           |
      +-----+-----+
            |
            v
        Gold Layer
            |
            v
   Analytics-Ready Tables
````

---

## 🛠️ Technologies Used

* Azure Data Lake Storage Gen2
* Azure Data Factory
* Azure Databricks
* PySpark
* Spark SQL
* Delta Lake
* Python
* Git & GitHub

---

## 📊 Dataset

Synthetic banking data was generated for this project.

| File               | Records | Description             |
| ------------------ | ------: | ----------------------- |
| `customers.csv`    |   1,000 | Customer information    |
| `accounts.csv`     |   1,200 | Customer bank accounts  |
| `transactions.csv` |  10,000 | Banking transactions    |
| `branches.csv`     |      20 | Bank branch information |

### Data Relationships

```text
Customers
    |
    | customer_id
    v
Accounts
    |
    | account_id
    v
Transactions
```

---

## 🔄 Data Pipeline

### 1. Raw Layer

The four CSV files are uploaded to an Azure Data Lake Storage Gen2 `raw` container.

```text
customers.csv
accounts.csv
transactions.csv
branches.csv
```

### 2. Bronze Layer

Raw data is loaded into Databricks Bronze tables and stored using Delta format.

```text
bronze_customers
bronze_accounts
bronze_transactions
bronze_branches
```

### 3. Silver Layer

The Silver layer cleans and transforms the Bronze data.

Operations include:

* Data type conversion
* Data cleaning
* Standardization
* Preparing customer, account, transaction, and branch data for analytics

Silver tables:

```text
silver_customers
silver_accounts
silver_transactions
silver_branches
```

---

## ✅ Data Quality

A dedicated data quality process validates the Silver layer before further processing.

The data quality stage is used to validate the transformed data and ensure that it is suitable for downstream processing.

---

## 🔁 SCD Type 2

Slowly Changing Dimension Type 2 is implemented for customer data to preserve historical changes.

The customer dimension maintains:

```text
customer_id
name
city
state
effective_start_date
effective_end_date
is_current
```

When tracked customer attributes change, the previous record is closed and a new current version is created.

Example:

```text
Customer 1001

Version 1
City = Chennai
is_current = false

        ↓ Customer information changes

Version 2
City = Bangalore
is_current = true
```

This preserves customer history instead of overwriting previous values.

---

## ⭐ Gold Layer

The Gold layer contains business-ready analytical tables.

### Customer Transaction Summary

`gold_customer_transaction_summary`

Contains:

* Total transactions
* Total transaction amount
* Average transaction amount
* Customer information

### Daily Transaction Summary

`gold_daily_transaction_summary`

Contains:

* Transaction date
* Total transactions
* Total transaction amount
* Average transaction amount

### Account Transaction Summary

`gold_account_transaction_summary`

Contains:

* Account information
* Total transactions
* Total transaction amount
* Average transaction amount

### Transaction Analysis

`gold_transaction_analysis`

Provides transaction analysis by:

* Transaction type
* Channel
* Total transactions
* Total amount
* Average amount

---

## ⚙️ Azure Data Factory Orchestration

Azure Data Factory orchestrates the Databricks processing notebooks.

The final pipeline is:

```text
silver_layer
      |
      v
silver_data_quality_check
      |
      v
SCDType2_Production
      |
      v
gold_layer
```

Each activity runs sequentially after the successful completion of the previous activity.

The complete pipeline was successfully executed with all activities completing successfully.

---

## 📓 Databricks Notebooks

The project includes the following notebooks:

```text
01_bronze_ingestion_code
02_silver_layer
03_silver_data_quality_check
04_SCDType2- Checks
05_SCDType2_Production
06_gold_layer
```

| Notebook                       | Purpose                                |
| -------------------------------| -------------------------------------- |
| `01_bronze_ingestion_code`     | Bronze data ingestion                  |
| `02_silver_layer`              | Data cleaning and transformation       |
| `03_silver_data_quality_check` | Silver layer data validation           |
| `04_SCDType2- Checks`          | SCD Type 2 testing                     |
| `05_SCDType2_Production`       | Production-style SCD Type 2 processing |
| `06_gold_layer`                | Creation of analytical Gold tables     |

---

## 📁 Project Structure

```text
azure-banking-transaction-analytics/
│
├── data/
│   ├── customers.csv
│   ├── accounts.csv
│   ├── transactions.csv
│   └── branches.csv
│
├── notebooks/
│   ├── 01_bronze_ingestion_code.ipynb
│   ├── 02_silver_layer.ipynb
│   ├── 03_silver_data_quality_check.ipynb
│   ├── 04_SCDType2- Checks.ipynb
│   ├── 05_SCDType2_Production.ipynb
│   └── 06_gold_layer.ipynb
│
│
├── architecture/
│   └── architecture.png
│
├── screenshots/
│   ├── adls_raw.png
│   ├── bronze_tables.png
│   ├── silver_tables.png
│   ├── data_quality.png
│   ├── scd_type2.png
│   ├── gold_tables.png
│   └── adf_pipeline.png
│
└── README.md
```

---

## 🎯 Key Data Engineering Concepts

This project demonstrates practical experience with:

* Azure Data Lake Storage Gen2
* Azure Data Factory
* Azure Databricks
* PySpark
* Spark SQL
* Delta Lake
* Medallion Architecture
* ETL / ELT
* Data Quality
* Data Transformation
* Slowly Changing Dimension Type 2
* Data Warehousing Concepts
* Analytical Aggregations
* Pipeline Orchestration
* Git & GitHub

---

## 🚀 Project Outcome

This project implements an end-to-end Azure data engineering workflow that transforms raw banking transaction data into cleaned, validated, historically tracked, and analytics-ready datasets.

Azure Data Factory orchestrates the Databricks processing workflow across the Bronze, Silver, and Gold layers.

---

## 👩‍💻 Author

**Vishnuu Priya**

Azure Data Engineer | Azure | Databricks | PySpark | SQL

```
```

