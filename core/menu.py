import os
import time
import random
import sys

# --- Colors for Hacker Look ---
G = "\033[1;32m" # Green
R = "\033[1;31m" # Red
Y = "\033[1;33m" # Yellow
C = "\033[1;36m" # Cyan
W = "\033[0m"    # Reset

def slow_print(text, speed=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def main_menu():
    os.system("clear")
    print(f"{G}=================================================={W}")
    print(f"{C}          GARAENA FF - PREMIUM INJECTOR v3.1      {W}")
    print(f"{G}=================================================={W}")
    print(f"{Y}[💻 Status: Mainframe Connected]{W}\n")
    
    print(f"{C}[1]{W} Generate Google Play Redeem Code")
    print(f"{C}[2]{W} Inject Free Fire Diamonds (Direct)")
    print(f"{C}[3]{W} Bypass Garena Anticheat Firewall")
    print(f"{R}[4] Exit Tool{W}")
    
    choice = input(f"\n{Y}Apna Option Chuno (1-4): {W}")
    
    if choice == '1':
        redeem_code_prank()
    elif choice == '2' or choice == '3':
        fake_injection()
    elif choice == '4':
        print(f"\n{R}Exiting Tool... Bye!{W}")
        sys.exit()
    else:
        print(f"\n{R}[!] Invalid Option! Dobara try karo.{W}")
        time.sleep(1)
        main_menu()

def redeem_code_prank():
    os.system("clear")
    print(f"{C}--- REDEEM CODE GENERATOR MODE ---{W}\n")
    uid = input(f"{W}Apni Free Fire Player UID dalo: {W}")
    amount = input(f"{W}Amount Select Karo (80, 160, 400, 800): ₹")
    
    print(f"\n{Y}[*] Connecting to Play Store API...{W}")
    time.sleep(1.5)
    print(f"{G}[+] Connection Established!{W}")
    time.sleep(1)
    
    # Fake terminal logs scroll karne ke liye
    print(f"\n{C}[*] Fetching unused tokens from database...{W}")
    for _ in range(3):
        rand_hex = "".join(random.choices("0123456789ABCDEF", k=8))
        print(f"{Y}Searching block: 0x{rand_hex}... {G}OK{W}")
        time.sleep(0.4)
        
    print(f"\n{C}[*] Bypassing Garena security protocols...{W}")
    time.sleep(1.5)
    
    # Fake Progress Bar
    for i in range(1, 101, 10):
        print(f"\r{Y}Generating Code: [{('█'*(i//10)).ljust(10)}] {i}%{W}", end="")
        time.sleep(0.15)
        
    # Fake Code Format
    fake_code = "GOOG-" + "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=4)) + "-" + "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=4)) + "-" + "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=4))
    
    print(f"\n\n{G}[🎉 SUCCESS] Code successfully generated for UID {uid}!{W}")
    print(f"{Y}Aapka Redeem Code: {W}{R}{fake_code}{W}")
    print(f"\n{C}⚠️ Warning: Ise agle 5 minutes mein use karein warna expire ho jayega!{W}")
    
    input(f"\n{G}Main Menu par wapas jaane ke liye Enter dabao...{W}")
    main_menu()

def fake_injection():
    os.system("clear")
    print(f"{R}--- FIREWALL BYPASS & DIAMOND INJECTION ---{W}\n")
    input(f"{W}Enter Target Username/UID: {W}")
    print(f"\n{R}[!] WARNING: High risk operation detected.{W}")
    print(f"{C}[*] Initializing proxy chains...{W}")
    time.sleep(2)
    
    slow_print(f"{Y}[*] Injecting malicious payload into server...{W}", 0.02)
    slow_print(f"{R}[!] Error 403: Garena Firewall Blocked the Request!{W}", 0.01)
    slow_print(f"{Y}[*] Retrying with alternative port 8080...{W}", 0.02)
    slow_print(f"{G}[+] Success! Inside the database.{W}", 0.02)
    
    time.sleep(1)
    print(f"\n{R}[❌ SYSTEM HALTED] Script stopped: Device is not Rooted!{W}")
    print(f"{Y}Tip: Is feature ke liye aapko root access chahiye hoga (Just Kidding!).{W}")
    
    input(f"\n{G}Main Menu par wapas jaane ke liye Enter dabao...{W}")
    main_menu()

if __name__ == "__main__":
    main_menu()
