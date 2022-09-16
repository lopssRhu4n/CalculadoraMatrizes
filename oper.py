
class oper:
    def selectNumberOfMatrix():
        n = int(input('Digite o número de matrizes que irá criar: '))
        
        return n

    def selectRows():
        rows = int(input('Digite o número de linhas: '))
        
        return rows

    def selectCols():
        cols = int(input('Digite o número de colunas: '))
        return cols

    def createMatrix(self):
        matrix = []
        rows = self.selectRows()
        cols = self.selectCols()
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
            
    def somaMatrix(self, matrix1, matrix2):
        
        if self.verifyMatrix(matrix1, matrix2) == True:
            return print('Linhas e colunas das matrizes não batem!')
        
        else:    
            newMatrix = []
            for i in matrix1:
                newMatrixRow = []
                indexRow = matrix1.index(i)
                
                for j in i:
                    indexCol = i.index(j)
                    
                    
                    res = j + matrix2[indexRow][indexCol]
                    print(f'Resultado: {res}')
                    newMatrixRow.append(res)
                    
                newMatrix.append(newMatrixRow)
            
            return newMatrix


    def subtraiMatrix(self, matrix1, matrix2):
        
        if self.verifyMatrix(matrix1, matrix2) == True:
            return print('Linhas e colunas das matrizes não batem!')
        
        else:    
            newMatrix = []
            for i in matrix1:
                newMatrixRow = []
                indexRow = matrix1.index(i)
                
                for j in i:
                    indexCol = i.index(j)
                    
                    
                    res = j - matrix2[indexRow][indexCol]
                    print(f'Resultado: {res}')
                    newMatrixRow.append(res)
                    
                newMatrix.append(newMatrixRow)
            
            return newMatrix
        

    #for n in range(numberOfMatrix): 
    matrix1 = createMatrix()
    matrix2 = createMatrix()        


    newMatrix = somaMatrix(matrix1, matrix2)
    matrixSub = subtraiMatrix(matrix1, matrix2)    

    print(f'Matriz soma: {newMatrix}')
    print(f'Matriz subtração: {matrixSub}')