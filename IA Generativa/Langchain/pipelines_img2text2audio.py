from transformers import pipeline
import scipy
from langchain import PromptTemplate, LLMChain
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAI
import torch
from IPython.display import Image
from datasets import load_dataset

from dotenv import load_dotenv 
import os

# Cargar variables de entorno
load_dotenv()
# Configurar el motor de OpenAI
engine = "gpt-3.5-turbo"
api_key=os.getenv("OPENAI_API_KEY")

llm = OpenAI(openai_api_key=api_key, temperature=1)

captioner = pipeline("image-to-text",model="Salesforce/blip-image-captioning-base", max_new_tokens=20)

def image2text(image):
    text_result = captioner(image)
    return text_result[0]['generated_text']

def crear_historia(topic):
    template = """
    You are a writer and story teller.
    Your task is generate short stories from a shrot description. The story cannot have more than 50 words.
    CONTEXT: {topic}
    STORY:
    """
    topic_template = PromptTemplate(template=template, input_variables=['topic'])
    
    topic_chain = LLMChain(llm=llm, prompt=topic_template)
    response = topic_chain.invoke(topic)
    print(response.get('text'))
    return response.get('text')

def crear_audio(text):
    synthesiser = pipeline("text-to-speech", model="microsoft/speecht5_tts")
    embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
    speaker_embedding = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)
    
    speech = synthesiser(f"{text}", forward_params={"speaker_embeddings": speaker_embedding})
    
    scipy.io.wavfile.write("historia.wav", rate=speech["sampling_rate"], data=speech["audio"])

generated_topic = image2text("https://huggingface.co/datasets/Narsil/image_dummy/resolve/main/parrots.png")
historia = crear_historia(generated_topic)
crear_audio(historia)