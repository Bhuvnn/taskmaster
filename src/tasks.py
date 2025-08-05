import webbrowser
from pywhatkit import playonyt

def handle_youtube(intent,query=None):
    if intent=="open_youtube":
        webbrowser.open("https://www.youtube.com")
    elif intent=="play_on_youtube" and query:
        playonyt(query)
    else:
        print("I apologize for my inablity to execute this command.")

def handle_google(intent,query=None):
    if intent=="open_google":
        webbrowser.open("https://www.google.com")
    if intent=="search_on_google":
        webbrowser.open(f"https://www.google.com/search?q={query.replace(' ', '%20')}")
