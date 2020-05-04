#!/usr/bin/env python3.8

message = input("Enter your message: ")
print(f'First character of your message is {message[0]}')

print(f'Last character of your message is {message[-1]}')


print(f'Odd index of your message is {message[1::2]}')
print(f'Even index of your message is {message[0::2]}')

print(f'Reverse of your message is {message[::-1]}')

midChar = int(len(message) / 2) 

print(f'Middle Character is {message[midChar]}')