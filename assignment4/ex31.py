print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good Job!")
    elif bear == "2":
        print("The bear eats your leggs off. Good Job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

        print("""The bear wanders off with a jar of honey
         that it found. You look down the hall that you didn't
         notice before and see a faint glow.""")
        print("1. Go investigate the light.")
        print("2. Stay here I don't want to follow a bear.")

        follow = input("> ")

        if follow == "1":
            print("The bear turns around and eats your face off.")
        elif follow == "2":
            print("You get a cut and die of sepsis. Dungeons are dirty.")
        else:
            print("You win choosing not to decide is a choice.")
elif door == "2":
    print("You stare into the endless abyss at Cthulu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

else:
    print("You stumble around and fall on a knife and die. Good job!")