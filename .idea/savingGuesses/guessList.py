def get_redGuesses():
    red_guesses = []
    with open("redGuesses.txt", "r") as file:
        for line in file:
            red_guesses.append({"guess": line.rstrip("\n\r")})
        return red_guesses


def add_redUsername(guess):
    with open("redGuesses.txt", "a") as file:
        file.write(username + "\n")


def get_blueGuesses():
    blue_guesses = []
    with open("blueGuesses.txt", "r") as file:
        for line in file:
            blue_guesses.append({"guess": line.rstrip("\n\r")})
        return blue_usernames


def add_blueUsername(guess):
    with open("blueGuesses.txt", "a") as file:
        file.write(guess + "\n")