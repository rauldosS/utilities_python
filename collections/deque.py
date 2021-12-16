"""
Decks are double ended rows

d = collections.deque('abcdefg')
    
                | a | b | c | d | e | f | g |
appendleft()                                    append()
popleft()                                       pop()                
"""

import collections
import string


def main():
     # Boot a deck with lowercase letters
     little_letters = collections.deque(string.ascii_lowercase)

     # Decks support len() method, show deque size
     print("Item count: {}".format(str(len(little_letters))))

     # Iterate over the created deck
     for letter in little_letters:
         print(letter.upper(), end=",")

     # Manipulate items in any of the terminals
     little_letters.pop()
     little_letters.popleft()
     little_letters.append(2)
     little_letters.appendleft(1)
     print(little_letters)

     # Rotate the deck
     print(little_letters)
     little_letters.rotate(10)
     print(little_letters)


if __name__ == "__main__":
     main()