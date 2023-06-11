import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    au = r.listen(source)
    try:
        text = r.recognize_google(au)
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize what you said")