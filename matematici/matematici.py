def findMat(list_row):
    name = input("find: ")

    for row in list_row:
        list_data = row.split(",")
        # SB: print(list_data)
        # SB: print(list_data[-1], name)

        if list_data[-1] == name:
            print(int(list_data[0]))

def readFile(name_file):
    file = open(name_file, "r")
    list_row = []
    list_row = file.readlines()

    findMat(list_row)



name_file = "mate.csv"
readFile(name_file)