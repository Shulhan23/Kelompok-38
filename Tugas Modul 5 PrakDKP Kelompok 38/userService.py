def __init__(akun, email, password):
        akun.email = email
        akun.password = password
        akun.data = {
        "rendykelompok38@gmail.com": {
            "email"     : "rendykelompok38@gmail.com",
            "password"  : "12345",
            "Mahasiswa" : "Rendy Akbar Permana"
        },
        "shulhankelompok38@gmail.com" : {
            "email"     : "shulhankelompok38@gmail.com",
            "password"  : "67890",
            "Mahasiswa" : "Shulhan Aziz"
        },
        "wisnukelompok38@gmail.com" : {
            "email"     : "wisnukelompok38@gmail.com",
            "password"  : "111213",
            "Mahasiswa" : "Raditya Wisnu"
        },
        "neztakelompok38@gmail.com"    : {
            "email"     : "neztakelompok38@gmail.com",
            "password"  : "141516",
            "Mahasiswa" : "Nezta Mizgi Febiandanu"
        }
    }

class userService:
    def __init__(akun, email, password):
        akun.email = email
        akun.password = password
        akun.data = {
"rendykelompok38@gmail.com": {
            "email"     : "rendykelompok38@gmail.com",
            "password"  : "12345",
            "Mahasiswa" : "Rendy Akbar Permana"
        },
        "shulhankelompok38@gmail.com" : {
            "email"     : "shulhankelompok38@gmail.com",
            "password"  : "67890",
            "Mahasiswa" : "Shulhan Aziz"
        },
        "wisnukelompok38@gmail.com" : {
            "email"     : "wisnukelompok38@gmail.com",
            "password"  : "111213",
            "Mahasiswa" : "Raditya Wisnu"
        },
        "neztakelompok38@gmail.com"    : {
            "email"     : "neztakelompok38@gmail.com",
            "password"  : "141516",
            "Mahasiswa" : "Nezta Mizgi Febiandanu"
        }
    }

    
    def checkCredential(akun):
        for nilai in akun.data:
            if nilai == akun.email:
                password_user = akun.data[nilai]
                if akun.password == password_user['password']:
                    return password_user
                else:
                    return False
                
    
    def login(akun):
            Info = ['Kendal', 'Padang', 'Semarang', 'Jakarta'], ['Teknik Komputer 2022'], ['Futsal', 'Basket', 'Main Musik']
            data = akun.checkCredential()
            if data:
                print("\nSelamat Datang " ,data['Mahasiswa'])
                print("\nLogin menggunakan Email: " ,data['email'])
                print("\nData Diri Anda: ")
                if akun.email == "rendykelompok38@gmail.com":
                    print("Asal :",Info[0][0],"\nJurusan :",Info[1][0],"\nHobi :",Info[2][0])
                elif akun.email == "shulhankelompok38@gmail.com":
                    print("Asal :",Info[0][1],"\nJurusan :",Info[1][0],"\nHobi :",Info[2][1])
                elif akun.email == "wisnukelompok38@gmail.com":
                    print("Asal :",Info[0][2],"\nJurusan :",Info[1][0],"\nHobi :",Info[2][0])
                elif akun.email == "neztakelompok38@gmail.com":
                    print("Asal :",Info[0][3],"\nJurusan :",Info[1][0],"\nHobi :",Info[2][2])
            else:
                print("\nEmail atau Password yang dimasukkan salah!!!!!!!!\n")
                exit()



