import sqlite3


def load_users_to_database(users, db_name="warehouse.db"):
    conn= sqlite3.connect(db_name)
    cursor = conn.cursor()

    user_tuples = [
        (user["name"], user["age"], user["email"])
        for user in users
    ]   

    cursor.executemany("""
        INSERT OR IGNORE INTO users (name, age, email)
        VALUES (?, ?, ?)
    """, user_tuples)

    conn.commit()
    rows_inserted = cursor.rowcount
    conn.close()

    return rows_inserted


if __name__ == "__main__":
    from extract import extract_users_from_csv
    from transform import transform_user_data

    raw_data = extract_users_from_csv()
    clean_data = transform_user_data(raw_data)
    count = load_users_to_database(clean_data)

    print(f"Loaded {count} users into the database successfully.")
