import csv
import matplotlib.pyplot as plt

list_check = []

with open('nfcap.csv') as data_doc:
    reader = csv.reader(data_doc)
    for i in reader:
        list_check.append(i)

ibyt = 0
price = 0
x_Time = []
y_Bytes = []


for i in range(len(list_check)):
    if '192.0.73.2' in list_check[i]:
        ibyt += float(list_check[i][12])
        x_Time.append(float(list_check[i][11]))
        y_Bytes.append(float(list_check[i][12]))


if ibyt > 200:  # Т. к. общий объём трафика по абоненту меньше заявленного во варианте, было решено рассматривать байты.
    ibyt = ibyt-200
    price += 0.5*200

price += ibyt*1
print(price)

x_Time.sort()
y_Bytes.sort()
assert len(x_Time) == len(y_Bytes)
plt.plot(x_Time, y_Bytes)
plt.grid(True)
plt.show()
