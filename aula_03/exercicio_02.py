#### Feito por:
### Leandro Costa
### com ajuda de: Carlos Augusto Moreno, [01.05.20 01:44]
from selenium.webdriver import Chrome
from time import sleep

url = 'https://curso-python-selenium.netlify.app/exercicio_02.html'

navegador = Chrome()
navegador.get(url)

sleep(2)

a = navegador.find_element_by_tag_name('a')
ps = navegador.find_elements_by_tag_name('p')

def localiza_premio():
    ps = navegador.find_elements_by_tag_name('p')
    ps_text = ps[-1].text.split()[-1]
    print(ps_text)
    return ps_text

premio = localiza_premio()

a.click()
numero_gerado = localiza_premio()

print(numero_gerado)
print(premio)

while numero_gerado != premio:
    a.click()
    numero_gerado = localiza_premio()
