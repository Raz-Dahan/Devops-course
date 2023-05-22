
def is_palindrome():
    WORD = input('Enter a string:')
    R_WORD = WORD[::-1]
    if WORD == R_WORD:
        return 'palindrome'
    else:
        return 'not a palindrome'


print(is_palindrome())
