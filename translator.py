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
<<<<<<< HEAD
print(do you want to help)
=======

>>>>>>> ced87360b6784ffb03de08979011f5f5482d6287
<<<<<<< HEAD

=======



>>>>>>> 7b7abd71a8adbbf0bc59a2b6798966de97dd24b4
