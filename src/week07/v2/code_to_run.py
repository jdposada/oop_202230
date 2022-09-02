# %%
from probability import Hat, Experiment
import matplotlib.pyplot as plt
# %%
hat = Hat(n_balls=1000, colors=['red', 'green', 'blue'])
# %%
hat.create_balls()
# %%
experiment = Experiment(hat=hat)
# %%
experiment.run_experiment(n_sample=50)
# %%
mult_exp = experiment.run_multiple_experiments(n_sample=50,
                                               n_experiments=1000)
# %%
# Optional: Plot the Distribution
plt.hist(mult_exp['red'], color='r');

# %%
plt.hist(mult_exp['green'], color='g');
# %%
plt.hist(mult_exp['blue'], color='b');
# %%
# Pick at the true values
for color in hat.colors:
    count = hat.balls.count(color)
    print(f"True probability for balls of color {color} {count / hat.n_balls}")
# %%
