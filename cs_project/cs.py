import turtle
import time
import random

class WhackAMoleGame:
    def __init__(self):
        self.score = 0
        self.mole_position = None
        self.game_running = True
        self.mole_speed = 0.8
        self.time_left = 30

        self.screen = turtle.Screen()
        self.screen.title("Whack-a-Mole")
        self.screen.bgcolor("dodger blue")
        self.screen.setup(width=1.0, height=1.0)

        self.score_turtle = turtle.Turtle()
        self.score_turtle.hideturtle()
        self.score_turtle.penup()
        self.score_turtle.color("white")
        self.score_turtle.goto(0, 260)
        self.score_turtle.write("Score: 0", align="center", font=("Arial", 24, "bold"))

        self.underline_turtle = turtle.Turtle()
        self.underline_turtle.hideturtle()
        self.underline_turtle.penup()
        self.underline_turtle.color("white")

        # Draw underline once
        x, y = self.score_turtle.position()
        print(self.score_turtle.position())
        text_width = 150
        self.underline_turtle.goto(x - text_width / 2, y - 5)
        self.underline_turtle.pendown()
        self.underline_turtle.forward(text_width)
        self.underline_turtle.penup()
        
        # Grid setup
        self.hole_positions = []
        self.hole_radius = 50
        self.start_x = -150
        self.start_y = 100
        self.gap = 150

        self.grid_drawer = turtle.Turtle()
        self.grid_drawer.hideturtle()
        self.grid_drawer.penup()
        self.grid_drawer.speed(0)
        self.grid_drawer.fillcolor("black")

        for row in range(3):
            for col in range(3):
                x = self.start_x + col * self.gap
                y = self.start_y - row * self.gap
                self.hole_positions.append((x, y))

                self.grid_drawer.goto(x, y - self.hole_radius)
                self.grid_drawer.begin_fill()
                self.grid_drawer.circle(self.hole_radius)
                self.grid_drawer.end_fill()

        self.mole = turtle.Turtle()
        self.screen.addshape("mole3.gif")
        self.mole.shape("mole3.gif")
        self.mole.penup()
        self.mole.speed(0)
        self.mole.hideturtle()

        self.screen.onclick(self.whack)
        

    def whack(self, x, y):
        if not self.game_running or self.mole_position is None:
            return

        mx, my = self.mole_position
        if abs(x - mx) < 40 and abs(y - my) < 40:
            self.score += 1
            self.mole_position = None
            self.mole.hideturtle()
            self.update_score()

    def update_score(self):
        self.score_turtle.clear()
        self.score_turtle.goto(0, 260)
        self.score_turtle.write(f"Score: {self.score}", align="center", font=("Arial", 24, "bold"))

    def show_mole(self):
        if not self.game_running:
            return

        self.mole_position = random.choice(self.hole_positions)
        self.mole.goto(self.mole_position)
        self.mole.showturtle()
        self.screen.update()
        time.sleep(self.mole_speed)
        self.mole.hideturtle()
        self.mole_position = None

        self.mole_speed = max(0.3, self.mole_speed - 0.02)

        self.screen.ontimer(self.show_mole, int(self.mole_speed * 1000))

    def end_game(self):
        self.game_running = False
        self.mole.hideturtle()
        self.score_turtle.goto(-700, -10)
        self.score_turtle.color("black")
        self.score_turtle.write(f"Game Over!\nFinal Score: {self.score}",
                                align="left", font=("Arial", 24, "bold"))

    def start(self):
        self.show_mole()
        self.screen.ontimer(self.end_game, 30000)
        self.screen.mainloop()

WhackAMoleGame().start()

