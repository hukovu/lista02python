## primeira questão
import math
from typing import Any
class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * self.raio **2
    # Exemplo de uso:
raio_circulo = 5
circulo = Circulo(raio_circulo)
area = circulo.calcular_area()
print("A área d ocírculo com raio", raio_circulo, "é: ", area)

##  Segunda Questão
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    def detalhes(self):
        return f"Título: {self.titulo}, Autor: {self.autor}"
    
    # Exemplo de uso:
    livro1 = Livro("Dom Quixote", "Miguel de Cervantes")
    livro2 = Livro("Crime e Castigo", "Fiodor Dostoiévski")
    print(livro1.detalhes())
    print(livro2.detalhes())

## Terceira Questão
    class Retangulo:
        def __init__(self, base, altura):
            self.base = base
            self.altura = altura
        def calcular_area(self):
            return self.base * self.altura
    # Exemplo de uso:
    base_retangulo = 5
    altura_retangulo = 50
    retangulo = Retangulo(base_retangulo, altura_retangulo)
    area = retangulo.calcular_area()
    print("A área do retângulo com base", base_retangulo, "e altura", altura_retangulo, "é: ", area)

## Quarta questão
    class ContaBancaria:
        def __init__(self, titular, saldo=0):
            self.titular = titular
            self.saldo = saldo
        def depositar(self, valor):
            if valor > 0:
                self.saldo += valor
                print(f"Depósito de {valor} realizado. Novo saldo: {self.saldo}")
            else:
                print("Valor de depósito invalido.")

        def sacar(self, valor):
            if 0 <  valor <= self.saldo:
                self.saldo -= valor
                print (f"Saque de {valor} realizado. Novo saldo: {self.saldo}")

    # Exemplo de uso
    conta = ContaBancaria("joão", 1000)
    print ("Saldo inicial:", conta.saldo)
    conta.depositar(500)
    conta.sacar(200)
    conta.sacar (1500)

## Quinta questão
    class Pessoa:
        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade
        def falar(self):
            print(f"{self.nome} está falando...")
    #exemplo de uso:
        pessoa = Pessoa("joão", 30)
        pessoa.falar()

## Sexta questão:
    class Produto:
        def __init__(self, nome, preco, quantidade):
            self.nome = nome
            self.preco = preco 
            self.quantidade = quantidade

    #Exemplo de uso:
    produto = Produto("Camiseta", 25.0, 3)
    total = produto.calcuolar_total()
    print("Total do produto:", total)

## Sétima questão
    class Carro:
        def __init__(self, marca, modelo, ano):
            self.marca = marca
            self.modelo = modelo
            self.ano = ano

        def detalhges(self):
            return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano {self.ano}"
        
    #Exemplo de uso:
    carro1 = Carro ("Toyota", "Corolla", 2020)
    carro2 = Carro ("Ford", "Focus", 2018)
    print(carro1.detalhes())
    print(carro2.detalhes())

## Oitava questão:
    class Aluno:
        def __init__(self, nome, notas):
            self.nome = nome
            selfnotas = notas
        
        def media(self):
            if len(self.notas) == 0:
                return 0
            return sum (self.notas) / len(self.notas)
        
    #Exemplo de uso:
        aluno1 = Aluno("joão", [8, 6, 9, 5])
        aluno2 = Aluno("Joana", [5, 6, 9, 9])
        print(f"A média das notas do(a) aluno(a) {aluno1.nome} é: {aluno1.calcular_media()}")
        print(f"A média das notas do(a) aluno(a) {aluno2.nome} é: {aluno2.calcular_media()}")

## Nona questão:
    class Triangulo:
        def __init__(self, lado1, lado2, lado3):
            self.lado1 = lado1
            self.lado2 = lado2
            self.lado3 = lado3
        def calcular_perimetro(self):
            return self.lado1 + self.lado2 + self.lado3
    #Exemplo de uso
    triangulo = Triangulo(3, 4, 5)
    perimentro = triangulo.calcular_perimetro()
    print("O perimetro do triângulo é: ", perimentro)


## Décima questão:
    class Funcionario:
        def __init__(self, nome, salario, cargo):
            self.nome = nome
            self.salario = salario
            self.cargo = cargo

            def aumentar_salario(self, percentual_aumento):
                aumento = self.salario * (percentual_aumento / 100)
            self.salario += aumento
            print(f"Salário de {self.nome} atualizado para R${self.salario:.2f}.")

    # Exemplo de uso
        funcionario = Funcionario ("Maria", 3500, "Desenvolvedora")
        print(f"Salário inicial de {funcionario.nome}: R${funcionario.salario:.2f}")
        funcionario.aumentar_salario(10)