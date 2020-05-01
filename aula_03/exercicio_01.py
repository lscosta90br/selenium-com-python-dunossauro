from selenium.webdriver import Chrome
from time import sleep
import json


url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'

navegador = Chrome()
navegador.get(url)
sleep(1)


h1 = navegador.find_element_by_tag_name('h1')
ps = navegador.find_elements_by_tag_name('p')

d = {}
def gera_dict(chave, valor):
    # chave = 'H1'
    # valor = h1.text
    registro = f'{{"{chave}": "{valor}"}}'
    registro = json.loads(registro)
    d.update(registro)
    return d


gera_dict(chave='H1', valor=h1.text)


for atributo in range(3):
    chave = ps[atributo].get_attribute('atributo')
    valor = ps[atributo].text
    gera_dict(chave=chave, valor=valor)


print(f'{d}')
navegador.quit()

