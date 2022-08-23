# %%
class A:
    def __init__(self):
        pass
    def m1(self):
        print("class A")

class B:
    def __init__(self):
        pass
    def m1(self):
        print("class B")

# %%
class C(A, B):
    def __init__(self):
        pass

c = C()
c.m1()
# %%
class C(B, A):
    def __init__(self):
        pass

c = C()
c.m1()
# %%
# super: it is a function that allows access to the parent class
class WrapperB(B):
    def __init__(self):
        pass
    
    def m1_b(self):
        super().m1()

class C(A, WrapperB):
    def __init__(self):
        pass

c = C()
c.m1()
c.m1_b()
# %%