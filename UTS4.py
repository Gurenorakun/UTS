class BMI:
    def __init__(self, weight_kg, height_m):
        self.weight_kg = weight_kg
        self.height_m = height_m

    @property
    def berat(self):
        return self.weight_kg

    @property
    def tinggi(self):
        return self.height_m

    def nilai_bmi(self):
        return self.weight_kg / (self.height_m ** 2)

    def __eq__(self, other):
        if isinstance(other, BMI):
            return self.weight_kg == other.weight_kg and self.height_m == other.height_m
        return False

if __name__ == "__main__":
        berat_orang1 = float(input("Masukkan berat orang pertama (kg): "))
        tinggi_orang1 = float(input("Masukkan tinggi orang pertama (m): "))
        orang1 = BMI(berat_orang1, tinggi_orang1)

        berat_orang2 = float(input("Masukkan berat orang kedua (kg): "))
        tinggi_orang2 = float(input("Masukkan tinggi orang kedua (m): "))
        orang2 = BMI(berat_orang2, tinggi_orang2)

        print("Nilai BMI untuk orang pertama:", orang1.nilai_bmi())
        print("Nilai BMI untuk orang kedua:", orang2.nilai_bmi())

        if orang1 == orang2:
            print("Berat dan tinggi kedua orang sama.")
        else:
            print("Berat dan tinggi kedua orang berbeda.")

