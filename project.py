import random  # Used for generating random outcomes, like coin flips and shot percentages.
import time    # Used to pause the program, creating a more dramatic, paced feel.
from pyfiglet import Figlet # Used to display the winner's name in large ASCII art text.

def main():
    # Get the names for the two teams from the user and capitalize them.
    team1_name = input("Home Team Name: ").capitalize()
    team2_name = input("Away Team Name: ").capitalize()

    # Initialize scores for both teams at 0.
    team1_score = 0
    team2_score = 0

    # This loop ensures the user enters a valid number for possessions.
    while True:
        try:
            # Ask the user how many possessions the game should have.
            num_possessions = int(input("How many possesions for this game?: "))
            break  # Exit the loop if the input is a valid integer.
        except ValueError:
            # If the user enters something that's not a number, print an error and repeat the loop.
            print ("Please select a number")

    # --- Start of the Game ---
    print("Welcome to the Text-Based Basketball Simulation!")
    print(f"{team1_name} vs. {team2_name}\n")
    time.sleep(1)  # Pause for 1 second for dramatic effect.

    # --- Main Game Loop ---
    # This loop runs for each possession in the game.
    for possession in range(num_possessions):
        print(f"--- Possession {possession + 1} ---")
        time.sleep(1) # Pause before revealing who has the ball.

        # Decide which team has the ball for this possession.
        # random.choice([True, False]) acts like a virtual coin flip.
        if random.choice([True, False]):
            # If True, Team 1 is on offense.
            offense = team1_name
            defense = team2_name
            # Simulate the possession and get the score from that play.
            score = simulate_possession(offense, defense)
            # Add the score from this possession to Team 1's total score.
            team1_score += score
        else:
            # If False, Team 2 is on offense.
            offense = team2_name
            defense = team1_name
            # Simulate the possession for Team 2.
            score = simulate_possession(offense, defense)
            # Add the score to Team 2's total score.
            team2_score += score

        # After each possession, display the updated score.
        display_score(team1_name, team1_score, team2_name, team2_score)
        print() # Add a blank line for better readability.
        time.sleep(1.5) # A slightly longer pause to let the user read the score.

    # --- End of Regulation ---
    print("--- End of Regulation ---")
    time.sleep(1)

    # Check the final score to determine the outcome.
    if team1_score > team2_score:
        # If Team 1 has a higher score, they win.
        display_winner_ascii(team1_name)
    elif team2_score > team1_score:
        # If Team 2 has a higher score, they win.
        display_winner_ascii(team2_name)
    else:
        # If the scores are equal, the game goes to overtime.
        print("It's a tie at the end of regulation! We'll go to Overtime!!!")
        time.sleep(2)
        # Call the overtime function to determine the final winner.
        team1_score, team2_score = overtime(team1_name, team2_name, team1_score, team2_score)

def simulate_possession(offense_team, defense_team):

    print(f"{offense_team} has the ball.")
    time.sleep(1)

    # Generate a random float between 0.0 and 1.0.
    shot_attempt = random.random()
    # There is a 60% chance that a shot will be attempted.
    if shot_attempt < 0.6:
        print(f"{offense_team} attempts a shot...")
        time.sleep(1)
        # If a shot is attempted, call calculate_score to see the result.
        return calculate_score(0.4) # Pass the probability of the shot being successful.
    else:
        # If no shot is taken, the possession ends with 0 points.
        print(f"{offense_team} doesn't take a shot this possession.")
        time.sleep(1)
        return 0

def calculate_score(shot_success_probability):

    # Check if the shot is successful based on the passed probability (40%).
    if random.random() < shot_success_probability:
        # The shot is good! Now, is it a 2-pointer or a 3-pointer?
        # There is a 70% chance it's a 2-pointer.
        if random.random() < 0.7:
            print("It's a 2-pointer! They score!")
            time.sleep(1)
            return 2
        # Otherwise, it's a 3-pointer (30% chance).
        else:
            print("It's a 3-pointer! They score big!")
            time.sleep(1)
            return 3
    else:
        # If the shot was not successful, it's a miss.
        print("The shot misses.")
        time.sleep(1)
        return 0

def overtime(team1_name, team2_name, team1_score, team2_score):

    print("\n--- Overtime Begins ---")
    overtime_period = 1

    # This loop will continue as long as the scores remain tied.
    while team1_score == team2_score:
        print(f"\n--- Overtime Period {overtime_period} ---")
        time.sleep(1)
        # Each overtime period consists of 3 possessions.
        for possession in range(3):
            # Just like in regulation, a coin flip decides who gets the ball.
            if random.choice([True, False]):
                team1_score += simulate_possession(team1_name, team2_name)
            else:
                team2_score += simulate_possession(team2_name, team1_name)
            # Show the score after each possession in overtime.
            display_score(team1_name, team1_score, team2_name, team2_score)
            print()
            time.sleep(1.5)
        # Increment the overtime period counter for the next loop if still tied.
        overtime_period += 1

    # When the while loop ends, it means someone is winning.
    print("--- Overtime Over ---")
    time.sleep(1)
    # Check for the winner of the overtime period.
    if team1_score > team2_score:
        display_winner_ascii(team1_name)
    else:
        display_winner_ascii(team2_name)
    # Return the final scores back to the main function.
    return team1_score, team2_score

def display_score(team1_name, team1_score, team2_name, team2_score):
    #A function to print the current score in a consistent format.
    print(f"Score: {team1_name} - {team1_score}, {team2_name} - {team2_score}")
    time.sleep(1)

def display_winner_ascii(winner):
    #Displays the winner's name using large, stylized ASCII text.
    figlet = Figlet(font='banner')
    print(figlet.renderText(f"{winner} Wins!"))

if __name__ == "__main__":
    main()
