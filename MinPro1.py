print("\n" + "-"*45)
print("SISTEM INFORMASI ADMINISTRASI RUMAH SAKIT HEWAN")
print("-"*45)

daftar_pasien_hewan = [
    ("Naka", "Kucing", "Jihan", "Scabies"), 
    ("Mambo", "Anjing", "Peter", "Heat Stroke"),
    ("Unul", "Kucing", "Nakhwa", "Cacingan"),
    ("Mr White", "Kelinci", "Adel", "Keracunan"),
    ("Elita", "Hamster", "Debora Lintang", "Pneumonia")
    ]

while True:
    print("\n" + "="*45)
    print("DAFTAR PILIHAN INFORMASI REGISTRASI")
    print("="*45)
    print("1. Menambah data pasien hewan")
    print("2. Melihat data pasien hewan")
    print("3. Mengubah data pasien hewan")
    print("4. Menghapus data pasien hewan")
    print("5. Keluar")
    print("="*45)

    pilihan = input("Pilihlah menu (1-5): ")

    if pilihan == "1":
        print("\n--- TAMBAHKAN DAFTAR PASIEN HEWAN ---")
        Nama = input("Masukkan nama hewan : ")
        Jenis_hewan = input("Masukkan jenis hewan : ")
        Nama_pemilik = input("Masukkan nama pemilik : ")
        Penyakit = input("Masukkan penyakit hewan : ")

        daftar_pasien_hewan.append(
            (Nama, Jenis_hewan, Nama_pemilik, Penyakit)
            )

        print("DATA BERHASIL DITAMBAHKAN")

    elif pilihan == "2":
        print("\n--- TAMPILKAN DATA PASIEN HEWAN ---")
        if len(daftar_pasien_hewan) == 0:
            print("Belum ada daftar pasien")

        else: 
            for pasien in daftar_pasien_hewan:
                print(pasien)

    elif pilihan == "3":
        print("\n--- UBAH DATA PASIEN HEWAN ---")

        if len(daftar_pasien_hewan) == 0:
            print("Belum ada data yang dapat diubah")
        else:
                while True:
                    nomor = int(input("Masukkan nomor data yang ingin diubah : "))
                    if 1 <= nomor <= len(daftar_pasien_hewan):
                        index = nomor - 1

                    Nama_baru = input("Masukan nama baru : ")
                    Jenis_baru = input("Masukkan jenis hewan baru : ")
                    Pemilik_baru = input("Masukkan nama pemilik baru : ")
                    Penyakit_baru  = input("Masukkan penyakit baru : ")

                    daftar_pasien_hewan[index] = (Nama_baru, Jenis_baru, Pemilik_baru, Penyakit_baru)

                    print("DATA BERHASIL DI UBAH")
                    break

    elif pilihan == "4":
        print("\n--- HAPUS DATA PASIEN ---")

        if not daftar_pasien_hewan:
            print("Data pasien kosong. Tidak ada data yang bisa dihapus.")
        else:
            for i in range(len(daftar_pasien_hewan)):
                print(f"{i + 1}. {daftar_pasien_hewan[i][0]} ({daftar_pasien_hewan[i][1]})")

        while True:
            nomor = int(input("\nMasukkan nomor pasien yang ingin dihapus : "))
            if 1 <= nomor <= len(daftar_pasien_hewan):
                        pasien_dihapus = daftar_pasien_hewan.pop(nomor - 1)
                        print(f"Data pasien pasien_dihapus[0] berhasil dihapus dari sistem.")
                        break
            else:
                        print("Nomor pasien tidak ditemukan")

    elif pilihan == "5":
        print("\n" + "-"*45)
        print("Sistem Administrasi SELESAI. Terima kasih")
        print("-"*45)
        break