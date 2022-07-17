import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pygetwindow
import pyautogui
import pywinauto.mouse as mouse
from pywinauto.keyboard import send_keys
import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt
import sys
import re
import fitz
import six
#import autoit



foro = pd.read_excel(r'C:\Users\mac1196\Desktop\Robô_INICIAL\DBRobo_Inicial\SP\Dados_AYMORE\Pasta1.xlsx', sheet_name='Planilha1')
for index, valor in foro.iterrows():
     valor[index] = valor[index].rstrip('\r\n').replace('\n',' ')
     comarca = valor['foro']
     if (comarca == " "):
      print(comarca)



     #guia = valor['guia']#versão antiga de extrair a guia
     #if(guia ==" "):
      #print(valor['guia'][9:24]+'-0001')
      #print(valor['guia'])

     cep = valor['cep']
     if (cep == " "):
      cep = re.sub("\_x000D_|\'|\?", "", cep)

     cnpj = valor["cnpj"]
     if (cnpj == " "):
      print(valor['cnpj'])

     cpf = valor['cpf']
     if (cpf == " "):
      print(valor['cpf'])

     nome = valor['nome']
     nome = re.sub("\_x000D_|\'|\?", "", nome)
     print(nome)

     numero = valor['numero']
     if (numero == " "):
      numero = re.sub("\_x000D_|\'|\?", "", numero)
     print(numero)

     rg = valor['rg']
     rg = re.sub("\_x000D_|\'|\?", "", rg)
     print(rg)

     orgao = valor['orgao']
     if (orgao == " "):
      orgao = re.sub("\_x000D_|\'|\?", "", orgao)

     print(orgao)

     causa = valor['valor']
     if (causa == " "):
      causa = re.sub("\_x000D_|\'|\?", "", causa)
     print(causa)

     camin = valor['caminho']
     if (camin == " "):
      camin = re.sub("\_x000D_|\'|\?", "", camin)
     print(camin)

     # Extrair o número do DARE
     # faz a leitura
     with fitz.open(camin) as pdf:
         texto = ""
         for pagina in pdf:
             texto += pagina.get_text()
         texto
     print(texto)

     causa2 = re.findall(r'(?<=corresponde à)\s\S.+', texto)
     print(causa2)

     camin2 = valor['caminho2']
     if (camin2 == " "):
      camin2 = re.sub("\_x000D_|\'|\?", "", camin2)
     print(camin2)

     camin3 = valor['caminho3']
     if (camin3 == " "):
      camin3 = re.sub("\_x000D_|\'|\?", "", camin3)
     print(camin3)

     camin4 = valor['caminho4']
     if (camin4 == " "):
      camin4 = re.sub("\_x000D_|\'|\?", "", camin4)
     print(camin4)

     camin5 = valor['caminho5']
     if (camin5 == " "):
      camin5 = re.sub("\_x000D_|\'|\?", "", camin5)
     print(camin5)

     camin6 = valor['caminho6']
     if (camin6 == " "):
      camin6 = re.sub("\_x000D_|\'|\?", "", camin6)
     print(camin6)

     camin7 = valor['caminho7']
     if (camin7 == " "):
      camin7 = re.sub("\_x000D_|\'|\?", "", camin7)
     print(camin7)

     camin8 = valor['caminho8']
     if (camin8 == ""):
      camin8 = re.sub("\_x000D_|\'|\?", "", camin8)
      print(camin8)

     camin9 = valor['caminho9']
     if (camin9 == " "):
      camin9 = re.sub("\_x000D_|\'|\?", "", camin9)
     print(camin9)

     camin10 = valor['caminho10']
     if (camin10 == " "):
      camin10 = re.sub("\_x000D_|\'|\?", "", camin10)
     print(camin10)

     camin11 = valor['caminho11']
     if (camin11 == " "):
      camin11 = re.sub("\_x000D_|\'|\?", "", camin11)
     print(camin11)

     camin12 = valor['caminho12']
     if (camin12 == " "):
      camin12 = re.sub("\_x000D_|\'|\?", "", camin12)
     print(camin12)



