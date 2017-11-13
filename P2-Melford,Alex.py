import random
def main():
    print(":::: Welcome to the Guessing Game! ::::\n"
          "\n Choose your difficulty level"
          "\n1. - Easy(10) 2. - Medium(100) 3. - Hard(1000) ")
    user_num = int(input())
    if user_num == 1:
        easy()
    elif user_num == 2:
        medium()
    elif user_num == 3:
        hard()


def easy():
    print("First to 10 guesses loses. Good Luck!\n"
          "\n Player 1, try and guess the random number between 1 and 10")
    random_num = random.randrange(10)
    user_num = int(input())
    count = 0
    while random_num != user_num:
        if user_num < random_num:
            print("Higher")
            user_num = int(input())
            count = count + 1
        elif user_num > random_num:
            print("Lower")
            user_num = int(input())
            count = count + 1
    while random_num == user_num:
        print("Congratulations you got the number!")
        count = count + 1
        count = str(count)
        print("It took you " + count + " tries to guess the number")
        break
    print("\nPlayer 2, try and guess a number between 1 and 10 ")
    random_num2 = random.randrange(10)
    user_num2 = int(input())
    count2 = 0
    while random_num2 != user_num2:
        if user_num2 < random_num2:
            print("Higher")
            user_num2 = int(input())
            count2 = count2 + 1
        elif user_num2 > random_num2:
            print("Lower")
            user_num2 = int(input())
            count2 = count2 + 1
    while random_num2 == user_num2:
        print("Congratulations you got the number!")
        count2 = count2 + 1
        count2 = str(count2)
        print("It took you " + count2 + " tries to guess the number")
        break

    if count < count2:
        print("Player 1 wins!")
    elif count > count2:
        print("Player 2 wins!")
    else:
        print("Tie")
    replay()


def medium():
    print("First to 15 guesses loses. Good Luck!\n"
          "\n Player, try and guess the random number between 1 and 100")
    random_num = random.randrange(100)
    user_num = int(input())
    count = 0
    while random_num != user_num:
        if user_num < random_num:
            print("Higher")
            user_num = int(input())
            count = count + 1
        elif user_num > random_num:
            print("Lower")
            user_num = int(input())
            count = count + 1
    while random_num == user_num:
        print("Congratulations you got the number!")
        count = count + 1
        count = str(count)
        print("It took you " + count + " tries to guess the number")
        break
    print("\nPlayer 2, try and guess a number between 1 and 100 ")
    random_num2 = random.randrange(100)
    user_num2 = int(input())
    count2 = 0
    while random_num2 != user_num2:
        if user_num2 < random_num2:
            print("Higher")
            user_num2 = int(input())
            count2 = count2 + 1
        elif user_num2 > random_num2:
            print("Lower")
            user_num2 = int(input())
            count2 = count2 + 1
    while random_num2 == user_num2:
        print("Congratulations you got the number!")
        count2 = count2 + 1
        count2 = str(count2)
        print("It took you " + count2 + " tries to guess the number")
        break
    if count < count2:
        print("Player 1 wins!")
    elif count > count2:
        print("Player 2 wins!")
    else:
        print("Tie")
    replay()



def hard():
    print("First to 30 guesses loses. Good Luck!\n"
          "\n Player, try and guess the random number between 1 and 1000")
    random_num = random.randrange(1000)
    user_num = int(input())
    count = 0
    while random_num != user_num:
        if user_num < random_num:
            print("Higher")
            user_num = int(input())
            count = count + 1
        elif user_num > random_num:
            print("Lower")
            user_num = int(input())
            count = count + 1
    while random_num == user_num:
        print("Congratulations you got the number!")
        count = count + 1
        count = str(count)
        print("It took you " + count + " tries to guess the number")
        break
    print("\nPlayer 2, try and guess a number between 1 and 1000 ")
    random_num2 = random.randrange(1000)
    user_num2 = int(input())
    count2 = 0
    while random_num2 != user_num2:
        if user_num2 < random_num2:
            print("Higher")
            user_num2 = int(input())
            count2 = count2 + 1
        elif user_num2 > random_num2:
            print("Lower")
            user_num2 = int(input())
            count2 = count2 + 1
    while random_num2 == user_num2:
        print("Congratulations you got the number!")
        count2 = count2 + 1
        count2 = str(count2)
        print("It took you " + count2 + " tries to guess the number")
        break
    if count < count2:
        print("Player 1 wins!")
    elif count > count2:
        print("Player 2 wins!")
    else:
        print("Tie")

    replay()



def replay():
    print("\nWould you like to play again?(Y/N)"
          "\n1. Y  2. N\n "
          "\n Please choose a number")
    choice = int(input())
    if choice == 1:
        main()
    else:
        print("Game Over")



main()