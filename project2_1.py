import random
import matplotlib.pyplot as plt
import pandas as pd

channel = 79
channel_prob = [] #channel出現次數
device_num = 70 #device數
prev_channel = [] #每個device上次挑選的channel
collision_time = 0
hop_per_sec = 1600 #每秒跳頻次數
sec = 100 #秒數
time = 0 #第幾次選channel
threshold = 0 #出現超過此機率的算bad channel
collision_total = [] #每個channel碰撞次數
total_bad_channel = 0 #bad channel總數

#找出重複channel
def f3(L):
  return [e for e in set(L) if L.count(e) > 1]

for i in range(device_num):
    prev_channel.append(0)
print(prev_channel)

for i in range(channel):
    collision_total.append(0)

while True:
    for i in range(device_num):
        temp = random.randint(1,channel)
        if temp != prev_channel[i]: #device 選到和上次不同的channel
            prev_channel[i] = temp
        else:
            temp = random.randint(1,channel)
            prev_channel[i] = temp

    print(time+1,":",prev_channel)   

    #各channel碰撞次數
    print(f3(prev_channel))
    for i in range(len(f3(prev_channel))):
        collision_total[f3(prev_channel)[i]-1] += 1
        
    #總碰撞次數
    collision_time += len(f3(prev_channel))

    time += 1    
    if time == hop_per_sec*sec:
        break
# print("collision_probability =",collision_time/(hop_per_sec*sec))

print(collision_total)
for i in range(len(collision_total)):
    collision_total[i] /= hop_per_sec*sec


C = []
for i in range(channel):
    C.append(i+1)
print(C)

print(collision_total)



plt.bar(C, collision_total, color='b')
plt.xlabel('Channel ID') # 設定x軸標題
plt.ylabel('Average collision percentage') # 設定y軸標題
# plt.xticks(C, rotation='vertical') # 設定x軸label以及垂直顯示
plt.title('device = 70') # 設定圖表標題
plt.show()