from random import randint, sample

class Balls:
    def __init__(self, color: str, n_balls: int) -> None:
        self.color = color
        self.n_balls = n_balls

class Hat:
    def __init__(self, colors: list, n_balls: list) -> None:
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
    def __init__(self, hat: Hat) -> None:
        self.hat = hat
    
    def run_experiment(self, n_sample: int):
        
        experiment_result = {}
        # this function suffle the list randomly. This is it alters the order randomly
        shuffled_colors = sample(population=self.hat.colors, 
                                  k=len(self.hat.colors))

        n_remaining = n_sample
        for color in shuffled_colors:
            ball = self.hat.balls[color]
            if n_remaining > 0:
                n_balls_experiment = randint(1, n_remaining)
                experiment_result.update({color: n_balls_experiment / n_sample})
                n_remaining = n_remaining - n_balls_experiment
        
        return experiment_result
    
    def run_multiple_experiments(self, n_experiments: int, n_sample: int):
        
        experiments = {color: [] for color in self.hat.colors}
        for i in range(n_experiments):
            experiment_result = self.run_experiment(n_sample=n_sample)

            for color, prob in experiment_result.items():
                experiments[color].append(prob)
        
        return experiments



