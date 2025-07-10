# Basketball Game Simulation
#### Video Demo: https://youtu.be/s_UGU2zXOKk?si=SFpxSm2j78EzdtpT


#### Description:

This is my final project for **CS50’s Introduction to Programming with Python**. It is a **text-based basketball game simulator** written in Python. The game allows two users to input team names and the number of possessions for a match. It then simulates a full basketball game possession by possession using randomness to determine outcomes such as shot attempts, shot success, and point values.

Each possession is assigned to a team at random, like a virtual coin toss. The program then decides whether a shot is attempted, and if so, whether it results in a 2-pointer, a 3-pointer, or a missed shot. All this is controlled using the `random` module, which makes each simulation unique.

The score is updated live after each possession, and the game continues until all possessions are completed. If the game ends in a tie, it enters **overtime**, where three additional possessions are played. If the score remains tied after overtime, the game continues into additional overtime periods until a winner is determined, since basketball games cannot end in a tie.

At the end of the simulation, the name of the winning team is displayed in large **ASCII art** using the `pyfiglet` library, providing a visually engaging end to the game.

---

## 📁 Files Included

- **`project.py`**
  This is the main Python file that contains all the game logic:
  - Input for team names and number of possessions
  - Possession loop with score updates
  - Overtime handling
  - ASCII display of the winning team using `pyfiglet`

- **`test_project.py`**
  A separate test file created using `pytest` and `unittest.mock` to test the core functions like `calculate_score`, `simulate_possession`, and `overtime`.

- **`test_project.py`**
  A separate file with pip-installable libraries used for this project.

---

## 📦 Dependencies

- [`pyfiglet`](https://pypi.org/project/pyfiglet/)
  Used to render the winning team’s name in large ASCII text. Install it using:

  ```bash
  pip install pyfiglet

---

💡 Design Decisions

I chose to simulate a basketball game because I enjoy sports and wanted to combine that interest with programming. I wanted the game to feel dynamic, so I included play-by-play updates and added delays using time.sleep() to simulate real-time game progression.

The use of ASCII art with pyfiglet was a design choice to enhance the terminal experience and provide a satisfying visual payoff at the end of each game. I also considered a GUI version using tkinter, but for the scope of this project, I focused on perfecting the text-based version first.

To make testing possible despite the randomness, I used mocking to control random.random() and random.choice() in the test suite. This helped ensure that all edge cases like missed shots and overtime conditions were covered.

---

🏁 Final Thoughts

This project helped me apply many key Python concepts from the course: functions, conditionals, loops, imports, testing, and external libraries. It was a fun and rewarding way to combine programming with one of my personal interests—sports.

I hope you enjoy playing the simulation as much as I enjoyed building it!
