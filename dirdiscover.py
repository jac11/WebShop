#!/usr/bin/env python

import time
import sys
import os
import random
import requests

p  = "\033[96m"
R  = "\033[91m"
s  = "\033[0m"
O  ='\33[37m'
b  = '\33[34m'  

class DirDiscover:

   def readwordlist(self,**kwargs):
      print(f"{R}\nDISCOVERY Directories {s}")
      print('='*25)
      print()
      self.output.writelines("\nDISCOVERY Directories\n" + "="*25 + "\n")
      try:
         with open(f"{self.path_wordlist}user-agents.txt", 'r') as useregint:
            useragents = useregint.readlines()
            choiceagentst = random.choice(useragents).strip()
            if self.args.DIRLIST:
               wordlist = f"{self.path_wordlist}dirwordlist.txt"
            elif self.args.dirpath:
               wordlist = self.args.dirpath  
            elif self.args.all:
               wordlist = f"{self.path_wordlist}dirwordlist.txt"

         with open(wordlist, 'r') as worddir:
             directories = worddir.readlines()
         for directory in directories:
            directory = directory.strip()  
            if not directory or "#" in directory:
               continue        
            session = requests.Session()
            if '/' in self.args.URL[-1]:
               dirurl = f"{self.args.URL}{directory}"  
            else:
               dirurl = f"{self.args.URL}/{directory}" 
            try:
               response = session.get(dirurl.strip(), headers={'User-Agent': choiceagentst}, timeout=60)  
               code = str(response.status_code)
               
            except Exception as a :
               code = "ERR"
            if code == "200":
               if self.args.URL == str(response.url):
                  code_fmt = f"{b}[404]{s}"
                  print(f"[+] Dire {code_fmt} ...........| {directory}") 
                  sys.stdout.write('\x1b[1A')
                  sys.stdout.write('\x1b[2K') 
               else:  
                  code_fmt = f"{O}[{code}]{s}"
                  time.sleep(0.25)
                  self.count9 +=1
                  print(f"[+] Dire {code_fmt} ...........| {dirurl}")
                  self.output.writelines(f"[+] Dire {code_fmt} ...........| {dirurl}\n")
            elif code == "301" or code=='302':
               code_fmt = f"{R}[{code}]{s}"
               time.sleep(0.25)
               self.count9 += 1
               print(f"[+] Dire {code_fmt} ...........| {dirurl}")
               self.output.writelines(f"[+] Dire {code_fmt} ...........| {dirurl}\n")
            elif code == "403" or code=='302':
               code_fmt = f"{R}[{code}]{s}"
               time.sleep(0.25)
               self.count9 += 1
               print(f"[+] Dire {code_fmt} ...........| {dirurl}")
               self.output.writelines(f"[+] Dire {code_fmt} ...........| {dirurl}\n")   
            else:
               code_fmt = f"{b}[{code}]{s}"
               print(f"[+] Dire {code_fmt} ...........| {directory}")
               sys.stdout.write('\x1b[1A')
               sys.stdout.write('\x1b[2K') 
            continue              
                          
      except FileNotFoundError as e:
         print(f"File not found: {e}")
      except Exception as e:
         print(f"Error: {e}")

if __name__ == "__main__":
    discover = DirDiscover()
