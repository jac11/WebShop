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
import random

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

    def extract_links_form(self):
        try:
            self.session = requests.Session()  
            self.target_url = self.args.URL
            if '/' not in self.target_url[-1]:
                self.target_url = self.target_url + '/'
                print("[*]URL ............| ", self.target_url)              
            else:
                pass
            self.target_links = []
            try:
                response = self.session.get(self.target_url) 
                if response.ok:
                    return re.findall('(?:href=")(.*?)"', str(response.content))                           
                else:
                    output_A = self.output.writelines('\n\n' + self.banner + "[-]link ..........| No links Discover " + '\n' + "="*25)
                    output_25 = self.output.writelines("[*]input  ...........| " + self.target_url + '\n')  
                    print('[-]link ..........| No links Discover ')
                    print("[&]web  ..........| This Website login required to grep information ")
                    exit()
            except requests.exceptions.ConnectionError:
                print("[-]Error  ..........| No status line received - the server has closed the connection")
                exit()
        except KeyboardInterrupt:
            print(self.banner)
            exit()

    def discover_link(self):
        try:
            try:
                output_0 = self.output.writelines('\n\n' + self.banner + '\n' + "###-Discover links" + '\n' + "="*25 + '\n')    
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
        try:
            outbut_01 = self.output.write("\n###-Discover links" + '\n' + '='*25 + '\n')
            try:
                with open('.data.txt', 'r') as read_line:
                    self.line_read = read_line.readlines()
                    print("\n###-Discover Form ")
                    print('='*25)
                    print()

                for self.line in self.line_read:
                    time.sleep(0.25)  
                    try:      
                        response = self.session.get(self.line,timeout=(0.2, 5))
                    except Exception :
                        response = self.session.get(self.line,allow_redirects=False,timeout=(0.2, 5))   
                    header_html = BeautifulSoup(response.content, 'lxml')
                    if response.ok:
                        form_list = header_html.findAll('form')
                        self.list_input = header_html.findAll('input')
                        post_data = {}
                        for form in form_list:
                            self.action = form.get('action')
                            self.url_path = urllib.parse.urljoin(self.line, self.action)
                            self.method = form.get('method')
                            output_2 = self.output.write('\n' + "###-Discover Form " + '\n' + '='*25 + '\n')
                            output_2 = self.output.writelines("[*]action ...........| " + self.url_path + '\n')
                            output_3 = self.output.writelines("[*]method ...........| " + str(self.method) + '\n')
                        for input in self.list_input:
                            self.input_get = input.get('name')  
                            self.type = input.get('type')                      
                            self.value = input.get('value')   
                            print("[*]action ...........| ", self.url_path)
                            print("[*]method ...........| ", self.method)     
                            print("[*]input  ...........| ", self.input_get)
                            print("[*]type   ...........| ", self.type)
                            print("[*]value  ...........| ", self.value) 
                            output_4 = self.output.writelines("[*]input  ...........| " + str(self.input_get) + '\n')
                            output_5 = self.output.writelines("[*]type   ...........| " + str(self.type) + '\n')
                            output_6 = self.output.writelines("[*]value  ...........| " + str(self.value) + '\n')
                            print()     
                            print('='*25)   
                    else:
                        print()
                        self.replace = self.line.replace('\n', '')
                        print("[*]link ...........|", self.replace)  
                        print("[*]Form ...........| No Form Discover")
                        sys.stdout.write('\x1b[1A')
                        sys.stdout.write('\x1b[2K')
                        sys.stdout.write('\x1b[1A')
                        sys.stdout.write('\x1b[2K')
                        sys.stdout.write('\x1b[1A')
                        sys.stdout.write('\x1b[2K')
                        
            except KeyboardInterrupt:
                print(self.banner)
                exit()
        except requests.exceptions.ConnectionError:
            print("[-]Error  ..........| No status line received - the server has closed the connection")
            pass

    def sub_domain(self):
        try:
            print("\n###-Discover sub-Domain")
            print("this scan will take a while please patience")
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
                    print("[+]Sub-Domain ...........| ", sub_domain_url_join)
                    sys.stdout.write('\x1b[1A')
                    sys.stdout.write('\x1b[2K')
                else:
                    print("[+]Sub-Domain ...........| ", sub_domain_url_join)
                    output_13 = self.output.writelines("[+]Sub-Domain ...........| " + sub_domain_url_join + '\n')
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
            print("[-]Email ...........| Email Scan Finish")
            output_20 = self.output.write("[-]Email ...........| Email Scan finish" + '\n')
        except KeyboardInterrupt:
            print(self.banner)
            exit()

    def robotstxt_read(self):
        try:
            with open('.domain', 'r') as read_line_sub:
                self.line_domain = read_line_sub.readlines()
                output_15 = self.output.write('\n' + "###-Discover Robots.txt" + '\n' + '=' * 25 + '\n')
            for robots in self.line_domain:
                self.link_robot = urllib.parse.urljoin(robots, '/robots.txt')
                self.link_robot_str = str(self.link_robot)
                response_robots = requests.get(self.link_robot, data=None)
                Beautiful_robots = str(BeautifulSoup(response_robots.content, 'lxml'))
                Beautiful_robots = Beautiful_robots.replace('<html>', '')
                Beautiful_robots = Beautiful_robots.replace('<body>', '')
                Beautiful_robots = Beautiful_robots.replace('<p>', '')
                Beautiful_robots = Beautiful_robots.replace('</p>', '')
                Beautiful_robots = Beautiful_robots.replace('</body>', '')
                Beautiful_robots1 = Beautiful_robots.replace('</html>', '')
                time.sleep(0.25)
                print("\n###-Discover Robots.txt")
                print("="*25)
                output_15 = self.output.write('\n' + "###-Discover Robots.txt" + '\n' + '=' * 25 + '\n')
                print()
                print("[*]link ..........|", self.link_robot)
                print()
                print(('*' * 30))
                print(Beautiful_robots1)
                print(('*' * 30))
                output_16 = self.output.write("[*]link ..........| " + self.link_robot + '\n' + '*' * 25 + '\n')
                output_17 = self.output.writelines(Beautiful_robots1 + '\n' + '*' * 25 + '\n')
            else:
                print("\n[*]Robots.txt ..........| Robots.txt Scan finish ")
                output_21 = self.output.write('\n' + "[*]Robots.txt ..........| Robots.txt Scan finish  " + '\n')
                try:
                   # if os.path.isfile(".domain"):
                    #    os.remove(".domain")
                    if os.path.isfile('.data.txt'):
                        os.remove('.data.txt')
                        print(self.banner)
                        output_A = self.output.writelines('\n\n' + self.banner + " [-]SCAN ..........| Webshop finish sacn " + '\n' + "=" * 25)
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
        parser.add_argument("--URL", action=None, help="url target website") 
        parser.add_argument("-o", "--output", action=None, required=True, help="save the output into file") 
        parser.add_argument("-w", "--wordlist", action=None, required=False, help="select wordlist of subdomain") 
        parser.add_argument("-R", "--robots", action="store_true", required=False, help="Check robots file") 
        parser.add_argument("-E", "--email", action="store_true", required=False, help="Discover Email address") 
        parser.add_argument("-S", "--subdomain", action="store_true", required=False, help="Discover subdomains")  
        parser.add_argument("-A", "--all", action="store_true", required=False, help="Discover all Options")

        self.args = parser.parse_args()
        if len(sys.argv) != 1:
            pass
        else:
            parser.print_help()
            exit()

    def main(self):
        if self.args.output:
            self.output = open(self.args.output, 'w')
            if os.path.isfile(".domain"):
                os.remove(".domain")
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