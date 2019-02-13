
input_word = input("Word to check if it is a palindrome: ")
input_word = input_word.lower()
test_word = ""
for char in range(len(input_word)-1, -1, -1):
    test_word += input_word[char]
if input_word == test_word:
    print("'Tis a palindrome!")
else:
    print("Sorry, but 'tis not a palindrome.")
