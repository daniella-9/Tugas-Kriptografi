"""Modul untuk program enkripsi dan deskripsi teknik substitutions"""

import random
import string

def buat_kunci() -> dict:
    """
    Menghasilkan secara acak kunci subtitusi untuk tiap huruf dalam alfabet

    Returns:
        kunci_substitusi (dict): kunci substitusi untuk proses enkripsi dan dekripsi
    """

    huruf = string.ascii_letters
    huruf_acak = list(huruf)
    random.shuffle(huruf_acak)

    kunci_substitusi = dict(zip(huruf, huruf_acak))
    return kunci_substitusi

def enkripsi_pesan(pesan: str, kunci: dict) -> str:
    """
    Mengenkripsi pesan menggunakan kunci substitusi

    Args:
        pesan (str): pesan yang akan dienkripsi
        kunci (dict): kunci yang digunakan untuk enkripsi pesan

    Return:
        pesan_dienkripsi (str): hasil enkripsi
    """

    pesan_dienkripsi = ""

    for karakter in pesan:
        if karakter in kunci:
            pesan_dienkripsi += kunci[karakter]
        else:
            pesan_dienkripsi += karakter

    return pesan_dienkripsi

def dekripsi_pesan(pesan_dienkripsi: str, kunci: dict) -> str:
    """
    Mendekripsi pesan dienkripsi menggunakan kunci substitusi

    Args:
        pesan_dienkripsi (str): pesan yang akan didekripsi
        kunci (dict): kunci yang digunakan untuk dekripsi pesan
    
    Returns:
        pesan (str): pesan asli dari pesan yang dienkripsi
    """

    kunci_terbalik = {nilai:indeks_kunci for indeks_kunci, nilai in kunci.items()}
    pesan = ''

    for karakter in pesan_dienkripsi:
        if karakter in kunci_terbalik:
            pesan += kunci_terbalik[karakter]
        else:
            pesan += karakter

    return pesan

CONTOH_PESAN = "Ini adalah program untuk enkripsi dan deskripsi dari teknik substitutions."
contoh_kunci = buat_kunci()

contoh_pesan_dienkripsi = enkripsi_pesan(
    pesan=CONTOH_PESAN,
    kunci=contoh_kunci
)

pesan_asli = dekripsi_pesan(
    pesan_dienkripsi=contoh_pesan_dienkripsi,
    kunci=contoh_kunci
)

print(f"""
Pesan Asli: {CONTOH_PESAN}
Kunci Substitusi: {contoh_kunci}
Pesan Dienkripsi: {contoh_pesan_dienkripsi}
Pesan Didekripsi: {pesan_asli}
""")
