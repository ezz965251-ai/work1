def count_vowels(text):
    vowels = ['a','o','e','y']
    count = 0
    for letter in text:
        print(letter)
        if letter in vowels:
            count += 1
    return count
print(count_vowels("привет"))