import socket
from telnetlib import STATUS
import threading
import time

PORT = 5050
FORMATO = 'utf-8'
SERVER = "192.168.48.1"
ADDR = (SERVER, PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def handle_mensagens():
    while(True):
        msg = client.recv(1024).decode()
        mensagem_splitada = msg.split("=")
        print(mensagem_splitada[0] + ": " + mensagem_splitada[1])

def enviar_mensagem(mensagem):
        client.send(mensagem.encode(FORMATO))
    
def iniciar_envio():
    status = True
    while(status):
        mensagem = input()
        enviar_mensagem("msg=" + mensagem)
        # if mensagem == "#":
        #     print('Desconectando Cliente')
        #     status = False
        #     print(status)
        #     t = threading.currentThread()

        #     break

def iniciar():
    thread1 = threading.Thread(target=handle_mensagens)
    thread2 = threading.Thread(target=iniciar_envio)
    thread1.start()
    thread2.start()

nome = input('Digite seu nome: ')
enviar_mensagem("nome=" + nome)
enviar_mensagem("msg=" + "Entrou no grupo!")

iniciar()