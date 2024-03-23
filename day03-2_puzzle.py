import os

os.system('cls')

#Sets the working directory to wherever the script is so that it can find the puzzlefile
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#Opens the puzzle file and reads it into puzzleinput variable
with open('day03_puzzleinput.txt','r') as puzzlefile:
    puzzleinput = puzzlefile.read() 

#Splits the entire file into individual lines inside a list
puzzles = puzzleinput.splitlines()

stars = []
stars_with_two_or_more_digits = []



current_puzzle = 0

for puzzle in puzzles[0::]:
   #this loop goes through each puzzle looking for symbols. If it finds one,
   #it logs the index in puzzles and the location in that puzzle.
    
    current_position = 0

    for character in puzzle:
        if character == '*':
            stars.append([current_puzzle, current_position])
        current_position += 1 
    current_puzzle += 1

print('\n\n')
print(f'Location of stars found: \n{stars}')
print('\n\n')
print(len(stars))

for star in stars:
    digitcount = 0
     
    if puzzles[star[0]-1][star[1]-1].isdigit():
        digitcount += 1
    if puzzles[star[0]-1][star[1]].isdigit():
        digitcount += 1
    if puzzles[star[0]-1][star[1]+1].isdigit():
        digitcount += 1
    if puzzles[star[0]][star[1]+1].isdigit():
        digitcount += 1
    if puzzles[star[0]+1][star[1]+1].isdigit():
        digitcount += 1
    if puzzles[star[0]+1][star[1]].isdigit():
        digitcount += 1        
    if puzzles[star[0]+1][star[1]-1].isdigit():
        digitcount += 1
    if puzzles[star[0]][star[1]-1].isdigit():
        digitcount += 1

    star.append(digitcount)
 
for i in range(len(stars)-1,-1,-1):
    if stars[i][2] < 2:
        stars.pop(i)

print('\n\n')
print(f'Location of stars with two or more digits surrounding it: \n{stars}')
print('\n\n')

print(len(stars))