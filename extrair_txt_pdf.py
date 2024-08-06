import os
import PyPDF2
from docx import Document

def txt_pdf(file_path):
    # Abre o arquivo PDF em modo de leitura binária
    with open(file_path, 'rb') as file:
        ler = PyPDF2.PdfReader(file)
        texto = ""
        for page in ler.pages:
            texto += page.extract_text()
        return texto

caminho_arquivo= r'C:\Users\diogo_nagasse\Desktop\PROJETO_OCR\ocr_project\imagens_pdfs\pdf.pdf'
texto_extraido = txt_pdf(caminho_arquivo)

# Caminho para a pasta "Downloads" do usuário
pasta_download = os.path.join(os.path.expanduser('~'), 'Downloads')

# Nome do arquivo de saída
arquivo_de_saida = os.path.join(pasta_download, 'texto_extraido.docx')

#
doc = Document()
doc.add_paragraph(texto_extraido)

# Salva o documento
doc.save(arquivo_de_saida)

print(f'Texto extraído salvo em: {arquivo_de_saida}')