camin13 = valor['caminho13']
if camin13 == camin13:
#if (camin13 == " "):
   camin13 = re.sub("\_x000D_|\'|\?", "", camin13)
print(valor['caminho13'])
#Extrair o número do DARE
     #faz a leitura
with fitz.open(camin12) as pdf:
    texto = ""
    for pagina in pdf:
      texto += pagina.get_text()
    texto
print(texto)

dare = re.findall(r'(?<=Financeiro)\s\S.+', texto)
print(dare)


camin14 = valor['caminho14']
if (camin14 == " "):
  camin14 = re.sub("\_x000D_|\'|\?", "", camin14)
print(camin14)

camin15 = valor['caminho15']
if (camin15 == " "):
  camin15 = re.sub("\_x000D_|\'|\?", "", camin15)
print(camin15)

camin16 = valor['caminho16']
if (camin16 == " "):
  camin16 = re.sub("\_x000D_|\'|\?", "", camin16)
print(camin16)

camin17 = valor['caminho17']
if (camin17 == " "):
 camin17 = re.sub("\_x000D_|\'|\?", "", camin17)
print(camin17)

camin18 = valor['caminho18']
if (camin18 == " "):
  print(camin18)


camin19 = valor['caminho19']
if (camin19 == " "):
  print(camin19)


#numero = pd.read_excel(r'C:\Users\mac1017\Desktop\DEV_Consulta_DB\teste1.xlsx', sheet_name='Planilha1',usecols='K')
#cpf = pd.read_excel(r'C:\Users\mac1017\Desktop\DEV_Consulta_DB\teste1.xlsx', sheet_name='Planilha1',usecols='F')


#pasta = r'P:\### PUBLICA - MAC BARBOSA ###\04.JURIDICO\ANDREA MAIA\PENDÊNCIAS - EXTINÇÕES JURÍDICO\CONTRATOS PARA PETICIONAR NO TJ\ROBÔ\GO'
#for diretorio, subpastas, arquivos in os.walk(pasta):
#    for arquivo in arquivos:
#       print(os.path.join(os.path.join(diretorio), arquivo))
#       time.sleep(1)
options = webdriver.ChromeOptions()
options.headless = False
options.add_extension('C:/Users/mac1196/Desktop/Robô_INICIAL/DBRobo_Inicial/SP/extensão/Web Signer 2.14.3.0.crx')
navegador = webdriver.Chrome(r"C:/Users/mac1196/Desktop/Robô_INICIAL/DBRobo_Inicial/SP/DriveChrome/chromedriver.exe", chrome_options=options)
#navegador = webdriver.Chrome(r"C:/Users/mac1017/Desktop/Robôs_finalizados/DriveChrome/chromedriver.exe")
navegador.implicitly_wait(20)

navegador.get("https://esaj.tjsp.jus.br/esaj/portal.do?servico=190090")
#time.sleep(2)
navegador.find_element_by_xpath('//*[@id="identificacao"]/strong/a').click()
#time.sleep(5)
#Clica no cpf
navegador.find_element_by_xpath('//*[@id="linkAbaCpf"]').click()
time.sleep(5)
#INSERE O LOGIN
navegador.find_element_by_xpath('/html/body/table[4]/tbody/tr/td/table[2]/tbody/tr[1]/td[1]/div/table/tbody/tr[1]/td/div[2]/div[2]/form/div[1]/table/tbody/tr[1]/td[2]/input').send_keys('10208311890')
time.sleep(5)
#insere a senha
navegador.find_element_by_xpath('/html/body/table[4]/tbody/tr/td/table[2]/tbody/tr[1]/td[1]/div/table/tbody/tr[1]/td/div[2]/div[2]/form/div[1]/table/tbody/tr[2]/td[2]/input').send_keys('mac@abril')
time.sleep(7)

