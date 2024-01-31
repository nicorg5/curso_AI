#SIN LAINGCHAIN
from typing import List
from openai import OpenAI
from dotenv import load_dotenv 
import os

# Cargar variables de entorno
load_dotenv()
# Configurar el motor de OpenAI
engine = "gpt-3.5-turbo"
api_key=os.getenv("OPENAI_API_KEY")

prompt_template = "Tell me a short joke about {topic}"
# Inicializar el modelo de OpenAI con la clave de API 
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def call_chat_model(messages: List[dict]) -> str: 
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )
    return response.choices[0].message.content


def invoke_chain(topic: str) -> str:
    prompt_value = prompt_template.format(topic=topic) 
    messages = [{"role": "user", "content": prompt_value}] 
    return call_chat_model(messages)
    
print(invoke_chain("ice cream"))


# CON LAINGCHAIN
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

prompt = ChatPromptTemplate.from_template(
    "Tell me a short joke about {topic}"
)

output_parser = StrOutputParser()
model = ChatOpenAI(model="gpt-3.5-turbo", api_key=api_key, temperature=1) 
chain = (
    {"topic": RunnablePassthrough()} 
    | prompt
    | model
    | output_parser
)

response = chain.invoke("ice cream") 
print(response)