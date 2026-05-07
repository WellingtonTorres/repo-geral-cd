## 1º etapa: Classe base Funcionario (Encapsulamento)
# Decisão: usar duplo underscore (__nome, __salario_base) ativa o 'name mangling'
# do Python, que é a forma idiomática de simular atributos privados.
# Esses atributos NÃO podem ser acessados diretamente de fora da classe.
class Funcionario:
    def __init__(self, nome, salario_base):
        self.__nome = nome              # atributo privado
        self.__salario_base = salario_base  # atributo privado

    # Getters: única 'porta de leitura' para os atributos encapsulados.
    # Optei por get_nome / get_salario_base (estilo Java/C#) por ser mais
    # didático para o exercício do que usar @property.
    def get_nome(self):
        return self.__nome

    def get_salario_base(self):
        return self.__salario_base

    ## 2º etapa: Método calcular_pagamento()
    # Para um Funcionario comum, o pagamento é simplesmente o salário base.
    def calcular_pagamento(self):
        return self.__salario_base


## 3º etapa: Classe filha Professor (Herança)
# A sintaxe 'class Professor(Funcionario)' indica que Professor HERDA
# todos os atributos e métodos de Funcionario.
class Professor(Funcionario):
    def __init__(self, nome, salario_base, horas_extras_orientacao):
        # super().__init__ reaproveita a inicialização da classe pai,
        # evitando duplicação de código e respeitando o encapsulamento
        # dos atributos privados (__nome, __salario_base).
        super().__init__(nome, salario_base)
        # Atributo público porque o enunciado não exigiu encapsulamento aqui.
        self.horas_extras_orientacao = horas_extras_orientacao

    ## 4º etapa: Polimorfismo
    # Sobrescrevemos calcular_pagamento(): mesmo NOME do método da classe pai,
    # mas com COMPORTAMENTO diferente (adiciona o bônus por hora-extra).
    # Como __salario_base sofre name mangling, a subclasse NÃO consegue
    # acessá-lo diretamente — por isso usamos o getter herdado get_salario_base().
    def calcular_pagamento(self):
        return self.get_salario_base() + (self.horas_extras_orientacao * 50)


## 5º etapa: Demonstração de uso
# Instanciamos um objeto de cada classe para validar o comportamento
# polimórfico: o mesmo método calcular_pagamento() retorna valores
# diferentes dependendo do tipo do objeto.
func = Funcionario('Ana Silva', 3000)
prof = Professor('Carlos Souza', 4000, 10)

print(f'Funcionário: {func.get_nome()}')
print(f'Pagamento: R$ {func.calcular_pagamento():.2f}\n')

print(f'Professor: {prof.get_nome()}')
print(f'Horas extras de orientação: {prof.horas_extras_orientacao}')
print(f'Pagamento: R$ {prof.calcular_pagamento():.2f}')
# Resultado esperado do Professor: 4000 + (10 * 50) = R$ 4500.00