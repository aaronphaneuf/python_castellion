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
specific_tiles = {'triangle': ' ^ ', 'square': ' □ ', 'circle': ' O '}

#dictionary containing remaining tiles
specific_tile_number = {'seer_triangle' : 6, 'seer_square' : 6, 'seer_circle' : 6, 'chameleon_triangle' : 6, 'chameleon_square' : 6, 'chameleon_circle' : 6, 'pyro_triangle' : 6, 'pyro_square' : 6, 'pyro_circle' : 6,
'juggler_triangle' : 6, 'juggler_square' : 6, 'juggler_circle' : 6 }

def result():

    lives = 3


    while lives != 0:

        rand = random.randint(100, 10000) * 0.010
        temp_tile = (random.choice(tiles))
        temp_shape = (random.choice(shapes))

        if all(x==0 for x in specific_tile_number.values()):
            print("There are no tiles left!")
            print("The game is over")
            break

        if specific_tile_number[temp_tile + "_" + temp_shape] == 0:
            temp_tile = (random.choice(tiles))
            temp_shape = (random.choice(tiles))

        if rand < 85.72:

            z = False

            print_to_board = ""

            #This pulls from the dictionary titles specific_tile_number
            specific_tile_number[temp_tile + "_" + temp_shape] -= 1


            print ("You drew a " + temp_tile +" "+ temp_shape+". There are "+ str(specific_tile_number[temp_tile + "_" + temp_shape]) +" remaining")

            #assigns the tile to print_to_board and prints it to the screen
            print_to_board = specific_tile_outer[temp_tile][:1] + specific_tiles[temp_shape] + specific_tile_outer[temp_tile][-1:]
            print(print_to_board)

            while z != True:

                row_placement = int(input("Enter the row: "))
                col_placement = int(input("Enter the column:"))

                if row_placement not in range(6) or col_placement not in range(6):
                    print("That is not a valid placement location")

                if board[row_placement][col_placement] != "[   ]":
                    print ("There is a tile there already!")
                else: z = True

                if row_placement != 5:
                    if (board[row_placement+1][col_placement] == "[   ]"):
                        print("Tile must be placed ontop of another!")
                        z = False

                #check to see if there is a matching shape on either the left or right of choice
                if col_placement != 0:
                    if (board[row_placement][col_placement-1][2]) == (specific_tiles[temp_shape][1]):
                        print("Similar shapes cannot be placed next to eachother!")
                        z = False
                    if col_placement != 5:
                        if (board[row_placement][col_placement+1][2]) == (specific_tiles[temp_shape][1]):
                            print("Similar shapes cannot be placed next to eachother!")
                            z = False

                #check to see if there is a matching shape either above or below choice
                if row_placement != 0:
                    if (board[row_placement-1][col_placement][2]) == (specific_tiles[temp_shape][1]):
                        print("Similar shapes cannot be placed ontop of eachother!")
                        z = False
                    if row_placement != 5:
                        if (board[row_placement+1][col_placement][2]) == (specific_tiles[temp_shape][1]):
                            print("Similar shapes cannot be placed next ontop of eachother!")
                            z = False

            board[row_placement][col_placement] = print_to_board
            print("\n")
            print_board(board)
            print("\nTile Reminder | Seer: ( ), Chameleon: [ ], Juggler: { }, Pyro: | |")



        if rand > 85.72:
            lives -= 1
            print("You drew a Traitor tile. There are %s remaining" % lives)



result()
