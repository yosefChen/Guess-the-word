from random import choice

def show_start_menu()->None:
    print("=" * 50)
    print("          WELCOME TO WORD GUESSER!  ")
    print("=" * 50)
    print(r"""
        _______
        |/      |
        |      (_)
        |      \|/
        |       |
        |      / \
       _|___
    """)
    print("-" * 50)
    print("  HOW TO PLAY:")
    print("  1. Guess the hidden word one letter at a time.")
    print("  2. You have 5 attempts before the game ends.")
    print("-" * 50)
    print("             Let's get started! ")
    print("-" * 50)
    print()

def show_menu()->int:
    print('Please choose from the options:')
    print('Give a letter-> 1')
    print('Exit-> 2')
    decision = get_number()
    while decision < 1 or decision > 2:
        print('Invalid choice. Please choose 1 or 2')
        decision = get_number()
    return decision

def get_number()->int:
    try:
        num = int(input('Your decision: '))
    except ValueError:
        num = 0
    return num

def choose_catagory()->int:
    print('Please choose from these categories:')
    print('Animals -> 1')
    print('Coding -> 2')
    print('Food -> 3')
    print('Space -> 4')
    print('Sports -> 5')
    print('Countries -> 6')
    print('Music -> 7')
    word_type = get_number()
    while word_type < 1 or word_type > 7:
        print('Invalid choice. Please choose from 1 - 7')
        word_type = get_number()
    return word_type

def random_word()->tuple:
    word_list_dict = {
        1: ["platypus", "giraffe", "dolphin", "tiger"],
        2: ["python", "algorithm", "dictionary", "syntax"],
        3: ["croissant", "guacamole", "spaghetti", "pizza"],
        4: ["asteroid", "nebula", "galaxy", "astronaut", "jupiter"],
        5: ["basketball", "olympics", "marathon", "volleyball", "tennis"],
        6: ["switzerland", "australia", "argentina", "thailand", "norway"],
        7: ["saxophone", "orchestra", "rhythm", "synthesizer", "guitar"]
    }
    num = choose_catagory()
    chosen_word = choice(word_list_dict[num])
    return chosen_word , ["_" for i in range(len(chosen_word))]

def show_word(failed_attempt,wrg_ltr)->None:
    print(f'You have {5-failed_attempt} more tries!')
    print(f'The letters you checked are - {" ".join(wrg_ltr)}')
    print(' '.join(guessed_letters))

def letter_choise()->str:
    letter = input('Please choose a letter from a-z or type exit to quit: ')
    while letter == 'exit' or len(letter) != 1 or letter not in "abcdefghijklmnopqrstuvwxyz":
        if letter == 'exit':
            return 'exit'
        else:
            letter = input('Wrong input! please choose a letter from a-z: ')
    return letter.lower()

def check_word(ltr,wrd)->bool:
    if ltr in wrd:
        return True
    else:
        return False
    
def write_letter(ltr,wrd,old_lst)->list:
    for i , w in enumerate(wrd):
        if ltr == w:
            old_lst[i] = w
    return old_lst

def check_existing_letters(ltr,gsd_ltr,wrng_ltr):
    if ltr in gsd_ltr or ltr.upper() in wrng_ltr:
        print('You tried this letter already!')
        return False
    else:
        return True

def check_endgame(lst,chances)->int:
    if '_' not in lst:
        return 1
    if chances == 5:
        return 2
    else:
        return 3

def win_or_lose(num,count=0):
    if num == 1 :
        print("\n" + "★" * 15)
        print("  YOU WON!!!!!!!")
        print("★" * 15)
    elif num == 2 and count<5:
        print("You used all your chances, you lost!")
    else:
        return None
        

show_start_menu()
word , guessed_letters = random_word()
wrong_letters=[]
failed_guesses_count = 0
while check_endgame(guessed_letters,failed_guesses_count) == 3:
    show_word(failed_guesses_count,wrong_letters)
    letter = letter_choise()
    if letter == 'exit':
        break
    while not check_existing_letters(letter,guessed_letters,wrong_letters):
        letter = letter_choise()
    if check_word(letter,word):
        guessed_letters = write_letter(letter,word,guessed_letters)
    else:
        failed_guesses_count += 1
        wrong_letters.append(letter.upper())
if letter == 'exit':
    pass
elif check_endgame(guessed_letters,failed_guesses_count) == 1:
    win_or_lose(1,)
else:
    win_or_lose(2,failed_guesses_count)
word_percent = int(len([i for i in guessed_letters if i != "_"])*100/len(word))
print(f'The word was - {word}')
print(f"you've guessed corrently: {''.join(guessed_letters)} , which is {word_percent}% of the word.")
print('Come back again!')