import requests
import re
import socket
import time

R  = "\033[91m"
s  = "\033[0m"
O  ='\33[37m' 
 
print(f"{R}\n###-Discover sub-Domain_API{s}")
print('='*25)
print()
class API_SubDomains_Scan:

    def find_subdomains(self, **kwargs):
  
        pattern = r"https?://(?:www\.)?([^/\s]+)" 
        domain = str("".join(re.findall(pattern, self.args.URL)))
        if not domain:
            domain = self.args.URL.strip()
        subdomains = None
        try:
            url = f"https://api.hackertarget.com/hostsearch/?q={domain}"
            resp = requests.get(url, timeout=10)
            if resp.status_code == 200:
                text = resp.text.strip()
                if "API count exceeded" not in text and "error" not in text.lower():
                    subdomains = [line.split(",")[0] for line in text.splitlines()]
                    print(f"{O}[*]API_refrance  ...........|   Using Hackertarget API{s}")
        except Exception:
            pass

        if not subdomains:
            try:
                url = f"https://crt.sh/?q=%25.{domain}&output=json"
                resp = requests.get(url, timeout=10)
                if resp.status_code == 200:
                    try:
                        data = resp.json()
                        subdomains = list({entry["name_value"] for entry in data})
                        print(f"{O}[*]API_refrance  ...........| Using crt.sh API{s}")
                    except Exception:
                        pass
            except Exception:
                pass

        if not subdomains:
            try:
                url = f"https://rapiddns.io/subdomain/{domain}?full=1"
                resp = requests.get(url, timeout=10)
                if resp.status_code == 200:
                    matches = re.findall(r"<td>([a-zA-Z0-9.-]+\." + re.escape(domain) + r")</td>", resp.text)
                    if matches:
                        subdomains = matches
                        print(f"{O}[*]API_refrance  ...........|Using RapidDNS API{s}")
            except Exception:
                pass
        if not subdomains:
            print(f"\n[*]MainDomain ...........| {domain}/")
            print("[*]MainDomain ...........| No subdomains found.")
            return []
        results = []
        for sub in sorted(set(subdomains)):
            try:
                socket.setdefaulttimeout(2)
                ip = socket.gethostbyname(sub)
                results.append((sub, ip))
            except Exception:
                continue
        if results:
            with open(".Sdomain", "w") as f:
                pass
            print(f"\n[*]MainDomain ...........| {domain}/")
            with open(".Sdomain", "a+") as f:
                f.write(f"[*]MainDomain ...........| {domain}\n")
                for sub, ip in results:
                    time.sleep(.20)
                    print(f"[+]Sub-Domain ...........| https://{sub:<50} ---------| {ip}")
                    f.write(f"[+]Sub-Domain ...........| https://{sub:<50} ---------| {ip}\n")
            return results
        else:
            print("[!] No valid subdomains with IPs found.")
            return []

if __name__ == "__main__":
    API_SubDomains_Scan()