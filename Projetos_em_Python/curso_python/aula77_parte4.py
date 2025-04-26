# Exercício - sistema de perguntas e respostas

import os
perguntas = [
    {
        "Pergunta": "Quanto é 2+2?",
        "Opções": ["1", "3", "4", "5"],
        "Resposta": "4",
    },
    {
        "Pergunta": "Quanto é 5*5?",
        "Opções": ["25", "55", "10", "51"],
        "Resposta": "25",
    },
    {
        "Pergunta": "Quanto é 10/2?",
        "Opções": ["4", "5", "2", "1"],
        "Resposta": "5",
    },
]


acertos = 0

for pergunta in perguntas:
    print("Pergunta:", pergunta["Pergunta"])
    print()

    opcoes = pergunta["Opções"]
    for i, opcao in enumerate(opcoes): # Enumera os indices em "Opções"
        print(f"{i})", opcao)
        
    resposta_usuario = input("Escolha uma opção: ")

    acertou = False
    resposta_usuario_int = None
    qtd_opcoes = len(opcoes)
    
    if resposta_usuario.isdigit():
        resposta_usuario_int = int(resposta_usuario)

    if resposta_usuario_int is not None:
        if resposta_usuario_int >= 0 and resposta_usuario_int < qtd_opcoes:
            if opcoes[resposta_usuario_int] == pergunta["Resposta"]:
                acertou = True
    print()
    if acertou:
        print("Você acertou ✅")
        acertos += 1
    else:
        print("Você errou ❌")

    print()

os.system('clear')
print(f"Você acertou {acertos} de {len(perguntas)}")

