import requests
import re
import socket
import time, timeit

R  = "\033[91m"
s  = "\033[0m"
O  = '\33[37m'

print(f"{R}\n=== Subdomain API Discovery {s}")
print('=' * 40)
print()


class API_SubDomains_Scan:

    def find_subdomains(self, **kwargs):
        if self.args.subapi:
            self.start = timeit.default_timer()
        else:
            pass

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
                    print(f"{O}[*] API Reference ..........| Hackertarget API used{s}")
        except Exception:
            pass
        if not subdomains:
            try:
                url = f"https://crt.sh/?q=%25.{domain}&output=json"
                resp = requests.get(url, timeout=10)
                if resp.status_code == 200:
                    try:
                        data = resp.json()
                        subdomains = list({entry["common_name"] for entry in data})
                        print(f"{O}[*] API Reference ..........| crt.sh API used{s}")
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
                        print(f"{O}[*] API Reference ..........| RapidDNS API used{s}")
            except Exception:
                pass
        if not subdomains:
            print(f"\n[*] Main Domain ...........| {domain}/")
            print("[*] Status ................| No subdomains were found.")
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
            print(f"\n[*] Main Domain  ...........| {domain}/")
            with open(".Sdomain", "a+") as f:
                f.write(f"[*] Main Domain  ...........| {domain}\n")
                for sub, ip in results:
                    self.count4 += 1
                    time.sleep(.20)
                    print(f"[+] Subdomain    ...........| https://{sub:<40} ---------| {ip}")
                    f.write(f"[+] Subdomain    ...........| https://{sub:<40} ---------| {ip}\n")
            return results
        else:
            print("[!] Status  ................| No valid subdomains with IPs found.")
            return []


if __name__ == "__main__":
    API_SubDomains_Scan()
