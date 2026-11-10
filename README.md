# SQLite ETL Data Pipeline

A modular, production-ready ETL (Extract, Transform, Load) pipeline implemented in Python and SQLite, designed with industry-standard separation of concerns, robust error handling, and idempotent loading.

---

## 🏗 Architecture & Workflow

```text
[ users_data.csv ]  (Raw CSV Source)
        │
        ▼ (Extract)
[ extract.py ]      (CSV parsing via DictReader)
        │
        ▼ (Transform)
[ transform.py ]    (Type casting, string normalization, range validation)
        │
        ▼ (Load)
[ load.py ]         (Batch insertion with SQLite 'INSERT OR IGNORE')
        │
        ▼
[ warehouse.db ]    (Relational database storage)
        ▲
        │ (Query)
[ query.py ]        (Analytics and formatted terminal reporting)

sqlite-etl-data-pipeline/
├── database.py       # SQLite connection and schema initialization
├── extract.py        # Extraction module: parses raw CSV data
├── transform.py      # Transformation module: data cleaning & validation
├── load.py           # Loading module: idempotent batch database writing
├── pipeline.py       # Orchestrator: end-to-end pipeline execution & logging
├── query.py          # Data retrieval and analytics reporting
├── users_data.csv    # Source raw input dataset
└── warehouse.db      # SQLite database file (created on runtime)

⚙️ Key Engineering Highlights
Decoupled Architecture: Each step of the ETL cycle is isolated in dedicated modules with distinct responsibilities.

Idempotency: Safe repeated pipeline runs using INSERT OR IGNORE combined with UNIQUE email constraints to prevent duplicate entries.

Data Cleansing: Strips whitespace, standardizes name casing (.title()), normalizes email formatting (.lower()), and enforces valid age limits.

Defensive Error Handling: Uses try-except blocks with error reporting directed to sys.stderr and non-zero exit codes (sys.exit(1)).

🚀 Getting Started
1. Prerequisites
Python 3.9+

SQLite3 (bundled with standard Python installation)
