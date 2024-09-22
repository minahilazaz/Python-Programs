# Palindrome Check: Check if a given string is a palindrome.

string1 = input('enter a string ')


if string1 == string1[::-1]:
    print('string is palinfrome')
else:
    print('string is not palinfrome')