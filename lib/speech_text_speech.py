# speech_text_speech.py v. 0.1.1  20.03.2021
# скрипт записывает голос с микрофона
# переводит запись в текст
# переводит текст в голос

import pyttsx3
import speech_recognition as sr


# выводит список записывающих устройств, если нужно.
# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

def record_volume():
    # -----> Натройки голоса
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
        if voice.name == 'Anna':  # Имя голосового помощника
            tts.setProperty('voice', voice.id)

    # <----- Натройки голоса

    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:  # device_index=  индекс устройства записи.
        print('Настраиваюсь.')
        r.adjust_for_ambient_noise(source, duration=0.9)  # настройка посторонних шумов
        print('Слушаю...')
        tts.say('Слушаю')
        tts.runAndWait()
        audio = r.listen(source)
    print('Услышала.')
    try:  # попытка распознать голос
        query = r.recognize_google(audio, language='ru-RU')
        print(f'Вы сказали: {query.lower()}')
        text = {query.lower()}

        # Произнести текст
        tts.say(text)
        tts.runAndWait()
        return text

    except:  # Исключение
        print('Ошибка распознавания.')
        tts.say('Не расслышала, пожалуйста повторите!')
        tts.runAndWait()


if __name__ == "__main__":
    pass
