from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import GameHacker

def create():   
    print("Iniciando o robo...")

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(options=options)
    driver.get("https://stopots.com.br/")

    time.sleep(3)


    driver.find_element(By.CLASS_NAME, "enter").click()

    time.sleep(3)

    driver.find_element(By.TAG_NAME, "input").clear()
    driver.find_element(By.TAG_NAME, "input").send_keys("Paulinho")
    driver.find_element(By.CLASS_NAME, "icon-gear").click()

    time.sleep(1)
    oldTemas = driver.find_elements(By.CLASS_NAME, "del")

    for i in oldTemas:
        i.send_keys(Keys.RETURN)

    newTemas=["Cor","CEP","Nome","Anime/Desenho","Serie/Filme","Animal","Super Poder","Personagem Ficticio", "Marca","Teste3","Teste2","Teste1"]

    inputTemas = driver.find_element(By.NAME,"themeAdd")

    for i in newTemas:
        inputTemas.send_keys(i)
        inputTemas.send_keys(Keys.RETURN)
        inputTemas.clear()

    driver.find_element(By.CLASS_NAME,"icon-exclamation").click()
    time.sleep(10)
    link = driver.find_element(By.CLASS_NAME, 'PopShare').text
    link = link[5:10]
    return(link)


