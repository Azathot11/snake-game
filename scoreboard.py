from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highest_score = 0
        self.color('white')
        self.penup()
        self.goto(0, 250)
        # self.write(f'Score: {self.score}', align='center', font=('Arial', 24, 'normal'))
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score} High score {self.highest_score}', align='center', font=('Arial', 24, 'normal'))
        self.score += 1

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
        self.score = 0
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=('Arial', 24, 'normal'))
