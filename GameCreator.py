from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

print("Iniciando o robo")

driver = webdriver.Chrome('C:/Users/vitor/OneDrive/Área de Trabalho/Robos/chromedriver')
driver.get("https://stopots.com.br/")


driver.find_element_by_class_name("enter").send_keys(Keys.RETURN)

time.sleep(3)

driver.find_element_by_tag_name("input").clear()
driver.find_element_by_tag_name("input").send_keys("Paulinho")
driver.find_elements_by_class_name("icon-gear")[0].send_keys(Keys.RETURN)

time.sleep(1)
oldTemas = driver.find_elements_by_class_name("del")

for i in oldTemas:
    i.send_keys(Keys.RETURN)

newTemas=["Cor","CEP","Nome","Anime/Desenho","Serie/Filme","Animal","Super Poder","Personagem Ficticio", "Marca","Teste3","Teste2","Teste1"]

inputTemas = driver.find_element_by_name("themeAdd")

for i in newTemas:
    inputTemas.send_keys(i)
    inputTemas.send_keys(Keys.RETURN)
    inputTemas.clear()

driver.find_element_by_class_name("icon-exclamation").send_keys(Keys.RETURN)


