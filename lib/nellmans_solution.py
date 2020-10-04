""" Please copy this file an rename it with your name.

"""


# your function
def ki(matrix_x, matrix_y, snakebody_x, snakebody_y, head_x, head_y, food_x, food_y):
    """Put your Algorithm/AI here.

    Matrix_x and y are the coordintes of the matrix, everything outside is dead, top left is 0,0 and increases towarsd the bottomom right.
    snakebody x and y are a list of numbers with the body of the snake, including the current head.
    head_x and y gells you the current position of the head of the snake.
    food_x and y are the current coordinates of the food.
    please return first the change on the x axis, then on the y axis (one of them has to be zero!)
    The Stepsize is (-)1 or 0.

    """
    # print(head_x, head_y, food_x, food_y)
    x = 0
    y = 0

    # see the following example algorithm for how to use the numbers.
    j = True
    skip = 0
    if head_x < food_x:
        for i in range(0, len(snakebody_x)):
            if head_x+1 == snakebody_x[i] and head_y == snakebody_y[i]:
                j = False
        if j and skip == 0:
            x = 1
            skip = 1

    j = True
    if head_y > food_y:
        for i in range(0, len(snakebody_x)):
            if head_x == snakebody_x[i] and head_y-1 == snakebody_y[i]:
                j = False
        if j and skip == 0:
            y = -1
            skip = 1

    j = True
    if head_x > food_x:
        for i in range(0, len(snakebody_x)):
            if head_x-1 == snakebody_x[i] and head_y == snakebody_y[i]:
                j = False
        if j and skip == 0:
            x = -1
            skip = 1

    j = True
    if head_y < food_y:
        for i in range(0, len(snakebody_x)):
            if head_x == snakebody_x[i] and head_y+1 == snakebody_y[i]:
                j = False
            if j and skip == 0:
                y = 1
                skip = 1

    if skip == 0:
        x = -1

    # print(snakebody_x, snakebody_y)
    # print(x,y)
    return x, y  # this return statement has to stay like this
##############################################################################