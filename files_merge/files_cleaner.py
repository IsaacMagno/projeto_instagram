import os # https://docs.python.org/3/library/os.html

# Armazene o caminho da pasta onde contem os arquivos a serem apagados
folder = './mp3'

# Defina a função
def file_cleaner():
    # Itere sobre cada arquivo da pasta
    for filename in os.listdir(folder):
        # Concatene o nome e o caminho do arquivo
        file_path = os.path.join(folder, filename)
        # Verifique se é um arquivo
        if os.path.isfile(file_path):
            # E então remova
            os.remove(file_path)
            print(f"Arquivo {filename} deletado com sucesso.")

# Chame a função
file_cleaner()
