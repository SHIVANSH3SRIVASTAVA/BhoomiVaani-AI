from stt import transcribe_hindi
from tts import speak_hindi
from langchain_rag import ask_llm
from prediction import predict_crop, predict_weather

def main():
    print("🎤 BhoomiVaani: Speak your query in Hindi...")
    text = transcribe_hindi()
    print(f"📝 You said: {text}")
    
    if "fasal" in text or "crop" in text:
        prediction = predict_crop()
    elif "barsaat" in text or "rain" in text:
        prediction = predict_weather()
    else:
        prediction = ask_llm(text)
    
    print(f"🤖 BhoomiVaani says: {prediction}")
    speak_hindi(prediction)

if __name__ == "__main__":
    main()
