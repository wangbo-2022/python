def multiple_table():

    row = 1

    while row <= 9:

        column = 1

        while column <= row :
            print("%d * %d = %d" % (column,row,row*column) , end="\t")
            column += 1

        print("")
        row += 1
