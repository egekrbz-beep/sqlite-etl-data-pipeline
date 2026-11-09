# SQLite Production-Grade ETL Pipeline & Relational Reporting

A lightweight, production-grade Python ETL (Extract, Transform, Load) pipeline demonstrating data ingestion, data sanitization, dead-letter queue (DLQ) error isolation, relational schema modeling with SQLite, and formatted SQL JOIN reporting.

---

## Architecture Overview
+-------------------+
                  |   ogrenciler.csv  | (Raw / Dirty Ingestion)
                  +---------+---------+
                            |
                            v
                  +-------------------+
                  |   ETL Pipeline    | (Type Casting & Validation)
                  +----+---------+----+
                       |         |
        [Invalid Rows] |         | [Valid Clean Rows]
                       v         v
 +-----------------------+     +-----------------------+
 |      hatalar.log      |     |        okul.db        |
 |  (Dead-Letter Queue)  |     |   (SQLite Database)   |
 +-----------------------+     +-----------+-----------+
                                           |
                                           v
                               +-----------------------+
                               |  add_grades.py (Mock) |
                               +-----------+-----------+
                                           |
                                           v
                               +-----------------------+
                               |    query_join.py      | (INNER JOIN + Tabular Report)
                               +-----------------------+

---

## Key Features

- **Automated Ingestion & Sanitization (`pipeline.py`):** Reads CSV data, handles trailing whitespaces, performs safe type conversions, and isolates corrupted records.
- **Dead-Letter Queue (DLQ) Pattern:** Quarantines corrupt rows into a structured log file (`hatalar.log`) without interrupting pipeline execution.
- **Bulk Loading Performance:** Utilizes `cursor.executemany()` for batch insertion and transactional integrity.
- **Relational Data Modeling (`add_grades.py`):** Establishes a secondary relational entity linked via Foreign Key / Primary Key constraints.
- **SQL INNER JOIN Reporting (`query_join.py`):** Joins relational entities and renders a CLI reporting dashboard with dynamic `f-string` tabular padding.

---

## File Structure

```text
├── .gitignore          # Excludes *.db, *.log, and runtime caches
├── pipeline.py         # Ingestion, validation, and DLQ handling
├── add_grades.py       # Secondary relational table generation
├── query_join.py       # SQL INNER JOIN query and formatted dashboard
├── sorgula.py          # Standalone verification query script
└── ogrenciler.csv      # Sample dirty dataset for pipeline validation