from langchain_google_genai import GoogleGenerativeAI
from google.api_core.exceptions import GoogleAPIError
from langchain.prompts import PromptTemplate


def load_llm(api_key):
    try:
        llm = GoogleGenerativeAI(model="gemini-2.5-flash", api_key=api_key)
        print("✅ LLM loaded successfully.")
        return llm

    except ValueError as ve:
        print(f"❌ ValueError: {ve}")
        print("Check if the API key is correctly formatted or passed.")
    
    except GoogleAPIError as gae:
        print(f"❌ Google API Error: {gae}")
        print("There might be a problem with your API credentials or quota.")
    
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        print("Something went wrong while loading the LLM.")


def intent_extraction(llm,intent_list,text):
    try:
        template = '''
        You are a smart assistant, Given the user input: {user_input}, do the following steps:
        
        1. extract the most accurate and appropriate intent from the list:{intent_list}.
        2. Extract the query or subject if present (e.g. song name, reminder, time, website name or etc) 
        
        make sure you return **strictly in this JSON format** without anything extra:
        {{
            "intent":"..",
            "query":".."
        }}
        '''
        
        
        prompt = PromptTemplate(
            input_variables=["user_input", "intent_list"],
            template=template
        )
        
        chain = prompt | llm

        result = chain.invoke({
            "user_input": text,
            "intent_list": intent_list
        })
        
        return result.content if hasattr(result, "content") else result
    
    except KeyError as ke:
        print(f"[KeyError] Missing input variable: {ke}")
        return None
    except ValueError as ve:
        print(f"[ValueError] Issue with input values: {ve}")
        return None
    except Exception as e:
        print(f"[Error] Something went wrong during intent extraction: {e}")
        return None








