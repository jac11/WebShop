#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup , XMLParsedAsHTMLWarning
import argparse
import sys
import os
import urllib.parse
import re
import readline
import time,timeit
import json
import random
import socket
import warnings
import datetime

p  = "\033[96m"
R  = "\033[91m"
s  = "\033[0m"
O  ='\33[37m'  

class Shopping:
    def __init__(self):
        self.visited = set()
        self.hidden_links = set()
        self.wordlist = ["admin", "login", "test", "staging", "backup.zip"]      
        self.depth = 0
        self.headers = {"User-Agent": "Mozilla/5.0"}
        self.count1 = self.count2 = self.count3 = self.count4 = self.count5 = self.count6 = self.count7 = 0
        self.banner = R + f"""
          ██     ██ ███████ ██████  ███████ ██   ██  ██████  ██████  
          ██     ██ ██      ██   ██ ██      ██   ██ ██    ██ ██   ██ 
          ██  █  ██ █████   ██████  ███████ ███████ ██    ██ ██████  
          ██ ███ ██ ██      ██   ██      ██ ██   ██ ██    ██ ██      
           ███ ███  ███████ ██████  ███████ ██   ██  ██████  ██      
                                    """ + O + """@jacstory""" + s
    # Ensure clean print
        print(self.banner.strip() + '\n')
        self.control()
        self.main()  
    def APIKEY(self):

            self.start = timeit.default_timer()
            self.session = requests.Session()
            if not os.path.exists(".APIKEY.KEY") and not self.args.APIKEY:
                print("WHOIS INFORMATION\n")
                print("[+] API file   ............| No API key found\n")
                print(O + "[+] How to obtain a host.io API key".upper() + s)
                lines = [
                        
                        "_"*40,
                        "\n  1. Visit: https://host.io",
                        "  2. Sign up (GitHub or Google login is supported).",
                        "  3. After signing in, open your dashboard.",
                        "  4. Copy your API key (token).",
                        "  5. Provide it to the script as follows:",
                        "_"*40,
                        "\n  Usage: python webshop_p3.py -K YOUR_API_KEY",
                        "_"*40,
                        "\nIMPORTANT NOTES:",
                        "_"*40,
                        "\n   - Free accounts have limited daily requests.",
                        "   - Paid plans offer higher limits and more detailed data.\n",
                        "_"*40
                    ]

                for line in lines:
                    print(R+line+s)
                    time.sleep(0.25) 
                             
            elif os.path.exists(".APIKEY.KEY") and self.args.APIKEY:   
                with open(".APIKEY.KEY", 'w') as key_file:
                    key_file.write(self.args.APIKEY)  
                print("\nAPI KEY INFORMATION\n")  
                print('[+] API Key     ............| ',self.args.APIKEY)
                print('[+] API key file............| ',"file:///.APIKEY.KEY") 
                print("="*30)
               
                
            else:
                with open(".APIKEY.KEY", 'r') as key_file:
                    self.args.APIKEY = key_file.read()
                self.output.writelines("\nAPI KEY INFORMATION\n")  
                self.output.writelines('[+] API Key     ............| '+self.args.APIKEY+"\n")
                self.output.writelines('[+] API key file............| '+"file:///.APIKEY.KEY\n") 
                self.output.writelines("="*30+"\n")

            def APIKEYCALL(self) :  
             #  pass
                
                if self.args.APIKEY :     
                    with open('.APIKEY.KEY', 'r') as key_file:
                        key = key_file.read().strip()
                    DominCheck = self.args.URL.split('//')[1].replace("www.","")  
                    url = f"https://host.io/api/full/{DominCheck.replace('/','')}?token={key}"

                    headers = {
                         "User-Agent": "curl/7.68.0"}
                    
                    response = self.session.get(url, headers=headers)
              
                    if response.status_code == 200:
                        if 'application/json' in response.headers.get('Content-Type', ''):
                            data = response.json()
                             # Parse JSON
                        else:
                            header_html = BeautifulSoup(response.content, 'lxml')
                            data = header_html.prettify()
                            
                        time.sleep(.30)        
                    try:        
                        print(f"{R}\nWHOIS INFORMATION\n{s}")
                        print("="*30)
                        print(f"{O}\nDomain information{s}")
                        print("_"*15+'\n')
                        self.output.writelines("\nWHOIS INFORMATION")
                        self.output.writelines("\n"+"="*30+"\n")
                        self.output.writelines("\nDomain information"+"\n")
                        self.output.writelines("_"*15+'\n\n')
                        time.sleep(0.25)
                        print('   [+] Main domain   ............| ',data['domain'])
                        self.output.writelines('   [+] Main domain   ............| '+ data['domain']+'\n')
                        time.sleep(0.25)
                        print('   [+] URL           ............| ', self.args.URL)
                        self.output.writelines('   [+] URL           ............| '+  self.args.URL+'\n')
                        time.sleep(0.25)
                        print('   [+] Rank          ............| ', data['web']['rank'])
                        self.output.writelines('   [+] Rank          ............| '+ str(data['web']['rank'])+'\n')
                        time.sleep(0.25)
                        print('   [+] GTM           ............| ', data['web']['gtm']) 
                        self.output.writelines('   [+] GTM           ............| '+ data['web']['gtm']+'\n')   
                    except UnboundLocalError:
                            print('   [+] Main domain    ............| ',self.args.URL)
                            print('   [+] API key status...........| Failed to retrieve WHOIS information')
                            print("_"*15+'\n')
                            self.output.writelines('   [+] Main domain    ............| '+self.args.URL)
                            self.output.writelines('   [+] API key status...........| Failed to retrieve WHOIS information')
                            self.output.writelines("_"*15+'\n')
                    except KeyError:
                         pass
                    try:
                                 
                        print(f"{O}\nIP information{s}") 
                        self.output.writelines("\nIP information\n")
                        print("_"*15+'\n')  
                        self.output.writelines("_"*15+'\n\n')
                        time.sleep(0.25)
                        print('   [+] IP address    ............| ',data['dns']['a'][0])
                        self.output.writelines('   [+] IP address    ............| '+data['dns']['a'][0]+'\n')
                        time.sleep(0.25)
                        print('   [+] City          ............| ',data['ipinfo'][data['dns']['a'][0]]['city'])
                        self.output.writelines('   [+] City          ............| '+data['ipinfo'][data['dns']['a'][0]]['city']+'\n')
                        time.sleep(0.25)
                        print('   [+] Country       ............| ',data['ipinfo'][data['dns']['a'][0]]['country'])
                        self.output.writelines('   [+] Country       ............| '+data['ipinfo'][data['dns']['a'][0]]['country']+'\n')
                        time.sleep(0.25)
                        print('   [+] Hosting       ............| ',data['ipinfo'][data['dns']['a'][0]]['asn']['domain'])
                        self.output.writelines('   [+] Hosting       ............| '+data['ipinfo'][data['dns']['a'][0]]['asn']['domain']+'\n')
                        time.sleep(0.25)
                        print('   [+] Route         ............| ',data['ipinfo'][data['dns']['a'][0]]['asn']['route'])
                        self.output.writelines('   [+] Route         ............| '+data['ipinfo'][data['dns']['a'][0]]['asn']['route']+'\n')
                        time.sleep(0.25)
                        print('   [+] ASN type      ............| ',data['ipinfo'][data['dns']['a'][0]]['asn']['type'])
                        self.output.writelines('   [+] ASN type      ............| '+data['ipinfo'][data['dns']['a'][0]]['asn']['type']+'\n')
                    except KeyError:
                         pass  
                    except UnboundLocalError :
                        print('   [+] API key status...........| Failed to retrieve IP information')
                        print("_"*15+'\n')
                        self.output.writelines('   [+] API key status...........| Failed to retrieve IP information')
                        self.output.writelines("_"*15+'\n')     
                    try:     
                        print(f"{O}\nDNS information{s}") 
                        self.output.writelines("\nDNS information\n")
                        print("_"*15 + '\n\n')
                        self.output.writelines("_"*15 + '\n\n')
                        for  dns in data['dns']['mx']:
                            time.sleep(0.25)
                            print('   [+] MX record    ............| ', dns[0:-1])
                            self.output.writelines('   [+] MX record    ............| '+ dns[0:-1]+'\n')
                        for  dns in data['dns']['ns']:
                            print('   [+] NS record    ............| ', dns[0:-1]) 
                            self.output.writelines('   [+] NS record    ............| '+ dns[0:-1]+'\n')
                            time.sleep(0.25)   
                    except KeyError:
                         pass   
                    except UnboundLocalError :  
                        print('   [+] API key status...........| Failed to retrieve DNS information')
                        print("_"*15+'\n')
                        self.output.writelines('   [+] API key status...........| Failed to retrieve DNS information')
                        self.output.writelines("_"*15+'\n')   
                    try :        
                        print(f"{O}\nSocial media links{s}")
                        self.output.writelines("\nSocial media links\n")
                        print("_"*15+'\n') 
                        self.output.writelines("_"*15+'\n\n')   
                        for  web in data['web']['links']:
                            time.sleep(.25)
                            print('   [+] Link         ............| '+ web) 
                            self.output.writelines('   [+] Link         ............| '+ web+'\n') 
                        print("_"*15+'\n')
                        self.output.writelines("_"*15+'\n')  
                    except KeyError:
                         pass
                    except UnboundLocalError:
                        print('   [+] API key status...........| Failed to retrieve social media information')
                        print("_"*15+'\n')
                        self.output.writelines('   [+] API key status...........| Failed to retrieve social media information')
                        self.output.writelines("_"*15+'\n')  
                else:
                    pass  
                             
            APIKEYCALL(self)
          
    def extract_links_form(self):
       
        try:
            self.session = requests.Session()  
            self.target_url = self.args.URL
            if '/' not in self.target_url[-1]:
                self.target_url = self.target_url + '/'           
            else:
                pass
            self.target_links = []
            headers = {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                        }
            try:
                response = self.session.get(self.target_url,headers=headers) 

                if response.ok:
                    return re.findall('(?:href=")(.*?)"', str(response.content))  
                else:
                    print("="*25)
                    self.output.writelines("[-]link ..........| No links discovered\n" + "="*25)
                    self.output.writelines("[*]input  ...........| " + self.target_url + '\n')  
                    print('[-] No links discovered.')
                    print("[&] Note: This website may require authentication to extract information.")
                    exit()

            except requests.exceptions.ConnectionError:
                print("="*25)
                print("[-] Connection error: The server closed the connection unexpectedly.")
                exit()
            

        except KeyboardInterrupt:
            print(self.banner)
            exit()

    def discover_link(self, url, depth=0):
        all_Links = set()   
        seen_links = getattr(self, "seen_links", set())
        self.seen_links = seen_links
        try:
            if self.args.email :
                print(f"{R}\nEMAIL DISCOVERY{s}")
                print("=" * 25)
                output_14 = self.output.write('\n' + "EMAIL DISCOVERY " + '\n' + '=' * 25 + '\n') 

            else:    
                self.output.writelines("\nDISCOVERED LINKS\n" + "="*25 + "\n")
                print(f"{R}\nDISCOVERED LINKS (static structure) {s}")
                print("="*25 + "\n")
            herf_links = self.extract_links_form()
            if not self.args.email:
                for link in herf_links:
                    link = urllib.parse.urljoin(str(self.target_url), str(link))
                    if "#" in link:
                        link = link.split('#')[0]
                    norm_link = link.strip().rstrip("/")
                    if self.target_url in link and norm_link not in self.target_links and norm_link not in seen_links:
                        seen_links.add(norm_link)
                        self.target_links.append(norm_link)
                        try:
                            resp = self.session.get(norm_link, headers=self.headers, timeout=5)
                            code = str(resp.status_code)
                        except:
                            code = "ERR"
                        if code == "200":
                            code_fmt = f"{O}[{code}]{s}"
                        else:
                            code_fmt = f"{R}[{code}]{s}"
                        self.count1 += 1
                        all_Links.add(norm_link)
                        print(f"[+] Link {code_fmt} ...........| {norm_link}")
                        self.output.writelines(f"[+] Link  {code} ...........| {norm_link}\n")
                with open(".data.txt", "w") as file_links:
                    file_links.writelines("%s\n" % i for i in self.target_links)
            else:
                for link in herf_links:
                    link = urllib.parse.urljoin(str(self.target_url), str(link))
                    if "#" in link:
                        link = link.split('#')[0]
                    norm_link = link.strip().rstrip("/")
                    if self.target_url in link and norm_link not in self.target_links and norm_link not in seen_links:
                        seen_links.add(norm_link)
                        self.target_links.append(norm_link)
                        try:
                            resp = self.session.get(norm_link, headers=self.headers, timeout=5) 
                        except:
                          continue  
                with open(".data.txt", "w") as file_links:
                    file_links.writelines("%s\n" % i for i in self.target_links)            
                self.Email_Scan()
                self.print_summary()   
                self.output.close() 
                if self.args.pdf:
                    from pdfout import PDF_OUT
                    pdf = PDF_OUT()
                    txt_file = "Webshop_" + self.resreach.group(1) + ".txt"
                    pdf_file = txt_file.replace(".txt", ".pdf")
                    pdf.txt_to_pdf(txt_file, pdf_file)
                    os.remove(txt_file)
                    exit()
                exit()               
            self.output.writelines("\nHIDDEN LINKS\n" + "="*25 + "\n")
            print(f"{R}\nHIDDEN LINKS {s}")
            print("="*25 + "\n")
            html_re = self.session.get(url, headers=self.headers, timeout=10)
            html = html_re.text
            if depth > self.depth or url in self.visited:
                return
            self.visited.add(url)
            if not html:
                return
            soup = BeautifulSoup(html, "html.parser")
            for link in soup.find_all("a", href=True):
                href = link["href"]
                if href.startswith("/"):
                    full = urllib.parse.urljoin(url, href)
                elif href.startswith("http"):
                    full = href
                else:
                    continue
                norm_full = full.strip().rstrip("/")
                if norm_full not in seen_links:
                    seen_links.add(norm_full)
                    try:
                        resp = self.session.get(norm_full, headers=self.headers, timeout=5)
                        code = str(resp.status_code)
                    except:
                        code = "ERR"
                    if code == "200":
                        code_fmt = f"{O}[{code}]{s}"
                    else:
                        code_fmt = f"{R}[{code}]{s}"
                    self.count2 += 1
                    all_Links.add(norm_full)
                    print(f"[+] Link {code_fmt} ...........| {norm_full}")
                    self.output.writelines(f"[+] Link  {code} ...........| {norm_full}\n")

            self.output.writelines("\nJAVASCRIPT FILES\n" + "="*25 + "\n")
            print(f"{R}\nJAVASCRIPT FILES {s}")
            print("="*25 + "\n")
            for script in soup.find_all("script", src=True):
                src = script["src"]
                if src.startswith("/"):
                    js_url = urllib.parse.urljoin(url, src)
                elif src.startswith("http"):
                    js_url = src
                else:
                    continue
                norm_js = js_url.strip().rstrip("/")
                if norm_js not in seen_links:
                    seen_links.add(norm_js)
                    try:
                        resp = self.session.get(norm_js, headers=self.headers, timeout=5)
                        code = str(resp.status_code)
                    except:
                        code = "ERR"
                    if code == "200":
                        code_fmt = f"{O}[{code}]{s}"
                    else:
                        code_fmt = f"{R}[{code}]{s}"
                    self.count3 += 1
                    all_Links.add(norm_js)
                    print(f"[+] File {code_fmt} ...........| {norm_js}")
                    self.output.writelines(f"[+] File  {code} ...........| {norm_js}\n")

            self.output.writelines("\nAPI ENDPOINTS\n" + "="*25 + "\n")
            print(f"{R}\nAPI ENDPOINTS {s}")
            print("="*25 + "\n")
            self.output.writelines("\nAPI ENDPOINTS\n" + "="*25 + "\n")

            def is_valid_api(url):
                  
                invalid = ['`', '${', '};', '?token=', '?key=', 'example', 'localhost', '127.0.0.1', '</', '<a', 'href=']
                if any(indicator in url.lower() for indicator in invalid):
                    return False
                
                static_files = ['.js', '.css', '.png', '.jpg', '.jpeg', '.gif', '.svg', '.ico']
                if any(url.lower().endswith(ext) for ext in static_files):
                    return False
                
                api_keywords = ['/api/', '/v1/', '/v2/', '/v3/', '/rest/', '/graphql/', '-api']
                return any(keyword in url.lower() for keyword in api_keywords)

            seen_apis = set()

            for page in all_Links:
                try:
                    resp = self.session.get(page, headers=self.headers, timeout=10)
                    html = resp.text
                    base_domain = '/'.join(page.split('/')[:3])
                    
                    patterns = [
                        r'https?://[a-zA-Z0-9.-]+[^"\']*api[^"\']*',
                        r'https?://[a-zA-Z0-9.-]+/api/[a-zA-Z0-9/_-]+',
                        r'https?://[a-zA-Z0-9.-]+/v\d+/[a-zA-Z0-9/_-]+',
                        r'["\'](/[a-zA-Z0-9_-]*/api/[a-zA-Z0-9/_-]+)["\']',
                        r'["\'](/[a-zA-Z0-9_-]*/v\d+/[a-zA-Z0-9/_-]+)["\']'
                    ]
                    
                    for pattern in patterns:
                        matches = re.findall(pattern, html, re.IGNORECASE)
                        for api in matches:
                            if api.startswith('/'):
                                full_url = base_domain + api
                            else:
                                full_url = api
                            
                            if full_url not in seen_apis and is_valid_api(full_url):
                                seen_apis.add(full_url)
                                norm_api = full_url.strip().rstrip("/")
                                
                                try:
                                    r = requests.get(norm_api, headers=self.headers, timeout=5)
                                    code = str(r.status_code)
                                    content_type = r.headers.get("Content-Type", "").lower()
                                    
                                    if "application/json" in content_type:
                                        tag = f"{p}[JSON]{s}"
                                        self.count6 += 1
                                    elif any(x in content_type for x in ['xml', 'text/plain']):
                                        tag = f"{O}[Text]{s}"
                                        self.count6 += 1
                                    else:
                                        continue
                                    if "200" in code:
                                        code_fmt = f"{O}[{code}]{s}"
                                    else:
                                        code_fmt = f"{R}[{code}]{s}"    
                                    print(f"{tag} link {code_fmt} ...........| {norm_api}")
                                    self.output.writelines(f"{tag} link  {code} ...........| {norm_api}\n")
                                    time.sleep(0.15)
                                    
                                except Exception:
                                    continue
                except Exception as e:
                  continue
        except requests.exceptions.ConnectionError:
           print("[-] Error: Connection error — the server closed the connection.")
           return
        except KeyboardInterrupt:
            print(self.banner)
            exit()
    def form_Check(self):
        countform = 0

        warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)
        try:
            self.output.write("\nFORMS FOUND\n" + '\n' + '='*25 + '\n')
            try:
                with open('.data.txt', 'r') as read_line:
                    self.line_read = read_line.readlines()
                    print(f"{R}\nFORM DISCOVERY {s}")
                    print('='*25)
                    print()
                    unique_actions = set()
                    for self.line in self.line_read:
                        time.sleep(0.25)
                        try:
                            response = self.session.get(self.line, timeout=(0.2, 5))
                            header_html = BeautifulSoup(response.content, 'lxml')
                        except Exception:
                            try:
                                response = self.session.get(self.line, allow_redirects=False, timeout=(0.2, 5))
                                header_html = BeautifulSoup(response.content, 'lxml')
                            except Exception :
                                self.replace = self.line.replace('\n', '')
                                print(f"[*] URL ...........| {self.replace}")
                                print("[*] Form ..........| No form found")
                                sys.stdout.write('\x1b[1A'); sys.stdout.write('\x1b[2K')
                                sys.stdout.write('\x1b[1A'); sys.stdout.write('\x1b[2K')
                        try:      
                            if not response.ok:
                                self.replace = self.line.replace('\n', '')
                                print(f"[*] URL ...........| {self.replace}")
                                print("[*] Form ..........| No form found")
                                sys.stdout.write('\x1b[1A'); sys.stdout.write('\x1b[2K')
                                sys.stdout.write('\x1b[1A'); sys.stdout.write('\x1b[2K')
                        except UnboundLocalError :        
                            continue
                        try:   
                  
                            form_list = header_html.find_all('form')
                            self.list_input = header_html.find_all('input')
                            for form in form_list:
                                self.action = form.get('action')
                                if self.action and self.action not in unique_actions:
                                    unique_actions.add(self.action)
                                    self.url_path = urllib.parse.urljoin(self.line, self.action)
                                    self.method = form.get('method')
                                    self.output.writelines('\n' + "FORM DETAILS\n" + '='*25 + '\n')
                                    self.output.writelines(f"[+] URL    ..........| {self.line}")
                                    self.output.writelines(f"[*] action ..........| {self.url_path}\n")
                                    self.output.writelines(f"[*] method ..........| {str(self.method)}\n")
                                    print(f"[+] URL    ..........| {self.line}".replace('\n',''))
                                    print(f"[*] Action ..........| {self.url_path}")
                                    print(f"[*] Method ..........| {self.method}")
                                    print(f"{O}\nForm details"+'\n'+'_'*12+f'\n{s}')
                                    self.output.writelines("\nForm details"+'\n'+'_'*12+'\n')
                                    for input in self.list_input:
                                        self.input_get = input.get('name')
                                        self.type = input.get('type')
                                        self.value = input.get('value')
                                        countform += 1
                                        self.output.writelines(f"    [*] Input name ...........| {str(self.input_get)}\n")
                                        self.output.writelines(f"    [*] Type       ...........| {str(self.type)}\n")
                                        self.output.writelines(f"    [*] Default    ...........| {str(self.value)}\n")
                                        print(f"    [*] Input name ...........| {self.input_get}")
                                        print(f"    [*] Type       ...........| {self.type}")
                                        print(f"    [*] Default    ...........| {self.value}")
                                    print('\n'+'='*25+'\n')    
                            else:
                                self.replace = self.line.replace('\n', '')
                                print(f"[*] URL ...........| {self.replace}")
                                print("[*] Form ..........| No form found")
                                sys.stdout.write('\x1b[1A'); sys.stdout.write('\x1b[2K')
                                sys.stdout.write('\x1b[1A'); sys.stdout.write('\x1b[2K')
                        except UnboundLocalError :    
                            self.replace = self.line.replace('\n', '')
                            print(f"[*] URL ...........| {self.replace}")
                            print("[*] Form ..........| No form found")
                            sys.stdout.write('\x1b[1A'); sys.stdout.write('\x1b[2K')
                            sys.stdout.write('\x1b[1A'); sys.stdout.write('\x1b[2K')    
                        
                    if countform == 0:
                        print("[*] Status ...........| No forms were discovered")
            except KeyboardInterrupt:
                print(self.banner)
                exit()
        except requests.exceptions.ConnectionError:
            print("[-] Connection error: the target server appears to be down.")
            pass
        except KeyboardInterrupt:
            print(self.banner)
            exit()
                      
    def sub_domain(self):   
        try:
            print(f"{R}\nSUBDOMAIN DISCOVERY{s}")
            print('='*25)
            print()
            self.target_url = self.args.URL
            output_11 = self.output.write('\n' + "SUBDOMAIN DISCOVERY" + '\n' + '='*25 + '\n')
            if 'http://' in self.target_url:      
                url_replase = self.target_url.replace('http://', '')
            elif 'https://' in self.target_url: 
                url_replase = self.target_url.replace('https://', '')
            if 'www.' in self.target_url: 
                url_replase = url_replase.replace('www.', '')
            print ('[*] Main domain  ...........|', url_replase)
            output_12 = self.output.write('[*] Main domain  ...........| ' + url_replase + '\n')
            try:
                if not self.args.wordlist:
                    wordlist = "./small_list.txt"
                else:    
                    wordlist = self.args.wordlist
                with open(wordlist, 'r') as sub_read:
                    content = sub_read.read()
                    subdomain = content.splitlines()
            except IOError:
                print("[*] Error: Specified wordlist file does not exist.")
                exit()
            for sub in subdomain:
                if "https://" in self.args.URL:
                    sub_domain_url = 'https://', sub, '.', url_replase
                    sub_domain_url_join = ''.join(sub_domain_url)
                elif "http://" in self.args.URL:
                    sub_domain_url = 'http://', sub, '.', url_replase
                    sub_domain_url_join = ''.join(sub_domain_url)
                try:
                    if "/" in sub_domain_url_join[-1]:
                        sub_domain_url_join = sub_domain_url_join[0:-1]
                    else:
                        sub_domain_url_join = sub_domain_url_join   
                    try:    
                        requests.get(sub_domain_url_join, timeout=3)
                    except Exception:
                        continue    
                except requests.ConnectionError:
                    print("[+] Unreachable  ...........|", sub_domain_url_join)
                    sys.stdout.write('\x1b[1A')
                    sys.stdout.write('\x1b[2K')
                else:
                    try:
                        socket.setdefaulttimeout(1)
                        SubIp = socket.gethostbyname(sub_domain_url_join.replace("https://",""))
                    except Exception :
                       print("[+] Subdomain lookup failed ...........|", sub_domain_url_join)
                       sys.stdout.write('\x1b[1A')
                       sys.stdout.write('\x1b[2K')
                    else:  
                        self.count4 +=1 
                        print("[+] Subdomain    ...........| "+f'{sub_domain_url_join:<35}',f'{"---------|":>15}', SubIp)
                        output_13 = self.output.writelines("[+] Subdomain   ...........| "+f'{sub_domain_url_join:<35}'+f'{"---------| ":>15}'+SubIp+'\n')
                        list_domain = []
                        if sub_domain_url_join not in list_domain:
                            list_domain.append(sub_domain_url_join)
                            string_list = ''.join(list_domain)
                        with open('.domain', 'a') as append_list:
                            append_list.write(string_list + '\n')
        except KeyboardInterrupt:
            print(self.banner)
            exit()
        except requests.exceptions.ConnectionError:
            print("[-] Connection error: the server closed the connection.")
            exit()
    def Email_Scan(self):
        try:
            with open('.data.txt', 'r') as read_line:
                self.line_read = read_line.readlines()
            if self.args.email:
               pass 
            else:        
                print(f"{R}\nEMAIL DISCOVERY{s}")
                print("=" * 25)
                output_14 = self.output.write('\n' + "EMAIL DISCOVERY " + '\n' + '=' * 25 + '\n')
            email_list = []
            for self.line in self.line_read:
                replace_spaces = self.line.strip()
                try:
                    response = requests.get(replace_spaces)
                    emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}", str(response.content))
                    for email in emails:
                        if not email.endswith(('.png', '.jpg', '.jpeg', '.gif', '.zip')):
                            if email not in email_list:
                                email_list.append(email)
                                print("[+] Email found    ...........| ", email)
                                self.count5 +=1
                                output_13 = self.output.writelines("[+] Email found ...........| " + email + '\n')
                except requests.exceptions.ConnectionError:
                    print("[-] Connection error: the server closed the connection.")
                    continue  
                if not emails:
                    list_of_messages = ['... please wait ...', '... scanning ...', '... email scan in progress ...']
                    random_message = random.choice(list_of_messages)
                    print("[+] Email Scaning  ...........| ", random_message)
                    sys.stdout.write('\x1b[1A')
                    sys.stdout.write('\x1b[2K')

            output_20 = self.output.write("[-] Email scan completed" + '\n')
        except KeyboardInterrupt:
            print(self.banner)
            exit()
    def robotstxt_read(self):
        print(f"{R}\nROBOTS.TXT DISCOVERY{s}")
        print("="*25)
        num = 0 
        try:
            with open('.domain', 'r') as read_line_sub:
                if self.args.URL not in read_line_sub:
                   self.line_domain = read_line_sub.readlines()
                   self.line_domain.append(self.args.URL)
                else:
                    self.line_domain = read_line_sub.readlines()
                output_15 = self.output.write('\n' + "ROBOTS.TXT DISCOVERY" + '\n' + '=' * 25 + '\n')
            for robots in self.line_domain:
                self.link_robot = urllib.parse.urljoin(robots, '/robots.txt')
                self.link_robot_str = str(self.link_robot)
                response_robots = requests.get(self.link_robot, data=None)
               # Beautiful_robots = str(BeautifulSoup(response_robots.content, 'lxml'))
                with open (".2",'w') as code :
                     code.write(str(response_robots.content))

                with open(".2",'r') as code:
                    Beautiful_robots = code.readlines()
                for Parse in Beautiful_robots:
                    if "Disallow:" in Parse:
                        num +=1
                        Parse = Parse.replace('<html>', '').replace('</body>', '').replace('<body>', '').replace('<p>', '').replace('</p>', '')
                        Beautiful_robots1 = "\n".join(Parse.replace('</html>', '').replace("b'",'').replace("'",'').split("\\n"))
                        output_15 = self.output.write('\n' + "ROBOTS.TXT DISCOVERY" + '\n' + '=' * 25 + '\n')
                        print("[*] File URL ..........|", self.link_robot+'\n')
                        print(('*' * 30))
                        print(Beautiful_robots1)
                        print(('*' * 30))
                        output_16 = self.output.write("[*] File URL ..........| " + self.link_robot + '\n' + '*' * 25 + '\n')
                        output_17 = self.output.writelines(Beautiful_robots1 + '\n' + '*' * 25 + '\n')
                        #links = set(re.findall(r'(?<=Disallow:\s).*|(?<=Allow:\s).*', Beautiful_robots1) )
                        links = set(re.findall(r'^(?:Disallow|Allow|Sitemap):\s*(\S+)', Beautiful_robots1 , re.MULTILINE))
                        
                        print(O+"\nRobots.txt details"+'\n'+'_'*12+s+'\n')
                        self.output.writelines("\nRobots.txt details"+'\n'+'_'*12+'\n\n')
                        for data in links :
                            if 'User-agent: *' in data  or 'user-agent: *' in data:
                                pass
                            if self.args.URL in data:
                                time.sleep(.20)
                                print("   [*] Path ..........|", data.strip().replace('\n',''))
                                output_17 = self.output.writelines(f"    [*] Path ..........| {data.strip().replace('\n','')}\n")

                            else:    
                                time.sleep(.20)
                                print("   [*] Path ..........|", self.args.URL+data.strip().replace('\n',''))
                                output_17 = self.output.writelines(f"    [*] Path ..........| {self.args.URL+data.strip().replace('\n','')}\n")
                                self.count7 +=1
                        print(O+'_'*30+s+'\n')
                    else:
                        print("[+] No robots.txt entries detected at", self.link_robot )
                        sys.stdout.write('\x1b[1A')
                        sys.stdout.write('\x1b[2K')

            else:
                if num == 0 :
                     print("\n[*] robots.txt ..........| No robots.txt file found")
                output_21 = self.output.write('\n' + "[*] robots.txt ..........| robots.txt scan complete  " + '\n')
                try:
                    if os.path.isfile(".domain"):
                        os.remove(".domain")
                    if os.path.isfile('.data.txt'):
                        os.remove('.data.txt') 
                    if os.path.isfile(".2"):      
                        os.remove(".2")  
                   
                except IOError:
                    pass
        except KeyboardInterrupt:
            print(self.banner)
            exit()
        except IOError:
            print(f"{R}\nROBOTS.TXT DISCOVERY{s}")
            print("=" * 25)
            print("[-] robots.txt ..........| No robots.txt discovered")
            exit()
        except requests.exceptions.ConnectionError:
            print("[-] Connection error: the server closed the connection.")
            pass
    def control(self):
        parser = argparse.ArgumentParser(
        description="WebShop: Subdomain and Email Discovery Tool\n\n"
                    "Modes:\n"
                    "  1. Scan Mode → requires --URL\n"
                    "  2. API Key Mode → only -K is needed\n",
        formatter_class=argparse.RawTextHelpFormatter
    )
        
        scan_group = parser.add_argument("--man",action="store_true",
            help="display man page")
        scan_group = parser.add_argument_group("Scan Options",
            "Options for scanning a target domain (require --URL).")
        apikey_group = parser.add_argument_group("API Key Options",
            "Options for managing/storing API keys.")
        apikey_group.add_argument("-K", "--APIKEY",
            help="API key for domain analysis (optional in scans, "
                 "or can be used alone to just store the key)")
        scan_group.add_argument("--URL",
            help="Target website URL (e.g., https://www.example.com)")
        scan_group.add_argument("-w", "--wordlist",
            help="Path to wordlist file for subdomain brute-force discovery")
        scan_group.add_argument("-E", "--email", action="store_true",
            help="Discover email addresses from the target domain")
        scan_group.add_argument("-S", "--subdomain", action="store_true",
            help="Discover subdomains using a wordlist")
        scan_group.add_argument("-a", "--all", action="store_true",
            help="Run all discovery modules (subdomains, emails, APIs).\n"
                 "If combined with --api, wordlist-based subdomain discovery is skipped.")
        scan_group.add_argument("-R", "--robots", action="store_true",
            help="Discover robots.txt file.\n"
                 "If combined with --api, wordlist-based subdomain discovery is skipped.")
        scan_group.add_argument("--api", action="store_true",
            help="Use API-based subdomain discovery (crt.sh, RapidDNS, Hackertarget).\n"
                 "When used with --all, disables wordlist brute-force and only uses APIs.")
        scan_group.add_argument("-s", "--subapi", action="store_true",
            help="Fetch subdomains specifically using the crt.sh, RapidDNS, Hackertarget API")
        scan_group.add_argument("--pdf", action="store_true",
            help="Generate output report in PDF format")
        self.args = parser.parse_args()
        scanning_opts = any([  self.args.pdf,self.args.wordlist, 
                               self.args.email, self.args.api,
                               self.args.subdomain, self.args.all,
                               self.args.subapi,self.args.robots]
                            )
        if scanning_opts and not self.args.URL:
            parser.error("--URL is required when running scans")

        if len(sys.argv) != 1:
            pass
        else:
            parser.print_help()
            exit()
    def print_summary(self):
        today = datetime.date.today().strftime("%Y-%m-%d")
        stop = timeit.default_timer()
        sec = stop  - self.start
        start_str = time.strftime("%H:%M:%S",time.gmtime(self.start))
        stop_str = time.strftime("%H:%M:%S",time.gmtime(stop))
        fix_time = time.gmtime(sec)
        Tresult = time.strftime("%H:%M:%S",fix_time)
        self.summary = (
        O+"\n" + "="*40 + "\n" +
        R+"📊  Scan Summary Report\n" +
        O+"="*40 + "\n" +
        f"📅 Date                 : {today}\n"+
        f"🟢 Scan started         : {start_str}\n"+
        f"🔴 Scan finished        : {stop_str}\n"+
        f"🕦 Total duration       : {Tresult}\n"+
        O+"_"*30+'\n\n'+
        f"{R}[+] Static links found  : {O} {self.count1}\n" +
        f"{R}[+] Hidden links found  : {O} {self.count2}\n" +
        f"{R}[+] JS files discovered : {O} {self.count3}\n" +
        f"{R}[+] Subdomains found    : {O} {self.count4}\n" +
        f"{R}[+] Emails found        : {O} {self.count5}\n" +
        f"{R}[+] API endpoints found : {O} {self.count6}\n" +
        f"{R}[+] Robots.txt entries  : {O} {self.count7}\n" +
        O+"="*40 + "\n" +
        R+"✅ Scan completed successfully\n" +
        O+"="*40+s + "\n"
        )
        print(self.summary)
        if self.args.pdf:
            print("[+] Report saved to........| file://"+os.getcwd()+"/Webshop_"+str(self.resreach.group(1))+".pdf")  
        else:
             print("[+] Report saved to........| file://"+os.getcwd()+"/Webshop_"+str(self.resreach.group(1))+".txt")  
        print(self.banner)
        output_A = self.output.writelines('\n\n'+str(self.summary.\
        replace(f"{O}",'').replace(f"{R}",'').replace(f"{s}",''))+ self.banner.replace(f'{R}','')\
        .replace(f'{s}','').replace(f"{O}",'')+"\n" + "=" * 25)
        
        
    def main(self):
        if self.args.man:
           from info import  ManPage
           ManPage()
           exit()
        if self.args.APIKEY :
            self.APIKEY()
            exit()
        if not  self.args.URL.startswith("http") :
           self.args.URL =self.args.URL.replace("www.",'')
           self.args.URL = f"http://{self.args.URL}"

        pattern = r"https?://(?:www\.)?(?:[a-zA-Z0-9-]+\.)?([a-zA-Z0-9-]+)\."
        self.resreach = re.search(pattern , self.args.URL)
        self.output = open(str("Webshop_"+self.resreach.group(1))+".txt", 'w')
        self.output.writelines('\n' + self.banner + '\n')
        if os.path.isfile(".domain"):
            os.remove(".domain")
        if os.path.isfile(".2"):     
           os.remove(".2")
        with open(".data.txt",'w') as data:
            with open('.domain','w') as domain:
                pass 
        if self.args.robots:
            self.robotstxt_read() 
            exit()
        self.APIKEY()
        if self.args.all:           
            self.extract_links_form()
            self.discover_link(self.args.URL)
            self.form_Check()
            self.Email_Scan()
            if self.args.api :
                from SubAPI import API_SubDomains_Scan as API
                API.find_subdomains(self, args=self.control) 
                with open("./.Sdomain",'r') as readf:
                    readS = readf.read()
                output_C = self.output.writelines("\nSUBDOMAIN (API)\n"+'='*25+"\n"+readS+"\n")   
                os.remove("./.Sdomain") 
            else:    
                self.sub_domain() 
            self.robotstxt_read() 
            
        else:
            if self.args.email:
                self.extract_links_form()
                self.discover_link(self.args.URL)
                self.Email_Scan()
            elif self.args.subdomain:
                self.sub_domain()
            elif self.args.subapi:
                
                from SubAPI import API_SubDomains_Scan as API
                API.find_subdomains(self, args=self.control)
                with open("./.Sdomain",'r') as readf:
                    readS = readf.read()
                output_C = self.output.writelines("\nSUBDOMAIN (API)\n"+'='*25+"\n"+readS+"\n")  
                os.remove("./.Sdomain")
        
        self.print_summary()
        self.output.close() 
        if self.args.pdf:
            from pdfout import PDF_OUT
            pdf = PDF_OUT()
            txt_file = "Webshop_" + self.resreach.group(1) + ".txt"
            pdf_file = txt_file.replace(".txt", ".pdf")
            pdf.txt_to_pdf(txt_file, pdf_file)
            os.remove(txt_file)


if __name__ == "__main__":
    Shopping()
