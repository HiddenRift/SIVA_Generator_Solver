"""Program to work out possible solutions for siva puzzle 3"""


def main():
    # enter numbers top to bottom
    start_value = 0
    end_value = 10
    column1 = [1, 2, 3, -4, -5]
    column2 = [1, 2, 3, -4, -5]
    column3 = [1, 2, 3, -4, -5]
    column4 = [1, 2, 3, -4, -5]
    column5 = [1, 2, 3, -4, -5]

    test_column_values(1, column1)

    for num1 in column1:
        for num2 in column2:
            for num3 in column3:
                for num4 in column4:
                    for num5 in column5:
                        if calc_numbers(start_value, num1, num2, num3, num4, num5) == end_value:
                            print(str(num1), str(num2), str(num3), str(num4), str(num5), "equals", str(end_value))
    return


def test_column_values(column_number, column):
    for i in range(0, 3):
        if column[i] < 0:
            print("Error in", str(column_number), ", Element", str(i))
    for i in range(3, 5):
        if column[i] >= 0:
            print("Error in", str(column_number), ", Element", str(i))


def calc_numbers(start, num1, num2, num3, num4, num5):
    num_to_return = start + num1
    num_to_return += num2
    num_to_return += num3
    num_to_return += num4
    num_to_return += num5
    return num_to_return


if __name__ == '__main__':
    main()
