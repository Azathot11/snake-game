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
        self.get_highestScore()

    def get_highestScore(self):
        with open('data.txt') as file:
            self.highest_score = int(file.read())
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score} High score {self.highest_score}', align='center', font=('Arial', 24, 'normal'))

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open('data.txt', mode='w') as file:
                file.write(str(self.highest_score))
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

