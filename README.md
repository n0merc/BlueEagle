#  BLUE EAGLE - Bluetooth Spammer Tool

**Warning: This tool is for educational and authorized testing purposes only. Unauthorized use is illegal and can result in criminal charges.**

---

##  Overview

Blue Eagle is a powerful Bluetooth spammer tool designed for penetration testing and security research. It allows you to scan for nearby Bluetooth devices and flood them with connection requests, causing disruption and demonstrating Bluetooth vulnerabilities.

### ⚠️ **DISCLAIMER**
- **FOR EDUCATIONAL PURPOSES ONLY**
- **USE ONLY ON DEVICES YOU OWN OR HAVE EXPLICIT PERMISSION TO TEST**
- **UNAUTHORIZED ACCESS TO COMPUTER SYSTEMS IS ILLEGAL**
- **THE DEVELOPERS ARE NOT RESPONSIBLE FOR ANY MISUSE**

---

##  Features

-  **Device Scanning**: Discover nearby Bluetooth devices
-  **Multi-Device Spamming**: Attack multiple targets simultaneously
-  **Custom Targeting**: Spam specific devices with custom packet counts
-  **User-Friendly Menu**: Easy-to-use terminal interface
-  **Scary Visuals**: Intimidating "Blue Eagle" ASCII logo
-  **Multi-threaded**: Efficient spamming with threading

---

##  Prerequisites

### System Requirements
- **Linux** (Kali, Ubuntu, etc.) or **Termux** on Android
- **Root privileges** (for Bluetooth operations on Linux)
- **Python 3.7+**
- **Bluetooth adapter** (built-in or USB)

---

##  Installation

### Method 1: Quick Install
```bash
# Clone the repository
git clone https://github.com/n0merc/blueEagle.git
cd blueEagle

# Install dependencies
pip install -r requirements.txt

# Make executable
chmod +x blueEagle.py
```

### Method 2: Manual Install
```bash
# Install required packages
sudo apt-get update
sudo apt-get install bluetooth bluez bluez-tools
pip install pybluez colorama
```

---

##  Usage

### Basic Usage
```bash
# Run with root privileges
sudo python3 blueEagle.py
```

### Menu Options
1. **Scan for nearby Bluetooth devices** - Discover targets
2. **Spam all discovered devices** - Attack all found devices
3. **Custom spam to specific device** - Target a specific MAC address
4. **Clear target list** - Reset discovered devices
5. **Show discovered devices** - List current targets
6. **Exit** - Quit the tool

### Example Workflow
```
1. Select option 1 to scan for devices
2. Note the MAC addresses of targets
3. Select option 2 to spam all devices
4. Press Ctrl+C to stop spamming
```

---

##  Technical Details

### How It Works
1. **Device Discovery**: Uses `bluetooth.discover_devices()` to find nearby devices
2. **Spam Techniques**:
   - L2CAP ping floods (`l2ping`)
   - Connection request floods (`hcitool`)
   - Service discovery floods (`sdptool`)
3. **Multi-threading**: Each target gets its own spam thread
4. **Packet Crafting**: Sends malformed or excessive Bluetooth packets

### Supported Attacks
- **Bluetooth DoS**: Denial of Service by flooding connection requests
- **Device Disruption**: Causes instability in target devices
- **Battery Drain**: Rapid connection attempts drain device batteries

---

##  Legal & Ethical Use

### Authorized Testing Only
- Test on your own devices
- Get written permission for penetration tests
- Follow responsible disclosure policies

### Prohibited Uses
- ❌ Attacking public networks
- ❌ Targeting devices without permission
- ❌ Causing damage or disruption to others
- ❌ Any illegal activities

---

##  Risks & Limitations

### Risks
- **Legal consequences** for unauthorized use
- **Device damage** from excessive spamming
- **Detection** by security systems
- **Ethical violations**

### Limitations
- Works best on Linux systems
- Requires root privileges
- Limited range (typically 10-100 meters)
- May not work on all Bluetooth versions

---

##  Security Recommendations

### For Defenders
1. Disable Bluetooth when not in use
2. Use non-discoverable mode
3. Update Bluetooth firmware regularly
4. Monitor for unusual connection attempts

### For Testers
1. Document all testing activities
2. Use isolated lab environments
3. Follow penetration testing frameworks
4. Obtain proper authorization

---

##  Educational Purpose

This tool demonstrates:
- Bluetooth protocol vulnerabilities
- Wireless attack vectors
- Importance of Bluetooth security
- Ethical hacking methodologies

---

##  Troubleshooting

### Common Issues
1. **"No devices found"**
   - Ensure Bluetooth is enabled
   - Check adapter with `hciconfig`
   - Run as root

2. **Permission errors**
   ```bash
   sudo python3 blueEagle.py
   ```

3. **Python module errors**
   ```bash
   pip install --upgrade pybluez
   ```

4. **Bluetooth service not running**
   ```bash
   sudo systemctl start bluetooth
   ```

---

##  License

This project is licensed under the **GNU General Public License v3.0** - see the [LICENSE](LICENSE) file for details.

```
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

##  Contributors

- **n0merc** - Lead Developer
- **HUBAX Team** - Security Research

---

##  Support

If you find this tool useful:
- Give it a star on GitHub
- Report issues and suggestions
- Contribute to development
- Share responsibly with the security community

---


**Remember: With great power comes great responsibility. Use this tool ethically and legally.**

🦅 **BLUE EAGLE - Fly High, Test Responsibly** 🦅
*"The eagle doesn't hunt flies. It hunts prey worth its time." - n0merc*
