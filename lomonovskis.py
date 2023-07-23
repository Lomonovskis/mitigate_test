import random

def check_limit(value, min, max):
    if value < min:
        value = min
    elif value > max:
        value = max
    return value

def check_input_spelling(input_text, alternative_text, value_type):
    while True:
        try:
            value = value_type(input(input_text))
            break
        except:
            print(alternative_text)
    return value


# rules used as dictionaries instead of condiitonal statements
rules = {
    "rock": {"rock": None, "paper": 0, "scissors": 1, "lizard": 1, "spock": 0},
    "paper": {"rock": 1, "paper": None, "scissors": 0, "lizard": 0, "spock": 1},
    "scissors": {"rock": 0, "paper": 1, "scissors": None, "lizard": 1, "spock": 0},
    "lizard": {"rock": 0, "paper": 1, "scissors": 0, "lizard": None, "spock": 1},
    "spock": {"rock": 1, "paper": 0, "scissors": 1, "lizard": 0, "spock": None}
}

# this list holds names for computer, as well as used to control number of for-loop cycles together with user input
funny_names = [
    "Chris Cross",
    "Donald Duck",
    "Flint Sparks",
    "Foster Child",
    "Honey Bee",
    "Kerry Oki",
    "King Queene",
    "Max Little",
    "Stan Still",
  ]

list_keys_of_choices = list(rules.keys())
string_of_choices =   ",".join(list_keys_of_choices)

limit_rounds = check_limit(check_input_spelling("How many round would you play? Min 1 and max is 5\n", "Number of rounds shall be numeric", int), 1, 5)
limit_pc_count = check_limit(check_input_spelling("How many computers you want to play with? Min 1 and max is 9\n", "Number of rounds shall be numeric", int), 1, 9)
        
        
victory_points = 0
computer_in_game = funny_names[:limit_pc_count]

for pc_name in computer_in_game:
    
    results_man = 0
    results_pc = 0
    rounds = 0

    while rounds != limit_rounds:
        rounds += 1
        print(f"\nRound {rounds} with {pc_name}: ", end="")
        man = input(f'Make a choice of {string_of_choices} \n').lower()
        while True:
            if man in list_keys_of_choices:
                break
            man = input(f'Please make a choice of {string_of_choices} one more time with correct spelling \n').lower()
        
        pc_choice = random.choice(list_keys_of_choices)
        print(f"{pc_name} choice is {pc_choice}")
        
        result = rules[man][pc_choice]
        if result == 0:
            results_pc +=1
            print(f"{pc_name} got this round!")
        elif result == 1:
            results_man +=1
            print("You got this round!")
        else:
            print("Draw!")
            
            
    victory_points += 1 if results_man > results_pc else 0
    winner = "You won" if results_man > results_pc else "You lost" if results_pc > results_man else "You have draw with"
    print(f"{winner} {pc_name}, current victory points: {victory_points}!")
    
    
if victory_points == len(computer_in_game):
    print("You win all games!")
else:
    print("You lost!")