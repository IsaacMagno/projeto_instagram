from pytube import YouTube, Playlist # https://pytube.io/en/latest/
from download_youtube import youtube_downloader # Função criada no post anterior

# Primeiro definimos a função
def playlist_downloader():
    # Ao iniciar a função o URL da playlist é solicitado
    url = input(str("Digite a URL da Playlist: "))

    # Com o URL a playlist é requisitada e as informações são armazenadas
    video_links = Playlist(url)

    # Para cada link da playlist a função é chamada e o download do audio é feito em mp3
    for link in video_links:
        youtube_downloader(link)

    # Ao finalizar o download uma mensagem é exibida no console
    print("Todos os arquivos foram baixados!")

# Agora é só chamar a função e iniciar os downloads!
playlist_downloader()
