import os
from process_pdfs import process_pdfs
from vectorizer import Vectorizer

def carregar_pdfs(data):
    textos = []
    for arquivo in os.listdir(data):
        if arquivo.endswith(".pdf"):
            caminho = os.path.join(data, arquivo)
            textos.append(process_pdfs(caminho))
    return textos

def main():
    data = "pdfs"
    textos = carregar_pdfs(data)

    if not textos:
        print("Nenhum arquivo PDF encontrado no diretório!")
        return

    print("PDFs carregados e processados com sucesso!")
    vetor = Vectorizer(textos)

    print("\nDigite sua pergunta:")
    while True:
        pergunta = input("Pergunta: ")
        if pergunta.lower() in ["sair", "exit", "quit"]:
            break
        resposta = vetor.buscar_resposta(pergunta)
        print(f"Resposta: {resposta}")

if __name__ == "__main__":
    main()
