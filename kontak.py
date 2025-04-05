'Berisi kelas kontak untuk menjalankan program kontak'

import dokumen

class Kontak:
    def __init__(self):
        self.kontak = dokumen.membuka_kontak()

    def melihat_kontak(self):
        # melihat kontak
        if self.kontak:
            # melihat semua kontak
            for num, item in enumerate(self.kontak, start=1):
                print(f'{num}. ' + item)
        else:
            print("Kontak masih kosong!")
            return 1

    def menambah_kontak(self):
        # menambahkan kontak
        nama = input("Masukkan Nama Kontak yang Baru :")
        HP = input("Masukkan Nomor Kontak yang Baru :")
        email = input("Masukkan email Kontak yang Baru :")
        kontak_baru = f'{nama} ({HP}, {email})' + '\n'
        self.kontak.append(kontak_baru)
        print("Kontak baru berhasil di tambahkan!")

    def menghapus_kontak(self):
        # menghapus kontak
        if self.melihat_kontak() == 1:
            return
        else :
            try:
                i_hapus = int(input("Masukkan nomor kontak yang akan di hapus :"))
                del self.kontak[i_hapus - 1]
                print("Kontak yang dimaksud sudah di hapus")
            except:
                print("Input yang anda masukkan salah")

    def keluar_kontak(self):
        dokumen.menyimpan_kontak(isi=self.kontak)