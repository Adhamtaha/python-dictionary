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
<<<<<<< HEAD
=======



>>>>>>> 7b7abd71a8adbbf0bc59a2b6798966de97dd24b4
