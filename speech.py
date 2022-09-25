import pyttsx3


def speech(text, gender):

    """
    Function to convert text to speech
    :param text: text
    :param gender: gender
    :return: None
    """
    voice_gender = {"Male": 0, "Female": 1}
    code = voice_gender[gender]

    engine = pyttsx3.init()

    if engine._inLoop:
        engine.endLoop()

    # Setting up voice rate
    engine.setProperty("rate", 150)

    # Setting up volume level  between 0 and 1
    engine.setProperty("volume", 0.8)

    # Change voices: 0 for male and 1 for female
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[code].id)

    engine.say(text)
    engine.runAndWait()