#clica no botão
navegador.find_element_by_xpath('/html/body/table[4]/tbody/tr/td/table[2]/tbody/tr[1]/td[1]/div/table/tbody/tr[1]/td/div[2]/div[2]/form/div[1]/table/tbody/tr[4]/td[2]/input[4]').click()
#time.sleep(50)
#Popup DE ALERTA
#title = 'Alerta de Segurança'
#window = pygetwindow.getWindowsWithTitle(title)[0]
#window.activate()
#mouse.click(coords=(548, 480))
#time.sleep(20)
#insere o pin
#title = 'Introduzir PIN'
#window = pygetwindow.getWindowsWithTitle(title)[0]
#window.activate()
#pyautogui.typewrite("86536")
#mouse.click(coords=(501, 424))
time.sleep(10)
#Clica em peticionamento eletronico
navegador.find_element_by_xpath('//*[@id="esajMenuArea"]/li[14]/a').click()
#time.sleep(5)
navegador.find_element_by_xpath('//*[@id="esajMenuArea"]/li[14]/ul/li[2]/a').click()
#time.sleep(2)
navegador.find_element_by_xpath('//*[@id="esajMenuArea"]/li[14]/ul/li[2]/ul/li[1]/a').click()
#time.sleep(10)
#Clica em informar dados
navegador.find_element_by_xpath('//*[@id="containerDadosBasicos"]/div/div/button').send_keys("/")
pyautogui.press({"Enter"})
pyautogui.press({"TAB"})
pyautogui.press({"Enter"})
time.sleep(2)
send_keys(comarca,with_spaces=True,pause=0)
time.sleep(5)
navegador.find_element_by_xpath('//*[@id="ui-select-choices-row-3-0"]/span').click()
#navegador.implicitly_wait(30)
time.sleep(5)
pyautogui.press({"TAB"})
send_keys('Cível')
#pyautogui.typewrite("civ")
navegador.find_element_by_xpath('//*[@id="ui-select-choices-row-4-0"]/span').click()
#navegador.implicitly_wait(30)
#Clica em classe
navegador.find_element_by_xpath('//*[@id="btnAbrirArvoreClasses"]/span').click()
#navegador.implicitly_wait(30)
navegador.find_element_by_xpath('//*[@id="inputFiltroArvore"]').send_keys(81)
#navegador.implicitly_wait(3)
navegador.find_element_by_xpath('//*[@id="nodo_8546"]').click()
#navegador.implicitly_wait(3)
navegador.find_element_by_xpath('//*[@id="btnConfirmarSelecaoTree"]').click()
#navegador.implicitly_wait(5)
#Clica em assunto pricipal
navegador.find_element_by_xpath('//*[@id="btnAbrirArvoreAssuntos"]/span').click()
#navegador.implicitly_wait(5)
navegador.find_element_by_xpath('//*[@id="inputFiltroArvore"]').send_keys(9582)
#navegador.implicitly_wait(5)
navegador.find_element_by_xpath('//*[@id="nodo_9582"]').click()
#navegador.implicitly_wait(5)
navegador.find_element_by_xpath('//*[@id="btnConfirmarSelecaoTree"]').click()
time.sleep(9)
#navegador.implicitly_wait(20)
#Clica em pedido de liminar
pyautogui.press({"TAB"})
pyautogui.press({"TAB"})
pyautogui.press({"TAB"})
pyautogui.press({"SPACE"})

navegador.implicitly_wait(5)
#Clica em segredo de justiça
pyautogui.press({"TAB"})
pyautogui.press({"SPACE"})
navegador.implicitly_wait(5)
#Clica em Valor da ação
pyautogui.press({"TAB"})
#valor da causa
navegador.find_element_by_xpath('//*[@id="inputValorAcao"]').send_keys(causa2)
#send_keys(causa)
time.sleep(10)
#pyautogui.typewrite(causa)

#clica em guia de recolhimento
#pyautogui.press({"TAB"})
#pyautogui.press({"TAB"})
#pyautogui.press({"TAB"})
#pyautogui.press({"TAB"})
#pyautogui.press({"DOWN"})
#pyautogui.press({"space"})
#navegador.implicitly_wait(5)
#Move a barra de rolagem
navegador.execute_script('window.scrollTo(0, window.scrollY + 1000)')
time.sleep(10)
#Clica no botão documento
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[2]/div/div/section[2]/div/div[2]/div/div[5]/div/ng-include/div[1]/radio-input[2]/div/label').click()
time.sleep(6)
pyautogui.press({"TAB"})
pyautogui.press({"space"})
time.sleep(6)
#Move a barra de rolagem
navegador.execute_script('window.scrollTo(0, window.scrollY + 200)')
time.sleep(10)

