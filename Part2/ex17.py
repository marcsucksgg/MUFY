import random
name = input("what is your name?")
codenames = ["dragon", "phoenix", "tiger", "thunder"]
print("marcus " + "your codename is: " + random.choice(codenames) )
print("your lucky number is:" + str(random.randint(0,100)))