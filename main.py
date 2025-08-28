import os 
import re
import json
from dotenv import load_dotenv
from src.speech_to_text import record_audio,normalize_audio,transcribe_audio
from src.intent_classification import load_llm,intent_extraction
from src.tasks import handle_youtube,handle_google,ai_answering


load_dotenv()
api_key=os.getenv("API_KEY")



if __name__=="__main__":
    
    #speech to text section
    model_name="small.en"
    frames=record_audio([])
    audio=normalize_audio(frames)
    transcribed_result=transcribe_audio(model_name,audio)
    print(transcribed_result)
    # Intent classification and extraction section
    intent_list=["open_youtube","play_on_youtube","search_on_youtube","open_google","search_on_google","check_weather","ai_answering"]
    model=load_llm(api_key=api_key)
    result=intent_extraction(model,str(intent_list),transcribed_result)
    # def extract_json(text):
    #     match = re.search(r'\{.*?\}', text, re.DOTALL)
    #     if match:
    #         return match.group(0)
    #     return None
    
    # result=extract_json(result)
    # result=json.loads(result)
    print(type(result))
    print(f"Identified Intent: {result['intent']}")
    
    if result["intent"]=="open_youtube" or result["intent"]=="play_on_youtube" or result["intent"]=="search_on_youtube":
        handle_youtube(result["intent"],result["query"])
    elif result["intent"]=="open_google" or result["intent"]=="search_on_google":
        handle_google(result["intent"],result["query"])
    elif result["intent"]=="ai_answering":
        ai_answering(result["query"])
    

