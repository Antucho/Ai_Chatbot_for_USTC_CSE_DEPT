from langchain.llms import ollama
ollama = ollama(base_url= 'http://localhost:11434',
                model = "USTC_CSE_Dept")
print(ollama("who are you"))