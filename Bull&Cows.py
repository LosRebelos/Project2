from random import randint

def random_unique_number() -> str:
    while True:
        number = str(randint(1000, 9999))
        if len(number) == len(set(number)):
            return number

def summary(num, guess) -> int:
    bulls, cows = (0, 0)

    for i, j in zip(num, guess):
        if j in num:
            if j == i:
                bulls += 1
            else:
                cows += 1

    if bulls <= 1:
        s_bulls = str(bulls) + " bull"
    if bulls > 1:
        s_bulls = str(bulls) + " bulls"
    if cows <= 1:
        s_cows = str(cows) + " cow"
    if cows > 1:
        s_cows = str(cows) + " cows"

    return s_bulls, s_cows, bulls, cows

def start_with_zero(guess) -> bool:
    if guess[0] != "0":
        return True
    else:
        return False

def lenght_control(guess) -> str:
    if len(guess) == len(random_unique_number()):
        return True
    else:
        return False

def no_duplicates(guess) -> bool:
    if len(guess) == len(set(guess)):
        return True
    else:
        return False

def only_digit(guess) -> bool:
    if guess.isdigit():
        return True
    else:
        return False
    
def main():
    separator = 50 * "-"
    tries = 0
    
    print(f"""
{separator}
Hi there!
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
{separator}    
    """)

    num = random_unique_number()
    print(num)
    while True:
        guess = input("Enter a number: ")
        

        if not only_digit(guess):
            print("Pouze číselný vstup!")
            continue

        if not start_with_zero(guess):
            print("Číslice nesmí začínat nulou")
            continue

        if not lenght_control(guess):
            print("Číslo musí mít 4 znaky")
            continue

        if not no_duplicates(guess):
            print("Číslo musí být unikátní, bez duplikací")
            continue    
        
        tries += 1
        sum = summary(num, guess)
        print(f"""{sum[0]}, {sum[1]}
{separator}""")
        
        if sum[2] == 4:
            print(f"Correct, you've guessed the right number in {tries} guesses!")
            break
        
main()