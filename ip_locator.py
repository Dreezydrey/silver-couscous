import sys
import socket
import urllib.request
import gzip
import os

try:
    import pygeoip
except ImportError:
    print("[!] Failed to import pygeoip")
    choice = input("[*] Attempt to auto-install pygeoip? [y/N]: ").strip().lower()
    if choice and choice[0] == "y":
        print("[*] Attempting to install pygeoip...")
        sys.stdout.flush()
        try:
            from pip._internal import main
            main(["install", "-q", "pygeoip"])
            import pygeoip
            print("[Done]")
        except Exception:
            print("[Fail]")
            sys.exit(1)
    else:
        print("[*] Install skipped")
        sys.exit(1)

class Locator:
    def __init__(self, url=False, ip=False, datfile=False):
        self.url = url
        self.ip = ip
        self.datfile = datfile
        self.target = ""

    def check_database(self):
        if not self.datfile:
            self.datfile = "/usr/share/GeoIP/GeoLiteCity.dat"
        if not os.path.isfile(self.datfile):
            print("[!] Database not found")
            choice = input("[*] Attempt to auto-install database? [y/N]: ").strip().lower()
            if choice and choice[0] == "y":
                print("[*] Attempting to install database...")
                os.makedirs("/usr/share/GeoIP", exist_ok=True)
                try:
                    urllib.request.urlretrieve(
                        "http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz",
                        "/usr/share/GeoIP/GeoLiteCity.dat.gz"
