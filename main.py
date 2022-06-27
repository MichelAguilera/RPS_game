import random

# Sprites
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices = [rock, paper, scissors]
score = [0, 0, 0]

def main():
    def play():
        selection = int(input("Enter your selection:\n1 for Rock,\n2 for Paper,\n3 for Scissors\n")) - 1
        if selection >= 0 and selection <= 2:
            return selection
        else:
            print("Please choose 1, 2, or 3")
            main()

    selection = play()

    print(choices[selection])

    def enemy_choice():
        e_selection = random.randint(0, len(choices) - 1)
        return e_selection

    e_selection = enemy_choice()
    print(f"Computer chose: {choices[e_selection]}")

    if selection == e_selection:
        print("Tie!")
        score[2] += 1
    elif selection == e_selection - 1 or selection == e_selection + 2:
        print("You lose!")
        score[1] += 1
        score[2] += 1
    elif selection == e_selection + 1 or selection == e_selection - 2:
        print("You win!")
        score[0] += 1
        score[2] += 1

    def replay_promt():
        choice = str(input(f"Your score is: {score[0]} Wins, {score[1]} Losses.\nYou have played {score[2]} times.\nWould you like to play again? y/n = "))
        if choice == "y":
            print(chr(27) + "[2J")
            main()
        else: 
            print(chr(27) + "[2J")
            print(f"Thanks for playing!\nYour score is: {score[0]} Wins, {score[1]} Losses.\nYou have played {score[2]} times.")

    replay_promt()

print("Welcome to Rock, Paper, Scissors:\nthe revolutionary new game!")
main()