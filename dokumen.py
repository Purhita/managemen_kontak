'Berisi fungsi menyimpan dan membuka kontak'

def membuka_kontak(path='kontak.txt'):
    with open(path, mode='r') as file:
        kontak = file.readlines() #membaca menjadi bentuk list
    return kontak

def menyimpan_kontak(path='kontak.txt', isi=[]):
    with open(path, mode='w') as file:
        file.writelines(isi)
