import q

Anggota=q.Tea()
Anggota.anggota_kelompok(38)

print("\n                  AbdulTea ") 
print("|___________________________________________|\n") 
print("      Teh             |    Harga ") 
print("1. Lemon Tea          | Rp 6.000,00 |") 
print("2. Jasmine Tea        | Rp 5.000,00 |") 
print("3. Clove Tea          | Rp 5.000,00 |") 
print("|___________________________________________|") 

def beli(): 
 pembeli = int(input("Berapa orang yang membeli : ")) 
 print("Masukan nama Pembeli : ") 
 for i in range(int(pembeli)):
     i += 1
     n = input("Pembeli ke- {} : ".format(i))
 total_harga = pembeli * harga 
 print("\nTotal Harga yang dibayar adalah Rp ", total_harga)
 print("-----------------------------------") 
 meja = input("Ingin disajikan pada meja yang mana: ") 
 print("-----------------------------------") 
 print("Terima Kasih Telah Berbelanja Di sini XD") 
 print("Teh Anda Akan Segera Kami Sajikan, SIlahkan Menunggu di meja ", meja) 
 print("-----------------------------------") 
 print("jika ingin beli lagi ketik 1, jika tidak ketik 2 : ")
 
 lagi =int(input())
 if (lagi ==1):
     return beli()
 elif (lagi == 2):
     exit(0)
 else:
     exit(0)

Teh = int(input("\nMasukan Pilihan Teh yang ingin dibeli : ")) 
if (Teh == 1): 
 harga = 6000
 beli() 
elif (Teh == 2): 
 harga = 5000 
 beli() 
elif (Teh == 3): 
 harga = 5000
 beli() 
else: 
 print("Tidak Ada Pilihan Teh .") 
