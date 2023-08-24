def MakeBlockList():

    data = '''
1100001000001000
0110011011001100
0000010001100100
0000000000000000

0000001000000100
1111001000000100
0000001011110100
0000001000000100

0110011001100110
0110011001100110
0000000000000000
0000000000000000

0100010000000100
1110011011101100
0000010001000100
0000000000000000

1000011000000100
1110010011100100
0000010000101100
0000000000000000

0010010000001100
1110010011100100
0000011010000100
0000000000000000

0110010000001000
1100011001101100
0000001011000100
0000000000000000'''


    block_list = []
    matrix_rows = data.strip().split('\n\n')
    matrix_list = []

    for matrix_data in matrix_rows:
        matrix = []
        lines = matrix_data.strip().split('\n')
        print(lines)
        
        for line in lines:
            if line:
                row = [int(cell) for cell in line]
                matrix.append(row)
        
        matrix_list.append(matrix)

    for i in range(7):
        block_list.append([])
        for j in range(4):
            block_list[i].append([])
            for l in range(4):
                block_list[i][j].append([])
                block_list[i][j][l].extend(matrix_list[i][l][j * 4 : (j + 1) * 4])

    for i in block_list:
        for j in i:
            for l in j:
                print(l)
            print()

    return block_list