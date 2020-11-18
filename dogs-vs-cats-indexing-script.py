import csv

data_list = []
for i in range(12499):
    image_idx='dog.'+str(i)+'.jpg'
    data_list.append([image_idx, 1])
for i in range(12499):
    image_idx='cat.'+str(i)+'.jpg'
    data_list.append([image_idx, 0])  
print(data_list[:10])

with open('Data/dogs-vs-cats/dogs-vs-cats-index.csv', 'w', newline='\n') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerows(data_list)
file.close()