"Program Manajemen Kontak"


def melihat_kontak():
    # melihat kontak
    if kontak:
        # melihat semua kontak
        for num, item in enumerate(kontak, start=1):
            print(f'\n{num}. {item["nama"]} ({item["HP"]},{item["email"]})')
    else:
        print("Kontak masih kosong!")
        return 1

def menambah_kontak():
    # menambahkan kontak
    nama = input("Masukkan Nama Kontak yang Baru :")
    hp = input("Masukkan Nomor Kontak yang Baru :")
    email = input("Masukkan email Kontak yang Baru :")
    kontak_baru = {'nama': nama, 'HP': hp, 'email': email}
    kontak.append(kontak_baru)
    print("Kontak baru berhasil di tambahkan!")

def menghapus_kontak():
    # menghapus kontak
    if melihat_kontak() == 1:
        return
    else :
        i_hapus = int(input("Masukkan nomor kontak yang akan di hapus :"))
        del kontak[i_hapus - 1]
        print("Kontak yang dimaksud sudah di hapus")

kontak1 = {'nama' : "Andi", 'HP': '081234577862', 'email': 'Andi@pyton,com'}
kontak2 = {'nama' : "Ani", 'HP': '081234574325', 'email': 'Ani@pyton,com'}
kontak = [kontak1, kontak2]

while True:
    print("\nMenu Kontak")
    print("1. Melihat Semua Kontak")
    print("2. Menambahkan Kontak Baru")
    print("3. Menghapus Kontak")
    print("4. Keluar dari Kontak")

    pilihan = input("Masukkan pilihan menu kontak (1,2,3 atau 4): ")
    #apapun yang masuk ke dalam input menjadi tipe string

    if pilihan == '1':
        melihat_kontak()

    elif pilihan == '2' :
        menambah_kontak()

    elif pilihan == '3' :
        menghapus_kontak()

    elif pilihan == '4' :
        # keluar dari kontak
        break
    else:
        print("Anda memasukkan pilihan yang salah !")
