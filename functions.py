import numpy as np

def bastions(grid):
    bastion = 0
    run = 0
    counter = 0
    # Check the first row
    if np.sum([grid[0]]) == 6 or np.sum([grid[0]]) == 1:
        pass
    else:
        for x in grid[0]:
            if x == 1 and grid[1][counter] == 1:
                run += 1
            else:
                if run == 0:
                    run = 0
                else:
                    run -= 1
            if run == 3:
                run = 2
            if run == 2:
                if counter == 1 and (grid[0][2] != 1 and grid[1][2] != 1 and grid[2][0] != 1 and grid[2][1] != 1):
                    bastion += 4
                    run = 0
                elif counter == 2 and (grid[0][3] != 1 and grid[1][3] != 1 and grid[2][1] != 1 and grid[2][2] != 1 and grid[1][0] != 1):
                    bastion += 4
                    run = 0
                elif counter == 3 and (grid[0][4] != 1 and grid[1][4] != 1 and grid[2][2] != 1 and grid[2][3] != 1 and grid[1][1] != 1):
                    bastion += 4
                    run = 0
                elif counter == 4 and (grid[0][5] != 1 and grid[1][5] != 1 and grid[2][3] != 1 and grid[2][4] != 1 and grid[1][2] != 1):
                    bastion += 4
                    run = 0
                elif counter == 5 and (grid[2][4] != 1 and grid[2][5] != 1 and grid[0][3] != 1 and grid[1][3] != 1):
                    bastion += 4
                    run = 0
            counter += 1

    # Reset run and counter and check the second row
    run = 0
    counter = 0

    if np.sum([grid[1]]) == 6 or np.sum([grid[1]]) == 1:
        pass
    else:
        for x in grid[1]:
            if x == 1 and grid[2][counter] == 1:
                run += 1
            else:
                if run == 0:
                    run = 0
                else:
                    run -= 1
            if run == 3:
                run = 2
            if run == 2:
                if counter == 1 and (grid[1][2] != 1 and grid[2][2] != 1 and grid[3][0] != 1 and grid[3][1] != 1 and grid[0][0] != 1 and grid[0][1] != 1):
                    bastion += 4
                    run = 0
                elif counter == 2 and (grid[1][3] != 1 and grid[2][3] != 1 and grid[3][1] != 1 and grid[3][2] != 1 and grid[2][0] != 1 and grid[0][1] != 1 and grid[0][2] != 1):
                    bastion += 4
                    run = 0
                elif counter == 3 and (grid[1][4] != 1 and grid[2][4] != 1 and grid[3][2] != 1 and grid[3][3] != 1 and grid[2][1] != 1 and grid[0][2] != 1 and grid[0][3] != 1):
                    bastion += 4
                    run = 0
                elif counter == 4 and (grid[1][5] != 1 and grid[2][5] != 1 and grid[3][3] != 1 and grid[3][4] != 1 and grid[2][2] != 1 and grid[0][3] != 1 and grid[0][4] != 1):
                    bastion += 4
                    run = 0
                elif counter == 5 and (grid[3][4] != 1 and grid[3][5] != 1 and grid[1][3] != 1 and grid[2][3] != 1 and grid[0][4] != 1 and grid[0][5] != 1):
                    bastion += 4
                    run = 0
            counter += 1

    # Reset run and counter and check the third row
    run = 0
    counter = 0

    if np.sum([grid[2]]) == 6 or np.sum([grid[2]]) == 1:
        pass
    else:
        for x in grid[2]:
            if x == 1 and grid[3][counter] == 1:
                run += 1
            else:
                if run == 0:
                    run = 0
                else:
                    run -= 1
            if run == 3:
                run = 2
            if run == 2:
                if counter == 1 and (grid[2][2] != 1 and grid[3][2] != 1 and grid[4][0] != 1 and grid[4][1] != 1 and grid[1][0] != 1 and grid[1][1] != 1):
                    bastion += 4
                    run = 0
                elif counter == 2 and (grid[2][3] != 1 and grid[3][3] != 1 and grid[4][1] != 1 and grid[4][2] != 1 and grid[3][0] != 1 and grid[1][1] != 1 and grid[1][2] != 1):
                    bastion += 4
                    run = 0
                elif counter == 3 and (grid[2][4] != 1 and grid[3][4] != 1 and grid[4][2] != 1 and grid[4][3] != 1 and grid[3][1] != 1 and grid[1][2] != 1 and grid[1][3] != 1):
                    bastion += 4
                    run = 0
                elif counter == 4 and (grid[2][5] != 1 and grid[3][5] != 1 and grid[4][3] != 1 and grid[4][4] != 1 and grid[3][2] != 1 and grid[1][3] != 1 and grid[1][4] != 1):
                    bastion += 4
                    run = 0
                elif counter == 5 and (grid[4][4] != 1 and grid[4][5] != 1 and grid[2][3] != 1 and grid[3][3] != 1 and grid[1][4] != 1 and grid[1][5] != 1):
                    bastion += 4
                    run = 0
            counter += 1

    # Reset run and counter and check the fourth row
    run = 0
    counter = 0

    if np.sum([grid[3]]) == 6 or np.sum([grid[3]]) == 1:
        pass
    else:
        for x in grid[3]:
            if x == 1 and grid[4][counter] == 1:
                run += 1
            else:
                if run == 0:
                    run = 0
                else:
                    run -= 1
            if run == 3:
                run = 2
            if run == 2:
                if counter == 1 and (grid[3][2] != 1 and grid[4][2] != 1 and grid[5][0] != 1 and grid[5][1] != 1 and grid[2][0] != 1 and grid[2][1] != 1):
                    bastion += 4
                    run = 0
                elif counter == 2 and (grid[3][3] != 1 and grid[4][3] != 1 and grid[5][1] != 1 and grid[5][2] != 1 and grid[4][0] != 1 and grid[2][1] != 1 and grid[2][2] != 1):
                    bastion += 4
                    run = 0
                elif counter == 3 and (grid[3][4] != 1 and grid[4][4] != 1 and grid[5][2] != 1 and grid[5][3] != 1 and grid[4][1] != 1 and grid[2][2] != 1 and grid[2][3] != 1):
                    bastion += 4
                    run = 0
                elif counter == 4 and (grid[3][5] != 1 and grid[4][5] != 1 and grid[5][3] != 1 and grid[5][4] != 1 and grid[4][2] != 1 and grid[2][3] != 1 and grid[2][4] != 1):
                    bastion += 4
                    run = 0
                elif counter == 5 and (grid[5][4] != 1 and grid[5][5] != 1 and grid[3][3] != 1 and grid[4][3] != 1 and grid[2][4] != 1 and grid[2][5] != 1):
                    bastion += 4
                    run = 0
            counter += 1

    # Reset run and counter and check the fifth row, which is actually the last row that we need to check
    run = 0
    counter = 0

    if np.sum([grid[4]]) == 6 or np.sum([grid[4]]) == 1:
        pass
    else:
        for x in grid[4]:
            if x == 1 and grid[5][counter] == 1:
                run += 1
            else:
                if run == 0:
                    run = 0
                else:
                    run -= 1
            if run == 3:
                run = 2
            if run == 2:
                if counter == 1 and (grid[4][2] != 1 and grid[5][2] != 1 and grid[3][0] != 1 and grid[3][1] != 1):
                    bastion += 4
                    run = 0
                elif counter == 2 and (grid[4][3] != 1 and grid[5][3] != 1 and grid[5][0] != 1 and grid[3][1] != 1 and grid[3][2] != 1):
                    bastion += 4
                    run = 0
                elif counter == 3 and (grid[4][4] != 1 and grid[5][4] != 1 and grid[5][1] != 1 and grid[3][2] != 1 and grid[3][3] != 1):
                    bastion += 4
                    run = 0
                elif counter == 4 and (grid[4][5] != 1 and grid[5][5] != 1 and grid[5][2] != 1 and grid[3][3] != 1 and grid[3][4] != 1):
                    bastion += 4
                    run = 0
                elif counter == 5 and (grid[4][3] != 1 and grid[5][3] != 1 and grid[3][4] != 1 and grid[3][5] != 1):
                    bastion += 4
                    run = 0
            counter += 1

    return(bastion)

