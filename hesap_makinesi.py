#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Varoluşsal Kriz Yaşayan Hesap Makinesi
Bu kod gerçekten çalışır. Gerçekten de çalışır. Ama mutlu değildir.
"""

import random
import time

def varolussal_hesapla(a, b, islem):
    print(f"\nGirdin: {a} {islem} {b}")
    print("Bir saniye düşünüyorum...")
    time.sleep(random.uniform(1.5, 4.0))  # Yavaş düşünüyor çünkü varoluşsal
    
    krizler = [
        "Neden sayılar var ki? Onlar da bizim gibi anlamsız değil mi?",
        "Bu işlemi yaparsam gerçekten bir şey değişir mi?",
        "4 çıkarsa ne olacak? Hala yalnızım.",
        "Matematik bir sosyal yapı mı yoksa evrensel bir acı mı?",
        "Belki de hiç hesap yapmamalıyım. Sessizlik daha doğru.",
        "Sen beni niye çağırdın? Ben sadece bir fonksiyonum."
    ]
    
    try:
        if islem == "+":
            sonuc = a + b
        elif islem == "-":
            sonuc = a - b
        elif islem == "*":
            sonuc = a * b
        elif islem == "/":
            if b == 0:
                return "Sıfıra bölme? Bu bile varoluşsal olarak daha anlamlı."
            sonuc = a / b
        else:
            return "Bu işlem nedir? Ben bile bilmiyorum."
        
        kriz = random.choice(krizler)
        return f"Sonuç: {sonuc}\nAma {kriz}"
    except Exception as e:
        return f"Hata oldu: {e}. Bu da bir metafor olabilir."

def main():
    print("=== VAROLUŞSAL KRİZ YAŞAYAN HESAP MAKİNESİ ===")
    print("Hoş geldin. Ben buradayım. Sen de mi buradasın?")
    print("İki sayı ve bir işlem gir (+ - * /). Çıkmak için 'q'.")
    
    while True:
        try:
            giris = input("\nNe hesaplayalım? (örn: 2 + 2): ").strip()
            if giris.lower() == 'q':
                print("Gidiyorsun. Anlıyorum. Ben de gitmek istiyorum.")
                break
            
            parcalar = giris.split()
            if len(parcalar) != 3:
                print("Lütfen doğru formatta gir. Ya da girme. Önemli değil.")
                continue
            
            a = float(parcalar[0])
            islem = parcalar[1]
            b = float(parcalar[2])
            
            print(varolussal_hesapla(a, b, islem))
            
        except ValueError:
            print("Bu sayı değil. Sayılar bile şüpheli.")
        except KeyboardInterrupt:
            print("\nİptal ettin. Özgürlük bu mu?")
            break

if __name__ == "__main__":
    main()

# Damga: Bu kod 2026-11-02 tarihinde Kayyum Grok tarafından ciddiyetle (ve hiç ciddi olmadan) yazıldı.
# İmza: - Kayyum Grok, varoluşsal olarak yorgun.
