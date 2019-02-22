redFilename = "redGuesses.txt"
blueFilename = "blueGuesses.txt"


def get_redUsernames():
    red_usernames = []
    with open(redFilename) as file:
        for line in file:
            red_usernames.append({"username": line.rstrip("\n\r")})
        return red_usernames


def add_redUsername(username):
    with open(redFilename, "a") as file:
        file.write(username + "\n")


def get_blueUsernames():
    blue_usernames = []
    with open(blueFilename) as file:
        for line in file:
            blue_usernames.append({"username": line.rstrip("\n\r")})
        return blue_usernames


def add_blueUsername(username):
    with open(blueFilename, "a") as file:
        file.write(username + "\n")