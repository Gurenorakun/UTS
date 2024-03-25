import datetime

def hitung_tanggal(hari):
    hari_ini = datetime.datetime.now()

    tanggal_mendatang = hari_ini + datetime.timedelta(days=hari)

    return tanggal_mendatang

def format_tanggal(tanggal):
    nama_hari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
    bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']

    hari = nama_hari[tanggal.weekday()]
    tanggal_hari = tanggal.day
    nama_bulan = bulan[tanggal.month - 1]
    tahun = tanggal.year

    tanggal_terformat = f"{hari} pada tanggal {tanggal_hari} {nama_bulan} {tahun}"
    return tanggal_terformat

def main():
        hari = int(input("Masukkan jumlah hari dari sekarang: "))
        tanggal_mendatang = hitung_tanggal(hari)
        tanggal_terformat = format_tanggal(tanggal_mendatang)
        print("Tanggal setelah", hari, "hari dari sekarang adalah:", tanggal_terformat)

if __name__ == "__main__":
    main()
