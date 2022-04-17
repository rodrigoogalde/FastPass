import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support.select import Select
from datetime import datetime
import os


class Chrome:
    def __init__(self, fecha):
        self.options = Options()
        self.fecha = fecha
        self.options.page_load_strategy = 'eager'
        self.options.add_argument(r"--user-data-dir=C:/Users/condo/AppData/Local/Google/Chrome/User Data")
        self.options.add_argument(r'--profile-directory=Default')
        self.driver = webdriver.Chrome(executable_path=r'C:/Users/condo/chromedriver.exe', chrome_options=self.options)

    def Iniciar(self):
        self.driver.get('https://online.fleetuptrace.com/v4/index.do#!/Dashboard%20/%20Reporte')

        self.driver.find_element(By.XPATH, '//*[@id="checkUserForm"]/button').send_keys(Keys.ENTER)
        time.sleep(5)
        # self.driver.find_element(By.XPATH, '//*[@id="menu_8"]/span').click()
        self.driver.get('https://online.fleetuptrace.com/v4/index.do#!/Dashboard%20/%20Reporte')
        self.driver.refresh()

        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="tools-list"]/div[3]/button[2]').send_keys(Keys.ENTER)
        lis = Select(self.driver.find_element(By.XPATH, '//*[@id="main"]/div/section[1]/div/main/form/div[1]/label[2]/select'))
        lis.select_by_visible_text('Reporte de Datos de Velocidad Diaria')

        self.driver.find_element(By.XPATH, "//div[@id='main']/div/section/div/main/form/div[2]/div/div/label/input").send_keys(Keys.ENTER)
        # /html/body/div[11]/div[1]/ul/li[7]
        # xpath=//form/div[2]/div/div/label/input

        self.driver.find_element(By.XPATH, "/html/body/div[11]/div[1]/ul/li[7]").click()
        # //*[@id="1"]/div[11]/div[3]/div[1]/table
        tabla = self.driver.find_element(By.XPATH, '//*[@id="1"]/div[11]/div[3]/div[1]/table')
        # ubi = tabla.find_elements(By.PARTIAL_LINK_TEXT, 10)
        body = tabla.find_elements(By.TAG_NAME, 'tbody')
        celda = body.find_elements(By.TAG_NAME, 'td')

        for ele in celda:
            print(ele.text)


        datapicker = Select(self.driver.find_element(By.XPATH, '//*[@id="startDate"]'))
        # //*[@id="startDate"]
        # self.driver.find_element(By.XPATH, '//*[@id="main"]/div/section[1]/div/main/form/div[2]/div[1]/div/label/input[1]').send_keys(Keys.ENTER)
        datapicker.select_by_visible_text('Rango personalizado')

        # datapicker.send_keys(Keys.ENTER)
        self.driver.find_element(By.XPATH, "//*[@id=\'1\']/div[11]/div[1]/ul/li[7]").click()




Obj = Chrome('10/04/2022')
Obj.Iniciar()