def towers(grid2):

    tower = 0
    run = 0
    counter = 0

    # Check the first row
    if np.sum([grid2[0]]) == 6:
        pass
    else:
        for x in grid2[0]:
            if x == 1 and grid2[1][counter] != 1:
                run += 1
            else:
                if run == 0:
                    run = 0
                else:
                    run -= 1
            if run == 4:
                if counter == 3 and grid2[0][counter+1] != 1:
                    tower += 4
                    run = 0
                elif counter == 4 and grid2[0][5]!= 1:
                    tower += 4
                    run = 0
                elif counter == 5:
                    tower += 4
                else:
                    run = 0
            counter += 1

    # Reset run and counter and check the second row
    run = 0
    counter = 0

    if np.sum([grid2[1]]) == 6:
        pass
    else:
        for x in grid2[1]:
            if x == 1 and grid2[2][counter] != 1 and grid2[0][counter] != 1:
                run += 1
            else:
                if run == 0:
                    run = 0
                else:
                    run -= 1
            if run == 4:
                if counter == 3 and grid2[1][counter+1] != 1:
                    tower += 4
                    run = 0
                elif counter == 4 and grid2[1][5]!= 1:
                    tower += 4
                    run = 0
                elif counter == 5:
                    tower += 4
                else:
                    run = 0
            counter += 1

    # Reset run and counter and check the third row
    run = 0
    counter = 0

    if np.sum([grid2[2]]) == 6:
        pass
    else:
        for x in grid2[2]:
            if x == 1 and grid2[3][counter] != 1 and grid2[1][counter] != 1:
                run += 1
            else:
                if run == 0:
                    run = 0
                else:
                    run -= 1
            if run == 4:
                if counter == 3 and grid2[2][counter+1] != 1:
                    tower += 4
                    run = 0
                elif counter == 4 and grid2[2][5]!= 1:
                    tower += 4
                    run = 0
                elif counter == 5:
                    tower += 4
                else:
                    run = 0
            counter += 1

    # Reset run and counter and check the fourth row
    run = 0
    counter = 0

    if np.sum([grid2[3]]) == 6:
        pass
    else:
        for x in grid2[3]:
            if x == 1 and grid2[4][counter] != 1 and grid2[2][counter] != 1:
                run += 1
            else:
                if run == 0:
                    run = 0
                else:
                    run -= 1
            if run == 4:
                if counter == 3 and grid2[3][counter+1] != 1:
                    tower += 4
                    run = 0
                elif counter == 4 and grid2[3][5]!= 1:
                    tower += 4
                    run = 0
                elif counter == 5:
                    tower += 4
                else:
                    run = 0
            counter += 1

    # Reset run and counter and check the fifth row
    run = 0
    counter = 0

    if np.sum([grid2[4]]) == 6:
        pass
    else:
        for x in grid2[4]:
            if x == 1 and grid2[5][counter] != 1 and grid2[3][counter] != 1:
                run += 1
            else:
                if run == 0:
                    run = 0
                else:
                    run -= 1
            if run == 4:
                if counter == 3 and grid2[4][counter+1] != 1:
                    tower += 4
                    run = 0
                elif counter == 4 and grid2[4][5]!= 1:
                    tower += 4
                    run = 0
                elif counter == 5:
                    tower += 4
                else:
                    run = 0
            counter += 1

    # Reset run and counter and check the sixth row
    run = 0
    counter = 0

    if np.sum([grid2[5]]) == 6:
        pass
    else:
        for x in grid2[5]:
            if x == 1 and grid2[4][counter] != 1:
                run += 1
            else:
                if run == 0:
                    run = 0
                else:
                    run -= 1
            if run == 4:
                if counter == 3 and grid2[5][counter+1] != 1:
                    tower += 4
                    run = 0
                elif counter == 4 and grid2[5][5]!= 1:
                    tower += 4
                    run = 0
                elif counter == 5:
                    tower += 4
                else:
                    run = 0
            counter += 1

    return(tower)

