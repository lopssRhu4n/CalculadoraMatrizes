from oper import oper
import func
from view import view

class Controler:
    def __init__(self):
        self.view = view()
        self.oper = oper()
    def start(self):
        escolha = self.view.menu()
        
        if escolha == '1':
            self.oper.somaMatrix()
            input()
        if escolha == '2':
            self.oper.subtraiMatrix()
            input(5)
        if escolha == '3':
            self.oper.multiplicaMatrix()
            input()
        if escolha == '4':
            self.oper.createMatrix()
        
        if escolha == '5':
            return self.finish()        
        
        return self.start()
    
    def finish(self):
        print('Obrigado por usar nosso programa!')
        
a = Controler()
a.start()