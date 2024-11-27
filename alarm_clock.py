import time
import datetime
import pygame
import os

def set_alarm(alarm_time, alarm_sound_path):
    # Verifica se o arquivo de som existe
    if not os.path.isfile(alarm_sound_path):
        print(f"Error: The file {alarm_sound_path} does not exist.")
        return

    # Inicializa o pygame mixer
    pygame.mixer.init()

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Current Time: {current_time}")
        if current_time == alarm_time:
            print("Alarm! Wake up!")
            pygame.mixer.music.load(alarm_sound_path)  # Carrega o arquivo de som
            pygame.mixer.music.play()  # Toca o arquivo de som
            while pygame.mixer.music.get_busy():  # Espera até que o som termine de tocar
                time.sleep(1)
            break
        time.sleep(1)  # Verifica o tempo a cada segundo

if __name__ == "__main__":
    alarm_time = input("Enter the time in HH:MM:SS format: ")
    alarm_sound_path = ""

    # Loop para garantir que o usuário forneça um caminho válido
    while True:
        alarm_sound_path = input("Enter the full path to the alarm sound file (e.g., C:/path/to/alarm.mp3): ")
        if not alarm_sound_path:
            print("Error: The path to the alarm sound file is empty. Please enter a valid path.")
        elif not os.path.isfile(alarm_sound_path):
            print(f"Error: The file {alarm_sound_path} does not exist. Please enter a valid path.")
        else:
            break

    set_alarm(alarm_time, alarm_sound_path)
