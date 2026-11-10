import sqlite3


def get_all_users(db_name="warehouse.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name, age, email
        FROM users
        ORDER BY name ASC;
    """)

    users = cursor.fetchall()
    conn.close()

    return users


def display_users():
    users = get_all_users()

    if not users:
        print("No users found in the database.")
        return

    print("=" * 65)
    print(f"{'NAME':<20} | {'AGE':<6} | {'EMAIL':<30}")
    print("-" * 65)

    for user in users:
        name, age, email = user
        print(f"{name:<20} | {age:<6} | {email:<30}")

    print("=" * 65)


if __name__ == "__main__":
    display_users()