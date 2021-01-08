import speech_recognition as sr


class Speach:
    def __init__(self, clip_length):
        self.recognizer = sr.Recognizer()
        self.recognizer.dynamic_energy_threshold = True
        self.time_len = clip_length

    def recognise_speach(self):

        print(sr.Microphone.list_microphone_names())
        print("Speak:")

        try:
            with sr.Microphone(sample_rate=20000, chunk_size=2048) as d:
                audio = self.recognizer.listen(d, phrase_time_limit=self.time_len)
            print("done")
            try:
                data = self.recognizer.recognize_google(audio)
                print("You said " + data)
                return data
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
        except Exception as e:
            print(e)
            print("sorry")

        return ''
