USERS_FILE = "storage/users.json"

def load_users():
    try:
        with open(USERS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_users(users):
    with open(USERS_FILE, 'w') as file:
        json.dump(users, file, indent=4)

def register_user(name, user_id):
    users = load_users()
    users.append({"name": name, "user_id": user_id, "borrowed_books": []})
    save_users(users)
    print(f"User '{name}' registered successfully!")
