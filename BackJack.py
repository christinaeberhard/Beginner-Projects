import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

new_round = input("Hi there! Do you wanna play a game of Black Jack? Type 'y' or 'n'. ")

if new_round == "y":
    user_choice = random.choices(cards, k=2)
    user_score = sum(user_choice)
    user_difference = 21 - user_score
    dealer_choice = random.choices(cards, k=2)
    dealer_score = sum(dealer_choice)
    dealer_difference = 21 - dealer_score
    print(f"Your cards: {user_choice}, current score: {user_score}.")
    print(f"Computer's first card: {dealer_choice[0]}")
    should_continue = True

    while should_continue:
        another_card = input("Do you wanna take another card? 'y' or n'? ")
        if another_card == "y":
            third_card = random.choice(cards)
            user_choice.append(third_card)
            final_score = sum(user_choice)
            print(f"Your cards: {user_choice}, final score: {final_score}.")
            if final_score == 21:
                should_continue = False
                print(f"Your score is 21, the computer's score is {dealer_score}. You win!")
            elif final_score > 21:
                should_continue = False
                print(f"Your score is {final_score}, the computer's score is {dealer_score}. You lose!")
            elif final_score < 21:
                should_continue = True
            else:
                if dealer_difference > user_difference:
                    print(f"Your score is {final_score}, the computer's score is {dealer_score}. You win!")
                elif dealer_difference == user_difference:
                    print(f"Your score is {final_score}, the computer's score is {dealer_score}. That's a Draw!")
                else:
                    print(f"Your score is {final_score}, the computer's score is {dealer_score}. You lose!")
        else:
            should_continue = False
            if dealer_difference > user_difference:
                print(f"Your score is {user_score}, the computer's score is {dealer_score}. You win!")
            elif dealer_difference == user_difference:
                print(f"Your score is {user_score}, the computer's score is {dealer_score}. That's a Draw!")
            else:
                print(f"Your score is {user_score}, the computer's score is {dealer_score}. You lose!")

