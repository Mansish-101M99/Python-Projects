import random
import time


def action(choice):
    h_sum = b_sum = 0
    print("Let's get started !!")
    time.sleep(1)
    
    for die in range(choice):
        person = random.randint(1, 6)
        time.sleep(1)
        print("Human got the value : ", person)
        h_sum += person
    
    time.sleep(1)
    print("\nTotal sum of human : ", h_sum)
    time.sleep(1)
    print("\nNow its bot's turn....")
    time.sleep(1)
    
    for die in range(choice):
        bot = random.randint(1, 6)
        time.sleep(1)
        print("Bot got the value : ", bot)
        b_sum += bot
        
    time.sleep(1)
    print("\nTotal sum of bot : ", b_sum)
    time.sleep(2)

    total = "\n------Human Won this match---------" if h_sum > b_sum else "\n------Bot Won this match---------" if h_sum < b_sum else "\nIt's a tie......."
    print(total)
    time.sleep(1)
    

def play():
    die = 0
    rolling = " "
    while die == 0:
        choice = int(input("How many times you want the dice to roll (1 to 5) : "))
        if choice > 0 and choice < 6:
            action(choice)
            break
        else:
            print("Enter a number between 1 to 5...")
            
    print("Do you want to play again ? (Yes/No) ")
    while rolling != "yes":
        rolling = input().lower().capitalize()
        if rolling == "Yes":
            play()
        else:
            print("..........It was an amazing experience playing with a bot............")
            break
        
        

if __name__ == "__main__":
    play()