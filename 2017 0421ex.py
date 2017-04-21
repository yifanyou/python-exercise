def search4vowels(word):
    """Display any vowels in asked word"""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)

def search4letters(word:str, letters:str='aeiou') -> set:
    """Display any vowels in asked word"""
    vowels = set(letters)
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)

help(search4vowels)

word = input("Provide a word to search for vowels: ")

search4vowels(word)





