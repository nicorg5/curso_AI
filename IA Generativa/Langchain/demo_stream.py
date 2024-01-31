from langchain_openai import ChatOpenAI
import asyncio

# Primero autenticamos el usuario :
import sys

from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# Configurar el motor de OpenAI
engine = "gpt-3.5-turbo"
api_key=os.getenv("OPENAI_API_KEY")
model = ChatOpenAI(api_key=api_key)

chunks = []
total_tokens_used = 0

async def chatear():
    global total_tokens_used
    async for chunk in model.astream("hello. tell me something about yourself"): 
        chunks.append(chunk)
        total_tokens_used += 1
        
        print(chunk.content, end="|", flush=True) 

asyncio.run(chatear())
print(f"Tokens totales utilizados: {total_tokens_used}")