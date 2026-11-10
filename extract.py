import csv


def extract_users_from_csv(file_path="users_data.csv"):
    users = []
    with open(file_path, mode="r" , encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            users.append(row)
    return users


if __name__ == "__main__":
    extracted_data = extract_users_from_csv()
    print(f"Extracted {len(extracted_data)} users successfully:")
    for user in extracted_data:
        print(user)