import os
import extraFunctions as ef
import tournamentFunctions as tf


def open_tournament_Menu():
    tournament_name = ef.get_non_empty_string("What is the name of the tournament? \nEnter:  ")
    while True:
        if not os.path.exists(tournament_name):
            print("The tournament doesn't exist!")
            break
        print("What would you like to do?")
        print("1. View Tournament Information")
        print("2. View Players")
        print("3. View Leaderboard")
        print("4. Edit Tournament Information")
        print("5. Edit Player Information")
        print("6. Run Tournament")
        print("7. Go Back")
        userInput = ef.get_valid_integer("Enter your choice: ")
        if userInput == 1:
            pass
        elif userInput == 2:
            pass
        elif userInput == 3:
            pass
        elif userInput == 4:
            pass
        elif userInput == 5:
            pass
        elif userInput == 6:
            pass
        elif userInput == 7:
            break
        else:
            print("Invalid choice!")


def run_tournament_Menu(tournament_name):
    while True:
        print("What would you like to do?")
        print("1. View Leaderboard")
        print("2. Create Pairings")
        print("3. Update Scores")
        print("4. Edit Current Round")
        print("5. Go Back")
        userInput = ef.get_valid_integer("Enter your choice: ")
        if userInput == 1:
            pass
        elif userInput == 2:
            pass
        elif userInput == 3:
            pass
        elif userInput == 4:
            pass
        elif userInput == 5:
            break
        else:
            print("Invalid choice!")


if "__main__" == __name__:
    while True:
        print("Welcome to Swiss Matchmaking. What would you like to do?")
        print("1. Create tournament")
        print("2. Open a tournament")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            tf.create_tournament()
        elif choice == "2":
            open_tournament_Menu()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")
