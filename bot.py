from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException as erro
from webdriver_manager.chrome import ChromeDriverManager
import PySimpleGUI as sg
import time


class bot():
    
    loginusuario = 'DDIAS'
    loginsenha = 'risti123@'

    def __init__(self):
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        # self.navegador = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)  # Backgroud

        self.navegador = webdriver.Chrome(ChromeDriverManager().install())
        self.navegador.get('https://jfbricks.sienge.com.br/sienge/')

    def logIn(self):
        try:
            usuario = self.navegador.find_element_by_id('j_username')
            senha = self.navegador.find_element_by_id('j_password')
            usuario.send_keys(self.loginusuario)
            senha.send_keys(self.loginsenha)
            login = self.navegador.find_element_by_xpath("//button[@id='submit']").click()

        except erro:
            sg.popup('Erro')

        time.sleep(2)

    def logOff(self):
        self.navegador.find_element_by_xpath(
            "//div[@class='MuiAvatar-root MuiAvatar-circle MuiAvatar-colorDefault']").click()
        self.navegador.find_element_by_xpath("//span[@class='MuiButton-label']").click()

    def buscaInfo(self, emp):
        self.navegador.get('https://noroesteeng.sienge.com.br/sienge/8/index.html#/common/page/2590')


robo = bot()
robo.logIn()
robo.logOff()
