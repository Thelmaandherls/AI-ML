def log_access(user, query):
    with open("access.log", "a") as f:
        f.write(f"{user['username']} queried: {query}\n")
