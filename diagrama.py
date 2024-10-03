import matplotlib.pyplot as plt


with open('sequence.txt', 'r') as f:
    all = [num.strip() for num in f]

nechet = [v for k,v in enumerate(all) if not k%2]
chet = [v for k,v in enumerate(all) if k%2]

nechet = [abs(float(x)) for x in nechet]
chet = [abs(float(x)) for x in chet]
a = [abs(float(x)) for x in all]

average_chet = sum(chet) / len(chet) if chet else 0 
average_nechet = sum(nechet) / len(nechet) if nechet else 0
average_all = sum(a) / len(a) if a else 0

otnoshenie_chet_k_all = average_chet / average_all
otnoshenie_nechet_k_all = average_nechet / average_all

labels = 'Четные позиции', 'Нечетные позиции'

sizes = [otnoshenie_chet_k_all, otnoshenie_nechet_k_all]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%d%%')
plt.show() 
