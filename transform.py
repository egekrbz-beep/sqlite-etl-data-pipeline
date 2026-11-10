def transform_user_data(raw_users):
    cleaned_users = []

    for user in raw_users:
        name = user["name"].strip().title()
        age = int(user["age"])
        email = user["email"].strip().lower()

        if 0 < age < 120:
            cleaned_users.append({
                "name": name,
                "age": age,
                "email": email

            })

    return cleaned_users

if __name__ =="__main__":
    from extract import extract_users_from_csv

    raw_data = extract_users_from_csv()
    transformed_data = transform_user_data(raw_data)

    print(f"Transformed{len(transformed_data)} users successfully:\n")
    for user in transformed_data:
        print(user)
        