import os 
from dotenv import load_dotenv
from speech_to_text import record_audio,normalize_audio,transcribe_audio
from intent_classification import load_llm,intent_extraction


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
    intent_list=["open_youtube","set_an_alarm","set_reminder","check_weather"]
    model=load_llm(api_key=api_key)
    result=intent_extraction(model,str(intent_list),transcribed_result)
    print(result)
