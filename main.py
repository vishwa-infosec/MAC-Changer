import subprocess
from sys import argv

def printInterfacesLinux():
    #print the updated interface details
    print("[+] Updated Interface:")
    subprocess.call(["ifconfig", argv[1]])

def changeMacAddressLinux(interface, newMac):
    print(f"[+] Changing MAC address for {interface} to {newMac}")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", newMac])
    subprocess.call(["ifconfig", interface, "up"])

def printInterfacesWindows():
    print("[+] Available network interfaces:")
    subprocess.call(["ipconfig", "/all"])

def changeMacAddressWindows(interface, newMac):
    print(f"[+] Changing MAC address for {interface} to {newMac}")
    subprocess.call(["reg", "add", f"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\{interface}\Ndi\params\NetworkAddress", "/v", "NetworkAddress", "/t", "REG_SZ", "/d", newMac, "/f"])
    subprocess.call(["ipconfig", "/release"])
    subprocess.call(["ipconfig", "/renew"])


if "__main__" == __name__:
    changeMacAddressLinux(argv[1], argv[2])
    printInterfacesLinux()
