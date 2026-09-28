def transpose(mat: list[list[float | int]]) -> list[list]:
    '''меняет строки и столбцы матрицы местами
    
    [[1,2],[3,4]] -> [[1,3],[2,4]]'''
    
    if mat == []:
            return []
        
    for i in range(len(mat)):
        if len(mat[i])!=len(mat[0]):
            raise ValueError('строки матрицы разной длины')
   
    res=[[] for _ in range(len(mat[0]))]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            res[j].append(mat[i][j])
    
    return res



def row_sums(mat: list[list[float | int]]) -> list[float]:
    '''список сумм по каждой строке матрицы
    
    [[1, 2, 3], [4, 5, 6]] → [6, 15]'''
    
        
    for i in range(len(mat)):
        if len(mat[i])!=len(mat[0]):
            raise ValueError('строки матрицы разной длины')
   
    res=[]
    for i in range(len(mat)):
        res.append(0)
        for j in range(len(mat[i])):
            res[i]+=mat[i][j]
    
    return res




def col_sums(mat: list[list[float | int]]) -> list[float]:
    '''список сумм по каждому столбцу матрицы
    
    [[1, 2, 3], [4, 5, 6]] → [5, 7, 9]'''
    
        
    for i in range(len(mat)):
        if len(mat[i])!=len(mat[0]):
            raise ValueError('строки матрицы разной длины')
   
    res=[0 for _ in range(len(mat[0]))]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            res[j]+=mat[i][j]
    
    return res


# тесты

print(f'''
transpose
[[1, 2, 3]] -> {transpose([[1, 2, 3]])}
[[1], [2], [3]] -> {transpose([[1], [2], [3]])}
[[1, 2], [3, 4]] -> {transpose([[1, 3], [2, 4]])}
[] -> {transpose([])}
''')
# print(f'[[1, 2], [3]] -> {transpose([[1, 2], [3]])}')

print(f'''
row_sums
[[1, 2, 3], [4, 5, 6]] -> {row_sums([[1, 2, 3], [4, 5, 6]])}
[[-1, 1], [10, -10]] -> {row_sums([[-1, 1], [10, -10]])}
[[0, 0], [0, 0]] -> {row_sums([[0, 0], [0, 0]])}
''')
# print(f'[[1, 2], [3]] -> {row_sums([[1, 2], [3]])}')

print(f'''
col_sums
[[1, 2, 3], [4, 5, 6]] -> {col_sums([[1, 2, 3], [4, 5, 6]])}
[[-1, 1], [10, -10]] -> {col_sums([[-1, 1], [10, -10]])}
[[0, 0], [0, 0]] -> {col_sums([[0, 0], [0, 0]])}
''')
# print(f'[[1, 2], [3]] -> {col_sums([[1, 2], [3]])}')


