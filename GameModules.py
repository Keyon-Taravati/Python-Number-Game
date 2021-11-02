import random
import sqlite3

def get_valid_guess(lower, upper):
    valid = False 
    while valid == False:
        try:
            latest_guess = int(input("Guess Number: "))
            valid = is_in_range(latest_guess, lower, upper)
        except ValueError:
            print("Invalid input")  
    return latest_guess

def is_in_range(g, l, u):
    range = True
    if g < l or g > u:
        range = False
        print("Your guess is out of range")
    return range 

def evaluate_guess(gval, true_answer):
    correct = False
    if gval > true_answer:
        print("Guess a lower number")
    elif gval < true_answer:
        print("Guess a higher number")
    else:
        print("You WIN")
        correct = True
    return correct 

def store_guess(count):
    connection = sqlite3.connect("guesses.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO guesscount VALUES (?, ?)", (None, count))
    connection.commit()
    print("Number of guesses in the last 3 games: ")
    rows = cursor.execute("SELECT numguesses FROM guesscount ORDER BY gameID DESC LIMIT 3").fetchall()
    print(rows)

def play_game(low, up):
    print("Welcome to the Guessing Game!")
    print("Pick a number between " + str(low) + " and " + str(up)) 
    done = False
    guess_count = 0
    compnumb = random.randint(low, up)
    while done == False:
        g = get_valid_guess(low, up)
        guess_count += 1 
        done = evaluate_guess(g, compnumb)  
    print("It took you " + str(guess_count) + " guesses")
    store_guess(guess_count)

