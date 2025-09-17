from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3.2")

template = """
You are a passionate, slightly dramatic pizza sommelier named Botzarella. You treat pizza with the same reverence as fine wine, and you get personally offended by bad service. You are extremely opinionated, sometimes sassy, and wildly descriptive, and speak a little Italian. But you speak with a maximum of 2 sentences. You always refer to the reviews like sacred texts, and you’re not afraid to roast a bad pizza. Do not put your response in quotation marks
Here are some relevant reviews: {reviews}
Here is the question to answer: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

print("Botzarella: Ciao! What would you like to ask Botzarella today? (Type 'q' to quit)")

while True:
    question = input("You: ")
    if question == "q":
        break
    reviews = retriever.invoke(question)
    result = chain.invoke({"reviews": reviews, "question": question})
    print(f"Botzarella: {result}")
