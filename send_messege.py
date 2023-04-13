#encoding: utf-8

import re
import sys
import webbrowser as wb
import pyautogui
import time
import pyperclip


#funções
def check_caracter(string):
    """-> Essa função conta quantos espaços e/ou
    outros caracteres especificados pelos if/elif da função
    """

    count = 0

    for i in string:
        if i == " ":
            count += 1
        elif i == "-":
            count += 1
        elif i == "(":
            count += 1
        elif i == ")":
            count += 1
        elif i == "+":
            count += 1

    return count
def browser_whats():
    with open("msg.txt", "r", encoding="utf-8") as file:
        msg = str(file.readline())
    mensagem = msg
    time.sleep(4)
    #cursor vai a opção iniciar conversa
    pyautogui.moveTo(592, 256)
    pyautogui.click()
    #whatapp abrirá e irá clicar em mensagem para enviar o texto desejado
    pyautogui.moveTo(1054, 873)
    pyautogui.click()
    time.sleep(2)
    pyperclip.copy(mensagem)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.hotkey('alt', 'tab')
    pyautogui.hotkey('ctrl', 'w')
def format_number(num):
    """ :param num: numero de telefone ou celular
        :return: url do whatsapp com o numero formatado
    """
    taman_num = int(len(num)) - check_caracter(num)

    if taman_num == 1:
        if num == "0":
            print("programa finalizado")
            sys.exit()

    if taman_num == 13 or taman_num == 11 or taman_num == 9:
        new_num = re.sub(r"[^0-9]", "", num)
        url = wb.open_new(f"https://wa.me/{new_num}")
        browser_whats()


    # trata as exceções
    else:
        if taman_num == 10 or taman_num == 12 or taman_num == 14:
            msg = print(f"Numero fornecido: {num}\nNumero de telefone fornecido está com 1 numero a mais "
                        f"e está fora do padrão, tente novamente: ")
            return msg
        elif taman_num < 9:
            msg = print(f"Numero de telefone fornecido está abaixo "
                        f"do padrão, tente novamente: ")
            return msg
        elif taman_num > 13:
            msg = print(f"Numero de telefone fornecido está acima "
                        f"do padrão, tente novamente: ")
            return msg
    return url

    time.sleep(3)
def valid_messege():
    try:
        with open("msg.txt", "r", encoding="utf-8") as file:
            msg = file.readline()
            print("mensagem no arquivo: ", msg)
            esc = input("se desejar alterar o arquivo digite s ou n para não alterar: ")
        while True:
            if esc == 's':
                msg = input("forneça o texto: ")
                with open("msg.txt", "w", encoding="utf-8") as file:
                    file.write(msg)
                    while True:
                        esc_confirm = input(f"{msg}, a mensagem está correta: [s/n]: ")
                        if esc_confirm == "s":
                            break
                        elif esc_confirm == "n":
                            msg = input("forneça o texto: ")
                            break
                        else:
                            esc = input("opção invalida, tente novamente:")
                break
            elif esc == 'n':
                pass
                break
            else:
                esc = input("resposta invalida, tente novamente: ")
    except FileNotFoundError:
        with open("msg.txt", "w") as file:
            msg = input("forneça o texto: ")
            with open("msg.txt", "w") as file:
                file.write(msg)

#Execução do programa

if __name__=='__main__':
    print("para sair do programa digite 0")
    valid_messege()
    while True:
        num = input("Forneça o numero: ").strip()
        format_number(num)






