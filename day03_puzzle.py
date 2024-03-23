import os

os.system('cls')

#Sets the working directory to wherever the script is so that it can find the puzzlefile
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#Opens the puzzle file and reads it into puzzleinput variable
with open('day03_puzzleinput.txt','r') as puzzlefile:
    puzzleinput = puzzlefile.read() 

#Splits the entire file into individual lines inside a list
puzzles = puzzleinput.splitlines()

found_symbols = []
Step1Answer = 0


current_puzzle = 0

for puzzle in puzzles[0::]:
   #this loop goes through each puzzle looking for symbols. If it finds one,
   #it logs the index in puzzles and the location in that puzzle.
    
    current_position = 0

    for character in puzzle:
        if character != '.' and not character.isdigit():
            found_symbols.append([current_puzzle, current_position])
        current_position += 1 
    current_puzzle += 1

print('\n\n')
print(f'Location of symbols found: {found_symbols}')
print('\n\n')

def numberfinder(puzzle,init_position):
    #this function will take a row and a starting position and look left and 
    #right until it finds the first non-digit. It will then return an INT of 
    #what it finds.

    #Looking left
    if init_position > 0:
        #init_position is a digit so it moves the current position to the left
        current_position = init_position -1

        #print(f'init_position: {init_position}')
        #print(f'current_position: {current_position}')

        while puzzle[current_position].isdigit() and current_position >= 0:
            current_position -= 1
            #print('inside while loop')
            #print(f'current_position: {current_position}')
            
        current_position += 1
        #print(f'current_position: {current_position}')
    
    start = current_position

    if init_position < len(puzzle)-1:
        current_position = init_position + 1

        #print(f'init_position: {init_position}')
        #print(f'current_position: {current_position}')
        #print(f'Len of puzzle: {len(puzzle)}')

               
        while current_position < (len(puzzle)) and puzzle[current_position].isdigit():
            current_position += 1
            #print('inside while loop')
            #print(f'current_position: {current_position}')
            #if current_position == len(puzzle)-1:
                #break
        
        current_position -= 1
        #print(f'current_position: {current_position}')

    end = current_position

    value_to_return = puzzle[start:end+1:]

    puzzle_to_return = puzzle[:start] + ('.' * len(value_to_return) + puzzle[end+1:])
    
    return int(value_to_return),puzzle_to_return




for i in found_symbols:
    print(f'Location of symbol: {i}\n')
    print('---------10--------20--------30--------40--------50--------60--------70--------80--------90-------100-------110-------120-------130------140')
    print('01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789')
    print(f'\n{puzzles[i[0]-1]}')
    print(puzzles[i[0]])
    print(f'{puzzles[i[0]+1]}\n')
  
    #Look left of symbol
    if puzzles[i[0]][i[1]-1].isdigit():
        print(f'Found digit to the left: {puzzles[i[0]][i[1]-1]}')
                
        print(numberfinder(puzzles[i[0]],i[1]-1))
        print(f'Current Sum: {Step1Answer}')
                
               
        returned_value, returned_puzzle = numberfinder(puzzles[i[0]],i[1]-1)
        returned_value = int(returned_value)

        Step1Answer += returned_value
        puzzles[i[0]] = returned_puzzle
        
        
        
        
        print(f'After adding: {Step1Answer}')

    #Look right of symbol
    if puzzles[i[0]][i[1]+1].isdigit():
        print('Found a digit to the right')
        
        print(numberfinder(puzzles[i[0]],i[1]+1))
        print(f'Current Sum: {Step1Answer}')


        returned_value, returned_puzzle = numberfinder(puzzles[i[0]],i[1]+1)
        returned_value = int(returned_value)

        Step1Answer += returned_value
        puzzles[i[0]] = returned_puzzle 

        print(f'After adding: {Step1Answer}')

    #Look Up!
    if puzzles[i[0]-1][i[1]].isdigit():
        print('Found a digit above')
        print(numberfinder(puzzles[i[0]-1],i[1]))
        print(f'Current Sum: {Step1Answer}')
        
        
        returned_value, returned_puzzle = numberfinder(puzzles[i[0]-1],i[1])
        returned_value = int(returned_value)

        Step1Answer += returned_value
        puzzles[i[0]-1] = returned_puzzle       
        

        print(f'After adding: {Step1Answer}')
    else:
        if puzzles[i[0]-1][i[1]-1].isdigit():
            print(f'Found digit to the upper left: {puzzles[i[0]-1][i[1]-1]}')
                
            print(numberfinder(puzzles[i[0]-1],i[1]-1))
            print(f'Current Sum: {Step1Answer}')
            
            returned_value, returned_puzzle = numberfinder(puzzles[i[0]-1],i[1]-1)
            returned_value = int(returned_value)

            Step1Answer += returned_value
            puzzles[i[0]-1] = returned_puzzle            
            
            
                       
            print(f'After adding: {Step1Answer}')
        
        if puzzles[i[0]-1][i[1]+1].isdigit():
            print('Found a digit to the upper right')
                
            print(numberfinder(puzzles[i[0]-1],i[1]+1))
            print(f'Current Sum: {Step1Answer}')
            

            returned_value, returned_puzzle = numberfinder(puzzles[i[0]-1],i[1]+1)
            returned_value = int(returned_value)

            Step1Answer += returned_value
            puzzles[i[0]-1] = returned_puzzle 

            print(f'After adding: {Step1Answer}')

    #Look Down!
    if puzzles[i[0]+1][i[1]].isdigit():
        print('Found a digit below')
        print(numberfinder(puzzles[i[0]+1],i[1]))
        print(f'Current Sum: {Step1Answer}')
        
        
        returned_value, returned_puzzle = numberfinder(puzzles[i[0]+1],i[1])
        returned_value = int(returned_value)

        Step1Answer += returned_value
        puzzles[i[0]+1] = returned_puzzle       
        
        
        print(f'After adding: {Step1Answer}')
    else:
        if puzzles[i[0]+1][i[1]-1].isdigit():
            print('Found a digit on the lower left')
                
            print(numberfinder(puzzles[i[0]+1],i[1]-1))
            print(f'Current Sum: {Step1Answer}')
            

            returned_value, returned_puzzle = numberfinder(puzzles[i[0]+1],i[1]-1)
            returned_value = int(returned_value)

            Step1Answer += returned_value
            puzzles[i[0]+1] = returned_puzzle       
            
            
            print(f'After adding: {Step1Answer}')
        if puzzles[i[0]+1][i[1]+1].isdigit():
            print('Found a digit on the lower right')
                
            print(numberfinder(puzzles[i[0]+1],i[1]+1))
        
            print(f'Current Sum: {Step1Answer}')
            
            
            returned_value, returned_puzzle = numberfinder(puzzles[i[0]+1],i[1]+1)
            returned_value = int(returned_value)

            Step1Answer += returned_value
            puzzles[i[0]+1] = returned_puzzle 
            
            
            print(f'After adding: {Step1Answer}')
            
    print('\n')

print(f'Step1Answer: {Step1Answer}')
print('--- END OF LINE ---')

for puzzle in puzzles:
    print(puzzle)









