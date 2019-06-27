import random

board = []

for x in range (0,6):
  board.append((["[   ]"])*6)

def print_board(board):
  for x in board:
    print (" ".join(x))

#tiles
tiles = ['seer', 'chameleon', 'juggler', 'pyro']
shapes = ['square', 'triangle', 'circle']

#outer tile designs
specific_tile_outer = {'seer': "( )", 'chameleon': "[ ]", 'juggler': "{ }", 'pyro': "| |"}

#inner tile shapes
specific_tiles = {'triangle': ' ^ ', 'square': '|_|', 'circle': ' O '}

#dictionary containing remaining tiles
specific_tile_number = {'seer_triangle' : 6, 'seer_square' : 6, 'seer_circle' : 6, 'chameleon_triangle' : 6, 'chameleon_square' : 6, 'chameleon_circle' : 6, 'pyro_triangle' : 6, 'pyro_square' : 6, 'pyro_circle' : 6,
'juggler_triangle' : 6, 'juggler_square' : 6, 'juggler_circle' : 6 }

def result():

    lives = 3

    while lives != 0:
        rand = random.randint(100, 10000) * 0.010


        if rand < 85.72:
            print(rand)
            temp_tile = (random.choice(tiles))
            temp_shape = (random.choice(shapes))

            #checks to see if there are any tiles left in the dictionary
            if all(x==0 for x in specific_tile_number.values()):
                print("There are no tiles left!")
                break

            if specific_tile_number[temp_tile + "_" + temp_shape] == 0:
                temp_tile = (random.choice(tiles))
                temp_shape = (random.choice(tiles))



            print_to_board = ""
            print ("You drew a " + temp_tile +" "+ temp_shape)

            #assigns the tile to print_to_board and prints it to the screen
            print_to_board = specific_tile_outer[temp_tile][:1] + specific_tiles[temp_shape] + specific_tile_outer[temp_tile][-1:]
            print(print_to_board)

            #This pulls from the dictionary titles specific_tile_number
            specific_tile_number[temp_tile + "_" + temp_shape] -= 1
            print(specific_tile_number[temp_tile + "_" + temp_shape])

            row_placement = int(input("Enter the row: "))
            col_placement = int(input("Enter the column: "))

            if row_placement not in range(6) or col_placement not in range(6):
                print("That is not a valid placement location")
                break



            else:

                if board[row_placement][col_placement] != "[   ]":
                    print ("There is a tile there already!")
                    row_placement = int(input("Enter the row: "))
                    col_placement = int(input("Enter the column: "))

                if row_placement != 5:
                    if (board[row_placement+1][col_placement] == "[   ]"):
                        print("Tile must be placed ontop of another!")
                        row_placement = int(input("Enter the row: "))
                        col_placement = int(input("Enter the column: "))

                board[row_placement][col_placement] = print_to_board
                print_board(board)

        if rand > 85.72:
            print(rand)
            print("You drew a Traitor tile")
            lives -= 1



result()
