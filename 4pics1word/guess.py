filename = "guess.txt"


def get_Guesses():
    full_guessList = []
    with open(filename) as file:
        for line in file:
            full_guessList.append({"guess": line.rstrip("\n\r")})
        return full_guessList


def add_Guess(guess):
    with open(filename, "a") as file:
        file.write(guess + "\n")



print(add_Guess("technology"))
print(add_Guess("bubbles"))