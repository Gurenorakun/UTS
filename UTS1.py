import datetime

def hitung_jumlah_hari_dalam_tahun():
    tahun_sekarang = datetime.datetime.now().year

    if tahun_sekarang % 4 == 0 and (tahun_sekarang % 100 != 0 or tahun_sekarang % 400 == 0):
        return 366
    else:
        return 365

def main():
    bilangan_bulat = int(input("Masukkan sebuah bilangan bulat: "))

    jumlah_hari = hitung_jumlah_hari_dalam_tahun()

    hasil = bilangan_bulat / jumlah_hari

    hasil_terformat = "{:.11f}".format(hasil)
    print("Hasil:", hasil_terformat)

if __name__ == "__main__":
    main()
