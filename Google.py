from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


print("Realizando pesquisa")

def pesquisaTemas(Lista, Letra):
    driver = webdriver.Chrome('C:/Users/vitor/OneDrive/Área de Trabalho/Robos/chromedriver')
    driver.get("https://google.com")
    respostas = []

    for i in Lista:
        driver.find_element_by_class_name("gLFyf").send_keys("{0} com a letra {1}".format(i, Letra) )
        driver.find_element_by_class_name("gLFyf").send_keys(Keys.RETURN)
        driver.find_element_by_class_name("gLFyf").clear()
        







