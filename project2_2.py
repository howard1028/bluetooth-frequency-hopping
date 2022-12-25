from numpy import random
import matplotlib.pyplot as plt
import pandas as pd

channel = 79
channel_prob = [] #channel出現次數
device_num = 20 #device數
prev_channel = [] #每個device上次挑選的channel
collision_time = 0
hop_per_sec = 1600 #每秒跳頻次數
sec = 30 #秒數
time = 0 #第幾次選channel
threshold = 0.1 #出現超過此機率的算bad channel
collision_total = [] #每個channel碰撞次數
total_bad_channel = 0 #bad channel總數
channel_with_noise = []
channel_without_noise = []
bad = [] #bad channel id
bad_count = [] 
bad_total = [] #bad channel在某threshold的數量

#找出重複channel
def f3(L):
  return [e for e in set(L) if L.count(e) > 1]

for i in range(channel):
    bad_count.append(0)

for i in range(9):
    bad_total.append(0)


###################################

for i in range(device_num):
    prev_channel.append(0)
# print(prev_channel)

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

    # print(time+1,":",prev_channel)   

    #各channel碰撞次數
    # print(f3(prev_channel))
    for i in range(len(f3(prev_channel))):
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


####################################################

temp = []
for i in range(79):
    temp.append(i)

#沒受noise干擾
for i in range(39):
    random.shuffle(temp)
    channel_without_noise.append(temp.pop())

#受noise干擾    
for i in range(40):
    random.shuffle(temp)
    channel_with_noise.append(temp.pop())

print("channel_with_noise",channel_with_noise)
print("channel_without_noise",channel_without_noise)

noise_bad = random.poisson(lam=12) #channel_with_noise有幾個bad channels
print("noise bad channel count = ",noise_bad)

for i in range(noise_bad):
    random.shuffle(channel_with_noise)
    bad.append(channel_with_noise.pop())    
# print("noise bad channel=",bad,"\n")

#######################################
for k in range(9):
    threshold = (k+1)/10
    #初始化
    channel_without_noise.clear()
    channel_with_noise.clear()
    # bad.clear()
    for i in range(len(bad_count)):
        bad_count[i]=0

   
    #找出bad channel if > threshold 並加入
    count = noise_bad
    for i in range(len(collision_total)):
        if collision_total[i] >= threshold:
            if (i not in bad):
            # bad.append(i)
                count += 1

    bad_total[k] = count

print("bad_total=",bad_total)
C = []
for i in range(9):
    C.append((i+1)/10)
# print(C)




plt.bar(C, bad_total, color='b',width=0.05)
plt.xlabel('Threshold ζ') # 設定x軸標題
plt.ylabel('Bad channels') # 設定y軸標題
# plt.xticks(C, rotation='vertical') # 設定x軸label以及垂直顯示
plt.title('device = 20') # 設定圖表標題
plt.show()