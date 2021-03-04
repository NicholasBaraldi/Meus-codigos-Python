import sys

def read_line():
    line = input()
    string_list = line.split()

    i = 0
    int_list = []
    while (i < 4):
        int_list.append(int(string_list[i]))
    return (int_list)

def transpose_matrix(matrix):
    transposed_matrix = []
    i = 0

    while (i < 4):
        new_line = []
        j = 0
        while (j < 4):
            new_line.append(matrix[j][i])
            j += 1
        transposed_matrix.append(new_line)
        i += 1
    return (transposed_matrix)

N = 1
while (N > 0):
    N_str = sys.stdin.readline()
    if (N_str != ''):
        N = int(N_str)
    else:
        N = 0

    if (N > 0):
        matrix = []
        missing_x = -1
        remaining_x = -1
        missing_y = -1
        remaining_y = -1

        j = 0
        while (j < 4):
            matrix.append(read_line())
            j += 1

        print(matrix)

        j = 0
        while (j < 4):
            line_sum = sum(matrix[j])
            if (line_sum < 2):
                missing_y = j
            if (line_sum > 2):
                remaining_y = j
            j += 1

        transposed_matrix = transpose_matrix(matrix)

        j = 0
        while (j < 4):
            line_sum = sum(transposed_matrix[j])
            if (line_sum < 2):
                missing_x = j
            if (line_sum > 2):
                remaining_x = j
            j += 1

        if (missing_x != -1):
            print("Caso {}: MOVER CANGURU DE ({},{}) PARA ({},{})".format(N, remaining_y + 1, remaining_x + 1,
                                                                          missing_y + 1, missing_x + 1))
        else:
            print("Caso {}: CORRETO".format(N))