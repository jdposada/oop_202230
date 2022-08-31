# From problem definition to Implementation

This week we will read a problem definition, propose a UML and implement the solution on Python

## Problem Statement

### Goal

Create a Budget class that can instantiate objects based on different budget categories like food, clothing, and entertainment. These objects should allow for depositing and withdrawing funds from each category, as well computing category balances and transferring balance amounts between categories. The app should allow multiple users. 

### Considerations

This is a very interesting project as it allows not only to comprehend how a class is initialized and used, but also represented and used as input to other functions. You will learn how to add methods to your classes and print them in a way that allows complex representation of your class object at different points in the program. As a bonus, you will define a function that computes how much money you are spending across class categories as a % of your total expenses, something that can be very useful for the money-savvy programmer's among you.

### Approach

Define the purpose and flexibility of a class object; build its class methods using a modular approach and develop an understanding for how different instances of the same class can interact.

*Key concepts: Class initialization, instance methods and instance representation. Defining and using functions that take class instances as input parameters*

## UML Diagram

The simple diagram below allows a user to create as many categories as it wants and to keep track of budget items. The code for the diagram is in the `budget_uml.puml` file.

![UML Diagram](https://github.com/jdposada/oop_202230/blob/master/src/week06/budget_uml.png?raw=true)

## Python Code

A simple Python implementation using additions, substractions and dictionaries

To test the new code please run `code_to_run.py`
