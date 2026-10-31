
# PROGRAM KASIR SEDERHANA

print("================================")
print("       PROGRAM KASIR")
print("================================")

total_belanja = 0

while True:
    print("\nDaftar Menu:")
    print("1. Nasi Goreng  - Rp15.000")
    print("2. Mie Goreng   - Rp12.000")
    print("3. Es Teh       - Rp5.000")
    print("4. Selesai dan Bayar")

    pilihan = input("\nPilih menu (1-4): ")

    # Percabangan
    if pilihan == "1":
        harga = 15000
        nama = "Nasi Goreng"
    elif pilihan == "2":
        harga = 12000
        nama = "Mie Goreng"
    elif pilihan == "3":
        harga = 5000
        nama = "Es Teh"
    elif pilihan == "4":
        break
    else:
        print("Pilihan tidak tersedia!")
        continue

    jumlah = int(input("Masukkan jumlah pesanan: "))
    subtotal = harga * jumlah
    total_belanja += subtotal

    print(nama, "sebanyak", jumlah, "berhasil ditambahkan.")
    print("Subtotal: Rp", subtotal)

# Percabangan setelah perulangan
print("\n================================")
print("         STRUK PEMBAYARAN")
print("================================")
print("Total Belanja: Rp", total_belanja)

if total_belanja >= 50000:
    diskon = total_belanja * 0.10
    print("Diskon 10%: Rp", int(diskon))
else:
    diskon = 0
    print("Diskon: Rp 0")

total_bayar = total_belanja - diskon

print("Total Bayar: Rp", int(total_bayar))
print("Terima kasih sudah berbelanja!")
