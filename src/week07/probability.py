from random import randint

class Balls:
    def __init__(self, color: str, n_balls: int) -> None:
        self.color = color
        self.n_balls = n_balls

class Hat:
    def __init__(self, total_balls: int, colors: list, n_balls: list) -> None:
        self.total_balls = total_balls
        self.colors = colors
        self.n_balls = n_balls
        self.balls = {}
    
    def create_balls(self):
        for i in range(len(self.colors)):
            color = self.colors[i]
            n_ball = self.n_balls[i]
            balls = Balls(color=color, n_balls=n_ball)
            self.balls.update({color: balls})

class Experiment:
    def __init__(self, hat: Hat, n_experiments) -> None:
        self.hat = hat
        self.n_experiments = n_experiments
    
    def run_experiment(self, n_sample):
        
        experiment_result = {}
        for color in self.hat.colors:
            ball = self.hat.balls[color]
            n_balls_experiment = randint(1, ball.n_balls)
            experiment_result.update({color: n_balls_experiment})
