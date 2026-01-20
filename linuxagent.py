import os
os.environ["GOOGLE_API_KEY"] = "AIzaSyCLtyoFrk9e48SVqDA8YUxsjXY33F3I7MU"

# AI LLM MODEL ACCESS
from langchain_google_genai import ChatGoogleGenerativeAI
google_llm = ChatGoogleGenerativeAI( model="gemini-2.5-flash", temperature=0)

response = google_llm.invoke("how to install package on amazon linux")

print(response.content)