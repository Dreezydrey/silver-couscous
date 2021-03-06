import sys
import socket
import urllib
import gzip
import os



try:
    import pygeoip
except ImportError:
    print("[!] Failed to import pygeoip")
    try:
        choice = input("[*] Attempt to auto-install pygeoip? [y/N]: ")
    
    except KeyboardInterrupt:
        print("\n[!] User Interrupted Choice")
        sys.exit(1)
    if choice.strip().lower()[0] == "y":
        print("[*] Antempting to intsall pygeoip...")
        sys.stdout.flush()

        #
       
        try:
            import pip
            pip.main(["install", "-q", "pygeoip"])
            import pygeoip
            print("[DOne]")
        except Exception:
            print("[Fail")
    elif choice.strip().lower()[0] == "n":
        print("[*] User Denied Auto-install")
        sys.exit(1)
    else:
        print("[!] Invalid Decision")
        sys.exit()


class Locator(object):
    def __init__(self, url=False, ip=False, datfile=False):
        self.url = url
        self.ip = ip
        self.datfile = datfile
        self.target = ""

    def check_database(self):
        if not self.datfile:
            self.datfile = ("usr/share/Geoip/GeoLiteCity.dat")
        else:
            if not os.path.isfile(self.datfile):
                print("[!] Failed to detect specified database")
                sys.exit(1)
            else:
                return
        if not os.path.isfile(self.datfile):
            print("[!] Default Database detection failed")
            try:
                choice = input("[*] Attempt to auto-install database? [y/n]: ")
            except KeyboardInterrupt:
                print("\nuser interrupted choice")
                sys.exit(1)
            if choice.strip().lower(0) == ("y"):
                print("[*] Attempting to auto-install Database...")
                sys.stdout.flush()
            if not os.path.isdir("/usr/share/GeoIP"):
                os.makedirs("/usr/share/GeoIP")
            try:
                urllib.urlretrieve("http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz","/usr/share/GeoIP/GeoLiteCity.dat.gz")
            except Exception:
                print("[FAIL")
                print("[!] Failed to Download Database")
                sys.exit(1)

            try:
                with gzip.open("/usr/share/GeoIP/GeoLiteCity.dat.gz","rb") as compressed_dat:
                    with open("/usr/share/GeoIP/GeoLiteCity.dat", "wb") as new_dat:
                        new_dat.write(compressed_dat.read())
            except IOError:
                print("[FAIL]")
                print("[!] Failed to decompressed to database")
                sys.exit(1)
            os.remove("/usr/share/GeoIP/GeoLiteCity.dat.gz")
            print("[Done]\n")
        elif choice.strip().lower()[0] == ("n"):
            print("[!] User Denied Auto-Install")
            sys.exit(1)
        else:
            print("[!] Invalid Choice")
            sys.exit(1)
def args_url(url):
    return os.path.join(ARGS_URL, url)

def query(self):
    if not not self.url:
        print("[*] Translating %s: " %(self.url)),
        sys.stdout.flush()
        try:
            self.target += socket.gethostbyname(self.url)
            print(self.target)
        except Exception:
            print("\n[!] Failed to Resolve URl")
            return
    else:
        self.target += self.ip
    try:
        print("[*] Querying for Records of %s...\n" %(self.target))
        query_obj = pygeoip.GeoIP(self.datfile)
        for key, val in query_obj.record_by_addr(self.target).items():
            print("%s %s" %(key, val))
        print("\n[*] Query Complete!")
    except Exception:
        print("\n[!] Failed to Retrieve Records")
        return

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="IP Geolocation Tool")
    parser.add_argument("--url", help="Locate an Ip based on a url", action="store",default=False, dest="url")
    parser.add_argument("-t", "--target", help="Locate the specified IP", action="store", default=False, dest="ip")
    parser.add_argument("--dat", help="Custom database filepath", action="store", default=False, dest="datfile" )
    args = parser.parse_args()

if ((not not args_url) and (not not args.ip)) or ((not args.url) and (not args.ip)):
    parser.error("Invalid target specification")
try:
    Locator_object = Locator(url=args.url,ip = args.ip, datfile = args.datfile)
    Locator_object.check_database()
    Locator_object.query()
except Exception:
    print("\n\n[!] An Unknown Error  Occured")
    sys.exit(1)
except KeyboardInterrupt:
    print("\n\n [!] Unexpected User Interrupt")
    sys.exit(1)
    
























