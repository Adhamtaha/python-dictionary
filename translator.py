def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"  #convert vowel to g

        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))
print(my name is adham)
