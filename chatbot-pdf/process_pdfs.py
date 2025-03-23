import PyPDF2

def process_pdfs(caminho_pdf):
    try:
        with open(caminho_pdf, "rb") as arquivo:
            leitor = PyPDF2.PdfReader(arquivo)
            texto = ""
            for pagina in leitor.pages:
                texto += pagina.extract_text() + " "
            return texto.strip()
    except Exception as e:
        print(f"Erro ao processar o arquivo {caminho_pdf}: {e}")
        return ""