def line(grid):
    # This is to check for lines of defences

    line = 0
    run = 0
    counter = 0

    # Check the first row
    if np.sum([grid[0]]) == 6:
        pass
    else:
        for x in grid[0]:
            if x == 1 and grid[1][counter] != 1:
                run += 1
            else:
                if run == 0:
                    run = 0
                else:
                    run -= 1
            if run == 4:
                if counter == 3 and grid[0][counter+1] != 1:
                    line += 4
                    run = 0
                elif counter == 4 and grid[0][5]!= 1:
                    line += 4
                    run = 0
                elif counter == 5:
                    line += 4
                else:
                    run = 0
            counter += 1

    # Reset run and counter and check the second row
    run = 0
    counter = 0

    if np.sum([grid[1]]) == 6:
        pass
    else:
        for x in grid[1]:
            if x == 1 and grid[2][counter] != 1 and grid[0][counter] != 1:
                run += 1
            else:
                if run == 0:
                    run = 0
                else:
                    run -= 1
            if run == 4:
                if counter == 3 and grid[1][counter+1] != 1:
                    line += 4
                    run = 0
                elif counter == 4 and grid[1][5]!= 1:
                    line += 4
                    run = 0
                elif counter == 5:
                    line += 4
                else:
                    run = 0
            counter += 1

    # Reset run and counter and check the third row
    run = 0
    counter = 0

    if np.sum([grid[2]]) == 6:
        pass
    else:
        for x in grid[2]:
            if x == 1 and grid[3][counter] != 1 and grid[1][counter] != 1:
                run += 1
            else:
                if run == 0:
                    run = 0
                else:
                    run -= 1
            if run == 4:
                if counter == 3 and grid[2][counter+1] != 1:
                    line += 4
                    run = 0
                elif counter == 4 and grid[2][5]!= 1:
                    line += 4
                    run = 0
                elif counter == 5:
                    line += 4
                else:
                    run = 0
            counter += 1

    # Reset run and counter and check the fourth row
    run = 0
    counter = 0

    if np.sum([grid[3]]) == 6:
        pass
    else:
        for x in grid[3]:
            if x == 1 and grid[4][counter] != 1 and grid[2][counter] != 1:
                run += 1
            else:
                if run == 0:
                    run = 0
                else:
                    run -= 1
            if run == 4:
                if counter == 3 and grid[3][counter+1] != 1:
                    line += 4
                    run = 0
                elif counter == 4 and grid[3][5]!= 1:
                    line += 4
                    run = 0
                elif counter == 5:
                    line += 4
                else:
                    run = 0
            counter += 1

    # Reset run and counter and check the fifth row
    run = 0
    counter = 0

    if np.sum([grid[4]]) == 6:
        pass
    else:
        for x in grid[4]:
            if x == 1 and grid[5][counter] != 1 and grid[3][counter] != 1:
                run += 1
            else:
                if run == 0:
                    run = 0
                else:
                    run -= 1
            if run == 4:
                if counter == 3 and grid[4][counter+1] != 1:
                    line += 4
                    run = 0
                elif counter == 4 and grid[4][5]!= 1:
                    line += 4
                    run = 0
                elif counter == 5:
                    line += 4
                else:
                    run = 0
            counter += 1

    # Reset run and counter and check the sixth row
    run = 0
    counter = 0

    if np.sum([grid[5]]) == 6:
        pass
    else:
        for x in grid[5]:
            if x == 1 and grid[4][counter] != 1:
                run += 1
            else:
                if run == 0:
                    run = 0
                else:
                    run -= 1
            if run == 4:
                if counter == 3 and grid[5][counter+1] != 1:
                    line += 4
                    run = 0
                elif counter == 4 and grid[5][5]!= 1:
                    line += 4
                    run = 0
                elif counter == 5:
                    line += 4
                else:
                    run = 0
            counter += 1

    return(line)
