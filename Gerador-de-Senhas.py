import random
import string
import PySimpleGUI as sg      

layout = [[sg.Text("ok")],      
                 [sg.InputText()],      
                 [sg.Submit(), sg.Cancel()]]      

window = sg.Window('Window Title', layout)    

event, values = window.read()    
window.close()

text_input = values[0]    
sg.popup('You entered', text_input)


numero_de_senhas_geradas = 1
#fazer para que o usuario escolha a quantidades de senhas!!
numeros_de_caracteress = 9
#fazer para que o usuario escolha a quantidades de caracteres!!
senha = ""
for x in range(numeros_de_caracteress):
  senha += (''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(numero_de_senhas_geradas)))
print(senha)


event, values = sg.Window('Login Window',
                  [[sg.T('Enter your Login ID'), sg.In(key='-ID-')],
                  [sg.B('OK'), sg.B('Cancel') ]]).read(close=True)

login_id = values['-ID-']

