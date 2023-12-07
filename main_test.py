import unittest
from main import Product

class TestProduct(unittest.TestCase):

    # setar o valor para o test
    def setUp(self):
        #criando a instância da classe Product, todas as vezes que o test rodar, esses valores são criados
        self.product = Product(99,"test",1.99,10) #esses são os valores setados da instancia de teste

    #criando o construtor para verificação dos atributos da instância
    def test_constructor(self):
        # o teste passará se o valor setado, for igual ao passado como parametro
        self.assertEqual(self.product.id, 99)
        self.assertEqual(self.product.name,"test")
        self.assertEqual(self.product.price,1.99)
        self.assertEqual(self.product.stock,10)

    #testando os métodos
    def test_increase_stock(self):
        self.product.increase_stock(10)
        self.assertEqual(self.product.stock,20)
        # o stock setado inicialmente tem 10, foi incrementado 10, logo o resultado tem q ser 20
        #teste ok
    def test_decrease_stock(self):
        self.product.decrease_stock(10)
        self.assertEqual(self.product.stock,0)
        # o stock setado é de 10, logo o resultado do teste tem q ser 0

    def tearDown(self):
        #limpeza da instancia
        del self.product



#Linha de código necessária para rodar o teste
if __name__ == '__main__':
    unittest.main()