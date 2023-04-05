# -*- coding: utf-8 -*-
"""
Tobenna Nwufo
2054054
CISC 2348

"""

def output_roster(roster):
    print("ROSTER")
    for jersey_number, rating in sorted(roster.items()):
        print(f"Jersey number: {jersey_number}, Rating: {rating}")

def add_player(roster):
    input_jersey = int(input("Enter another player's jersey number:"))
    input_rating = int(input("Enter another player's rating:"))
    roster[input_jersey] = input_rating

def remove_player(roster):
    input_jersey = int(input("Enter a jersey number:"))
    if input_jersey in roster:
        del roster[input_jersey]
    else:
        print("Jersey number not found in the roster.")

def update_player_rating(roster):
    input_jersey = int(input("Enter a jersey number: "))
    if input_jersey in roster:
        input_rating = int(input("Enter a new rating for player: "))
        roster[input_jersey] = input_rating
    else:
        print("Jersey number not found in the roster.")

def output_players_above_rating(roster):
    input_rating = int(input("Enter a rating: "))
    print(f"ABOVE {input_rating}")
    for jersey_number, rating in sorted(roster.items()):
        if rating > input_rating:
            print(f"Jersey number: {jersey_number}, Rating: {rating}")

roster = {}
for i in range(5):
    input_jersey = int(input(f"Enter player {i+1}'s jersey number:\n"))
    input_rating = int(input(f"Enter player {i+1}'s rating:\n"))
    print()
    roster[input_jersey] = input_rating
    
output_roster(roster)
    
while True:
    print("\nMENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit\n")
    choice = input("Choose an option:\n")

    if choice == 'a':
        add_player(roster)
    elif choice == 'd':
        remove_player(roster)
    elif choice == 'u':
        update_player_rating(roster)
    elif choice == 'r':
        output_players_above_rating(roster)
    elif choice == 'o':
        output_roster(roster)
    elif choice == 'q':
        break
    else:
        print("Invalid choice. Please choose a valid option.")