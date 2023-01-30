"""Ex01: Chardle Assignment"""
__author__= "730490498"


word: str = input("Enter a 5-character word: ")

if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit ()
    

single_character: str = input("Enter a single character: ")
print("Searching for " + single_character + " in " + word)

if len(single_character) != 1:
    print("Error: Character must be a single character")
    exit()

if single_character == " ":
    print("Error: Character must be a single character")
    exit()

instances: int = 0

if (single_character == word[0]):
    print(single_character + " found at index 0")
    instances = instances + 1

if (single_character == word[1]):
    print(single_character + " found at index 1")
    instances = instances + 1

if (single_character == word[2]):
    print(single_character + " found at index 2")
    instances = instances + 1

if (single_character == word[3]):
    print(single_character + " found at index 3")
    instances + 1

if (single_character == word[4]):
    print(single_character + " found at index 4")
    instances = instances + 1

if (instances > 1):
    print(str(instances) + " instances of " + single_character + " found in " + word)
if (instances == 0): 
    print("No instances of " + single_character + " found in " + word)
if (instances == 1):
    print(str(instances) + " instance of " + single_character + " found in " + word)