class Animal:
    def falar(self):
        print("Som genérico")


class Cachorro(Animal):
    def falar(self):
        print("Au Au")


class Gato(Animal):
    def falar(self):
        print("Miau")


# Código principal
cachorro = Cachorro()
gato = Gato()

cachorro.falar()
gato.falar()