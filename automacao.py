import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"C:\Users\bruno\Documents\MeuProjetosPython\Python\chromedriver\chromedriver.exe") #Executar Webdriver
driver.get("https://www.google.com.br/") #Entrar na página do Google
element = driver.find_element(By.NAME, 'q').send_keys("abc") #Clicar na barra de pesquisa e escrever algo ""