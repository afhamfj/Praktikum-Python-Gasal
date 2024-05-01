#Contoh cara membuat Dictionary pada Python

# dict = {'Name': 'Afham', 'Age': 15, 'Class': '1 Intensif'}
# print(dict)
# print ("dict['Name']: ", dict['Name'])
# print ("dict['Age']: ", dict['Age'])
# print ("dict['Class']: ", dict['Class'])

#Update dictionary python

biodata = {'Name': 'Afham', 'Age': 15, 'Class': '1 Intensif'}
biodata ['Name'] = 'Afham' 
biodata ['School'] = "Pesantren Teknologi Majapahit" 

print(biodata)
del biodata['Name']
biodata.clear
del biodata