import os
from dotenv import load_dotenv
import azure.cognitiveservices.speech as speechsdk
import keyboard
import pyautogui
from volume import set_volume,extract_volume_percentage
import time
from display import display_notification
import threading

load_dotenv()
speech_config = speechsdk.SpeechConfig(subscription=os.getenv("SPEECH_KEY"), region=os.getenv("SPEECH_REGION"))
speech_config.speech_recognition_language = "en-IN"
audio_config = speechsdk.audio.AudioConfig(device_name="{0.0.1.00000000}.{B028636A-C291-419F-BA60-DC35890974B9}")

def recognize_from_microphone():
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    notification_thread = threading.Thread(target=display_notification, args=("Listening...",))
    notification_thread.start()
    print("Speak into your microphone.")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()
    print("Stopped listening!")
    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        return speech_recognition_result.text.strip(".").strip(" ").lower()

def start_recognition(e):
    if e.name == "q":
        command = recognize_from_microphone()
        if command == None:
            return
        if "play" in command or "pause" in command:
            print(command)
            keyboard.press_and_release('space')
        if "mute" in command or "unmute" in command:
            print(command)
            pyautogui.hotkey('Volumemute')
        if "volume" in command:
            print(command)
            volume_value = extract_volume_percentage(command)
            if volume_value is not None:
                set_volume(volume_value)
        if "next" in command:
            print(command)
            keyboard.press_and_release(["alt", "right"])
        if "previous" in command:
            print(command)
            keyboard.press_and_release(["alt", "left"])
        if "full" in command or "normal" in command:
            print(command)
            keyboard.press_and_release('f')
        if "close" in command:
            print(command)
            keyboard.press_and_release(["alt", "F4"])
        if "forward" in command:
            print(command)
            forward=True
            while forward:
                print("forwarding....")
                keyboard.press_and_release('right')
                time.sleep(0.5)
                if keyboard.is_pressed("n"):
                    forward=False
        if "rewind" in command:
            print(command)
            rewind=True
            while rewind:
                print("rewinding....")
                keyboard.press_and_release('left')
                time.sleep(0.5)
                if keyboard.is_pressed("n"):
                    rewind=False


keyboard.on_press_key("q", start_recognition)
keyboard.wait("esc")
