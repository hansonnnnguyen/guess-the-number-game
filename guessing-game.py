import random

secret_num = random.randint(1, 100)
guesses = 0

while True:
    print("\nWelcome to Guess-The-Number!!!\n")

    level = input("Choose your level: Easy / Medium / Hard: ").lower()

    if level == "easy":
        secret_num = random.randint(1, 20)
        max_tries = 15
        print("Choose a number between 1 - 20 (15 tries)\n")
    elif level == "medium":
        secret_num = random.randint(1, 50)
        max_tries = 10
        print("Choose a number between 1 - 50 (10 tries)\n")
    elif level == "hard":
        secret_num = random.randint(1, 100)
        max_tries = 5
        print("Choose a number between 1 - 100 (5 tries)\n")
    else:
        print("Sorry that is not any of the options!")


    while max_tries != 0:
            guess = int(input("Enter number: "))
            guesses += 1
            
            if guess > secret_num:
                max_tries -= 1
                print("Too high! Remaining tries:", max_tries)
            elif guess < secret_num:
                max_tries -= 1
                print("Too low! Remaining tries:", max_tries)
            else:
                print(f"Correct! You guessed the secret number {secret_num}! Tries:{max_tries}")
                break

            
            differences = abs(secret_num - guess) # 6 - 25 = 19(differences)
            if differences >= 10:
                print("Hint: You're really far!\n")
            elif differences < 10:
                print("Hint: You're really close!\n")
                
    else:
        print("You are out of tries!")
    play_again = input("Would you like to play again? (y/n)\n").lower()
    if play_again != "y":
        print("\nThanks for playing!")
        break

        
   