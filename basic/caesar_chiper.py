def enkripsi(teks_asli, geser):
    """
    Fungsi untuk mengenkripsi teks menggunakan metode Caesar Cipher yang mendukung huruf dan angka.

    Parameter:
        teks_asli (str): Teks yang akan dienkripsi.
        geser (int): Jumlah pergeseran huruf atau angka (misal 3 berarti A->D dan 1->4).

    Proses:
        - Huruf besar dan kecil akan digeser dalam rentang alfabet (A-Z atau a-z).
        - Angka (0-9) akan digeser dengan modulus 10.
        - Karakter lain seperti spasi, tanda baca, dll tidak diubah.

    Mengembalikan:
        str: Hasil teks yang sudah terenkripsi.
    """
    teks_terenkripsi = ""
    for karakter in teks_asli:
        if karakter.isalpha():  # Jika huruf (A-Z / a-z)
            dasar_pergeseran = ord('A') if karakter.isupper() else ord('a')
            karakter_baru = chr((ord(karakter) - dasar_pergeseran + geser) % 26 + dasar_pergeseran)
            teks_terenkripsi += karakter_baru
        elif karakter.isdigit():  # Jika angka (0-9)
            karakter_baru = chr((ord(karakter) - ord('0') + geser) % 10 + ord('0'))
            teks_terenkripsi += karakter_baru
        else:  # Karakter lain tidak diubah
            teks_terenkripsi += karakter
    return teks_terenkripsi


def dekripsi(teks_sandi, geser):
    """
    Fungsi untuk mendekripsi teks yang telah dienkripsi dengan metode Caesar Cipher.

    Parameter:
        teks_sandi (str): Teks yang telah terenkripsi.
        geser (int): Jumlah pergeseran yang digunakan saat enkripsi.

    Proses:
        - Huruf besar dan kecil akan dikembalikan ke posisi semula.
        - Angka (0-9) akan digeser mundur dengan modulus 10.
        - Karakter lain seperti spasi, tanda baca, dll tidak diubah.

    Mengembalikan:
        str: Hasil teks yang sudah terdekripsi (kembali ke bentuk aslinya).
    """
    teks_terdekripsi = ""
    for karakter in teks_sandi:
        if karakter.isalpha():  # Jika huruf
            dasar_pergeseran = ord('A') if karakter.isupper() else ord('a')
            karakter_baru = chr((ord(karakter) - dasar_pergeseran - geser) % 26 + dasar_pergeseran)
            teks_terdekripsi += karakter_baru
        elif karakter.isdigit():  # Jika angka
            karakter_baru = chr((ord(karakter) - ord('0') - geser) % 10 + ord('0'))
            teks_terdekripsi += karakter_baru
        else:
            teks_terdekripsi += karakter
    return teks_terdekripsi
