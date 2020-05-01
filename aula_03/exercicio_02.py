from selenium.webdriver import Chrome
from time import sleep

url = 'https://curso-python-selenium.netlify.app/exercicio_02.html'

navegador = Chrome()
navegador.get(url)

sleep(2)

ps = navegador.find_elements_by_tag_name('p')
for num in range(len(ps)):
    p = ps[num].text
    if "Numero esperado" in p:
        p = p.split(':')
        numero_esperado = int(p[1])

# print(numero_esperado)
# print(type(numero_esperado))
def localiza_premio():
    a = navegador.find_element_by_tag_name('a')
    a.click()
    sleep(2)
    ps = navegador.find_elements_by_tag_name('p')
    sleep(2)
    
    ps_text = {ps[-1].text}
    print(ps_text)
    return ps_text


while 1:
    lp = localiza_premio()
    if len(lp) > 1:
        print(f'aqui: {lp}')
        break