#Insere o valor da guia
navegador.find_element_by_xpath('//*[@id="numeroGuiaDare"]').send_keys(dare)
#navegador.find_element_by_xpath('//*[@id="numeroGuiaDare"]').send_keys(str(valor['guia']))#VERSÃO ANTIGA
pyautogui.press({"TAB"})
navegador.implicitly_wait(15)
pyautogui.press({"space"})
time.sleep(6)
#Clica na aba para fechar a janela preenchida
pyautogui.press({"TAB"})
pyautogui.press({"TAB"})
pyautogui.press({"TAB"})
pyautogui.press({"space"})
#Clica em polo ativo
pyautogui.press({"TAB"})
pyautogui.press({"space"})
pyautogui.press({"TAB"})
pyautogui.press({"space"})
navegador.implicitly_wait(2)
#Clica em Juridico
navegador.find_element_by_xpath('//*[@id="parteEditDadosPessoa"]/div[2]/div[1]/fieldset/radio-input[2]/div/label').click()
time.sleep(2)
navegador.find_element_by_xpath('//*[@id="inputCnpj"]').send_keys(valor['cnpj'])
time.sleep(5)
pyautogui.press({"TAB"})
time.sleep(20)

#Move a barra de rolagem
navegador.execute_script('window.scrollTo(0, window.scrollY + 1000)')
time.sleep(10)
#Clica em polo passivo
#Clica na parte polo passivo
navegador.find_element_by_xpath('//*[@id="adicionar-polopassivo"]/span[1]').click()
#time.sleep(2)
navegador.find_element_by_xpath('//*[@id="menu-adicionar-polopassivo"]/li/button').click()
#time.sleep(3)

#navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[2]/div/div/section[3]/div/div[2]/div/div/ng-include/div/div/div/div/ul/li[2]/button').send_keys("/")
#pyautogui.press({"TAB"})
#pyautogui.press({"space"})
#pyautogui.press({"TAB"})
#pyautogui.press({"space"})
#time.sleep(2)
#insere o cpf
navegador.find_element_by_xpath('//*[@id="campoCpf"]').send_keys(valor['cpf'])
time.sleep(10)
pyautogui.press({"TAB"})
#Limpa o campo do nome
navegador.find_element_by_xpath('//*[@id="campoNome"]').clear()
time.sleep(5)
#insere o nome

navegador.find_element_by_xpath('//*[@id="campoNome"]').send_keys(nome)
pyautogui.press({"TAB"})
time.sleep(5)
#insere o rg
navegador.find_element_by_xpath('//*[@id="campoRg"]').clear()
time.sleep(5)
navegador.find_element_by_xpath('//*[@id="campoRg"]').send_keys(rg)
#insere o orgão do rg
#Limpa o campo primeiro
navegador.find_element_by_xpath('//*[@id="campoOrgaoEmissor"]').clear()
time.sleep(4)
navegador.find_element_by_xpath('//*[@id="campoOrgaoEmissor"]').send_keys(valor['orgao'])
time.sleep(10)

#LImpar o campo
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[2]/div/div/section[4]/div/div[2]/div/div/ng-include/div/div/ng-if/div[2]/div/div/div[1]/div/input').clear()
time.sleep(5)

#Insere o cep
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[2]/div/div/section[4]/div/div[2]/div/div/ng-include/div/div/ng-if/div[2]/div/div/div[1]/div/input').send_keys(cep)
time.sleep(5)

#Limpara o campo
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[2]/div/div/section[4]/div/div[2]/div/div/ng-include/div/div/ng-if/div[2]/div/div/div[3]/div/input').clear()
time.sleep(5)

#Insere o número
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[2]/div/div/section[4]/div/div[2]/div/div/ng-include/div/div/ng-if/div[2]/div/div/div[3]/div/input').send_keys(numero)
time.sleep(5)

