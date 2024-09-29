#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import argparse
import sys
import os
import urllib.parse
import re
import readline
import time
import json
import random
import socket

class Shopping:
    def __init__(self):
        self.banner = """
        
  ██     ██ ███████ ██████  ███████ ██   ██  ██████  ██████  
  ██     ██ ██      ██   ██ ██      ██   ██ ██    ██ ██   ██ 
  ██  █  ██ █████   ██████  ███████ ███████ ██    ██ ██████  
  ██ ███ ██ ██      ██   ██      ██ ██   ██ ██    ██ ██      
   ███ ███  ███████ ██████  ███████ ██   ██  ██████  ██      
                                             by:jacstory                                                                                                                   
        """ 
        print(self.banner)
        self.control()
        self.main()  
    def APIKEY(self):
            self.session = requests.Session()
            if not os.path.exists(".APIKEY.KEY"):
                with open(".APIKEY.KEY", 'w') as key_file:
                    key_file.write(self.args.APIKEY)
                print("\n###-API_INFO\n")  
                print('[+]APIKEY     ............| ',self.args.APIKEY)
                print('[+]API-File   ............| ',"file///.APIKEY.KEY") 
                print("="*30)
                self.output.writelines("\n###-API_INFO\n")  
                self.output.writelines('[+]APIKEY     ............| '+self.args.APIKEY)
                self.output.writelines('[+]API-File   ............| '+"file///.APIKEY.KEY") 
                self.output.writelines("="*30)
            def APIKEYCALL(self) :       
                with open('.APIKEY.KEY', 'r') as key_file:
                    key = key_file.read().strip()
                DominCheck = self.args.URL.split('//')[1]   
                url = f"https://host.io/api/full/{DominCheck}?token={key}"
                response = self.session.get(url)
                if response.status_code == 200:
                    if 'application/json' in response.headers.get('Content-Type', ''):
                        data = response.json()  # Parse JSON
                    else:
                        header_html = BeautifulSoup(response.content, 'lxml')
                        data = header_html.prettify()
                    time.sleep(.30)        
                try:        
                    print("\n###-WHOIS INFO\n")
                    print("="*30)
                    print("\nDomain-info")
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
                except KeyError:
                     pass
                try:
                             
                    print("\nIp-info") 
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
                try:     
                    print("\nDNS-info") 
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
                try :        
                    print("\nSocailMeddia-info")
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
            if self.args.APIKEY:         
                APIKEYCALL(self)
            elif self.args.callapi:
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
            try:
                response = self.session.get(self.target_url) 
                if response.ok:
                    return re.findall('(?:href=")(.*?)"', str(response.content))                           
                else:
                    print("="*25)
                    output_A = self.output.writelines("[-]link ..........| No links Discover " + '\n' + "="*25)
                    output_25 = self.output.writelines("[*]input  ...........| " + self.target_url + '\n')  
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
    def discover_link(self):
        try:
            try:
                output_0 = self.output.writelines('\n' + "###-Discover links" + '\n' + "="*25 + '\n')    
                print("\n###-Discover links")
                print("="*25)
                print()
                herf_links = self.extract_links_form()
                for self.link in herf_links:
                    self.link = urllib.parse.urljoin(str(self.target_url), str(self.link))         
                    if "#" in self.link:
                        self.link = self.link.split('#')[0]
                    if self.target_url in self.link and self.link not in self.target_links:
                        self.target_links.append(self.link)
                        time.sleep(0.40)
                        if self.link[-10:] == ['logout.php']:
                            pass
                        else:
                            print("[+]link ...........| ", self.link)                                       
                            output_1 = self.output.writelines("[+]link ...........| " + self.link + '\n')  
                with open(".data.txt", "w") as file_links:
                    file_links.writelines("%s\n" % i for i in self.target_links)
            except KeyboardInterrupt: 
                print(self.banner)
                exit() 
        except requests.exceptions.ConnectionError:
            print("[-]Error  ..........| No status line received - the server has closed the connection")
            pass
    def form_Check(self):
        countform = 0
        try:
            self.output.write("\n###-Discover Forms" + '\n' + '='*25 + '\n')
            try:
                with open('.data.txt', 'r') as read_line:
                    self.line_read = read_line.readlines()
                    print("\n###-Discover Form ")
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
                        form_list = header_html.findAll('form')
                        self.list_input = header_html.findAll('input')
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
                                print("\nForm_Detalis"+'\n'+'_'*12+'\n')
                                self.output.writelines("\nForm_Detalis"+'\n'+'_'*12+'\n')
                                for input in self.list_input:
                                    self.input_get = input.get('name')
                                    self.type = input.get('type')
                                    self.value = input.get('value')
                                    countform += 1
                                    self.output.writelines(f"    [*]input  ...........| {str(self.input_get)}\n")
                                    self.output.writelines(f"    [*]type   ...........| {str(self.type)}\n")
                                    self.output.writelines(f"    [*]value  ...........| {str(self.value)}\n")
                                    print(f"    [*]input  ...........| {self.input_get}")
                                    print(f"    [*]type   ...........| {self.type}")
                                    print(f"    [*]value  ...........| {self.value}")
                                print('\n'+'='*25+'\n')    
                            else:
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
    def sub_domain(self):
        try:
            print("\n###-Discover sub-Domain")
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
            output_12 = self.output.write('[*]MainDomain ...........| ' + url_replase + '\n')
            try:
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
                    requests.get(sub_domain_url_join) 
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
            pass
        except requests.exceptions.ConnectionError:
            print("[-]Error  ..........| No status line received - the server has closed the connection")
            exit()
    def Email_Scan(self):
        try:
            with open('.data.txt', 'r') as read_line:
                self.line_read = read_line.readlines()
            print("\n###-Discover Emails ")
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
        print("\n###-Discover Robots.txt")
        print("="*25)
        num = 0 
        try:
            with open('.domain', 'r') as read_line_sub:
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
                        print("[*]link ..........|", self.link_robot)
                        print(('*' * 30))
                        print(Beautiful_robots1)
                        print(('*' * 30))
                        output_16 = self.output.write("[*]link ..........| " + self.link_robot + '\n' + '*' * 25 + '\n')
                        output_17 = self.output.writelines(Beautiful_robots1 + '\n' + '*' * 25 + '\n')
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
                    print("[+]Report-Scan ..........| file://"+os.getcwd()+"/Webshop_"+str(self.resreach.group(1))+".txt")  
                    print(self.banner)
                    output_A = self.output.writelines('\n\n'+ self.banner+"[-]SCAN ..........| Webshop finish sacn " + '\n' + "=" * 25)
                    
                    exit()
                except IOError:
                    pass
        except KeyboardInterrupt:
            print(self.banner)
            exit()
        except IOError:
            print("\n###-Discover Robots.txt")
            print("=" * 25)
            print("[-]Robots.txt ..........| NO Robots.txt Discover")
            exit()
        except requests.exceptions.ConnectionError:
            print("[-]Error  ..........| No status line received - the server has closed the connection")
            pass
    def control(self):
        parser = argparse.ArgumentParser(description="Usage: [Option] [arguments] [Option] [arguments] Example: ./webshop.py --URL https://www.site.com/ -o output")
        parser.add_argument("--URL", action="store", help="Target website URL") 
        parser.add_argument("-w", "--wordlist", action="store", required=False, help="Select wordlist for subdomain discovery") 
        parser.add_argument("-E", "--email", action="store_true", required=False, help="Discover email addresses") 
        parser.add_argument("-S", "--subdomain", action="store_true", required=False, help="Discover subdomains")  
        parser.add_argument("-A", "--all", action="store_true", required=False, help="Discover all options")
        parser.add_argument("-V", "--APIKEY", action="store", required=False, help=" Store API key for domain analysis")
        parser.add_argument("-C", "--callapi", action="store_true", required=False, help="Make API calls if set")
        self.args = parser.parse_args()
        if len(sys.argv) != 1:
            pass
        else:
            parser.print_help()
            exit()
    def main(self):
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
        if self.args.APIKEY or self.args.callapi:
            self.APIKEY()
        if self.args.all:           
            self.extract_links_form()
            self.discover_link()
            self.form_Check()
            self.Email_Scan()
            self.sub_domain() 
            self.robotstxt_read() 
        else:
            if self.args.email:
                self.extract_links_form()
                self.discover_link()
                self.Email_Scan()
            elif self.args.subdomain:
                self.sub_domain()
if __name__ == "__main__":
    Shopping()
