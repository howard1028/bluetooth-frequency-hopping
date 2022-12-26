import random
import matplotlib.pyplot as plt

channel = 79
channel_prob = [] #channel出現次數
device_num = 70 #device數
prev_channel = [] #每個device上次挑選的channel
collision_time = 0
hop_per_sec = 1600 #每秒跳頻次數
sec = 4 #秒數
time = 0 #第幾次選channel
threshold = 0.1 #出現超過此機率的算bad channel
collision_total = [] #每個channel碰撞次數
total_bad_channel = 0 #bad channel總數


bad_channel = [] #if bad則=最近的good channel，if good則=0
hopping_sequence = []


#找出重複channel
def f3(L):
  return [e for e in set(L) if L.count(e) > 1]

##################################################### 前4秒
temp = []
for i in range(79):
    temp.append(i)
# print(temp)


#每個device的hopping sequence
for i in range(device_num):
    a=random.sample(temp,79)
    hopping_sequence+=[a]
print("hopping sequence=",hopping_sequence)

for i in range(device_num):
    prev_channel.append(0)

#各channel碰撞次數
for i in range(channel):
    collision_total.append(0)

count=0
while True:
    for i in range(device_num):
        if len(hopping_sequence[i]) != 0:
            prev_channel[i] = hopping_sequence[i][count]
    count += 1

    # print(len(hopping_sequence[0]),len(hopping_sequence[1]))
    print("\n",time+1,":",prev_channel)   

    #各channel碰撞次數
    # print(f3(prev_channel))
    for i in range(len(f3(prev_channel))):
        collision_total[f3(prev_channel)[i]-1] += 1
    print("collision_total=",collision_total)

    #總碰撞次數
    collision_time += len(f3(prev_channel))

    time += 1    
    if time == channel:
        break
# print("collision_probability =",collision_time/(hop_per_sec*sec))

#換成機率
for i in range(len(collision_total)):
    collision_total[i] /= channel
# print("collision_total",collision_total)


######################################################## 後26秒

sec = 26
P = [] #該threshold平均碰撞機率

for i in range(channel):
    bad_channel.append([0,0,0,0,0,0,0,0,0])

# print("bad_channel=",bad_channel)

for i in range(channel):
    for j in range(9):
        threshold = (j+1)/10
        # channel機率 > threshold是bad channel
        if (collision_total[i] >= threshold):
            bad_channel[i][j] = i+1
for j in range(9):            
    for i in range(channel):
        threshold = (j+1)/10
        #bad channel，向左右找最近的good channel
        if (bad_channel[i][j] != 0):
            p1 = i
            p2 = i
            count1=0
            count2=0
            while p2 < channel:
                if bad_channel[p2][j] == 0:
                    break
                count2 += 1
                p2 += 1
            while p1 >= 0:
                if bad_channel[p1][j] == 0:
                    break
                count1 += 1
                p1 -= 1
            if p1 == -1 and p2 != 79:
                bad_channel[i][j] = p2+1
            if p1 != -1 and p2 == 79:
                bad_channel[i][j] = p1+1
            if p1 != -1 and p2 != 79:
                if count1<count2:
                    bad_channel[i][j] = p1+1
                else:
                    bad_channel[i][j] = p2+1

print("bad_channel=",bad_channel)

p=[] #new碰撞機率
for k in range(9):
    collision = [0]*79
    for i in range(sec*hop_per_sec):
        choice_channel=[0]*79
        for j in range(device_num):
            #good channel，選到該channel次數+1
            if bad_channel[hopping_sequence[j][i%79]][k]==0:
                choice_channel[hopping_sequence[j][i%79]]+=1
            #bad channel，跳到最近good channel
            else:
                choice_channel[bad_channel[hopping_sequence[j][i%79]][k]-1]+=1
        #兩個以上選到擇有碰撞
        for j in range(len(choice_channel)):
            if choice_channel[j] > 1:
                collision[j]+=choice_channel[j]
    #print(collision)
    sum=0
    for i in range(len(collision)):
        sum += collision[i]
    # sum=sum/sec/hop_per_sec/device_num
    sum /= sec*hop_per_sec*device_num
    p+=[sum]
print(p)






C = []
for i in range(9):
    C.append((i+1)/10)
# print(C)





plt.bar(C, p, color='b',width=0.05)
plt.xlabel('Threshold ζ') # 設定x軸標題
plt.ylabel('Average collision probability') # 設定y軸標題
# plt.xticks(C, rotation='vertical') # 設定x軸label以及垂直顯示
plt.title('device = 70') # 設定圖表標題
plt.show()