#Move a barra de rolagem para baixo
navegador.execute_script('window.scrollTo(0, window.scrollY + 200)')
time.sleep(9)
#pyautogui.moveTo(996,451)
#pyautogui.mouseUp()
#pyautogui.moveTo(997,185)
#Clica na janela de anexar arquivos sem passar pela janela abrir
test = camin
navegador.find_element_by_xpath('//*[@id="botaoAdicionarDocumento"]/input').send_keys(test)
#versão antiga de anexar pdf
#navegador.find_element_by_xpath('//*[@id="botaoAdicionarDocumento"]').send_keys("/")
#pyautogui.press({"ENTER"})
time.sleep(20)
#Clica no segundo botão para adicionar 2 pdf
test2 = camin2
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/section/button/input').send_keys(test2)
time.sleep(5)
#Move a barra para cima
navegador.execute_script('scrollBy(0,-1000);')
time.sleep(9)
#pyautogui.moveTo(997,423)
#pyautogui.press({'PAGEUP'})
#pyautogui.moveTo(996,357)
#pyautogui.press({'PAGEUP'})
#pyautogui.moveTo(1003,216)
#time.sleep(6)


#Clica no tipo de contrato
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/div/section[3]/div/footer/div/ul/li/div/nav/div/ul/li[3]/span/div/div[1]/span/span[1]').click()
#Insere valor do campo
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/div/section[3]/div/footer/div/ul/li/div/nav/div/ul/li[3]/span/div/input[1]').send_keys('Planilha de Calculos')
navegador.find_element_by_xpath('//*[@id="ui-select-choices-row-14-0"]/span/div').click()
#time.sleep(5)

#Isere 3 pdf
test3 = camin3
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/section/button/input').send_keys(test3)
time.sleep(5)
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/div/section[3]/div/footer/div/ul/li[2]/div/nav/div/ul/li[3]/span/div/div[1]/span/span[1]').click()
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/div/section[3]/div/footer/div/ul/li[2]/div/nav/div/ul/li[3]/span/div/input[1]').send_keys('Documento 1')
navegador.find_element_by_xpath('//*[@id="ui-select-choices-row-15-0"]/span/div').click()
#send_keys('Planilha de Cálculos',with_spaces=True,pause=0)
time.sleep(5)
#Move a barra para baixo
#navegador.execute_script('window.scrollTo(0, window.scrollY + 200)')
#time.sleep(9)
#pyautogui.moveTo(997,285)
#pyautogui.mouseDown()
#pyautogui.moveTo(996,326)
#pyautogui.moveTo(996,368)


time.sleep(5)
#Isere 4 pdf
test4 = camin4
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/section/button/input').send_keys(test4)
time.sleep(5)
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/div/section[3]/div/footer/div/ul/li[3]/div/nav/div/ul/li[3]/span/div/div[1]/span/span[1]').click()
time.sleep(2)
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/div/section[3]/div/footer/div/ul/li[3]/div/nav/div/ul/li[3]/span/div/input[1]').send_keys('Procuração')
time.sleep(2)
navegador.find_element_by_xpath('//*[@id="ui-select-choices-row-16-0"]/span/div').click()
time.sleep(5)

#Isere 5 pdf
test5 = camin5
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/section/button/input').send_keys(test5)
time.sleep(5)
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/div/section[3]/div/footer/div/ul/li[4]/div/nav/div/ul/li[3]/span/div/div[1]/span/span[1]').click()
#time.sleep(2)
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/div/section[3]/div/footer/div/ul/li[4]/div/nav/div/ul/li[3]/span/div/input[1]').send_keys('Procuração')
#time.sleep(2)
navegador.find_element_by_xpath('//*[@id="ui-select-choices-row-17-0"]/span/div').click()
#time.sleep(5)

#Isere 6 pdf
test6 = camin6
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/section/button/input').send_keys(test6)
time.sleep(5)
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/div/section[3]/div/footer/div/ul/li[5]/div/nav/div/ul/li[3]/span/div/div[1]/span/span[1]').click()
#time.sleep(2)
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/div/section[3]/div/footer/div/ul/li[5]/div/nav/div/ul/li[3]/span/div/input[1]').send_keys('Contrato Social')
#time.sleep(2)
navegador.find_element_by_xpath('//*[@id="ui-select-choices-row-18-0"]/span/div').click()
#time.sleep(5)

