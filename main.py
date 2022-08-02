from random import choice

player_win = 0
player_lose = 0

while True:
    print("H A N G M A N")
    player_option = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if player_option == "play":
        # Initial setup
        word_to_guess = choice(["python", "java", "swift", "javascript"])
        hint = "-" * len(word_to_guess)
        print(hint)

        # Amount of "lives" the player has.
        tries_left = 8

        # Convert hint to a list, so we can modify contents by index.
        hint = list(hint)
        already_guessed = []


        def update_hint():
            # Update hint to show letters that have already been guessed.
            for i in range(0, len(word_to_guess)):
                if word_to_guess[i] == user_guess:
                    hint[i] = user_guess


        def take_input():
            guess = input("Input a letter: ")
            return guess


        while tries_left > 0:
            user_guess = take_input()
            # Check if a single character was entered and if the type is string
            if len(user_guess) == 1 and type(user_guess) == str:
                # Check if the string is lowercase
                if user_guess.islower():
                    # Check if the character has not already been guessed
                    if user_guess not in already_guessed:
                        already_guessed += user_guess
                        # Check if the guess is correct
                        if user_guess in word_to_guess:
                            update_hint()
                            print("")
                            print("".join(hint))
                            # Check if hint = word_to_guess, if it is, game is won.
                            if "".join(hint) == word_to_guess:
                                player_win += 1
                                print(f"You guessed the word {word_to_guess}!")
                                print("You survived!")
                                break
                        else:
                            # Lower tries by 1 for each try until 0.
                            tries_left -= 1
                            print("That letter doesn't appear in the word.\n")
                            print("".join(hint))
                    else:
                        tries_left -= 1
                        print("You've already guessed this letter.\n")
                        print("".join(hint))

                else:
                    print("Please, enter a lowercase letter from the English alphabet.\n")
                    print("".join(hint))
            else:
                print("Please, input a single letter.\n")
                print("".join(hint))
        else:
            player_lose += 1
            print("You lost!")

    elif player_option == "results":
        print(f"You won: {player_win} times")
        print(f"You lost: {player_lose} times")
    elif player_option == "exit":
        break
    else:
        print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
