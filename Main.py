"""Program to work out possible solutions for siva puzzle 3"""


def main():
    # enter start and end values
    start_value = 0
    end_value = 10
    # enter numbers top to bottom
    column1 = [1, 2, 3, -4, -5]
    column2 = [1, 2, -2, -4, -5]
    column3 = [1, 2, 3, 7, -5]
    column4 = [1, 2, 3, -4, -5]
    column5 = [1, 2, 3, -4, -5]

    # test values are in expected ranges
    test_column_values(1, column1)
    test_column_values(2, column2)
    test_column_values(3, column3)
    test_column_values(4, column4)
    test_column_values(5, column5)

    # iterate through lists to check all possible sums
    for num1 in column1:
        for num2 in column2:
            for num3 in column3:
                for num4 in column4:
                    for num5 in column5:
                        if calc_numbers(start_value, num1, num2, num3, num4, num5) == end_value:
                            # print correct answers
                            print(str(num1), str(num2), str(num3), str(num4), str(num5), "equals", str(end_value))
    return


# tests if column values fall within expected ranges
def test_column_values(column_number, column):
    for i in range(0, 3):
        if column[i] < 0:
            print("Error in column", str(column_number), ", Element", str(i + 1))
    for i in range(3, 5):
        if column[i] >= 0:
            print("Error in column", str(column_number), ", Element", str(i + 1))
    return


# tests if list length is 5 and contains integers only
def is_integer(column):
    if len(column) == 5:
        for i in column:
            if not is_integer(i):
                print(str(i), "is not an integer")
    else:
        print("error: columns must contain 5 elements")
    return


# adds numbers together and returns result
def calc_numbers(start, num1, num2, num3, num4, num5):
    num_to_return = start + num1
    num_to_return += num2
    num_to_return += num3
    num_to_return += num4
    num_to_return += num5
    return num_to_return


# start of main execution path
if __name__ == '__main__':
    main()
