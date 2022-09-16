from func import linhaCheia, limpaTela
class view:
        def start(self):
             return self.menu()   
        
        def menu (self):
                limpaTela()
                print('Menu:') 
                linhaCheia()
                print(f'{"1 - Somar Matrizes":^50} \n{"2 - Subtrair Matrizes":^50} \n{"3 - Multiplicar Matrizes":^50} \n{"4 - Transpor Matrizes":^50} \n{"5 - Sair":^50}' )
                linhaCheia()
                escolha = input('Digite:')
                linhaCheia()
        
                linhaCheia()
                return escolha
