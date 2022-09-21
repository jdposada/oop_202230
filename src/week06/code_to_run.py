# %%
# Single User Example

from budget import Budget, User
user1 = User(name="jose", total_budget=1000)

user1.add_budget(category="food",
                 innitial_balance=400)
# %%
user1.add_budget(category="rent",
                 innitial_balance=300)
# %%
user1.add_budget(category="entertaiment",
                 innitial_balance=250)
# %%
# Let's attempt o create one that is greater than remaining
user1.add_budget(category="clothing",
                 innitial_balance=100)
# %%
user1.add_budget(category="clothing",
                 innitial_balance=50)
# %%
# let's do a transfer
user1.transfer_balance("food", "clothing", 100)

# %%
# Now try to use a command line interface to get more than one user