print("Hello! Whats your name? ")
name = input()
print("Hi", name, "! how has your day been? (good/bad/fine)")
day=input()
if day.lower() == "good":
    print("I'm glad to hear that!")
elif day.lower() == "bad":
    print("I'm sorry to hear that.")
elif day.lower() == "fine":
    print("It's okay, sometimes days are just fine.")
else:
    print("That's interesting!")
print("What do You like to eat? (Enter a food item)")
food= input()
if food.lower() == "pizza":
    print("Great choice! Pizza is delicious.")
elif food.lower() == "sushi":
    print("Sushi is a fantastic choice!")
elif food.lower() == "salad":
    print("Salad is healthy and tasty!")
else:
    print("That sounds good!")
print("it was nice talking to you. GoodBye!",name, "or do you want to talk? (yes/no)")
continue_choice=input()
if continue_choice.lower() == "yes":
    print("Great! Let's continue our conversation.")
    game_choice = input("what is your favourite game? ")
    choice=input()
    print("That's awesome! I love", game_choice, "too!")
    print("Bye now! ", name)
else:
    continue_choice.lower() == "no"
    print("Okay, have a great day ahead!", name)