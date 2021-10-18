import numpy as np
import json
import time
import random
import matplotlib.pyplot as plt

data = []
with open('output.txt', 'r', encoding='utf-8') as f:
    for line in f:
        tmp_str = line.replace('\n', '')
        data.append(tmp_str)

accelero_x = []
accelero_y = []
accelero_z = []
gyro_x = []
gyro_y = []
gyro_z = []
Range = [i for i in range(1, 401)]


for d in data:
    accelero_x.append(json.loads(d)['ACCELERO_X'])
    accelero_y.append(json.loads(d)['ACCELERO_Y'])
    accelero_z.append(json.loads(d)['ACCELERO_Z'])
    gyro_x.append(json.loads(d)['GYRO_X'])
    gyro_y.append(json.loads(d)['GYRO_Y'])
    gyro_z.append(json.loads(d)['GYRO_Z'])

# plt.subplot(3, 1, 1)
# plt.plot(Range, accelero_x, 'b')
# plt.xlabel(" Sample num ")
# plt.title("ACCELERO_X")
# plt.subplot(3, 1, 2)
# plt.plot(Range, accelero_y, 'r')
# plt.xlabel(" Sample num ")
# plt.title("ACCELERO_Y")
# plt.subplot(3, 1, 3)
# plt.plot(Range, accelero_z, 'y')
# plt.xlabel(" Sample num ")
# plt.title("ACCELERO_Z")

fig, axs = plt.subplots(3, 2)
axs[0, 0].plot(Range, accelero_x, 'b')
axs[0, 0].set_title('ACCELERO_X')
axs[1, 0].plot(Range, accelero_y, 'r')
axs[1, 0].set_title('ACCELERO_Y')
axs[2, 0].plot(Range, accelero_z, 'y')
axs[2, 0].set_title('ACCELERO_Z')

axs[0, 1].plot(Range, gyro_x, 'b')
axs[0, 1].set_title('GYRO_X')
axs[1, 1].plot(Range, gyro_y, 'r')
axs[1, 1].set_title('GYRO_Y')
axs[2, 1].plot(Range, gyro_z, 'y')
axs[2, 1].set_title('GYRO_Z')

plt.tight_layout()  # 隔開兩個圖
plt.show()
