start = '''
You wake up one morning and notice that out of all your friends, you are the only one without a prom date.
"Should I snag a date?" you wonder.
'''


print(start)

print("Do you want to know your ideal prom date?")
print("Type 'yes' or 'no'.")
user_input = input()
if user_input == "no":
    print("Do you want a date to prom? 'yes' or 'no'")
    user_input = input()
    if user_input == "no":
        print("Sell your ticket! Go somewhere where you'll actually have fun! Going to prom isn't the end of the world!")
if user_input == "yes":
    print("What is your ideal date? A. Movies B. Beach C. Restaurant D. Can't decide") # Asking the 1st "yes" question
    print ("Type 'A','B','C' or 'D'")
    user_input = input()
    if user_input == "A":
        print("Do you like___ guys? A. Tall B. Short C. Average D. Midgit")
    if user_input == "B":
        print("Do you like___ guys? A. Tall B. Short C. Average D. Midgit")
    if user_input == "C":
        print("Do you like___ guys? A. Tall B. Short C. Average D. Midgit")
    if user_input == "D":
        print("Do you like___ guys? A. Tall B. Short C. Average D. Midgit")
    user_input = input()
    if user_input == "A":
        print("What type of relationship are you into? A. Long Term B. Short Term C. Open D. No relationship")
    if user_input == "B":
        print("What type of relationship are you into? A. Long Term B. Short Term C. Open D. No relationship")
    if user_input == "C":
        print("What type of relationship are you into? A. Long Term B. Short Term C. Open D. No relationship")
    if user_input == "D":
        print("What type of relationship are you into? A. Long Term B. Short Term C. Open D. No relationship")
    user_input = input()
    print("Great! We've calculated who your ideal prom date should be from the answers you provided :")
    import random
    foo = ['Ryan Reynolds', 'Kevin Hart', 'Zac Efron', 'Danny Devito', 'Shaquille O Neal', 'Liam Hemsworth', ' Will Poulter', "young Leonardo Dicaprio', 'Jay Park', 'Drake'"]
    print(random.choice(foo))
