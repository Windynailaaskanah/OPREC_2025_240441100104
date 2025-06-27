Produk = {
    "Laptop" = 5500000,
    "Smartphone" = 3000000,
    "Tablet" = 2000000,
    "Smartwatch" = 1500000,
    "Headphone" = 500000
}


Nama = input("masukkan nama anda: ")
Umur = int(input("masukkan umur anda: "))
Member = input("apakah anda member? (ya/tidak): ")
Gadget = input("gadget mana yang ingin anda beli: ")
Jumlah = input("jumlah gadget yang ingin anda beli: ")
Tawar = input("apakah anda ingin menawar")

while True:
    if Umur <= 17 and Harga >= 3000000:
        print("maaf umur anda belum cukup untuk membeli produk ini.")
        break
    else:
        print("anda berhasil membeli produk ini")


    def cek_penawaran(tawar):
        if tawar >= 80.0:
            print("Harga diterima.")
        else:
            print("Penawaran ditolak, harga asli digunakan.")

    def Diskon(member, diskon):
        if member == "ya":
            if diskon >= 10.0 and 10000000:
                print("anda mendapatkan diskon member ")
            if diskon >= 5.0 and 5000000:
                print("anda mendapatkan diskon member")
            else:
                ("maaf. anda tidak mendapatkan diskon.")

    def transaksi():
        print("=== STRUK PEMBELIAN ===")
        print(f"Nama Pembeli : {Nama}")
        print(f"Produk Di beli : {Jumlah}")
        print("Harga/unit : ")
        print("Subtotal : ")
        print("Diskon : ")
        print("Total Akhir : ")

    ulangi = ("apakah anda ingin menambah produk? (ya/tidak) : ")
    if ulangi != "ya":
        break