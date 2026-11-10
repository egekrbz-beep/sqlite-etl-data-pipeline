import sys
from database import init_database
from extract import extract_users_from_csv
from transform import transform_user_data
from load import load_users_to_database


def run_pipeline():
    print("=" * 45)
    print("Starting SQLite ETL Data Pipeline...")
    print("=" * 45)

    try:
        # Step 1: Initialize database schema
        print("[1/4] Checking and creating database tables...")
        init_database()

        # Step 2: Extract raw data from CSV
        print("[2/4] Extracting raw data from CSV...")
        raw_users = extract_users_from_csv()
        print(f"      -> Extracted {len(raw_users)} raw records.")

        # Step 3: Transform and clean data
        print("[3/4] Transforming, casting types, and validating...")
        clean_users = transform_user_data(raw_users)
        print(f"      -> Cleaned {len(clean_users)} valid records.")

        # Step 4: Load cleaned data into database
        print("[4/4] Loading cleaned records into warehouse.db...")
        inserted_count = load_users_to_database(clean_users)
        print(f"      -> {inserted_count} records inserted (duplicates ignored).")

        print("=" * 45)
        print("Pipeline execution finished successfully!")
        print("=" * 45)

    except Exception as error:
        print(f"\n[ERROR] Pipeline failed: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    run_pipeline()
    