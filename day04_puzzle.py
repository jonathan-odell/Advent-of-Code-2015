import os

os.system('cls')

#Sets the working directory to wherever the script is so that it can find the puzzlefile
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#Opens the puzzle file and reads it into puzzleinput variable
with open('day04_puzzleinput.txt','r') as puzzlefile:
    puzzleinput = puzzlefile.read() 

#Splits the entire file into individual lines inside a list
puzzles = puzzleinput.splitlines()

#print(puzzles)

part_one_sum = 0

for puzzle in puzzles:
    card_start = puzzle.find(':')+1
    divider = puzzle.find('|')
    counter = 0

    print(puzzle)
    print(f'Here are the winning numbers:{puzzle[card_start:divider]}')
    print(f'Here is what we are looking at:{puzzle[divider+1::]}')

    for i in range(divider+1,len(puzzle),3):
        print(f'\tLooking for:{puzzle[i:i+3]}')
        if puzzle[card_start:divider:].find(puzzle[i:i+3]) != -1:
            print(f'\t\tFound it!')
            counter += 1

    if counter == 0:
        print('NADA\n')
    else:
        print(f'\tCard Total: {counter} - {2**(counter-1)}')
        part_one_sum += (2**(counter-1))
        print(f'\tNew Part One Total: {part_one_sum}\n')

print(f'Part One Total: {part_one_sum}')