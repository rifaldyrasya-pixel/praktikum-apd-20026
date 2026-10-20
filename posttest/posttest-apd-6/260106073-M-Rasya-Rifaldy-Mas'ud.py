import os

users = {
    "rasya": {"pin": "073", "role": "admin"},
    "smk": {"pin": "123", "role": "user"}
}

antrean_servis = {}

id_counter = 1

while True:
    user_login = ""
    role_login = ""

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("==========================================")
        print("         MOTOCARE MANAGER - LOGIN         ")
        print("==========================================")
        print("1. Login Akun")
        print("2. Register Akun Baru")
        print("3. Keluar Program")
        print("==========================================")
        pilihan_auth = input("Pilih menu (1-3): ")

        if pilihan_auth == "1":
            print("\n--- SILAHKAN LOGIN ---")
            input_user = input("Masukkan Username : ")
            input_pin = input("Masukkan PIN      : ")

            data_user = users.get(input_user)
            if data_user and data_user["pin"] == input_pin:
                user_login = input_user
                role_login = data_user["role"]
                print(f"\n>> Login Berhasil! Selamat datang, {user_login} ({role_login}).")
                input("Tekan Enter untuk masuk ke menu utama...")
                break
            else:
                print("\n>> Username atau PIN salah! Silakan coba lagi.")
                input("Tekan Enter untuk melanjutkan...")

        elif pilihan_auth == "2":
            print("\n--- REGISTER AKUN BARU ---")
            reg_user = input("Buat Username baru : ")

            if reg_user in users:
                print(">> Username tersebut sudah digunakan! Gunakan yang lain.")
            else:
                reg_pin = input("Buat PIN baru      : ")
                users[reg_user] = {"pin": reg_pin, "role": "user"}
                print(">> Akun berhasil didaftarkan! Silakan login.")
            input("Tekan Enter untuk melanjutkan...")

        elif pilihan_auth == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Program dihentikan. Terima kasih!")
            exit()
        else:
            print("\n>> Pilihan tidak valid.")
            input("Tekan Enter untuk melanjutkan...")

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("==========================================")
        print(f"   BENGKEL MOTOCARE - [Login: {user_login}]")
        print("==========================================")
        print("1. Lihat Daftar Antrean (Read)")
        if role_login == "admin":
            print("2. Tambah Antrean Motor (Create)")
            print("3. Update Status Pengerjaan (Update)")
            print("4. Motor Selesai / Hapus Antrean (Delete)")
        print("5. Logout / Ganti Akun")
        print("6. Keluar Program")
        print("==========================================")
        
        pilihan_menu = input("Pilih menu: ")

        if pilihan_menu == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=== DAFTAR ANTREAN SERVIS BENGKEL ===")
            if len(antrean_servis) == 0:
                print("Belum ada antrean motor saat ini.")
            else:
                for key_id, val in antrean_servis.items():
                    print(f"ID [{key_id}] | [{val['status']}] {val['nama']} - {val['merk']} ({val['plat']}) | Keluhan: {val['keluhan']}")
            input("\nTekan Enter untuk kembali ke menu...")

        elif pilihan_menu == "2" and role_login == "admin":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=== TAMBAH ANTREAN MOTOR BARU ===")
            nama = input("Nama pemilik  : ")
            plat = input("Plat nomor    : ")
            merk = input("Merk motor    : ")
            keluhan = input("Keluhan       : ")

            str_id = str(id_counter)
            antrean_servis[str_id] = {
                "nama": nama,
                "plat": plat,
                "merk": merk,
                "keluhan": keluhan,
                "status": "Antri"
            }
            id_counter += 1

            print("\n>> Data antrean motor berhasil ditambahkan!")
            input("\nTekan Enter untuk kembali ke menu...")

        elif pilihan_menu == "3" and role_login == "admin":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=== UPDATE STATUS PENGERJAAN ===")
            if len(antrean_servis) == 0:
                print("Belum ada antrean motor untuk di-update.")
            else:
                for key_id, val in antrean_servis.items():
                    print(f"ID [{key_id}] {val['nama']} - {val['merk']} ({val['plat']}) [Status: {val['status']}]")
                
                pilih_id = input("\nMasukkan ID antrean yang mau diubah: ")
                
                if pilih_id in antrean_servis:
                    print(f"Status sekarang: {antrean_servis[pilih_id]['status']}")
                    print("1. Dikerjakan")
                    print("2. Selesai")
                    st = input("Pilih status baru (1/2): ")
                    
                    if st == "1":
                        antrean_servis[pilih_id]["status"] = "Dikerjakan"
                        print(">> Status berhasil diubah jadi 'Dikerjakan'")
                    elif st == "2":
                        antrean_servis[pilih_id]["status"] = "Selesai"
                        print(">> Status berhasil diubah jadi 'Selesai'")
                    else:
                        print(">> Pilihan status tidak valid.")
                else:
                    print(">> ID antrean tidak ditemukan.")
            input("\nTekan Enter untuk kembali ke menu...")

        elif pilihan_menu == "4" and role_login == "admin":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=== HAPUS / SELESAI ANTREAN MOTOR ===")
            if len(antrean_servis) == 0:
                print("Belum ada antrean motor untuk dihapus.")
            else:
                for key_id, val in antrean_servis.items():
                    print(f"ID [{key_id}] {val['nama']} - {val['merk']} ({val['plat']})")
                
                pilih_id = input("\nMasukkan ID antrean yang ingin dihapus/diambil: ")
                
                if pilih_id in antrean_servis:
                    data_hapus = antrean_servis.pop(pilih_id)
                    print(f">> Data motor {data_hapus['merk']} ({data_hapus['plat']}) milik {data_hapus['nama']} berhasil dihapus dari antrean.")
                else:
                    print(">> ID antrean tidak ditemukan.")
            input("\nTekan Enter untuk kembali ke menu...")

        elif pilihan_menu == "5":
            print("\n>> Berhasil Logout.")
            input("Tekan Enter untuk kembali ke halaman login...")
            break

        elif pilihan_menu == "6":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Terima kasih telah menggunakan MotoCare Manager!")
            exit()
        else:
            print("\n>> Pilihan menu tidak valid atau hak akses tidak diizinkan.")
            input("Tekan Enter untuk melanjutkan...")