from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def hack_game(link, driver):
    print("Starting Hacker! Sit back and relax for a while")
    try:
        letra = driver.find_element(By.ID, "letter").text
        if letra == "?":
            exit(1)
        print(letra)

        temasRaw = driver.find_elements(By.TAG_NAME, "span")

        temas = []
        for i in temasRaw[3:]:
            temas.append(i.text)

        print(temas)
        return 0
    except Exception as e:
        print("An Error ocurred! Make sure your at the point where a letter is defined and the round has began! Error:", e)
        return 1


