print('##  Program Python Konversi Suhu  ##')
print('====================================')
print()

celc = int(input('Input suhu celsius: '))
 
fahr = (9/5 * celc) + 32
kelv = celc + 273.15
ream = celc * (4/5)

print(celc,'derajat celsius =',fahr,'derajat Fahrenheit')
print(celc,'derajat celsius =',kelv,'derajat Kelvin')
print(celc,'derajat celsius =',ream,'derajat Reamur')