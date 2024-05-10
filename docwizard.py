#Bibliotecas
import os # se for ler a APIKEY das variáveis de ambiente
import sys
import google.generativeai as genai

STEPSFILE = "steps.txt"

genai.configure(api_key=os.environ.get('GOOGLE_API_KEY'))

# genai.configure(api_key=userdata('GOOGLE_API_KEY'))

generation_config = {
  "candidate_count": 1,
  "temperature": 0.5,
}    

safety_settings={
    'HATE': 'BLOCK_NONE',
    'HARASSMENT': 'BLOCK_NONE',
    'SEXUAL' : 'BLOCK_NONE',
    'DANGEROUS' : 'BLOCK_NONE'
}

model = genai.GenerativeModel(model_name='gemini-1.0-pro',
                                  generation_config=generation_config,
                                  safety_settings=safety_settings,)

# response = model.generate_content("Que empresa criou o modelo de IA Gemini?")
# response.text

# Arquvido padrão
filename = 'kb0.txt'

#verifica se foi informado um arquivo para leitura
if len(sys.argv) > 1:
  filename = sys.argv[1]

with open(filename, 'r', encoding='utf-8') as my_file:
    my_text = my_file.read()

#print(my_text)

with open(STEPSFILE, 'r', encoding='utf-8') as my_steps:
    for step in my_steps:
      step_line = step.rstrip()
      r = "NOVO"
      while r.upper() == "NOVO":
        print(f"--- {step_line} ---\n")
        output = model.generate_content(step_line + my_text).text
        print(output + "\n")
        r = input("Digite 'novo' se o texto gerado não estiver OK e um novo texto será gerado: ")
      


