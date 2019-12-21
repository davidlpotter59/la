message = input("Enter a message: ")
print(message.lower())
print(message.upper())
print(message.capitalize())
print(message.title())



words = message.split()
print(words)


sorted_words = sorted(words)

print(sorted_words[0])
print(sorted_words[-1])

