def hitung_hasil_kali(n):
    hasil = 1
    for i in range(1, n + 1):
        hasil *= i
    return hasil

def main():
        tanggal_tes = int(input("Masukkan tanggal tes hari ini : "))
        hasil = hitung_hasil_kali(tanggal_tes)
        print("Hasil perkalian dari 1 hingga", tanggal_tes, "adalah:", hasil)

if __name__ == "__main__":
    main()
