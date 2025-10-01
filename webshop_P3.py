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
                print("###-WHOIS INFO\n")
                print("[+] API-File   ............| No APIKEY Found\n")
                print(O+"[+] How to Get a Host.io API Key".upper()+s)
                lines = [
                        
                        "_"*40,
                        "\n  1. Go to: https://host.io",
                        "  2. Click: Sign Up (GitHub or Google login works).",
                        "  3. After login: Open your Dashboard.",
                        "  4. Copy your API key (token).",
                        "  5. Use it in your script like this:",
                        "_"*40,
                        "\n  <Usage> python webshop_p3.py -K  YOUR_API_KEY <Usage> ",
                        "_"*40,
                        "\n⚠️  Notes:",
                        "_"*40,
                        "\n   - Free accounts: limited daily requests.",
                        "   - Paid plans: higher limits & detailed data.\n",
                        "_"*40
                    ]

                for line in lines:
                    print(R+line+s)
                    time.sleep(0.25) 
                             
            elif os.path.exists(".APIKEY.KEY") and self.args.APIKEY:   
                with open(".APIKEY.KEY", 'w') as key_file:
                    key_file.write(self.args.APIKEY)  
                print("\n###-API_INFO\n")  
                print('[+]APIKEY     ............| ',self.args.APIKEY)
                print('[+]API-File   ............| ',"file///.APIKEY.KEY") 
                print("="*30)
               
                
            else:
                with open(".APIKEY.KEY", 'r') as key_file:
                    self.args.APIKEY = key_file.read()
                self.output.writelines("\n###-API_INFO\n")  
                self.output.writelines('[+]APIKEY     ............| '+self.args.APIKEY+"\n")
                self.output.writelines('[+]API-File   ............| '+"file///.APIKEY.KEY\n") 
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
                        print(f"{R}\n###-WHOIS INFO\n{s}")
                        print("="*30)
                        print(f"{O}\nDomain-info{s}")
                        print("_"*15+'\n')
                        self.output.writelines("\n###-WHOIS INFO")
                        self.output.writelines("\n"+"="*30+"\n")
                        self.output.writelines("\nDomain-info"+"\n")
                        self.output.writelines("_"*15+'\n\n')
                        time.sleep(0.25)
                        print('   [+]MainDomain   ............| ',data['domain'])
                        self.output.writelines('   [+]MainDomain   ............| '+ data['domain']+'\n')
                        time.sleep(0.25)
                        print('   [+]URL          ............| ', self.args.URL)
                        self.output.writelines('   [+]URL          ............| '+  self.args.URL+'\n')
                        time.sleep(0.25)
                        print('   [+]Rank         ............| ', data['web']['rank'])
                        self.output.writelines('   [+]Rank         ............| '+ str(data['web']['rank'])+'\n')
                        time.sleep(0.25)
                        print('   [+]GTM          ............| ', data['web']['gtm']) 
                        self.output.writelines('   [+]GTM          ............| '+ data['web']['gtm']+'\n')   
                    except UnboundLocalError:
                            print('   [+]MainDomain     ............| ',self.args.URL)
                            print('   [+]APIKEY-Status   ............| Error Facth The ipinfo')
                            print("_"*15+'\n')
                            self.output.writelines('   [+]MainDomain     ............| '+self.args.URL)
                            self.output.writelines('   [+]APIKEY-Status   ............| Error Facth The ipinfo')
                            self.output.writelines("_"*15+'\n')
                    except KeyError:
                         pass
                    try:
                                 
                        print(f"{O}\nIp-info{s}") 
                        self.output.writelines("\nIp-info\n")
                        print("_"*15+'\n')  
                        self.output.writelines("_"*15+'\n\n')
                        time.sleep(0.25)
                        print('   [+]Ip-address   ............| ',data['dns']['a'][0])
                        self.output.writelines('   [+]Ip-address   ............| '+data['dns']['a'][0]+'\n')
                        time.sleep(0.25)
                        print('   [+]City         ............| ',data['ipinfo'][data['dns']['a'][0]]['city'])
                        self.output.writelines('   [+]City         ............| '+data['ipinfo'][data['dns']['a'][0]]['city']+'\n')
                        time.sleep(0.25)
                        print('   [+]Country      ............| ',data['ipinfo'][data['dns']['a'][0]]['country'])
                        self.output.writelines('   [+]Country      ............| '+data['ipinfo'][data['dns']['a'][0]]['country']+'\n')
                        time.sleep(0.25)
                        print('   [+]Server       ............| ',data['ipinfo'][data['dns']['a'][0]]['asn']['domain'])
                        self.output.writelines('   [+]Server       ............| '+data['ipinfo'][data['dns']['a'][0]]['asn']['domain']+'\n')
                        time.sleep(0.25)
                        print('   [+]Router       ............| ',data['ipinfo'][data['dns']['a'][0]]['asn']['route'])
                        self.output.writelines('   [+]Router       ............| '+data['ipinfo'][data['dns']['a'][0]]['asn']['route']+'\n')
                        time.sleep(0.25)
                        print('   [+]Type         ............| ',data['ipinfo'][data['dns']['a'][0]]['asn']['type'])
                        self.output.writelines('   [+]Type         ............| '+data['ipinfo'][data['dns']['a'][0]]['asn']['type']+'\n')
                    except KeyError:
                         pass  
                    except UnboundLocalError :
                        print('   [+]APIKEY-Status   ............| Error Facth The info')
                        print("_"*15+'\n')
                        self.output.writelines('   [+]APIKEY-Status   ............| Error Facth The info')
                        self.output.writelines("_"*15+'\n')     
                    try:     
                        print(f"{O}\nDNS-info{s}") 
                        self.output.writelines("\nDNS-info\n")
                        print("_"*15+'\n\n')
                        self.output.writelines("_"*15+'\n\n')
                        for  dns in data['dns']['mx']:
                            time.sleep(0.25)
                            print('   [+]MX           ............| ', dns[0:-1])
                            self.output.writelines('   [+]MX           ............| '+ dns[0:-1]+'\n')
                        for  dns in data['dns']['ns']:
                            print('   [+]NS           ............| ', dns[0:-1]) 
                            self.output.writelines('   [+]NS           ............| '+ dns[0:-1]+'\n')
                            time.sleep(0.25)   
                    except KeyError:
                         pass   
                    except UnboundLocalError :  
                        print('   [+]APIKEY-Status   ............| Error Facth The info')
                        print("_"*15+'\n')
                        self.output.writelines('   [+]APIKEY-Status   ............| Error Facth The info')
                        self.output.writelines("_"*15+'\n')   
                    try :        
                        print(f"{O}\nSocailMeddia-info{s}")
                        self.output.writelines("\nSocailMeddia-info\n")
                        print("_"*15+'\n') 
                        self.output.writelines("_"*15+'\n\n')   
                        for  web in data['web']['links']:
                            time.sleep(.25)
                            print('   [+]Meddia       ............| '+ web) 
                            self.output.writelines('   [+]Meddia       ............| '+ web+'\n') 
                        print("_"*15+'\n')
                        self.output.writelines("_"*15+'\n')  
                    except KeyError:
                         pass
                    except UnboundLocalError:
                        print('   [+]APIKEY-Status   ............| Error Facth The ipinfo')
                        print("_"*15+'\n')
                        self.output.writelines('   [+]APIKEY-Status   ............| Error Facth The info')
                        self.output.writelines("_"*15+'\n')  
                else:
                    pass  
                             
            APIKEYCALL(self)
          
    def extract_links_form(self,):
       
        try:
            self.session = requests.Session()  
            self.target_url = self.args.URL
            if '/' not in self.target_url[-1]:
                self.target_url = self.target_url + '/'           
            else:
                pass
            self.target_links = []
            try:
                response = self.session.get(self.target_url) 
                if response.ok:
                    return re.findall('(?:href=")(.*?)"', str(response.content))  
                else:
                    print("="*25)
                    self.output.writelines("[-]link ..........| No links Discover " + '\n' + "="*25)
                    self.output.writelines("[*]input  ...........| " + self.target_url + '\n')  
                    print('[-]link ..........| No links Discover ')
                    print("[&]web  ..........| This Website login required to grep information ")
                    exit()
            except requests.exceptions.ConnectionError:
                print("="*25)
                print("[-]Error  ..........| No status line received - the server has closed the connection")
                exit()
        except KeyboardInterrupt:
            print(self.banner)
            exit()

    def discover_link(self, url, depth=0):
        all_Links = set()   
        seen_links = getattr(self, "seen_links", set())
        self.seen_links = seen_links
        try:
            self.output.writelines("\n###-Discover links\n" + "="*25 + "\n")
            print(f"{R}\n###-Discover links static structure {s}")
            print("="*25 + "\n")
            herf_links = self.extract_links_form()
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
                    print(f"[+] link {code_fmt} ...........| {norm_link}")
                    self.output.writelines(f"[+] link  {code} ...........| {norm_link}\n")
            with open(".data.txt", "w") as file_links:
                file_links.writelines("%s\n" % i for i in self.target_links)
            self.output.writelines("\n###-Discover Hidden Links\n" + "="*25 + "\n")
            print(f"{R}\n###-Discover Hidden Links {s}")
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
                    print(f"[+] link {code_fmt} ...........| {norm_full}")
                    self.output.writelines(f"[+] link  {code} ...........| {norm_full}\n")

            self.output.writelines("\n###-Discover js Script\n" + "="*25 + "\n")
            print(f"{R}\n###-Discover js Script {s}")
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
                    print(f"[+] link {code_fmt} ...........| {norm_js}")
                    self.output.writelines(f"[+] link  {code} ...........| {norm_js}\n")

            self.output.writelines("\n###-Discover API Endpoints\n" + "="*25 + "\n")
            print(f"{R}\n###-Discover API Endpoints {s}")
            print("="*25 + "\n")
            self.output.writelines("\n###-Discover API Endpoints\n" + "="*25 + "\n")

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
                                        tag = "[Text]"
                                        self.count6 += 1
                                    else:
                                        continue
                                    
                                    code_fmt = f"{O}[{code}]{s}"
                                    print(f"{O}{tag}{s} link {code_fmt} ...........| {norm_api}")
                                    self.output.writelines(f"{O}{tag}{s} link  {code} ...........| {norm_api}\n")
                                    time.sleep(0.15)
                                    
                                except Exception:
                                    continue
                except Exception as e:
                  continue
        except requests.exceptions.ConnectionError:
           print("[-] Error: No status line received - the server closed the connection")
           return
        except KeyboardInterrupt:
            print(self.banner)
            exit()
    def form_Check(self):
        countform = 0

        warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)
        try:
            self.output.write("\n###-Discover Forms" + '\n' + '='*25 + '\n')
            try:
                with open('.data.txt', 'r') as read_line:
                    self.line_read = read_line.readlines()
                    print(f"{R}\n###-Discover Form {s}")
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
                                print(f"[*]link ...........| {self.replace}")
                                print("[*]Form ...........| No Form Discover")
                                sys.stdout.write('\x1b[1A'); sys.stdout.write('\x1b[2K')
                                sys.stdout.write('\x1b[1A'); sys.stdout.write('\x1b[2K')
                        try:      
                            if not response.ok:
                                self.replace = self.line.replace('\n', '')
                                print(f"[*]link ...........| {self.replace}")
                                print("[*]Form ...........| No Form Discover")
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
                                    self.output.writelines('\n' + "###-Discover Form " + '\n' + '='*25 + '\n')
                                    self.output.writelines(f"[+]link   ...........| {self.line}")
                                    self.output.writelines(f"[*]action ...........| {self.url_path}\n")
                                    self.output.writelines(f"[*]method ...........| {str(self.method)}\n")
                                    print(f"[+]link   ...........| {self.line}".replace('\n',''))
                                    print(f"[*]action ...........| {self.url_path}")
                                    print(f"[*]method ...........| {self.method}")
                                    print(f"{O}\nForm_Detalis"+'\n'+'_'*12+f'\n{s}')
                                    self.output.writelines("\nForm_Detalis"+'\n'+'_'*12+'\n')
                                    for input in self.list_input:
                                        self.input_get = input.get('name')
                                        self.type = input.get('type')
                                        self.value = input.get('value')
                                        countform += 1
                                        self.output.writelines(f"    [*]input     ...........| {str(self.input_get)}\n")
                                        self.output.writelines(f"    [*]type      ...........| {str(self.type)}\n")
                                        self.output.writelines(f"    [*]value     ...........| {str(self.value)}\n")
                                        print(f"    [*]input     ...........| {self.input_get}")
                                        print(f"    [*]type      ...........| {self.type}")
                                        print(f"    [*]value     ...........| {self.value}")
                                    print('\n'+'='*25+'\n')    
                            else:
                                self.replace = self.line.replace('\n', '')
                                print(f"[*]link ...........| {self.replace}")
                                print("[*]Form ...........| No Form Discover")
                                sys.stdout.write('\x1b[1A'); sys.stdout.write('\x1b[2K')
                                sys.stdout.write('\x1b[1A'); sys.stdout.write('\x1b[2K')
                        except UnboundLocalError :    
                            self.replace = self.line.replace('\n', '')
                            print(f"[*]link ...........| {self.replace}")
                            print("[*]Form ...........| No Form Discover")
                            sys.stdout.write('\x1b[1A'); sys.stdout.write('\x1b[2K')
                            sys.stdout.write('\x1b[1A'); sys.stdout.write('\x1b[2K')    
                        
                    if countform == 0:
                        print("[*] Status ...........| No Form Discovered")
            except KeyboardInterrupt:
                print(self.banner)
                exit()
        except requests.exceptions.ConnectionError:
            print("[-]Error ..........| No status line received - the server is down")
            pass
        except KeyboardInterrupt:
            print(self.banner)
            exit()
                      
    def sub_domain(self):   
        try:
            print(f"{R}\n###-Discover sub-Domain{s}")
            print('='*25)
            print()
            self.target_url = self.args.URL
            output_11 = self.output.write('\n' + "###-Discover sub-Domain" + '\n' + '='*25 + '\n')
            if 'http://' in self.target_url:      
                url_replase = self.target_url.replace('http://', '')
            elif 'https://' in self.target_url: 
                url_replase = self.target_url.replace('https://', '')
            if 'www.' in self.target_url: 
                url_replase = url_replase.replace('www.', '')
            print ('[*]MainDomain ...........|', url_replase)
            output_12 = self.output.write('[*+]MainDomain ...........| ' + url_replase + '\n')
            try:
                if not self.args.wordlist:
                    wordlist = "./small_list.txt"
                else:    
                    wordlist = self.args.wordlist
                with open(wordlist, 'r') as sub_read:
                    content = sub_read.read()
                    subdomain = content.splitlines()
            except IOError:
                print("[*]wordlist  ...........| File Not Exist")
                exit()
            for sub in subdomain:
                if "https://" in self.args.URL:
                    sub_domain_url = 'https://', sub, '.', url_replase
                    sub_domain_url_join = ''.join(sub_domain_url)
                elif "http://" in self.args.URL:
                    sub_domain_url = 'http://', sub, '.', url_replase
                    sub_domain_url_join = ''.join(sub_domain_url)
                try:
                    #requests.get(sub_domain_url_join) 
                    if "/" in sub_domain_url_join[-1]:
                        sub_domain_url_join = sub_domain_url_join[0:-1]
                    else:
                        sub_domain_url_join = sub_domain_url_join   
                    try:    
                        requests.get(sub_domain_url_join, timeout=3)
                    except requests.exceptions.InvalidURL:
                        continue    
                except requests.ConnectionError:
                    print("[+]Sub-Domain ...........|", sub_domain_url_join)
                    sys.stdout.write('\x1b[1A')
                    sys.stdout.write('\x1b[2K')
                else:
                    try:
                        socket.setdefaulttimeout(1)
                        SubIp = socket.gethostbyname(sub_domain_url_join.replace("https://",""))
                    except Exception :
                       print("[+]Sub-Domain ...........|", sub_domain_url_join)
                       sys.stdout.write('\x1b[1A')
                       sys.stdout.write('\x1b[2K')
                    else:  
                        self.count4 +=1 
                        print("[+]Sub-Domain ...........| "+f'{sub_domain_url_join:<35}',f'{"---------|":>15}', SubIp)
                        output_13 = self.output.writelines("[+]Sub-Domain ...........| "+f'{sub_domain_url_join:<35}'+f'{"---------| ":>15}'+SubIp+'\n')
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
            print("[-]Error  ..........| No status line received - the server has closed the connection")
            exit()
    def Email_Scan(self):
        try:
            with open('.data.txt', 'r') as read_line:
                self.line_read = read_line.readlines()
            print(f"{R}\n###-Discover Emails{s}")
            print("=" * 25)
            output_14 = self.output.write('\n' + "###-Discover Emails " + '\n' + '=' * 25 + '\n')
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
                                print("[+]Email ...........| ", email)
                                self.count5 +=1
                                output_13 = self.output.writelines("[+]Email ...........| " + email + '\n')
                except requests.exceptions.ConnectionError:
                    print("[-]Error  ..........| No status line received - the server has closed the connection")
                    continue  
                if not emails:
                    list_of_messages = ['.....patience.....', '......wait.....', '.....Email-Scan.....']
                    random_message = random.choice(list_of_messages)
                    print("[+]Email ...........| ", random_message)
                    sys.stdout.write('\x1b[1A')
                    sys.stdout.write('\x1b[2K')

            output_20 = self.output.write("[-]Email ...........| Email Scan finish" + '\n')
        except KeyboardInterrupt:
            print(self.banner)
            exit()
    def robotstxt_read(self):
        print(f"{R}\n###-Discover Robots.txt{s}")
        print("="*25)
        num = 0 
        try:
            with open('.domain', 'r') as read_line_sub:
                if self.args.URL not in read_line_sub:
                   self.line_domain = read_line_sub.readlines()
                   self.line_domain.append(self.args.URL)
                else:
                    self.line_domain = read_line_sub.readlines()
                output_15 = self.output.write('\n' + "###-Discover Robots.txt" + '\n' + '=' * 25 + '\n')
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
                        output_15 = self.output.write('\n' + "###-Discover Robots.txt" + '\n' + '=' * 25 + '\n')
                        print("[*]link ..........|", self.link_robot+'\n')
                        print(('*' * 30))
                        print(Beautiful_robots1)
                        print(('*' * 30))
                        output_16 = self.output.write("[*]link ..........| " + self.link_robot + '\n' + '*' * 25 + '\n')
                        output_17 = self.output.writelines(Beautiful_robots1 + '\n' + '*' * 25 + '\n')
                        #links = set(re.findall(r'(?<=Disallow:\s).*|(?<=Allow:\s).*', Beautiful_robots1) )
                        links = set(re.findall(r'^(?:Disallow|Allow|Sitemap):\s*(\S+)', Beautiful_robots1 , re.MULTILINE))
                        
                        print(O+"\nRobots.txt_Detalis"+'\n'+'_'*12+s+'\n')
                        self.output.writelines("\nRobots.txt_Detalis"+'\n'+'_'*12+'\n\n')
                        for data in links :
                            if 'User-agent: *' in data  or 'user-agent: *' in data:
                                pass
                            if self.args.URL in data:
                                time.sleep(.20)
                                print("   [*]link ..........|", data.strip().replace('\n',''))
                                output_17 = self.output.writelines(f"    [*]link ..........| {data.strip().replace('\n','')}\n")

                            else:    
                                time.sleep(.20)
                                print("   [*]link ..........|", self.args.URL+data.strip().replace('\n',''))
                                output_17 = self.output.writelines(f"    [*]link ..........| {self.args.URL+data.strip().replace('\n','')}\n")
                                self.count7 +=1
                        print(O+'_'*30+s+'\n')
                    else:
                        print("[+]Check-robots.txt  ...........|",self.link_robot )
                        sys.stdout.write('\x1b[1A')
                        sys.stdout.write('\x1b[2K')

            else:
                if num == 0 :
                     print("\n[*]Robots.txt ..........| No Robots.txt Found ")
                output_21 = self.output.write('\n' + "[*]Robots.txt ..........| Robots.txt Scan finish  " + '\n')
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
            print(f"{R}\n###-Discover Robots.txt{s}")
            print("=" * 25)
            print("[-]Robots.txt ..........| NO Robots.txt Discover")
            exit()
        except requests.exceptions.ConnectionError:
            print("[-]Error  ..........| No status line received - the server has closed the connection")
            pass
    def control(self):
        parser = argparse.ArgumentParser(
        description="WebShop: Subdomain and Email Discovery Tool\n\n"
                    "Modes:\n"
                    "  1. Scan Mode → requires --URL\n"
                    "  2. API Key Mode → only -K is needed\n",
        formatter_class=argparse.RawTextHelpFormatter
    )


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
            help="Fetch subdomains specifically using the Hackertarget API")
        scan_group.add_argument("--pdf", action="store_true",
            help="make output report file pdf format")
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
        f"📅 Today                : {today}\n"+
        f"🟢 Scan Started         : {start_str}\n"+
        f"🔴 Scan Finished        : {stop_str}\n"+
        f"⏱️  Total Duration       : {Tresult}\n"+
        O+"_"*30+'\n\n'+
        f"{R}[+] Static Links Found     : {O} {self.count1}\n" +
        f"{R}[+] Hidden Links Found     : {O} {self.count2}\n" +
        f"{R}[+] JS Files Discovered    : {O} {self.count3}\n" +
        f"{R}[+] Subdomains Found       : {O} {self.count4}\n" +
        f"{R}[+] Emails Found           : {O} {self.count5}\n" +
        f"{R}[+] API endPoint Found     : {O} {self.count6}\n" +
        f"{R}[+] Robots.txt Discovered  : {O} {self.count7}\n" +
        O+"="*40 + "\n" +
        R+"✅ Scan Finished Successfully\n" +
        O+"="*40+s + "\n"
        )
        print(self.summary)
        print("[+]Report-Scan ..........| file://"+os.getcwd()+"/Webshop_"+str(self.resreach.group(1))+".txt")  
        print(self.banner)
        output_A = self.output.writelines('\n\n'+str(self.summary.\
        replace(f"{O}",'').replace(f"{R}",'').replace(f"{s}",''))+ self.banner.replace(f'{R}','')\
        .replace(f'{s}','').replace(f"{O}",'')+"\n" + "=" * 25)
        
        
    def main(self):
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
                output_C = self.output.writelines("\n###-Discover sub-Domain_API"+"\n"+'='*25+"\n"+readS+"\n")   
                os.remove("./.Sdomain") 
            else:    
                self.sub_domain() 
            self.robotstxt_read() 
            
        else:
            if self.args.email:
                self.extract_links_form()
                self.discover_link()
                self.Email_Scan()
            elif self.args.subdomain:
                self.sub_domain()
            elif self.args.subapi:
                
                from SubAPI import API_SubDomains_Scan as API
                API.find_subdomains(self, args=self.control)
                with open("./.Sdomain",'r') as readf:
                    readS = readf.read()
                output_C = self.output.writelines("\n###-Discover sub-Domain_API"+"\n"+'='*25+"\n"+readS+"\n")  
                os.remove("./.Sdomain")
        
        self.print_summary()
        self.output.close() 
        if self.args.pdf:
            from pdfout import PDF_OUT
            pdf = PDF_OUT()
            txt_file = "Webshop_" + self.resreach.group(1) + ".txt"
            pdf_file = txt_file.replace(".txt", ".pdf")
            pdf.txt_to_pdf(txt_file, pdf_file)


if __name__ == "__main__":
    Shopping()
