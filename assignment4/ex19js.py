def eggs(eggs_of_gold, eggs_not_of_gold):
    print(f"You have {eggs_of_gold} golden eggs!")
    print(f"You have {eggs_not_of_gold} eggs to eat!")
    print("Golden geese what a pain\n" )


print("We can just give the function numbers directly:")
eggs(1, 900)


print("Or, we can use variables from our script:")
eggs_of_gold = 25
eggs_not_of_gold = 45

eggs(eggs_of_gold, eggs_not_of_gold)


print("We can even do math inside too:")
eggs(10 +20, 5 +6)


print("And we can combine the two, variables and math:")
eggs(eggs_of_gold + 100, eggs_not_of_gold + 1000)

eggs(eggs_of_gold + 25 - 45, eggs_not_of_gold - 2 + 200)
