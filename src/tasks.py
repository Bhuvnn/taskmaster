import webbrowser
import pyttsx3
import os
from langchain.prompts import PromptTemplate
from langchain.schema import OutputParserException
from pywhatkit import playonyt
from src.intent_classification import load_llm
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv("API_KEY")

def handle_youtube(intent,query=None):
    if intent=="open_youtube":
        webbrowser.open("https://www.youtube.com")
    elif intent=="search_on_youtube" and query:
        webbrowser.open(f"https://www.youtube.com/results?search_query={query.replace(' ', '%20')}")
    elif intent=="play_on_youtube" and query:
        playonyt(query)
    else:
        print("I apologize for my inablity to execute this command.")

def handle_google(intent,query=None):
    if intent=="open_google":
        webbrowser.open("https://www.google.com")
    if intent=="search_on_google":
        webbrowser.open(f"https://www.google.com/search?q={query.replace(' ', '%20')}")

def ai_answering(query):
    try:
        llm = load_llm(api_key=api_key)  # Make sure this function exists and works

        template = '''
        You are a virtual voice assistant. For the question: {query}
        Provide an answer in a concise yet explanatory format just like a voice assistant would do.
        '''
        prompt = PromptTemplate(input_variables=["query"], template=template)

        chain = prompt | llm
        response = chain.invoke({"query": query})
        print(response)
        engine = pyttsx3.init()
        engine.say("    "+response)
        engine.runAndWait()

    except ValueError as ve:
        print(f"[Value Error] Something went wrong with your input: {ve}")
    except OutputParserException as ope:
        print(f"[Parser Error] Couldn't parse the model's output: {ope}")
    except ConnectionError:
        print("[Connection Error] Failed to connect. Please check your internet.")
    except TimeoutError:
        print("[Timeout Error] The request took too long to respond.")
    except Exception as e:
        print(f"[Error] An unexpected error occurred: {e}")
