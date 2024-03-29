import random
from termcolor import colored

def choose_word():
    words = ["python", "developer", "coding", "challenge", "programming", "github"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def display_attempts(attempts_left):
    if attempts_left == 1:
        return colored(f"Attempts remaining: {attempts_left}", "red")
    else:
        return colored(f"Attempts remaining: {attempts_left}", "blue")

def save_game(player_data):
    with open(f"{player_data['name']}_saved_game.pkl", "wb") as file:
        pickle.dump(player_data, file)

def load_game(player_name):
    file_path = f"{player_name}_saved_game.pkl"
    if os.path.exists(file_path):
        with open(file_path, "rb") as file:
            return pickle.load(file)
    else:
        return None

def play_again():
    answer = input("Do you want to play again? (yes/no): ").lower()
    return answer == 'yes' or answer == 'y'

def guess_word():
    max_attempts = 5
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 0

    print(colored("Welcome to 'What's the word?'!", "green"))
    print(display_word(word_to_guess, guessed_letters))

    while attempts < max_attempts:
        current_display = display_word(word_to_guess, guessed_letters)
        print(current_display)
        print(display_attempts(max_attempts - attempts))

        guess = input(colored("Enter a letter: ", "magenta")).lower()

        if not guess.isalpha() or len(guess) != 1:
            print(colored("Please enter a single alphabet.", "yellow"))
            continue

        if guess in guessed_letters:
            print(colored("You already guessed that letter. Try again.", "red"))
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts += 1
            print(colored(f"Incorrect! {max_attempts - attempts} attempts remaining.", "red"))
        else:
            print(colored("Correct!", "green"))

        current_display = display_word(word_to_guess, guessed_letters)
        print(display_attempts(max_attempts - attempts))

        if "_" not in current_display:
            print(colored("Congratulations! You guessed the word.", "blue"))
            break

    if "_" in current_display:
        print(colored(f"Sorry, you've run out of attempts. The word was: {word_to_guess}", "red"))

if __name__ == "__main__":
    import pickle
    import os

    print(colored("Welcome to What's the word!", "blue"))
    player_name = input("Enter your name: ")
    player_password = input("Choose a password: ")

    player_data = load_game(player_name)

    if player_data and player_data["name"] == player_name and player_data["password"] == player_password:
        print(colored(f"Welcome back, {player_name}!", "green"))
    else:
        print(colored(f"Welcome, {player_name}!", "green"))
        player_data = {"name": player_name, "password": player_password, "completed_game": False}

    used_words = set()

    while True:
        guess_word()

        player_data["completed_game"] = True
        save_game(player_data)

        if not play_again():
            print("Thank you for playing 'What's the Word?' Goodbye!")
            break
