# send_messege
Envie mensagens automáticas com whatsapp desktop


Para utilizar esse script você precisa de algumas libs: re, sys, webbrowser, pyautogui, time, pyperclip

Funcionalidade do código:
         Assim que iniciar o programa ele vai abrir o prompt (caso tenha instalado com pyinstaller, se for usar como exe), senão vai abrir o prompt da sua IDLE, informe o texto que deseja e o programa vai criar um arquivo chamado msg.txt com o texto informado, seguindo com a declaração do numero e continuando com a execução do script. Na próxima vez que o script for executado, ele não vai mais precisar criar o arquivo msg.txt, mas o programa vai te perguntar se quer mudar o texto ou não. Você pode mudar o texto manualmente pelo arquivo msg.txt ou pelo programa.

Script foi idealizado para suprir uma necessidade de automação para enviar textos iguais para mais de um numero.

ATENÇÃO:
        dentro do código existe uma funcionalidade que pega a posição do seu mouse, ele é setado para um determinado padrão de resolução e para o desktop whatsapp janela
e não maximizada, caso tenha dificuldade com o pyautogui instalado na maquina vá em seu prompt python e import pyautogui e depois coloque pyautogui.position(), essa função vai exibir X e Y do seu mouse. Deixei marcado com comentario na função browser... quais partes precisam mudar caso necessário.

caso precise de ajuda meu contato: jesser.silva1508@gmail.com

para doações caso tenha ajudado, pix: jesser.silva1508@gmail.com (mercado pago)



 
