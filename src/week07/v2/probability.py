import random

class Hat:
  def __init__(self, n_balls: int, colors: list[str]) -> None:
    self.n_balls = n_balls
    self.colors = colors
    self.balls = []
  
  def create_balls(self):

    for i in range(self.n_balls):
      ball = random.choice(self.colors)
      self.balls.append(ball)
    
class Experiment:
  def __init__(self, hat: Hat) -> None:
    self.hat = hat
  
  def run_experiment(self, n_sample: int) -> dict:
    chosen_colors = random.choices(self.hat.balls, k=n_sample)

    # get the colors chosen using a set. 
    # This function return the unique elements in a list. 
    # You could also use a for loop to do it

    unique_colors = list(set(chosen_colors))

    # now let's use a list comprehension to create the final dictionary
    prob_dict = {color: chosen_colors.count(color) / n_sample for color in unique_colors}

    return prob_dict
  
  def run_multiple_experiments(self, n_sample: int, n_experiments: int) -> dict:
    total_experiments = {color: [] for color in self.hat.colors}
    for i in range(n_experiments):
      prob_dict = self.run_experiment(n_sample=n_sample)
      # let's iterate the dictionary using their keys and values
      for color, prob in prob_dict.items():
        total_experiments[color].append(prob)
    

    return total_experiments