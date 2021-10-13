from turtle import Turtle
import time
import pandas as pd
from datetime import datetime

FONT = ('Courier', 20, 'bold')
ALIGNMENT = 'center'


class Score(Turtle):

    def __init__(self):
        super().__init__()
        # Import record for printing
        self.df = pd.read_csv('record.csv')
        self.record_breaking_round = False
        # Sort dataframe to make sure it prints the current high score
        self.df = self.df.sort_values(by='score', ascending=False)
        # Initialise score
        self.score = 0
        # Get a hold of current time
        self.game_start_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        # Initiate a dictionary to store the record by current time.
        self.current_score = {}
        # Get a hold of current high score.
        try:
            self.high_score = self.df['score'].iloc[0]
        except IndexError:
            self.high_score = 0
        self.top_score = self.df.head(3)
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.speed("fastest")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.read_and_sort()
        self.goto(0, 260)
        self.clear()
        if self.score > self.high_score:
            self.clear()
            self.high_score = self.score
            self.goto(0, 200)
            self.color('yellow')
            self.write(arg='Congrats! You broke the record!', move=False
                       , align=ALIGNMENT, font=FONT)
            self.record_breaking_round = True

        self.goto(0, 260)
        self.write(arg=f'Score: {self.score} High Score: {int(self.high_score)}', move=False
                   , align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_scoreboard(self):
        # if self.score > self.high_score:
        #     self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def gameover_countdown(self):
        if self.record_breaking_round:
            for i in range(10, 0, -1):
                self.read_and_sort()
                time.sleep(1)
                self.color('yellow')
                self.goto(0, 0)
                self.clear()
                self.write('YOU JUST SET THE RECORD!', align=ALIGNMENT, font=("Courier", 35, 'bold'))
                self.goto(0, -50)
                self.color('yellow')
                self.write(f'Final Score: {self.score}', align=ALIGNMENT, font=FONT)
                self.goto(0, -200)
                self.color('white')
                self.write(f'{self.top_score.to_string(index=False)}', align=ALIGNMENT, font=FONT)
                self.goto(0, 150)
                self.color('white')
                self.write(f'{i}', align=ALIGNMENT, font=("Courier", 100, 'bold'))
            self.record_breaking_round = False
        else:
            for i in range(5, 0, -1):
                self.read_and_sort()
                time.sleep(1)
                self.color('green')
                self.goto(0, 0)
                self.clear()
                self.write('GAME OVER', align=ALIGNMENT, font=("Courier", 50, 'bold'))
                self.goto(0, -50)
                self.color('white')
                self.write(f'Final Score: {self.score}', align=ALIGNMENT, font=FONT)
                self.goto(0, -200)
                self.color('white')
                self.write(f'{self.top_score.to_string(index=False)}', align=ALIGNMENT, font=FONT)
                self.goto(0, 150)
                self.color('white')
                self.write(f'{i}', align=ALIGNMENT, font=("Courier", 100, 'bold'))

    def record_scores(self):
        self.current_score[self.game_start_time] = self.score
        pd.DataFrame.from_dict(self.current_score, orient='index').to_csv("record.csv", mode='a', header=False)

    def read_and_sort(self):
        self.df = pd.read_csv('record.csv')
        self.df = self.df.sort_values(by='score', ascending=False)
        self.high_score = self.df['score'].iloc[0]
        self.top_score = self.df.head(3)


    # def game_over(self):
    #     self.color('green')
    #     self.goto(0, 0)
    #     self.clear()
    #     self.write('GAME OVER', align=ALIGNMENT, font=("Courier", 50, 'bold'))
    #     self.goto(0, -50)
    #     self.color('white')
    #     self.write(f'Final Score: {self.score}', align=ALIGNMENT, font=FONT)
