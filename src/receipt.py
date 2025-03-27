from src.order import order_manager

def cetak_struk_dp():
    print("\n" + "=" * 30)
    print("       STRUK DP RESTORAN      ")
    print("=" * 30)

    if not order_manager.orders:
        print("        Tidak ada order")
    else:
        total_harga = 0
        print(f"{'No':<4}{'Meja':<6}{'Menu':<15}{'Qty':<5}")
        print("-" * 30)

        for idx, order in enumerate(order_manager.orders, start=1):
            print(f"{idx:<4}{order['meja']:<6}{order['menu']:<15}{order['jumlah']:<5}")
            total_harga += int(order['jumlah']) * 10000  # Simulasi harga per item 10,000

        print("-" * 30)
        print(f"{'Total Harga:':<25}Rp {total_harga:,.2f}")
        print(f"{'DP 50%:':<25}Rp {total_harga * 0.5:,.2f}")

    print("=" * 30)
    print("  Terima kasih telah memesan! ")
    print("=" * 30 + "\n")
