#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import socket
import threading
import tkinter as tk
import queue, select
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import random
from datetime import datetime
from matplotlib.ticker import MaxNLocator


root = tk.Tk()
root.title("Ha↗️Ha↘️Ha↗️Ha↘️Ha↗️Ha↘️Ha↗️")




def define_layout(obj, cols=1, rows=1):
    
    def method(trg, col, row):
        
        for c in range(cols):    
            trg.columnconfigure(c, weight=1)
        for r in range(rows):
            trg.rowconfigure(r, weight=1)

    if type(obj)==list:        
        [ method(trg, cols, rows) for trg in obj ]
    else:
        trg = obj
        method(trg, cols, rows)

div_size = 200
img_size = div_size * 4
align_mode = 'nswe'
pad = 0
div1 = tk.Frame(root,  width=img_size , height=img_size, bg = 'black')
div2 = tk.Frame(root,  width=div_size , height=div_size, bg = 'black')

div3 = tk.Frame(root,  width=div_size , height=div_size ,bg='black', highlightbackground="black", highlightthickness=2, bd=0)
div4 = tk.Frame(div3, width=div_size/4, height=div_size/4, bg='black',padx=pad, pady=pad)
div1.grid(column=0, row=0, padx=pad, pady=pad, rowspan=2, sticky=align_mode)
div2.grid(column=1, row=0, padx=pad, pady=pad, sticky=align_mode)
div3.grid(column=1, row=1, padx=pad, pady=pad)
div4.grid(column=0, row=1, sticky=align_mode)
define_layout(root, cols=2, rows=2)
define_layout([div1, div2, div3])




def buttons():
    for i in "Contorl fan", "change", "Clear", "Exit":
        if i == 'change':
            b = tk.Button(div4, text=i, bg='white', fg='black')
            yield b
        else:
            b = tk.Button(div3, text=i, bg='black', fg='yellow', width=40, height=10)
            yield b


b1, b2, b3, b4, = buttons()
b1.grid(column=0, row=0, sticky=align_mode)

b3.grid(column=1, row=0, sticky=align_mode)
b4.grid(column=1, row=1, sticky=align_mode)
text = tk.Text(div2, bg='black', fg='yellow')
text.grid(column=0, row=0, sticky=align_mode)

light_entry = tk.Entry(div4)
labelLight = tk.Label(div4, text = "Control Light(0~99)", bg='black', fg='yellow', width=20)
labelLight.grid(column=0, row=0, padx=5, pady=5, sticky=align_mode)
light_entry.grid(column=0, row=1, padx=50, pady=5, sticky=align_mode)
b2.grid(column=0, row=2,padx=5, pady=5)



def data_points(): 
    f = open("data.txt", "w") 
    for i in range(10): 
        f.write(str(random.randint(0, 10))+'\n') 
    f.close() 
 
    f = open("data.txt", "r") 
    data = f.readlines() 
    f.close() 
 
    l = [] 
    for i in range(len(data)): 
        l.append(int(data[i].rstrip("\n"))) 
    return l 
