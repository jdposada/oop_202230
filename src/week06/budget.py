class Budget:
    def __init__(self, category: str, innitial_balance: float) -> None:
        """
        category: the category for the particular expense like food, clothing, and entertainment
        innitial_balance: the innitial balance for the category
        """

        self.category = category
        self.innitial_balance = innitial_balance
        # running_balance: The running balance of the category after deductions or additions
        self._running_balance = innitial_balance

    
    def withdraw(self, amount: float) -> None:
        """
        Withdraw money from the running balance
        """

        self._running_balance = self._running_balance - amount
    
    def deposit(self, amount: float) -> None:
        """
        Deposit money to the running balance
        """

        self._running_balance = self._running_balance + amount
    
    def get_running_balance(self) -> float:
        """
        a getter for the available balance
        """

        return self._running_balance

class User:
    def __init__(self, name: str, total_budget: float) -> None:
        """
        name: user name
        total_budget: the total budget for a given user
        """

        self.name = name
        self.total_budget = total_budget
        self._remaining_budget = total_budget
        self.budgets = {}
    
    def add_budget(self, category: str, innitial_balance: float) -> None:
        """
        Creates a budget for a given user. Budget categories should be unique
        """
        
        if self._remaining_budget >= innitial_balance:

            budget = Budget(category=category, 
                            innitial_balance=innitial_balance)
            
            self.budgets.update({category: budget})

            self._remaining_budget = self._remaining_budget - innitial_balance
            print(f"{self._remaining_budget} are left from the total Budget")
        
        else:
            print(f"Not enough funds to allocate, please assign at most {self._remaining_budget}")
    
    def transfer_balance(self, sender: str, receiver: str, amount: float) -> None:
        """
        Transfer balance between categories
        """

        self.budgets[sender].withdraw(amount)
        self.budgets[receiver].deposit(amount)

        print(f"{sender} new balance {self.budgets[sender].get_running_balance()}")
        print(f"{receiver} new balance {self.budgets[receiver].get_running_balance()}")


