# From problem definition to Implementation

The excercise is taken from [link](https://towardsdatascience.com/3-useful-projects-to-learn-python-classes-cf0076c36297)

## Goal

Create a lottery ball, or Hat, that takes a variable number of arguments that specify the number of balls of each color that are in the hat. Give the object the ability to pick a random number of balls from the hat, which will then be used to compute the probability of picking a certain distribution of balls over a large number of experiments”


## Considerations 

This project resides at the intersection of probability and class creation. Using a Class object as an input to model a probabilistic output should allow for neat understanding of how python classes can be used iteratively to estimate event probabilities. The project also introduces the idea of creating classes ready to handle a dynamic number of input arguments.​

## Approach

Create class object and use it to set up a probabilistic experiment in which the class object will be continuously utilized to fetch and record the result of a lottery pick.​

## Key concepts 

Class initialization with variable number of arguments, instance methods and instance representation. Using classes to compute probabilistic experiments. Class clones.


There are two implementations v1 and v2. They are very similar but give different results. Implementation v2 is simpler, Implementation v1 looks very similar to the way we solve the budget app. Extensive comments are not included. Please make your own comments

