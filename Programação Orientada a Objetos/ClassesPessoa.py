#1
class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def mostrar_endereco(self):
        print(f"Endereço de {self.nome}: {self.endereco}")

    def alterar_endereco(self, novo_endereco):
        self.endereco = novo_endereco
        print(f"Endereço de {self.nome} alterado para: {self.endereco}")


if __name__ == "__main__":

    pessoa1 = Pessoa(nome="João", idade=25, endereco="Rua A, 123")

    pessoa1.mostrar_endereco()

    pessoa1.alterar_endereco("Avenida B, 456")

    pessoa1.mostrar_endereco()

#2
class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso

    def mostrar_curso(self):
        print(f"{self.nome} está matriculado no curso de {self.curso}")

    def alterar_curso(self, novo_curso):
        self.curso = novo_curso
        print(f"{self.nome} mudou para o curso de {self.curso}")


if __name__ == "__main__":

    aluno1 = Aluno(nome="Maria", matricula="2023001", curso="Engenharia Civil")

    aluno1.mostrar_curso()

    aluno1.alterar_curso("Ciência da Computação")

    aluno1.mostrar_curso()

#3
class Aluno:
    def __init__(self, matricula, nome, nota_prova1, nota_prova2, nota_prova3):
        self.matricula = matricula
        self.nome = nome
        self.nota_prova1 = nota_prova1
        self.nota_prova2 = nota_prova2
        self.nota_prova3 = nota_prova3

    def calcular_media(self):
        return (self.nota_prova1 + self.nota_prova2 + self.nota_prova3) / 3

    def status_aprovacao(self):
        media = self.calcular_media()
        if media >= 6:
            return "Aprovado"
        else:
            return "Reprovado"

alunos = []
for i in range(5):
    matricula = input("Matrícula do aluno: ")
    nome = input("Nome do aluno: ")
    nota_prova1 = float(input("Nota da primeira prova: "))
    nota_prova2 = float(input("Nota da segunda prova: "))
    nota_prova3 = float(input("Nota da terceira prova: "))

    aluno = Aluno(matricula, nome, nota_prova1, nota_prova2, nota_prova3)
    alunos.append(aluno)

aluno_maior_media = max(alunos, key=lambda x: x.calcular_media())
print(f"\nAluno com maior média geral: {aluno_maior_media.nome}, Média: {aluno_maior_media.calcular_media()}")

aluno_menor_media = min(alunos, key=lambda x: x.calcular_media())
print(f"Aluno com menor média geral: {aluno_menor_media.nome}, Média: {aluno_menor_media.calcular_media()}")

print("\nSituação de aprovação/reprovação:")
for aluno in alunos:
    print(f"{aluno.nome}: {aluno.status_aprovacao()}")

#4
class Horario:
    def __init__(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    def incrementar_segundos(self, segundos):
        total_segundos = self.hora * 3600 + self.minuto * 60 + self.segundo
        total_segundos += segundos

        self.hora = total_segundos // 3600
        self.minuto = (total_segundos % 3600) // 60
        self.segundo = total_segundos % 60

    def diferenca_entre_horarios(self, outro_horario):
        segundos_atual = self.hora * 3600 + self.minuto * 60 + self.segundo
        segundos_outro = outro_horario.hora * 3600 + outro_horario.minuto * 60 + outro_horario.segundo

        diferenca_segundos = abs(segundos_atual - segundos_outro)

        horas = diferenca_segundos // 3600
        minutos = (diferenca_segundos % 3600) // 60
        segundos = diferenca_segundos % 60

        return Horario(horas, minutos, segundos)

    def __str__(self):
        return f"{self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}"

if __name__ == "__main__":

    horario1 = Horario(hora=12, minuto=30, segundo=45)
    horario2 = Horario(hora=15, minuto=20, segundo=30)

    print("Horário 1:", horario1)
    print("Horário 2:", horario2)

    horario1.incrementar_segundos(120)

    print("\nHorário 1 após incremento de 120 segundos:", horario1)

    diferenca = horario1.diferenca_entre_horarios(horario2)

    print("\nDiferença entre Horário 1 e Horário 2:", diferenca)

#5

class Carro:
    def __init__(self, marca, ano, preco):
        self.marca = marca
        self.ano = ano
        self.preco = preco

    def mostrar_preco(self):
        print(f"O preço do carro {self.marca} ({self.ano}) é R${self.preco:.2f}")

    def exibir_dados(self):
        print(f"Marca: {self.marca}")
        print(f"Ano: {self.ano}")
        print(f"Preço: R${self.preco:.2f}")

if __name__ == "__main__":

    carro1 = Carro(marca="Toyota", ano=2022, preco=50000.00)

    carro1.mostrar_preco()
    print("\nDados do Carro:")
    carro1.exibir_dados()


#6
class Tamagushi:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

    def alterar_fome(self, nova_fome):
        self.fome = nova_fome

    def alterar_saude(self, nova_saude):
        self.saude = nova_saude

    def alterar_idade(self, nova_idade):
        self.idade = nova_idade

    def retornar_nome(self):
        return self.nome

    def retornar_fome(self):
        return self.fome

    def retornar_saude(self):
        return self.saude

    def retornar_idade(self):
        return self.idade

    def calcular_humor(self):
        humor = (self.fome + self.saude) / 2
        return humor

if __name__ == "__main__":
    tamagushi = Tamagushi(nome="Tama", fome=5, saude=8, idade=2)

    tamagushi.alterar_nome("Tama Jr.")
    tamagushi.alterar_fome(3)
    tamagushi.alterar_saude(7)
    tamagushi.alterar_idade(3)

    print(f"Nome: {tamagushi.retornar_nome()}")
    print(f"Fome: {tamagushi.retornar_fome()}")
    print(f"Saúde: {tamagushi.retornar_saude()}")
    print(f"Idade: {tamagushi.retornar_idade()}")

    humor_tamagushi = tamagushi.calcular_humor()
    print(f"Humor: {humor_tamagushi}")


#7

class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)
        print(f"{self.nome} comeu {alimento}.")

    def verBucho(self):
        print(f"{self.nome} tem no estômago: {', '.join(self.bucho)}.")

    def digerir(self):
        print(f"{self.nome} está digerindo...")
        self.bucho = []

macaco1 = Macaco("Coco")
macaco2 = Macaco("Banana")

macaco1.comer("Maçã")
macaco1.comer("Pêssego")
macaco1.verBucho()

macaco2.comer("Kiwi")
macaco2.verBucho()

macaco1.digerir()
macaco2.digerir()

try:
    macaco1.comer(macaco2)
except AttributeError as e:
    print(f"Erro: {e}")