#Isere 7 pdf
test7 = camin7
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/section/button/input').send_keys(test7)
time.sleep(5)
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/div/section[3]/div/footer/div/ul/li[6]/div/nav/div/ul/li[3]/span/div/div[1]/span/span[1]').click()
#time.sleep(2)
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/div/section[3]/div/footer/div/ul/li[6]/div/nav/div/ul/li[3]/span/div/input[1]').send_keys('Contrato')
#time.sleep(2)
navegador.find_element_by_xpath('//*[@id="ui-select-choices-row-19-0"]/span/div').click()
#time.sleep(5)

#Insere 8 pdf

#Se o 8 existe segue caminho do 20 em diante
camin8 == camin8

navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/section/button/input').send_keys(camin8)
time.sleep(5)
#if (test8 == test8):
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/div/section[3]/div/footer/div/ul/li[7]/div/nav/div/ul/li[3]/span/div/div[1]/span/span[1]').click()
#time.sleep(2)
#if (test8 == test8):
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/div/section[3]/div/footer/div/ul/li[7]/div/nav/div/ul/li[3]/span/div/input[1]').send_keys('Contrato')
#time.sleep(2)
#if (test8 == test8):
navegador.find_element_by_xpath('//*[@id="ui-select-choices-row-20-0"]/span/div').click()
#time.sleep(5

if camin9 == camin9:

     navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/section/button/input').send_keys(camin9)
     time.sleep(5)
     navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/div/section[3]/div/footer/div/ul/li[8]/div/nav/div/ul/li[3]/span/div/div[1]/span/span[1]').click()
     #time.sleep(2)
     navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/div/section[3]/div/footer/div/ul/li[8]/div/nav/div/ul/li[3]/span/div/input[1]').send_keys('Notificação Extrajudicial')
     #time.sleep(2)
     #if (test8 == test8):
     navegador.find_element_by_xpath('//*[@id="ui-select-choices-row-21-0"]/span/div').click()
     #time.sleep(5)

else:
  navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/section/button/input').send_keys(camin10)
  time.sleep(5)
  navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/div/section[3]/div/footer/div/ul/li[8]/div/nav/div/ul/li[3]/span/div/div[1]/span/span[1]').click()
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/div/section[3]/div/footer/div/ul/li[8]/div/nav/div/ul/li[3]/span/div/input[1]').send_keys('Notificação Extrajudicial')
navegador.find_element_by_xpath('//*[@id="ui-select-choices-row-21-0"]/span/div').click()

#Move a barra de rolagem
navegador.execute_script('window.scrollTo(0, window.scrollY + 200)')
time.sleep(9)


camin11 = camin11
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/section/button/input').send_keys(camin11)
time.sleep(3)
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/div/section[3]/div/footer/div/ul/li[9]/div/nav/div/ul/li[3]/span/div/div[1]/span/span[1]').click()
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/div/section[3]/div/footer/div/ul/li[9]/div/nav/div/ul/li[3]/span/div/input[1]').send_keys('Documento 2')
navegador.find_element_by_xpath('//*[@id="ui-select-choices-row-22-0"]/span/div').click()

test12 = camin12
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/section/button/input').send_keys(test12)
time.sleep(5)
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/div/section[3]/div/footer/div/ul/li[10]/div/nav/div/ul/li[3]/span/div/div[1]/span/span[1]').click()
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/div/section[3]/div/footer/div/ul/li[10]/div/nav/div/ul/li[3]/span/div/input[1]').send_keys('Guia de Custas')
navegador.find_element_by_xpath('//*[@id="ui-select-choices-row-23-0"]/span/div').click()

if camin13 == camin13:
 navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/section/button/input').send_keys(camin13)
time.sleep(3)
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/div/section[3]/div/footer/div/ul/li[11]/div/nav/div/ul/li[3]/span/div/div[1]/span/span[1]').click()
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/div/section[3]/div/footer/div/ul/li[11]/div/nav/div/ul/li[3]/span/div/input[1]').send_keys('Guia de Custas')
navegador.find_element_by_xpath('//*[@id="ui-select-choices-row-24-0"]/span/div').click()

