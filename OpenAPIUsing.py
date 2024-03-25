from openai import OpenAI

def get_words_from_gpt(letter: str = None, categorys: list = None):
    ### This function is a wrapper for the OpenAI API, it receives a letter and a list of categorys and returns a list of words that start with the letter and are related to the categorys
    prompt = "Estou jogando stop e preciso de ajuda: Faça uma lista em python com palavras em português iniciadas em {0}, a lista deve conter uma palavra para cada categoria a seguir:{1}, por favor mantenha na ordem dos temas, retorne apenas a lista e mais nada".format(letter, categorys)

    client = OpenAI()
   
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt}
    ])
    return response.choices[0].message.content

