class MeuModulo:
    def __init__(self, nome):
        self.nome = nome

    def printer(self):
        return self.nome
    
if __name__ == "__main__":
    meu_modulo = MeuModulo("Julia")
    print(meu_modulo.printer())
