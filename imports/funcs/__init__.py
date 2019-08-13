import webbrowser
import pyttsx3

# core jarvis funcs
def say_str(x, kwargs):
    print("im saying")
    x = x.replace(" ", "", 1)
    print(x)
    try:
        engine = pyttsx3.init();
        engine.setProperty("rate", 200)
        engine.say(x);
        engine.runAndWait() ;
    except:
        pass

def google(x, kwargs): 
    x = x.replace(" ", "", 1)
    webbrowser.open("https://www.google.com/search?source=hp&ei=wki6W44di8quBJ6og8AD&q={}&oq={}&gs_l=psy-ab.3..0i8i13i30k1l5.2206.3696.0.3945.11.10.0.0.0.0.143.1116.2j8.10.0....0...1c.1.64.psy-ab..1.10.1114.0..0j0i131k1j0i131i67k1j0i67k1j0i10k1j0i13k1j0i22i30k1.0.UGF2ylGfAX4".format(x, x))

def go_to_website(x, kwargs):
    x = x.replace(" ", "", 1)
    webbrowser.open(str(x))

def yahoo_run(x, kwargs):
    x = x.replace(" ", "", 1)
    webbrowser.open("https://uk.search.yahoo.com/search?p={}&fr=yfp-t-903-s&fp=1&toggle=1&cop=mss&ei=UTF-8".format(x))

def youtube_run(x, kwargs):
    x = x.replace(" ", "", 1)
    webbrowser.open("https://www.youtube.com/results?search_query={}".format(x))

def dprint(x, kwargs):
    webbrowser.open("https://octopi.local/")

def cancer(x, kwargs):
    webbrowser.open("https://www.bodmincollege.co.uk/")


youtube = ["search youtube for"] #jarvis search youtube for x
webcommand = ["google"] # jarvis google x
yahoo = ["have a look on yahoo for", "search yahoo for", "ask yahoo for", "search yahoo", "ask yahoo", "yahoo it"]
goto_website = ["go to website url", "go to web url"]# jarvis goto website http://chatsterio.co.uk
saystuff = ["say", "speak aloud"] # jarvis say x
dprinter = ["open 3d printer", "open octoprint"]
cancer_can = ["open cancer"]# jarvis open cancer
commands = [webcommand, goto_website, saystuff, yahoo, youtube, dprinter, cancer_can]    
functions = [google, go_to_website, say_str, yahoo_run, youtube_run, dprint, cancer]
