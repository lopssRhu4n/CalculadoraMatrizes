def selectNumberOfMatrix():
    n = int(input('Digite o número de matrizes que irá criar: '))
    
    return n

def selectRows():
    rows = int(input('Digite o número de linhas: '))
    
    return rows

def selectCols():
    cols = int(input('Digite o número de colunas: '))
    return cols

def createMatrix():
    matrix = []
    rows = selectRows()
    cols = selectCols()
    for i in range(rows):
        arr =  []
        for j in range(cols):
            num = int(input(f'Digite o número da coluna {j+1} e linha {i+1}: '))
            arr.append(num)
        
        matrix.append(arr)    
        
    return(matrix)

def verifyMatrix(matrix1, matrix2):
    if len(matrix1) != len(matrix2):
        return True
    
    else:
        for row in matrix1:
            indexRow = matrix1.index(row)
            
            if len(row) != len(matrix2[indexRow]):
                return True
        
            else:
                return False

def verifyMatrixMult(matrix1, matrix2):
    for row in matrix1:
        if len(row) != len(matrix2):
            return True
        else: 
            return False
    
    
            
        

        
def somaMatrix():
    
    matrix1 = createMatrix()
    matrix2 = createMatrix()
    
    if verifyMatrix(matrix1, matrix2) == True:
        return print('Linhas e colunas das matrizes não batem!')
    
    else:    
        newMatrix = []
        for row in matrix1:
            newMatrixRow = []
            indexRow = matrix1.index(row)
            
            for col in row:
                indexCol = row.index(col)
                
                
                res = col + matrix2[indexRow][indexCol]
                newMatrixRow.append(res)
                
            newMatrix.append(newMatrixRow)
        
        return newMatrix


def subtraiMatrix():
    
    matrix1 = createMatrix()
    matrix2 = createMatrix()
    
    if verifyMatrix(matrix1, matrix2) == True:
        return print('Linhas e colunas das matrizes não batem!')
    
    else:    
        newMatrix = []
        for row in matrix1:
            newMatrixRow = []
            indexRow = matrix1.index(row)
            
            for col in row:
                indexCol = row.index(col)
                
                
                res = col - matrix2[indexRow][indexCol]
                newMatrixRow.append(res)
                
            newMatrix.append(newMatrixRow)
        
        return newMatrix
    
def multiplicaMatrix():
    matrix1 = createMatrix()
    matrix2 = createMatrix()
    
    if verifyMatrixMult(matrix1, matrix2) == True:
        return print('Número de colunas e linha para multiplicação não batem!')
    else:
        print('Ok tá batendo')
        newMatrix = []
        
        for row in matrix1:
            newMatrixRow = []
            n = 0
            indexRow = matrix1.index(row)
            
            for col in row:
                
                indexCol = row.index(col)
                
                print(f'Valor A{indexRow}{indexCol}: {col}')
                print(f'Valor B{indexCol}{indexRow}: {matrix2[indexCol][indexRow]}')
                n += col*matrix2[indexCol][indexRow]
                print(f'resultado: {n}' )
                
            newMatrixRow = n
            newMatrix.append(newMatrixRow)    

        return newMatrix
#for n in range(numberOfMatrix): 


newMatrix = somaMatrix()
matrixSub = subtraiMatrix()
matrixMult = multiplicaMatrix()

print(f'Matriz soma: {newMatrix}')
print(f'Matriz subtração: {matrixSub}')
print(f'Matrix multiplicação: {matrixMult}')