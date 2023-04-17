from userService import userService

print("Form login Mahasiswa Baru")

email = input("\nMasukkan Alamat Email :")
password = input("Password Email: ")
    
logininfo = userService(email,password)
logininfo.login()
