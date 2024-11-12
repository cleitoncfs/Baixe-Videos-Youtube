import yt_dlp


def download_video(url):
    # Caminho completo para a pasta onde deseja salvar o vídeo
    output_path = 'C:/Users/cleiton/Videos/Youtube-Downloads/%(title)s.%(ext)s'

    # Opções para yt-dlp
    ydl_opts = {
        'format': 'best',  # Baixar na melhor qualidade disponível
        'outtmpl': output_path,  # Definir o nome do arquivo para o título do vídeo
        'noplaylist': True,  # Baixar um único vídeo se a URL fizer parte de uma playlist
        'quiet': False,  # Mostrar progresso do download no console
        'ignoreerrors': True,  # Continuar mesmo se um erro for encontrado
        'no_warnings': True,  # Suprimir avisos
    }
    try:
        # Usar yt-dlp para baixar o vídeo
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download concluído com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


# Substitua pela URL do vídeo do YouTube desejado
download_video('https://www.youtube.com/watch?v=moKF34zcSsI')
