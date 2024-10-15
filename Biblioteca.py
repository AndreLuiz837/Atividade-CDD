class Pessoa:
    def __init__(self,nome,peso,idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = False
        self.andando = False
        self.dormindo = False
    def comer(self):
        if self.comendo == False:
            if self.andando == False:
                if self.dormindo == False:
                    print("Foi comer")
                    self.comendo=True
                else:
                    print("Nao pode pois esta dormindo")
            else:
                print("Nao pode pois esta andando")
        else:
            print("Nao pode,pois esta comendo")

    def andar(self):
        if self.andando == False:
            if self.comendo == False:
                if self.dormindo == False:
                    print("Foi andar")
                    self.andando=True
                else:
                    print("Nao pode pois esta dormindo")
            else:
                print("Nao pode pois esta comendo")
        else:
            print("Nao pode pois esta andando")

    def dormir(self):
        if self.dormindo == False:
            if self.andando == False:
                if self.comendo == False:
                    print("Foi dormir")
                    self.andando=True
                else:
                    print("Nao pode pois esta comendo")
            else:
                print("Nao pode pois esta andando")
        else:
            print("Nao pode pois esta dormindo")

    def parar_de_comer(self):
        if self.comendo == True:
            print("Parou de comer")
            self.comendo = False

    def parar_de_andar(self):
        if self.andando == True:
            print("Parou de andar")
            self.andando = False

    def parar_de_dormir(self):
        if self.dormindo == True:
            print("Parou de dormir")
            self.dormindo = False