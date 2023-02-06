import os # https://docs.python.org/3/library/os.html
from pytube import YouTube  # https://pytube.io/en/latest/


# Aqui transformamos o codigo em uma função
def youtube_downloader(url):
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
    
    print("Arquivo baixado e convertido para mp3!")
