import sys




if "__main__" == __name__:
    if len(sys.argv) < 2:
        print("Please enter the file name as in python3 main.py 'file_name'")
        exit()

    try:
        file = open(sys.argv[1])

    except Exception as e:
        print(e)
        exit()

    current = 50

    zero_counter = 0

    for line in file:
        current += int(line[1:]) if line[0] == "R" else -int(line[1:])

        current = current%100

        if current < 0:
            current = 100 + current

        if current == 0:
            zero_counter += 1


    print("the count of zeros is ", zero_counter)
