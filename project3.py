import random
import matplotlib.pyplot as plt
import pandas as pd

channel = 79
channel_prob = [] #channel出現次數
device_num = 20 #device數
prev_channel = [] #每個device上次挑選的channel
collision_time = 0
hop_per_sec = 1600 #每秒跳頻次數
sec = 4 #秒數
time = 0 #第幾次選channel
threshold = 0.1 #出現超過此機率的算bad channel
collision_total = [] #每個channel碰撞次數
total_bad_channel = 0 #bad channel總數
channel_with_noise = []
channel_without_noise = []
bad = [] #bad channel id

bad_channel = [] #if bad 則 =1
hopping_sequence = []


#找出重複channel
def f3(L):
  return [e for e in set(L) if L.count(e) > 1]

#####################################################前4秒
temp = []
for i in range(79):
    temp.append(i)
print(temp)


#每個device的hopping sequence
for i in range(device_num):
    a=random.sample(temp,79)
    hopping_sequence.append(a)
print(hopping_sequence)




for i in range(device_num):
    prev_channel.append(0)
# print(prev_channel)

for i in range(channel):
    collision_total.append(0)

while True:

    for i in range(hopping_sequence[0]):
        prev_channel[i]=hopping_sequence[]

    #各channel碰撞次數
    # print(f3(prev_channel))
    for i in range(len(hopping_sequence[0])):
        collision_total[f3(prev_channel)[i]-1] += 1
        
    #總碰撞次數
    collision_time += len(f3(prev_channel))

    time += 1    
    if time == hop_per_sec*sec:
        break
# print("collision_probability =",collision_time/(hop_per_sec*sec))

#換成機率
for i in range(len(collision_total)):
    collision_total[i] /= hop_per_sec*sec
print("collision_total",collision_total)




# C = []
# for i in range(9):
#     C.append((i+1)/10)
# # print(C)




# plt.bar(C, bad_total, color='b',width=0.05)
# plt.xlabel('Threshold ζ') # 設定x軸標題
# plt.ylabel('Average collision probability') # 設定y軸標題
# # plt.xticks(C, rotation='vertical') # 設定x軸label以及垂直顯示
# plt.title('device = 20') # 設定圖表標題
# plt.show()