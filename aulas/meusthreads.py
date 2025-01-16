from time import sleep
from threading import Thread

# class MeuThread(Thread):
#     def __init__(self, texto, tempo):
#         self.tempo = tempo
#         self.tempo = tempo

#         super().__init__()

#     def run(self):
#         sleep(self.tempo)
#         print(self.texto)


# t1 = MeuThread('Thread 1', 2)
# t1.start()

# t2 = MeuThread('Thread 2', 3)
# t2.start()

# t3 = MeuThread('Thread 1', 5)
# t3.start()

# for i in range(20):
#     print(i)
#     sleep(1)

# def vai_demorar(tempo, texto):
#     sleep(tempo)
#     print(texto)

# t1 = Thread(target=vai_demorar, args=('ola mundo 1', 2))
# t1.start()

# t2 = Thread(target=vai_demorar, args=('ola mundo 2', 5))
# t2.start()

# t3 = Thread(target=vai_demorar, args=('ola mundo 3', 4))
# t3.start()

# for i in range(20):
#      print(i)
#      sleep(.5)

def vai_demorar(tempo, texto):
    sleep(tempo)
    print(texto)

t1 = Thread(target=vai_demorar, args=(10, 'ola mundo 1'))
t1.start()

while t1.is_alive():
    print('esperando a thread')
    sleep(2)

print('thread acabou!!')
