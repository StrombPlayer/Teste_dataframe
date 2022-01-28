from calendar import day_abbr
import time
from xml.etree.ElementInclude import include
from numpy import fix
import pandas as pd
import openpyxl

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

from partes import *
from info import *

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options=options)

site = 'http://plataforma.uberlandia.mg.gov.br/plataforma/f/t/segundaviaiptusel?tipoDivida=dmae'

fixed_pattern = '00030' 
mix = 201130100090000 
to_add = 100000000 

numbers_list = []
string_list = []
formatted_numbers = []
data_list = []
testing_df = []

df = pd.DataFrame()

#df = pd.DataFrame(columns=['Cod Reduzido', 'Insc Cadastral' ,'Imovel Endereco', 'Bairro', 'Quadra', 'Lote', 'Area Territorial', 'Area Predial', 'Testada', 'Cod Prefeitura', 'Contribuinte CPF', 'Contribuinte Nome', 'Contribuinte Endereco - CEP','Bairro'])

"""id = 1
while id < 30:
    # Tenho que setar a terceira parte em 0, para que o mix += 1.... funcione
    for number in range(30):
        mix += 10000
        numbers_list.append(mix)
    mix = 201130100090000 
    to_add += 100000000 
    mix += to_add
    id += 1"""

#primeira_parte(mix, numbers_list, formatted_numbers, fixed_pattern)

time.sleep(5)
driver.get(site)
#driver.find_element_by_xpath('/html/body/div[3]/form/div/center/table[4]/tbody/tr[4]/td[3]/span/input').send_keys('00030201130100090000')

def executar(terceira_parte, driver, df):
    terceira_parte(mix, numbers_list, formatted_numbers, fixed_pattern)
    for number in formatted_numbers:
        time.sleep(3)

        send_number = driver.find_element_by_xpath('/html/body/div[3]/form/div/center/table[4]/tbody/tr[4]/td[3]/span/input')
        send_number.send_keys(number)

        time.sleep(2)

        consultar = driver.find_element_by_xpath('/html/body/div[3]/form/div/div[2]/button[1]')
        consultar.click()

        time.sleep(3)

        try: 
            guardar_info(driver, df)
        except NoSuchElementException:
            time.sleep(5)
            limpar = driver.find_element_by_xpath('/html/body/div[3]/form/div/div[2]/button[2]')
            limpar.click()
        else:
            time.sleep(5)
            voltar = driver.find_element_by_xpath('/html/body/div[3]/form/div/div[2]/button[2]')
            voltar.click()

    print(df)
    df.to_excel('df_final.xlsx')
    #test1 = df.transpose()
    
        
executar(terceira_parte, driver, df)

