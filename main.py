import base64
import time
from tqdm import tqdm
import os
import platform

dev = """
    ##        ####    ##  ##   ######    ####    ##  ##    ####    ##   ##
    ##       ##  ##   ##  ##   ##       ##  ##   ##  ##     ##     ### ###
    ##       ##  ##   ##  ##   ##       ##        ####      ##     #######
    ##       ##  ##   ##  ##   ####      ####      ##       ##     ## # ##
    ##       ##  ##   ##  ##   ##           ##    ####      ##     ##   ##
    ##       ##  ##    ####    ##       ##  ##   ##  ##     ##     ##   ##
    ######    ####      ##     ######    ####    ##  ##    ####    ##   ##
"""
developer = "\033[91m" + dev + "\033[0m"


def change_terminal_title(title):
    system_name = platform.system()  # İşletim sistemini öğren

    if system_name == 'Windows':
        # Windows işletim sisteminde terminal başlığını değiştir
        os.system(f'title {title}')
    elif system_name == 'Darwin' or system_name == 'Linux':
        # Linux ve macOS'ta terminal başlığını değiştir
        print(f"\033]0;{title}\007")  # ANSI escape kodu
    else:
        print(f"[Error] Unsupported OS: {system_name}")

change_terminal_title("Lovesxim - Base64 Şifreleme/Çözme Programı")

def clear_screen():
    # Platforma bağlı olarak uygun komutu çalıştır
    if os.name == 'nt':  # Windows için
        os.system('cls')
    else:  # Linux/macOS için
        os.system('clear')


# Renkli Yükleme Çubuğu (progress bar)
def loading_animation():
    print("Yükleniyor, lütfen bekleyiniz...")
    for _ in tqdm(range(10), desc="Yükleniyor", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}", ncols=100, colour='magenta'):
        time.sleep(0.5)  # 5 saniye boyunca yükleme simülasyonu yapılıyor


def encode_base64():
    text_to_encode = input("Şifrelenecek veriyi girin: ")

    # Şifreleniyor mesajı
    print("\033[96mŞifreleniyor, lütfen bekleyiniz...\033[0m", end="")  # Mavi renk
    time.sleep(1)  # 1 saniye bekleme (canlandırma için)

    # Base64 şifreleme
    encoded_data = base64.b64encode(text_to_encode.encode('utf-8'))
    time.sleep(1)  # Şifreleme işlemi için kısa bir bekleme
    print(f"\033[92m\nŞifrelenmiş veri: {encoded_data.decode('utf-8')}\033[0m")  # Yeşil renk

    # 10 saniye bekleyip menüye dönme
    print("\033[93mŞifreleme başarılı. 10 saniye sonra ana menüye dönülecek...\033[0m")
    time.sleep(10)  # 10 saniye bekleme

    # Ekran Temizle
    clear_screen()


# Base64 çözme işlemi
def decode_base64():
    encoded_data = input("Base64 şifreli veriyi girin: ")

    for _ in tqdm(range(10), desc="Çözülüyor", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}", ncols=100, colour='magenta'):
        time.sleep(0.5)  # 5 saniye boyunca yükleme simülasyonu yapılıyor

    try:
        decoded_data = base64.b64decode(encoded_data)
        time.sleep(1)  # Çözme işlemi için kısa bir bekleme
        print(f"\nÇözülmüş veri: {decoded_data.decode('utf-8')}")
        
    except Exception as e:
        print(f"\nHata oluştu: {e}")

    # 10 saniye bekleyip menüye dönme
    print("\033[93mÇözme işlemi tamamlandı. 10 saniye sonra ana menüye dönülecek...\033[0m")
    time.sleep(10)  # 10 saniye bekleme

    # Ekran Temizle
    clear_screen()


# Ana program
def main():
    # Ekran Temizle
    clear_screen()
    # Developer Name
    print(developer)
    # Yükleniyor animasyonu
    loading_animation()
    # Ekran Temizle
    clear_screen()
    while True:
        print(developer)
        print("\nİşlem Seçin:")
        print("\033[92m1 - Base64 Şifrele\033[0m")
        print("\033[92m2 - Base64 Çöz\033[0m")
        print("\033[91mÇıkmak için 'q' tuşlayın.\033[0m")
        
        choice = input("Seçiminizi yapın (1/2/q): ")

        if choice == '1':
            encode_base64()  # Şifreleme işlemi
        elif choice == '2':
            decode_base64()  # Çözme işlemi
        elif choice.lower() == 'q':
            print("\033[91mProgramdan çıkılıyor...\033[0m")
            break  # Programdan çıkış
        else:
            # Ekran Temizle
            clear_screen()
            print(developer)
            print("\033[91mGeçersiz seçim! Lütfen '1', '2' veya 'q' girin.\033[0m")


# Programı çalıştır
if __name__ == "__main__":
    main()
