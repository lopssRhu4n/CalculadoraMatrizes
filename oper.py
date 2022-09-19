
class oper:
    
    
    def selectNumberOfMatrix(self):
        n = int(input('Digite o número de matrizes que irá criar: '))
        
        return n

    def selectRows(self):
        rows = int(input('Digite o número de linhas: '))
        
        return rows

    def selectCols(self):
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

    def verifyMatrix(self, matrix1, matrix2):
        if len(matrix1) != len(matrix2):
            return True
        
        else:
            for row in matrix1:
                indexRow = matrix1.index(row)
                
                if len(row) != len(matrix2[indexRow]):
                    return True
            
                else:
                    return False
            
    def verifyMatrixMult(self, matrix1, matrix2):
        for row in matrix1:
            if len(row) != len(matrix2):
                return True
            else: 
                return False
        
            
    def somaMatrix(self):
        matrix1 =  self.createMatrix()
        matrix2 = self.createMatrix()
        
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
            
            print(newMatrix)

    def subtraiMatrix(self):
        matrix1 = self.createMatrix()
        matrix2 = self.createMatrix()
        
        
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
            
            print(newMatrix)
        

    def multiplicaMatrix(self):
        matrix1 = self.createMatrix()
        matrix2 = self.createMatrix()
    
        if self.verifyMatrixMult(matrix1, matrix2) == True:
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

            print(newMatrix)

    
    #for n in range(numberOfMatrix): 

