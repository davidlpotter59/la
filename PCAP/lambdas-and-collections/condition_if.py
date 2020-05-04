#!/usr/local/bin/python3.9
my_var = 1 if 1 == 2 else 3
print(my_var)

print("A") if my_var == 3 else print("No way")

name = input("What is your first name? ")

print("Your name is as long or longer than the average first name in the United States"
) if len(name) >= 5 else print(
    "Your name is shorter than the average first name in the United States"
)

message = (
    "The first letter in your name is among the five most common"
    if name[0].lower() in ["a", "j", "m", "e", "l"]
    else "The first letter of your name is not among the five most common"
)

for letter in name:
    print(
        f"{letter} {'is a vowel' if letter.lower() in ['a', 'e', 'i', 'o', 'u'] else 'is a consonant'}"
    )

print(message)