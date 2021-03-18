import speech_recognition as sr

for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

import speech_recognition as sr
import pyttsx3


def record_volume():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print('Настраиваюсь.')
        r.adjust_for_ambient_noise(source, duration=0.9)  # настройка посторонних шумов
        print('Слушаю...')
        audio = r.listen(source)
    print('Услышала.')
    try:
        query = r.recognize_google(audio, language='ru-RU')
        text = query.lower()
        print(f'Вы сказали: {query.lower()}')
        text = {query.lower()}

        tts = pyttsx3.init()
        rate = tts.getProperty('rate')  # Скорость произношения
        tts.setProperty('rate', rate)

        volume = tts.getProperty('volume')  # Громкость голоса
        tts.setProperty('volume', volume + 0.9)

        voices = tts.getProperty('voices')

        # Задать голос по умолчанию
        tts.setProperty('voice', 'ru')

        # Попробовать установить предпочтительный голос
        for voice in voices:
            if voice.name == 'Anna':
                tts.setProperty('voice', voice.id)

        tts.say(text)
        tts.runAndWait()

    except:
        print('Error')


if __name__ == "__main__":
    while True:
        record_volume()
