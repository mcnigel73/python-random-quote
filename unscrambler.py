print("Welcome!")

user = input("What is your alias?: ")

scramble = input(user + ", Please enter the word from the challenge you wish to unscrambe: ")

while scramble != "exit":
    if scramble == "NFOULLWO":
        print("The word you are looking for is UNFOLLOW")
    elif scramble == "COLKB":
        print("The word you are looking for is BLOCK")
    elif scramble == "RPTERO":
        print("The word you are looking for is REPORT")
    else:
        print("Please try unscrambling a word that is given in the challenge as is.")

    scramble = input(user + ", Please enter the word from the challenge you wish to unscrambe: ")
            