from random import randint

array = ["Rock", "Paper", "Scissors"]

computerScore = 0
userScore = 0

while True:
    computer = randint(0, 2)
    print("\nChoose either Rock(R), Paper(P) or Scissors(S): ")

    userChoose = input()
    if userChoose == "Stop":
        print("The final score: \nMe: " + str(computerScore) + " and you: " + str(userScore))
        print("Thanks for playing:) Goodbye!")
        break
    elif userChoose != "Rock" and userChoose != "Paper" and userChoose != "Scissors":
        print("That is not a valid choice")
        continue
    user = 0

    for i, option in enumerate(array):
        if userChoose == option:
            user = i

    if computer == user:
        print("It's a tie!")
    else:
        n = user + 1
        if n > 2:
            n = 0

        if n == computer:
            computerScore += 1
            print("I chose " + array[computer] + " therefore I won, bruh. You loser")
        else:
            userScore += 1
            print("I chose " + array[computer] + " so you won! Congrats!!!")

    print("\nScore:\nMe: " + str(computerScore) + "\nYou: " + str(userScore))

