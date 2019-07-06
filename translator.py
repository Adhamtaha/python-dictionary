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
name = "jacob"
>>>>>>> ec597273ddb3357e42174f9f8b91b905e436d6b1
<<<<<<< HEAD
<<<<<<< HEAD
=======



>>>>>>> 7b7abd71a8adbbf0bc59a2b6798966de97dd24b4

=======
print("hej med dig")
#make a comment



>>>>>>> 7b7abd71a8adbbf0bc59a2b6798966de97dd24b4
