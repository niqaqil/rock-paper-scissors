import random

CHOICE = "| gun | rock | fire | scissors | snake | human | tree |\n" \
         "| wolf | sponge | paper | air | water | dragon | devil | lightning |"
USER_CHOICE = """Select your choice to play
example : rock,paper,scissors
default choice = rock | paper | scissors if no input\n"""
TURN = """!rating = check current score
!exit = exit game\n"""


def menu():
    name = input("Enter your name: ")
    print("Hello, {}!".format(name))
    # dict_name = []
    dict_name = read_file()
    rating = 0
    for key in dict_name:
        if name == key:
            print("Welcome back.")
            rating = dict_name[key]
    opt_list = ["gun", "rock", "fire", "scissors", "snake", "human", "tree",
                "wolf", "sponge", "paper", "air", "water", "dragon", "devil", "lightning"]
    print(CHOICE)
    user_choice = input(USER_CHOICE).split(",")
    print("Okay, let's start")
    comp_list = choice_list(opt_list, user_choice)
    choice = ""
    print(TURN)
    while choice != "!exit":
        check_choice = False
        win = False
        draw = False
        comp_turn = random.choice(comp_list)
        choice = input()
        if choice == comp_turn:
            check_choice = True
            draw = True
            if draw:
                rating += 50
        elif choice in comp_list:
            check_choice = True
            win = check_win(choice, comp_turn)
            if win:
                rating += 100
        elif choice == "!rating":
            print("Your rating: ", rating)
        elif choice == "!exit":
            print("Bye!")
        else:
            print("Invalid input")

        if check_choice:
            print(print_result(win, draw, comp_turn))
    write_file(name, rating)


def read_file():
    file = open("rating.txt")
    dict_name = []
    name_list = file.readlines()
    for a in name_list:
        a = a.split()
        for b in a:
            dict_name.append(b)
    file.close()
    dict_name = conv_list(dict_name)
    for key in dict_name:
        dict_name[key] = int(dict_name[key])
    return dict_name


def write_file(name, rating):
    file = open("rating.txt", 'a')
    file.write("{} {}\n".format(name, rating))
    file.close()


def choice_list(opt_list, user_choice):
    list_ = []
    if user_choice == ['']:
        list_ = ["rock", "paper", "scissors"]
    else:
        for opt in opt_list:
            if opt in user_choice:
                list_.append(opt)
    return list_


def conv_list(name_list):
    list_ = {name_list[i]: name_list[i + 1] for i in range(0, len(name_list), 2)}
    return list_


def check_win(choice, comp_turn):
    winning_cases = {
        'water': ['scissors', 'fire', 'rock', 'gun', 'lightning', 'devil', 'dragon'],
        'dragon': ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
        'devil': ['human', 'snake', 'scissors', 'fire', 'rock', 'gun', 'lightning'],
        'lightning': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
        'gun': ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
        'rock': ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
        'fire': ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
        'scissors': ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
        'snake': ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
        'human': ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
        'tree': ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
        'wolf': ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
        'sponge': ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
        'paper': ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
        'air': ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water']
    }
    if choice in winning_cases:
        if comp_turn in winning_cases[choice]:
            return True
    return False


def print_result(win, draw, comp_turn):
    if win:
        result = f"Well done. The computer chose {comp_turn} and failed"
    elif draw:
        result = f"There is a draw ({comp_turn})"
    else:
        result = f"Sorry, but the computer chose {comp_turn}"
    return result


menu()
