types_of_people = 10
x = f"there are {types_of_people} types of people"

binary = "binary"
do_not = "don't"
y = f"those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of....."
e = "a string with two sides I suppose this is the right."

print(w + e)
