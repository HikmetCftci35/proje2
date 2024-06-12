from personel import Personel
from doktor import Doktor
from hemsire import Hemsire
from hasta import Hasta


def main():
    try:
        personel1 = Personel(1, "Ömer", "Alkan", "Muhasebe", 20000)
        personel2 = Personel(2, "Mustafa", "Alp", "Yönetim", 18000)
        doktor1 = Doktor(3, "Ali", "Gece", "Cerrahi", 35000, "Ortopedi", 8, "Tınaztepe Hastanesi")
        doktor2 = Doktor(4, "Muaz", "Eriktaş", "Dahiliye", 30000, "Kardiyoloji", 4, "Seyfi Demirsoy Hastanesi")
        hemsire1 = Hemsire(5, "Hande", "Erçil", "Acil", 25000, 40, "Sertifika 1", "Tınaztepe Hastanesi")
        hasta1= Hasta(1, "Yunus", "Çetinkaya", "30-06-2005", "Boğaz Enfeksiyonu", "İlaç")
        hasta2 = Hasta(2, "Muhammed", "Karameşe", "30-07-1999", "Bronşit", "İlaç")

        personeller = [personel1, personel2, doktor1, doktor2, hemsire1]
        hastalar = [hasta1, hasta2]

        #Veri analizleri
        #Uzmanlık alanlarına göre doktor sayısı
        uzmanlik_gruplari = {}
        for personel in personeller:
            if isinstance(personel, Doktor):
                uzmanlik = personel.get_uzmanlik()
                if uzmanlik in uzmanlik_gruplari:
                    uzmanlik_gruplari[uzmanlik] += 1
                else:
                    uzmanlik_gruplari[uzmanlik] = 1
        print("Uzmanlık alanlarına göre doktor sayısı:")
        for uzmanlik, sayi in uzmanlik_gruplari.items():
            print(f"{uzmanlik}: {sayi}")

        #5 yıldan fazla deneyime sahip doktor sayısı
        deneyimli_doktor_sayisi = sum(1 for personel in personeller if isinstance(personel, Doktor) and personel.get_deneyim_yili() > 5)
        print(f"5 yıldan fazla deneyime sahip doktor sayısı: {deneyimli_doktor_sayisi}")

        #Hasta adlarına göre sıralama
        hastalar.sort(key=lambda h: h.get_ad())
        print("Hasta adlarına göre sıralı liste:")
        for hasta in hastalar:
            print(hasta)

        #Maaşı 26000 üstü olan personeller
        yuksek_maasli_personel = [personel for personel in personeller if personel.get_maas() > 26000]
        print("Maaşı 26000 TL üzerinde olan personeller: ")
        for personel in yuksek_maasli_personel:
            print(personel)

        #Doğum tarihi 2000 üstü olan hastalar
        yeni_dogumlu_hastalar = [hasta for hasta in hastalar if int(hasta.get_dogum_tarihi().split("-")[0])>= 2000]
        print("2000 ve sonrası doğumlu hastalar: ")
        for hasta in yeni_dogumlu_hastalar:
            print(hasta)
        
    except Exception as e:
        print(f"Bir Hata Oluştu: {e}")

if __name__ == "__main__":
    main()