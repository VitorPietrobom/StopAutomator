from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import GameHacker

def create_game(driver):
    print("Creating game... Sit back and relax for a while")

    driver.get("https://stopots.com.br/")
    time.sleep(1)

    driver.find_element(By.CLASS_NAME, "enter").click()
    time.sleep(1)

    driver.find_element(By.TAG_NAME, "input").clear()
    driver.find_element(By.TAG_NAME, "input").send_keys("Paulinho")
    driver.find_element(By.CLASS_NAME, "icon-gear").click()
    time.sleep(1)

    old_temas = driver.find_elements(By.CLASS_NAME, "del")
    for i in old_temas:
        i.send_keys(Keys.RETURN)

    new_temas = ["Cor", "CEP", "Nome", "Anime/Desenho", "Serie/Filme", "Animal", "Super Poder", "Personagem Ficticio", "Marca", "Teste3", "Teste2", "Teste1"]
    input_temas = driver.find_element(By.NAME, "themeAdd")

    for i in new_temas:
        input_temas.send_keys(i)
        input_temas.send_keys(Keys.RETURN)
        input_temas.clear()

    driver.find_element(By.CLASS_NAME, "icon-exclamation").click()
    time.sleep(10)
    link = driver.find_element(By.CLASS_NAME, 'PopShare').text
    link = link[5:10]
    print("Game created successfully! Link:", link)
    return link


