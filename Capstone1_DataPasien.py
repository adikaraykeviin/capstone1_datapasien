datapasien = [
    {
        'Nama': 'Joko Santoso',
        'Jenis Kelamin': 'Laki-Laki',
        'Tempat Lahir': 'Malang',
        'Tanggal Lahir': '17/07/1964',
        'Alamat' : 'Jl.Poncowati No.23A',
        'Anggota BPJS': True
    },
    {
        'Nama': 'Niko Kurniawan',
        'Jenis Kelamin': 'Laki-Laki',
        'Tempat Lahir': 'Surabaya',
        'Tanggal Lahir': '14/09/1996',
        'Alamat' : 'Jl. Rungkut Asri Raya No.17',
        'Anggota BPJS': False
    },
    {
        'Nama': 'Anaya Putri',
        'Jenis Kelamin': 'Perempuan',
        'Tempat Lahir': 'Jakarta',
        'Tanggal Lahir': '30/01/2008',
        'Alamat' : 'Jl. Salak 3 No.4',
        'Anggota BPJS': True
    }
]


def show_data():
    print("Data Pasien:")
    print("===================================")
    for idx, pasien in enumerate(datapasien, start=1):
        print(f"Nomor Pasien {idx}:")
        for key, value in pasien.items():
            print(f"{key}: {value}")
        print("----------------------------------")


def create_patient():
    nama_pasien = input("Masukan Nama Pasien: ")
    jenis_kelamin = input("Jenis Kelamin: ")
    tempat_lahir = input("Tempat Lahir: ")
    tanggal_lahir = input("Tanggal Lahir (dd/mm/yyyy): ")
    alamat_pasien = input('Alamat Pasien : ')
    anggota_bpjs_input = input("Apakah Pasien Anggota BPJS? (Y/N): ").upper()
    anggota_bpjs = anggota_bpjs_input == "Y"
    pasien_baru = {
        'Nama': nama_pasien,
        'Jenis Kelamin': jenis_kelamin,
        'Tempat Lahir': tempat_lahir,
        'Tanggal Lahir': tanggal_lahir,
        'Alamat' : alamat_pasien,
        'Anggota BPJS': anggota_bpjs
    }
    datapasien.append(pasien_baru)
    print("Data Pasien Sukses Dibuat!")


def update_patient():
    nomor_pasien = int(input("Masukan Nomor Pasien: "))
    if nomor_pasien < 1 or nomor_pasien > len(datapasien):
        print("Pasien Tidak Ditemukan Pada Nomor Pasien Yang Diinput!")
        return

    pasien = datapasien[nomor_pasien - 1]
    print(f"Data Pasien {nomor_pasien}: {pasien['Nama']}")
    for key, value in pasien.items():
        new_value = input(f"Masukan {key} (Data Saat ini: {value}): ")
        if new_value:
            pasien[key] = new_value

    print("Data Pasien Sukses Diubah")


def delete_patient():
    nomor_pasien = int(input("Masukan Nomor Pasien: "))
    if nomor_pasien < 1 or nomor_pasien > len(datapasien):
        print("Pasien Tidak Ditemukan Pada Nomor Pasien Yang Diinput!")
        return

    pasien = datapasien.pop(nomor_pasien - 1)
    print(f"Nomor Pasien {nomor_pasien} Terhapus: {pasien['Nama']}")
    print("Data Pasien Sukses Dihapus!")


def main():
    while True:
        print("\n====================Data Pasien Rumah Sakit====================")
        print("1. Tampilkan Seluruh Data Pasien")
        print("2. Tambah Pasien Baru")
        print("3. Rubah Data Pasien")
        print("4. Hapus Data Pasien")
        print("5. Selesai")

        inputanmenu = input("Silahkan Input nomor menu yang ingin dijalankan:: ")
        if inputanmenu == "1":
            show_data()
        elif inputanmenu == "2":
            create_patient()
        elif inputanmenu == "3":
            update_patient()
        elif inputanmenu == "4":
            delete_patient()
        elif inputanmenu == "5":
            print("Sampai Jumpa!")
            break
        else:
            print("Menu Tidak Ada. Silahkan Input Hanya 1 Sampai 5.")


