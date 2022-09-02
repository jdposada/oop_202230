# %%
from probability import Hat, Experiment
import matplotlib.pyplot as plt
# %%
hat = Hat(colors=['red', 'green', 'blue'],
          n_balls=[1000, 4000, 3000])

# %%
hat.create_balls()
# %%
experiment = Experiment(hat=hat)
# %%
experiment.run_experiment(n_sample=100)
# %%
results = experiment.run_multiple_experiments(n_experiments=1000,
                                             n_sample=100)
# %%
results
# %%
for color in results.keys():
    plt.hist(results[color])