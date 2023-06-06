import requests
from decouple import config

ELEVEN_LABS_API_KEY=config("ELEVEN_LABS_API_KEY")

def convert_text_to_speech(message):
    body ={
        "text":message,
        "voice_settings":{
            "stability":0,
            "similarity_boost":0,  
        }
    }

    voice_rachel="21m00Tcm4TlvDq8ikWAM"


    headers={"xi-api-key":ELEVEN_LABS_API_KEY,"Content-Type":"application/json","accept":"audio/mpeg"}
    endpoint=f"https://api.elevenlabs.io/v1/text-to-speech/{voice_rachel}"

    try:
        response=requests.post(endpoint,json=body,headers=headers)
    except Exception as e:
        return
    
    if response.status_code==200:
        return response.content
    else:
        return
    