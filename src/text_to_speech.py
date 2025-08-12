import edge_tts
import asyncio
import pyaudio

async def text_to_speech(response):
    communicator = edge_tts.Communicate(response, voice="en-US-GuyNeural")
    
    p = pyaudio.PyAudio()
    stream = p.open(
        channels=2,
        format=pyaudio.paInt16,
        rate=44100,
        output=True
    )
    
    print("stream started")
    async for chunk in communicator.stream():
        print("Chunk type:", chunk["type"], "Chunk size:", len(chunk.get("data", b"")))
        if chunk["type"] == "audio":
            stream.write(chunk["data"])
    print("stream finished")
    
    stream.stop_stream()
    stream.close()
    p.terminate()

if __name__ == "__main__":
    asyncio.run(text_to_speech("Hey there, it's a big pleasure to meet you"))



