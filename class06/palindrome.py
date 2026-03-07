word = input("Enter the word: ").lower() #Converts captial to all small letters
reverse_word = word[::-1]
if word == reverse_word:
    print("Is a Palindrome")
else:
    print("Not a Palindrome")