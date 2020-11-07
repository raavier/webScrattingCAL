import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time

url = "https://www.iusnatura.com/Default.aspx?ReturnUrl=%2fRelatorioAtendimentoNormaAreas.aspx"
USER = "01477569"
PASSWORD = "@@0809878"

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
  "download.default_directory": r"C:\Users\flavi\OneDrive\code\py_Vale\CAL_Files",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True,
})

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
# options.add_argument("--headless")
# options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome('C:/chromedriver/chromedriver.exe', chrome_options=options)
print("Headless Chrome Initialized")
driver.get(url)


driver.find_element_by_id('lgnDefault_UserName').send_keys(USER)
driver.find_element_by_id('lgnDefault_Password').send_keys(PASSWORD)
time.sleep(2)
driver.find_element_by_id('lgnDefault_LoginButton').click()

# Relatorio 1
driver.find_element_by_id('ctl00_ContentPlaceHolder1_chkTodosCal').click()

time.sleep(3)
driver.find_element_by_id('ctl00_ContentPlaceHolder1_btnExportarAcao').click()
print("Download button clicked Relatorio 1")


# Relatorio 2
driver.get('https://www.iusnatura.com/RelatorioAtendimentoNormaAreas.aspx')
driver.find_element_by_id('ctl00_ContentPlaceHolder1_chkTodosCal').click()

time.sleep(3)
driver.find_element_by_id('ctl00_ContentPlaceHolder1_btnExportarNormas').click()
print("Download button clicked Relatorio 2")

# Relatorio 3
names = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for item in names:
    driver.get('https://www.iusnatura.com/Relatorio_ConformidadeLegalArea.aspx')
    driver.find_element_by_id("ctl00_ContentPlaceHolder1_rblCal_" + item).click()
    time.sleep(5)
    driver.find_element_by_id('ctl00_ContentPlaceHolder1_btnExportar').click()
    print("Download button clicked Relatorio "+item)
print("Finalizou os 10 relatorios")

# Relatorio 4

driver.get('https://www.iusnatura.com/Seguranca.aspx')
time.sleep(2)
driver.find_element_by_id('ctl00_ContentPlaceHolder1_btExportar').click()
print("Download button clicked Relatorio 5")
print("Finalizado")
driver.refresh()
time.sleep(5)
driver.close()


