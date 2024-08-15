import csv
import os
import extraFunctions as ef
def create_tournament():
    # Initializes variables
    tour_name = ef.get_non_empty_string("What's the name of the tournament? \nEnter:  ")

    # Creates the directory for the tournament with the csv files
    if not os.path.exists(tour_name):
        os.makedirs(tour_name)

    # Gets the organizer of the tournament
    organizer = ef.get_non_empty_string("Organizer of the tournament? \nEnter:  ")

    # Gets the base time
    base_time = ef.get_valid_integer("Time control? \nBase time \nEnter: ")

    # Gets the time increment of the tournament
    increment = ef.get_valid_integer("Increment:\nEnter:  ")

    # Gets the location of the tournament
    location = ef.get_non_empty_string("Location:\nEnter:  ")

    # Gets the amount of rounds in the tournament
    rounds = int(ef.get_valid_integer("Rounds:\nEnter:    "))

    # Gets the date of the tournament
    date = ef.get_valid_integer("Date:\nEnter:    ")

    # Creates the time control string
    time_control = f"{base_time}+{increment}"

    # File paths inside the tournament directory
    csv_file_path = os.path.join(tour_name, f"{tour_name}.csv")
    leaderboard_file_path = os.path.join(tour_name, f"{tour_name}Leaderboard.csv")
    players_file_path = os.path.join(tour_name, f"{tour_name}Players.txt")

    # Write tournament details to CSV file
    with open(csv_file_path, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Tournament", "Organizer", "Location", "Date", "Time Control", "Rounds", "Current Round"])
        writer.writerow([tour_name, organizer, location, date, time_control, rounds, 1])

    # Write leaderboard to CSV file
    with open(leaderboard_file_path, mode='w', newline='') as leaderboardfile:
        writer = csv.writer(leaderboardfile)
        header = ["Placement", "Name", "Rating", "Score"] + [f"Round {i + 1}" for i in range(rounds)]
        writer.writerow(header)

    # Create an empty file for players
    open(players_file_path, 'w').close()