import random
import string
import secrets

word_list = [
    "Apple", "Banana", "Cat", "Dog", "Elephant", "Fish", "Guitar", "House", "Ice cream", "Jungle", "Kangaroo", "Lemon", "Mountain", "Ninja", "Orange", "Piano", "Queen", "Rabbit", "Sunflower", "Tiger", "Umbrella", "Volcano", "Watermelon", "Xylophone", "Yacht", "Zebra", "Book", "Candle", "Dragon", "Fireworks"]

def password():
    print("""
Choose your new password type:

    · weak = a word or two
    · medium = a word with numbers
    · strong = mix of lowercase letters, uppercase letters, numbers, and symbols
    """)
    type = input('The password you want is:').lower()
    while not (type == 'weak' or type == 'medium' or type == 'strong'):
        type = input('Please enter weak/medium/strong type:').lower()
    if type == 'weak':
        return weak_password()
    if type == 'medium':
        return medium_password()
    if type == 'strong':
        return strong_password()
    

def weak_password():
    random_word = random.choice(word_list)
    optional_word = ''
    if random.getrandbits(1):
        optional_word = random.choice(word_list)	
    password = random_word + optional_word
    return password

def medium_password():
    random_word = random.choice(word_list)
    random_numbers = ''.join(secrets.choice(string.digits) for i in range(4))
    password = random_word + random_numbers
    return password

def strong_password():
    random_keys = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password = ''.join(secrets.choice(random_keys) for i in range(8))
    return password

print(password())