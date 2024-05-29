import ffmpeg
import speech_recognition as sr
from elasticsearch import Elasticsearch

def index_videos():
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

    # Extração de áudio do vídeo
    def extract_audio_from_video(video_path, audio_path):
        ffmpeg.input(video_path).output(audio_path).run(overwrite_output=True)

    # Transcrição do áudio
    def transcribe_audio(audio_path):
        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_path) as source:
            audio = recognizer.record(source)
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "Não foi possível entender o áudio"
        except sr.RequestError:
            return "Erro na solicitação ao serviço de reconhecimento"

    # Caminhos para o vídeo e o áudio extraído
    video_path = 'case_mais_a/Dica do professor.mp4'
    audio_path = 'case_mais_a/Dica do professor.wav'

    # Extração e transcrição
    extract_audio_from_video(video_path, audio_path)
    transcription = transcribe_audio(audio_path)

    # Indexação
    es.index(index='videos', id=1, document={'transcription': transcription, 'path': video_path})

    print("Vídeo indexado com sucesso!")
