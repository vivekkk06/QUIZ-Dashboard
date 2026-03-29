import turtle
import time
import random

class WhackAMoleGame:
    def __init__(self):
        # Ask the player for their name
        self.player_name = turtle.textinput("Player Name", "Enter your name:")
        if not self.player_name:
            self.player_name = "Anonymous"  # Default name if nothing is entered

        # Game variables
        self.score = 0                     # Player score
        self.mole_position = None          # Current mole location (None means not visible)
        self.game_running = True           # Used to stop the game at the end
        self.mole_speed = 0.8              # How long the mole stays visible
        self.time_left = 30                # Total game time in seconds

        # File where all scores will be saved
        self.score_file = "scores.txt"

        # Setup the window
        self.screen = turtle.Screen()
        self.screen.title("Whack-a-Mole")
        self.screen.bgcolor("dodger blue")
        self.screen.setup(width=1.0, height=1.0)  # Fullscreen

        # Setup score display
        self.score_turtle = turtle.Turtle()
        self.score_turtle.hideturtle()
        self.score_turtle.penup()
        self.score_turtle.color("white")
        self.score_turtle.goto(0, 260)
        self.score_turtle.write("Score: 0", align="center", font=("Times New Roman", 24, "bold"))

        # Draw underline below score
        self.underline_turtle = turtle.Turtle()
        self.underline_turtle.hideturtle()
        self.underline_turtle.penup()
        self.underline_turtle.color("white")
        x, y = self.score_turtle.position()
        text_width = 150  # Width of underline
        self.underline_turtle.goto(x - text_width / 2, y - 5)
        self.underline_turtle.pendown()
        self.underline_turtle.forward(text_width)
        self.underline_turtle.penup()

        # Draw 3x3 grid of holes
        self.hole_positions = []   # Store all hole coordinates
        self.hole_radius = 50
        self.start_x = -150
        self.start_y = 100
        self.gap = 150             # Distance between each hole

        self.grid_drawer = turtle.Turtle()
        self.grid_drawer.hideturtle()
        self.grid_drawer.penup()
        self.grid_drawer.speed(0)
        self.grid_drawer.fillcolor("black")

        # Create 9 holes
        for row in range(3):
            for col in range(3):
                x = self.start_x + col * self.gap
                y = self.start_y - row * self.gap
                self.hole_positions.append((x, y))  # Save hole location
                self.grid_drawer.goto(x, y - self.hole_radius)
                self.grid_drawer.begin_fill()
                self.grid_drawer.circle(self.hole_radius)  # Draw hole
                self.grid_drawer.end_fill()

        # Setup the mole turtle
        self.mole = turtle.Turtle()
        try:
            self.screen.addshape("mole3.gif")  # Try loading custom mole image
            self.mole.shape("mole3.gif")
        except:
            self.mole.shape("circle")  # Use circle if image not found

        self.mole.penup()
        self.mole.speed(0)
        self.mole.hideturtle()  # Start hidden

        # Run whack() every time the screen is clicked
        self.screen.onclick(self.whack)

    def whack(self, x, y):
        # Ignore clicks if game over or mole not visible
        if not self.game_running or self.mole_position is None:
            return

        # Get mole position
        mx, my = self.mole_position

        # Check if click is close enough to the mole
        if abs(x - mx) < 40 and abs(y - my) < 40:
            self.score += 1
            self.mole_position = None   # Mole disappears
            self.mole.hideturtle()
            self.update_score()

    def update_score(self):
        # Update score display at the top
        self.score_turtle.clear()
        self.score_turtle.goto(0, 260)
        self.score_turtle.write(f"Score: {self.score}",
                                align="center", font=("Times New Roman", 24, "bold"))

    def show_mole(self):
        # Stop showing mole if game ended
        if not self.game_running:
            return

        # Choose a random hole
        self.mole_position = random.choice(self.hole_positions)
        self.mole.goto(self.mole_position)
        self.mole.showturtle()   # Show mole

        self.screen.update()
        time.sleep(self.mole_speed)  # Mole stays for some time

        self.mole.hideturtle()       # Hide mole
        self.mole_position = None    # Mole no longer exists

        # Speed up the game each cycle (minimum 0.3 sec)
        self.mole_speed = max(0.3, self.mole_speed - 0.02)

        # Schedule next mole appearance
        self.screen.ontimer(self.show_mole, int(self.mole_speed * 1000))

    def save_score(self):
        """Save the player's score in scores.txt"""
        with open(self.score_file, "a") as f:
            f.write(f"{self.player_name},{self.score}\n")

    def load_scores(self):
        """Load all scores and return the top 5"""
        scores = []
        with open(self.score_file, "r") as f:
            for line in f:
                name, score = line.strip().split(",")
                scores.append((name, int(score)))

        # Sort scores by highest first
        scores.sort(key=lambda s: s[1], reverse=True)

        return scores[:5]  # Return top 5

    def display_top_scores(self):
        # Read top scores
        top_scores = self.load_scores()
        y_start = 150

        display_turtle = turtle.Turtle()
        display_turtle.hideturtle()
        display_turtle.penup()
        display_turtle.goto(350, y_start)
        display_turtle.color("black")
        display_turtle.write("🏆 Top 5 Scores 🏆", font=("Arial", 24, "bold"))

        # Display 5 scores one below another
        for i, (name, score) in enumerate(top_scores, start=1):
            display_turtle.goto(400, y_start -10 - i * 40)
            display_turtle.write(f"{i}. {name}: {score}", font=("Comic Sans MS", 20, "normal"))

    def end_game(self):
        # Stop the game
        self.game_running = False
        self.mole.hideturtle()
        self.save_score()  # Save final score

        # Show game over text
        self.score_turtle.goto(-700, -10)
        self.score_turtle.color("black")
        self.score_turtle.write(
            f"Game Over!\nFinal Score: {self.score}",
            align="left", font=("Arial", 24, "bold")
            )

        # Show high scores on right side
        self.display_top_scores()

    def start(self):
        # Show the first mole
        self.show_mole()

        # End game after 30 sec
        self.screen.ontimer(self.end_game, 30000)

        # Start event loop
        self.screen.mainloop()

WhackAMoleGame().start()
