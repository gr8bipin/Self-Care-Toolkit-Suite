import random

motivation_quotes = [
"Peace comes from within. Do not seek it without.", 
"The mind is everything. What you think you become.",
"You will not be punished for your anger, you will be punished by your anger.", 
"It is a man's own mind, not his enemy or foe, that lures him to evil ways.", 
"Work out your own salvation. Do not depend on others.", 
"There is no path to happiness. Happiness is the path.", 
"We are shaped by our thoughts; we become what we think.", 
"The root of suffering is attachment.", 
"Holding on to anger is like grasping a hot coal with the intent of throwing it at someone else; you are the one who gets burned.", 
"Three things cannot be long hidden: the sun, the moon, and the truth." 
]

def motivation_quote_generator():
  random_index = random.randint(0, len(motivation_quotes) - 1)
  return motivation_quotes[random_index]

while True:
  
    print("Choose 1 for motivational quote. ")
    print("Choose 2 to exit. ") 

    choice = input("Enter your choice, 1 or 2: ")
    
    if choice == '1':
        print(motivation_quote_generator())
        print("--------------------------------------------------------------------------------------")
        print("--------------------------------------------------------------------------------------")
    elif choice == '2':
        print("Stay motivated! Bye! Bye!")
        break
    else:
        print("Wrong choice")
    