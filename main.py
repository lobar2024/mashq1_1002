class User:
    def __init__(self, username, age=18):
        self.username = username
        self.age = age

u1 = User("sara")
u2 = User("bek", 30)
print(u1.username, u1.age)  # sara 18
print(u2.username, u2.age)  # bek 30class User:
    def __init__(self, username, age=18):
        self.username = username
        self.age = age

u1 = User("sara")
u2 = User("bek", 30)
print(u1.username, u1.age)  # sara 18
print(u2.username, u2.age)  # bek 30
