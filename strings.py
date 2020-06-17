def form_sentence(name,age,school):
    sentence = f'{name} is {age} years old and goes to {school}'
    return sentence

def find_vowels(word,vowels):
    for letter in word:
        if letter in vowels:
            vowels[letter] += 1
    return vowels