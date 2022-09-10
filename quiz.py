import random
play_again = "yes"
while play_again == "yes":
    questions = ["How many Infinity Stones are there?","What type of scientist is Jane Foster in Thor?","What type of vehicle did Thanos briefly use in the comic books and make a brief appearance in the Loki series?","During which war did Captain America get his superhuman abilities?"]
    randomquestion = (random.choice(questions))
    def printq(question):
        print(question)
    def printoptions():
        #possibility1
        if randomquestion == "How many Infinity Stones are there?":
            print(" a) six \n b) seven \n c) five \n d) eight")
            userinput = input("Enter you choice a/b/c/d")
            if userinput == "a":
                print("You guessed it correct!")
            else:
                print("Oops, you guessed it wrong!")
        #possibility2
        if randomquestion == "What type of scientist is Jane Foster in Thor?":
            print(" a) Astronomer \n b) Biologist \n c) Chemist \n d) Dioptrics")
            userinput = input("Enter you choice a/b/c/d")
            if userinput == "a":
                print("You guessed it correct!")
            else:
                print("Oops, you guessed it wrong!")
        #possibility3
        if randomquestion == "What type of vehicle did Thanos briefly use in the comic books and make a brief appearance in the Loki series?":
            print(" a) A tank with “Infinity” written on it \n b) A helicopter with “Thanos” written on the side \n c) A car with “perfectly balanced” on the side \n d) A motorbike with “Titan” on the side")
            userinput = input("Enter you choice a/b/c/d")
            if userinput == "b":
                print("You guessed it correct!")
            else:
                print("Oops, you guessed it wrong!")
        #possibility4
        if randomquestion == "During which war did Captain America get his superhuman abilities?":
            print(" a) Civil War \n b) World War I \n c) Worlds War II \n d) The Cold War")
            userinput = input("Enter you choice a/b/c/d")
            if userinput == "c":
                print("You guessed it correct!")
            else:
                print("Oops, you guessed it wrong!")
        #possibility5
        if randomquestion == "What is the name of Peter Quill’s home planet?":
            print(" a) Mordor \n b) Goddricks Hollow \n c) Earth \n d) Morag")
            userinput = input("Enter you choice a/b/c/d")
            if userinput == "c":
                print("You guessed it correct!")
            else:
                print("Oops, you guessed it wrong!")


    printq(randomquestion)
    printoptions()
    play_again = input("Next question? (Yes/No)").lower()
    if play_again != "yes":
        break



