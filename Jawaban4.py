print("     |########|")
print("     |Provinsi|")
print("     |########|")
print("")
Prov_Kota = ['Kalimantan', 'Sumatra', 'Sulawesi']

for kota in Prov_Kota:
  ArahMataAngin = ['West', 'North', 'South']
  
  print("")
  
  while ArahMataAngin:
    print(kota, ArahMataAngin.pop(0))