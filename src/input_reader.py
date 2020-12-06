def read_input(file_name):
    file = open('../resources/input/' + file_name, 'r')
    lines = file.readlines()

    lines = [n.strip("\n") for n in lines]

    return lines
