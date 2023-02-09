import os # https://docs.python.org/3/library/os.html
from moviepy.editor import concatenate_audioclips, AudioFileClip
# https://zulko.github.io/moviepy/index.html


# Defina a função
def mp3_merge():
    # Primeiro armazene o caminho para a pasta que contem os arquivos mp3
    folder = "./mp3"

    # Inicie uma lista que vai armazenar o nome e o caminho de cada arquivo
    mp3_files = []

    # Inicie a lista que armazenara todos os arquivos que serão mesclados
    audio_files = []

    # Itere sobre cada arquivo na pasta
    for filename in os.listdir(folder):
        # Concatene o caminho e o nome do arquivo
        file_path = os.path.join(folder, filename)
        # Adicione o arquivo na lista
        mp3_files.append(f"{file_path}")

    # Itere sobre cada arquivo na lista mp3
    for file in mp3_files:
        # Armazene o arquivo de audio utilizando a lib, na lista audio_files
        audio_files.append(AudioFileClip(file))

    # Utilizando a lib importada todos os arquivos na lista são mesclados
    final_audio = concatenate_audioclips(audio_files)
    # Finalmente, escolha o caminho e o nome para o arquivo de saida
    final_audio.write_audiofile("./mp3/merged.mp3")

    print("Todos os arquivos foram mesclados!")

# Chame a função
mp3_merge()
