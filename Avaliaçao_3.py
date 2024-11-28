
   
def procurar_carros(pesquisa):
    encontrado = []
    with open("estoque_carros.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            nome, preco, ano, estado = linha.split(',')
            try:
                if isinstance(pesquisa, float) and float(preco) <= pesquisa:
                    encontrado.append({
                        'nome': nome,
                        'preco': float(preco),
                        'ano': int(ano),
                        'estado': estado.strip()
                    })
                elif isinstance(pesquisa, str) and estado.strip().lower() == pesquisa.lower():
                    encontrado.append({
                        'nome': nome,
                        'preco': float(preco),
                        'ano': int(ano),
                        'estado': estado.strip()
                    })
            except ValueError:
                pass
    if len(encontrado) > 0:
        return encontrado
    else:
        return "Carro não encontrado!"


def cadastrar_carro():
    nome = input("Digite o nome do carro: ")
    preco = float(input("Digite o preço do carro: "))
    ano_fabricacao = int(input("Digite o ano de fabricação do carro: "))
    estado = input("Digite o estado em que se encontra o carro: ")

    with open("estoque_carros.txt", "a+") as estoque_carros:
        estoque_carros.write(f'{nome},{preco},{ano_fabricacao},{estado}\n')
    return "Carro cadastrado com sucesso!"


while True:
    try:
        escolha = int(input("Digite a sua escolha: 0) Sair do programa  1) Cadastrar carro  2) Pesquisar carro   "))
        if escolha == 1:
            print(cadastrar_carro())
        elif escolha == 2:
            pesquisa = input("Digite um número para buscar o carro pelo preço ou uma palavra se deseja buscar pelo estado do carro: ")
            try:
                pesquisa = float(pesquisa)
            except ValueError:
                pesquisa = pesquisa.strip()
            resultado = procurar_carros(pesquisa)
            if isinstance(resultado, list):
                for carro in resultado:
                    print(carro)
            else:
                print(resultado)
        elif escolha == 0:
            print("O programa foi encerrado ")
            break
        else:
            print("Escolha inválida, digite novamente")
    except ValueError:
        print("Digite um número válido, por favor")
        

