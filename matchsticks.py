
# Online Python - IDE, Editor, Compiler, Interpreter

m = 21
print("\t\t||Game begins||\n")

for r in range(4):
    print("\nSelect 1/2/3/4 matchsticks for round ", r + 1)
    p = int(input("Matchsticks-"))
    if p < 1 or p > 4:
        print("Error.Pls select matchsticks from 1/2/3/4 only\n")
        break
    c = 5 - p
    print("\nMatchsticks picked by computer:- ", c)
    m = m - p - c
    print("\nTotal matchsticks left = ", m)
    if m == 1:
        print("\nNo. of matchsticks left is ", m)
        print("\nYour turn is last!")
        print("\nYou lost the game!Computer wins!!")