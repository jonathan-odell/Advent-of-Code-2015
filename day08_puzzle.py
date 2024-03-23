import os

os.system('cls')

#Sets the working directory to wherever the script is so that it can find the puzzlefile
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#Opens the puzzle file and reads it into puzzleinput variable
with open('day08_puzzleinput.txt','r') as puzzlefile:
    puzzleinput = puzzlefile.read() 

#Splits the entire file into individual lines inside a list
puzzles = puzzleinput.splitlines()


directions = puzzles[0]
locations = {}
stepcounter = 0

for puzzle in puzzles[2::]:
    #print(puzzle)
    locations[puzzle[0:3]] = [puzzle[7:10],puzzle[12:15]]

#print(locations)


current_location = 'AAA'

do_step_one = False


while current_location != 'ZZZ' and do_step_one:

    for direction in directions:
        stepcounter += 1
        print(f'Stepcounter: {stepcounter}')
        print(f'I am currently here: {current_location}')
        if direction == 'L':
            print(f'Go Left! {direction}')
            print(f'New Location: {locations[current_location][0]}\n')
            current_location = locations[current_location][0]
            
            #current_location = locations
        elif direction == 'R':
            print(f'Go Right! {direction}')
            print(f'New location: {locations[current_location][1]}\n')
            current_location = locations[current_location][1]

        if current_location == 'ZZZ':
            break

print('I made it to ZZZ!')

print(f'It took {stepcounter} steps.\n')

count = 0
for key in locations.keys():
    if key.endswith('A'):
        count += 1
    
print(count)

count = 0
for key in locations.keys():
    if key.endswith('Z'):
        count += 1
    
print(count)




'''
direction_dictionary = {'AAA':['a','b']}


current_position = 'AAA'
turn = 'R'

if turn == 'L':
    print(direction_dictionary['AAA'][0])
else:
    print(direction_dictionary['AAA'][1])    


'''

