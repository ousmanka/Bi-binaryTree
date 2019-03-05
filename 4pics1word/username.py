filename = "username.txt"


def get_usernames():
    full_usernames = []
    with open(filename) as file:
        for line in file:
            full_usernames.append({"username": line.rstrip("\n\r")})
        return full_usernames


def add_username(username):
    with open(filename, "a") as file:
        file.write(username + "\n")

def delete_username(username):
    with open(filename, "r") as file:
        lines = file.readlines()
        with open(filename, "w") as file:
            for line in lines:
                if line != username + "\n":
                    file.write(line)

