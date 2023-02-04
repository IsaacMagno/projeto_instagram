import os # https://docs.python.org/3/library/os.html
from pytube import YouTube  # https://pytube.io/en/latest/

# URL do video que contém a música
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Utilizando a URL puxe as informações do video
url = YouTube(str(url))

# Filtre apenas o audio do video
audio_stream = url.streams.filter(only_audio=True).first()

# Escolha onde salvar a música e faça o download
out_file = audio_stream.download(output_path="./mp3")

# Agora é só alterar a extensão do arquivo
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)