test14 = camin14
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/section/button/input').send_keys(test14)
time.sleep(3)
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/div/section[3]/div/footer/div/ul/li[12]/div/nav/div/ul/li[3]/span/div/div[1]/span/span[1]').click()
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/div/section[3]/div/footer/div/ul/li[12]/div/nav/div/ul/li[3]/span/div/input[1]').send_keys('Guia de Custas')
navegador.find_element_by_xpath('//*[@id="ui-select-choices-row-25-0"]/span/div').click()

#Move a barra de rolagem para baixo
navegador.execute_script('window.scrollTo(0, window.scrollY + 200)')
time.sleep(9)


test15 = camin15
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/section/button/input').send_keys(test15)
time.sleep(3)
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/div/section[3]/div/footer/div/ul/li[13]/div/nav/div/ul/li[3]/span/div/div[1]/span/span[1]').click()
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/div/section[3]/div/footer/div/ul/li[13]/div/nav/div/ul/li[3]/span/div/input[1]').send_keys('Guia de Custas')
navegador.find_element_by_xpath('//*[@id="ui-select-choices-row-26-0"]/span/div').click()

test16 = camin16
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/section/button/input').send_keys(test16)
time.sleep(3)
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/div/section[3]/div/footer/div/ul/li[14]/div/nav/div/ul/li[3]/span/div/div[1]/span/span[1]').click()
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/div/section[3]/div/footer/div/ul/li[14]/div/nav/div/ul/li[3]/span/div/input[1]').send_keys('Guia de Custas')
navegador.find_element_by_xpath('//*[@id="ui-select-choices-row-27-0"]/span/div').click()

test17 = camin17
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/section/button/input').send_keys(test17)
time.sleep(3)
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/div/section[3]/div/footer/div/ul/li[15]/div/nav/div/ul/li[3]/span/div/div[1]/span/span[1]').click()
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/div/section[3]/div/footer/div/ul/li[15]/div/nav/div/ul/li[3]/span/div/input[1]').send_keys('Guia de Custas')
navegador.find_element_by_xpath('//*[@id="ui-select-choices-row-28-0"]/span/div').click()

navegador.execute_script('window.scrollTo(0, window.scrollY + 200)')
time.sleep(9)

if camin18 == camin18:
 navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/section/button/input').send_keys(camin18)
time.sleep(3)
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/div/section[3]/div/footer/div/ul/li[16]/div/nav/div/ul/li[3]/span/div/div[1]/span/span[1]').click()
navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/div/section[3]/div/footer/div/ul/li[16]/div/nav/div/ul/li[3]/span/div/input[1]').send_keys('Guia de Custas')
navegador.find_element_by_xpath('//*[@id="ui-select-choices-row-29-0"]/span/div').click()

if camin19 == camin19:

   navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/section/button/input').send_keys(camin19)
   time.sleep(3)
   navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/div/section[3]/div/footer/div/ul/li[17]/div/nav/div/ul/li[3]/span/div/div[1]/span/span[1]').click()
   navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/div/article/div/section[3]/div/footer/div/ul/li[17]/div/nav/div/ul/li[3]/span/div/input[1]').send_keys('Guia de Custas')
   navegador.find_element_by_xpath('//*[@id="ui-select-choices-row-30-0"]/span/div').click()



#Clica em baixar protocolo
#navegador.find_element_by_xpath('/html/body/span/main/div/div/div/form/div/div/div[1]/div/div/section/div/div[1]/div/div/div/div/button').click()
time.sleep(5)

#Move a barra para cima
navegador.execute_script('scrollBy(0,-1000);')
time.sleep(9)

#Clica no botão download
navegador.find_element_by_xpath('//*[@id="icon"]/iron-icon//svg').click()


#Se O O8 NÃO EXISTIR SEGUE O CODIGO ACIMA


#navegador.close()HABILITAR SOMENTE QUANDO ESTIVER EM LINHA
sys.exit()
