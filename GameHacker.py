from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import Google


print("Iniciando o robo")

driver = webdriver.Chrome('C:/Users/vitor/OneDrive/Área de Trabalho/Robos/chromedriver')
link = "https://" + input("Link do jogo: ")
driver.get(link)

driver.find_element_by_class_name("enter").send_keys(Keys.RETURN)
time.sleep(2)
driver.find_element_by_tag_name("input").clear()
driver.find_element_by_tag_name("input").send_keys("SrPaulinho")
driver.find_element_by_class_name("icon-exclamation").send_keys(Keys.RETURN)


time.sleep(20)

letra = driver.find_element_by_id("letter").text[6]
print(letra)

newTemas=["COR","CEP","NOME","ANIME/DESENHO","SERIE/FILME","ANIMAL","SUPER PODER","PERSONAGEM FICTICIO", "MARCA","TESTE3","TESTE2","TESTE1"]

temasRaw = driver.find_elements_by_tag_name("span")
temas = []
for i in temasRaw:
    if(i.text in newTemas):
        temas.append(i.text)


print(temas)