class Server:
    clients = []

    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.open = 0
        self.count = 0
        self.send_data = ''
        self.inputs = [self.s]
        self.message_queues = {}
        self.outputs = []
        self.x=np.array ([datetime.now().strftime('%H:%M:%S')])
        self.moisture= np.array ([0])
        self.water_level= np.array ([0])
        self.co = np.array([0])

        self.fig = Figure(figsize=(5,5))
        self.a = self.fig.add_subplot(211)
        self.a.set_title ("Moisture", fontsize=8)
        
        
        self.b = self.fig.add_subplot(223)
        self.b.set_title("Water level", fontsize=8)
        
        self.c = self.fig.add_subplot(224)
        self.c.set_title("Air", fontsize=8)
        self.a.grid()
        self.b.grid()
        self.c.grid()
        self.fig.tight_layout()
        self.canvas = FigureCanvasTkAgg(self.fig, div1)
        self.canvas.get_tk_widget().pack(side="top",fill='both',expand=True)

    def connection(self):
        self.s.bind(("192.168.223.169", 8000))
        # self.s.bind(("10.43.201.174",8000))
        self.s.listen(10)
        now = str(datetime.now())[:-7]
        text.insert("end", "({}) : Connected.\n".format(now))
        print('connect')
        self.condition()

    def control_fan(self):
        # t = threading.Thread(target=self.plot())
        # t.start()
        self.count = 0
        if self.open == 1:
            self.send_data = '0nn'
            self.open = 0
            text.insert("end", f"fan closed\n")
        else:
            self.send_data = '1nn'
            self.open = 1
            text.insert("end", f"fan open\n")


    def receive(self):
        while(True):
            readable, writable, _ = select.select(self.inputs, self.outputs, [], 1)
            for sck in readable:
                if sck is self.s:
                    client, addr = sck.accept()
                    text.insert('end', f'connection from {addr}\n')
                    client.setblocking(0)
                    self.inputs.append(client)
                    #{client1: message_queue, client2: message_queue, ...}
                    self.message_queues[client] = queue.Queue()
                else:
                    data = sck.recv(1024).decode('utf-8')
                    if data != '':
                        print(f'received {data} from {sck.getpeername()}')
                        print(data)
                        self.message_queues[sck].put(data)
                        if sck not in self.outputs:
                            self.outputs.append(sck)
                    else:
                        # client closed connection
                        text.insert('end', (f'closing from {sck.getpeername()}\n'))
                        if sck in self.outputs:
                            self.outputs.remove(sck)
                        self.inputs.remove(sck)
                        sck.close()
                        #delete message queue
                        del self.message_queues[sck]
            for sck in writable:
                try:
                    next_message = self.message_queues[sck].get_nowait()
                except queue.Empty:
                    self.outputs.remove(sck)
                else:
                    if next_message == 'request':
                        if self.open == 1:
                            self.count += 1
                        if len(self.send_data) > 0:
                            sck.send((self.send_data).encode('utf-8'))
                            text.insert('end', f'send to stm32 {self.send_data}\n')
                            if self.send_data[0] == '1':
                                self.open = 1
                                self.count = 0
                            elif self.send_data[0] == '0':
                                self.open = 0
                            self.send_data = ''
                        else:
                            if self.count == 20 and self.open == 1:
                                sck.send('0nn'.encode('utf-8'))
                                self.open = 0
                                self.count = 0
                            else:
                                sck.send('no'.encode('utf-8'))
                    else:
                        detect_list = next_message.split("/")
                        if len(detect_list) > 5:
                            continue
                        print(f'else: {detect_list}')
                        self.x = np.append(self.x, datetime.now().strftime('%H:%M:%S'))
                        self.moisture = np.append(self.moisture,round(float(detect_list[0]), 4))
                        self.water_level = np.append(self.water_level,round(float(detect_list[1]), 4))
                        self.co = np.append(self.co,round(float(detect_list[2]), 4))
                        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                        if len(self.x) > 20: 
                            self.x = self.x[-20: ]
                            self.moisture = self.moisture[-20: ]
                            self.water_level = self.water_level[-20: ]
                            self.co = self.co[-20: ]
                        if float(detect_list[2]) > 0.1:
                            self.send_data = '1nn' 
                        if int(detect_list[3]) == 1:
                            text.insert('end', '!!! No water, please add water !!!\n')
                        t = threading.Thread(target=self.plot())
                        t.start()
        

    def condition(self):
        t1_2 = threading.Thread(target=self.receive)
        t1_2.daemon = True
        t1_2.start()
        t1_2.join(1)

    def send(self):
        print(light_entry.get().isnumeric())
        if light_entry.get().isnumeric() == False:
            text.insert('end', f'{light_entry.get()} not a valid value\n')
        else:
            num = int(light_entry.get())
            if num < 0 or num > 99:
                text.insert('end', f'{light_entry.get()} not a valid value\n')
            else:
                text.insert('end', f'change lightness to {light_entry.get()}%\n')
                if num < 10 and num >= 0:
                    self.send_data = 'l0'+str(num)
                else:
                    self.send_data = 'l' + str(num)
    
    def plot(self):
        self.a.cla() 
        self.a.grid() 
        self.a.plot(self.x, self.moisture, marker='o', color='orange')
        self.a.set_title ("Moisture", fontsize=8)
        self.a.set_ylim([0, 1])
        self.a.plot(self.x, [0.3 for i in range(len(self.x))], "k--", color='red')
        # plt.gcf().autofmt_xdate()
        # self.a.gcf().automt_xdate()
        self.a.xaxis.set_major_locator(MaxNLocator(6))
        self.b.cla() 
        self.b.grid() 
        self.b.plot(self.x, self.water_level, marker='o', color='orange')
        self.b.set_title ("Water_level", fontsize=8)
        self.b.set_ylim([0,4])
        self.b.xaxis.set_major_locator(MaxNLocator(3))
        self.c.cla() 
        self.c.grid() 
        self.c.plot(self.x, self.co, marker='o', color='orange')
        self.c.plot(self.x, [0.1 for i in range(len(self.x))], "k--", color='red')
        self.c.set_title ("CO", fontsize=8)
        self.c.set_ylim([0,1])
        self.c.xaxis.set_major_locator(MaxNLocator(3))
        self.canvas.draw() 


        


s1 = Server()


def control_fan():
    t1 = threading.Thread(target=s1.control_fan)
    t1.start()


def change_light():
    t2 = threading.Thread(target=s1.send)
    t2.start()


def clear():
    text.delete("1.0", "end")


def destroy():
    for i in s1.clients:
        i.close()
    s1.s.close()
    root.destroy()
    exit()


if __name__ == "__main__":
    b1.configure(command=control_fan)
    b2.configure(command=change_light)
    b3.configure(command=clear)
    b4.configure(command=destroy)
    define_layout(div1)
    define_layout(div2, rows=2)
    define_layout(div3, rows=4)
    t_connection = threading.Thread(target=s1.connection, daemon=True)
    t_connection.start()
    t0 = threading.Thread(target=root.mainloop)
    t0.run()