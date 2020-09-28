#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-



import requests
from bs4 import BeautifulSoup
import argparse
import sys
import os
import urlparse 
import re
import readline
import time


class Shopping:
   
  def __init__(self):
       
      self.panner="""
      
  ██     ██ ███████ ██████  ███████ ██   ██  ██████  ██████  
  ██     ██ ██      ██   ██ ██      ██   ██ ██    ██ ██   ██ 
  ██  █  ██ █████   ██████  ███████ ███████ ██    ██ ██████  
  ██ ███ ██ ██      ██   ██      ██ ██   ██ ██    ██ ██      
   ███ ███  ███████ ██████  ███████ ██   ██  ██████  ██      
                                             by:jacstory                                                                                                                     
 """
      print self.panner

     
      self.control()
      self.main()
     
  def extract_links_form(self):
      try:     
         self.session = requests.Session()  
         self.target_url =self.args.URL
         self.target_links = []
         response = self.session.get(self.target_url) 
         if response.ok == True:  
            return re.findall('(?:href=")(.*?)"',response.content)
         else:          	
           output_A = self.output.writelines('\n\n' + self.panner +" [-]link ..........| No links Discover " + '\n'+"="*25)	
           print '[-]link ..........| No links Discover '
      except KeyboardInterrupt :
             print self.panner
             exit()     
  def discover_link(self):
        
        try:
           output_0 = self.output.writelines('\n\n'+self.panner+'\n'+"###-Discover links"+'\n'+"="*25+'\n')	
           print "\n###-Discover links"
           print("="*25)
           print
           herf_links = self.extract_links_form()
 
           for self.link in herf_links:
             self.link = urlparse.urljoin(self.target_url ,self.link)
          
             if "#" in self.link :
               self.link = self.link.split('#')[0]
           
             if  self.target_url in self.link and self.link not in self.target_links:
                 self.target_links.append(self.link)
                 time.sleep(0.40)
                 if self.link[-10:]==['logout.php']:
                     pass
                 else:
                                     
                     print  "[+]link ...........| ",self.link 
                    
                     output_1 = self.output.writelines("[+]link ...........| "+self.link+'\n')  

           with open(".data.txt", "w") as file_links :
             file_links.writelines("%s\n" % i for i in self.target_links)
        except KeyboardInterrupt: 
               print self.panner
               exit()        
  def form_Check(self):
         outbut_01 = self.output.write("\n###-Discover links"+'\n'+'='*25+'\n')
         try: 
              with open('.data.txt','r') as read_line:
                 self.line_read = read_line.readlines() 
                 print "\n###-Discover Form "
                 print ('='*25)
                 print
             
              for self.line in self.line_read:  
                 time.sleep(0.25)        
                 response =  self.session.get(self.line)
                 header_html= BeautifulSoup(response.content,'lxml')
                
                 if response.ok == True:
                     form_list=  header_html.findAll('form')
                     self.list_input = header_html.findAll('input')
                     post_data ={}
                     for form in form_list :
                         self.action = form.get('action')
                         self.url_path = urlparse.urljoin(self.line,self.action)
                         self.method = form.get('method')
                         print "\n###-Discover Form "
                         print ('='*25)
                         print
                         print  "[*]action ...........| ",self.url_path
                         print  "[*]method ...........| ",self.method
                         output_2 = self.output.write('\n'+ "###-Discover Form "+'\n'+'='*25+'\n')
                         output_2 = self.output.writelines("[*]action ...........| "+self.url_path+'\n')
                         output_3 = self.output.writelines("[*]method ...........| "+str(self.method)+'\n')
                     for input in self.list_input:   
                         self.input_get = input.get('name')  
                         self.type = input.get('type')                      
                         self.value= input.get('value')        
                         print "[*]input ...........| ",self.input_get
                         print "[*]type  ...........| ",self.type
                         print "[*]value ...........| ", self.value 
                         output_4 = self.output.writelines("[*]input  ...........| "+str(self.input_get)+'\n')
                         output_5 = self.output.writelines("[*]type   ...........| "+str(self.type)+'\n')
                         reload(sys)  
                         sys.setdefaultencoding('utf-8')
                         output_6 = self.output.writelines("[*]value  ...........| " + (str(self.value)+'\n'))
                     print     
                     print('='*25)    
                 else:  
                        print 
                        self.replace = self.line.replace('\n','')
                        print "[*]link ...........|",self.replace  
                        print "[*]Form ...........| No Form Discover" 
                        output_7 = self.output.writelines('\n'+'='*25+'\n'+"[*]link  ...........|"+self.replace +'\n')
                        output_8 = self.output.writelines("[*]Form  ...........| No Form Discover" +'\n'+'='*25+'\n')                                 
                        print('='*25)
                   
                  
                      
         except KeyboardInterrupt: 
               print self.panner
               exit()
                                  
  def sub_domain(self):
      try : 
           print "\n###-Discover sub-Domain"
           print "this scan will take a while please patience"
           print ('='*25)
           print
           output_11 = self.output.write('\n'+"###-Discover sub-Domain" +'\n'+ '='*25 +'\n')
           if 'http://' in self.target_url:      
               url_replase =  self.target_url.replace('http://','')
           elif 'https://' in  self.target_url: 
               url_replase = self.target_url.replace('https://','')
           if 'www.'in self.target_url: 
               url_replase =  url_replase.replace('www.','')
           print '[*]MainDomain ...........|',url_replase
           output_12 = self.output.write( '[*]MainDomain ...........|'+ url_replase+'\n')
           with open('subdomains.txt','r') as sub_read :
               content = sub_read.read()
               subdomain = content.splitlines()    
           for sub in subdomain :
               sub_domain_url ='http://',sub,'.', url_replase
               sub_domain_url_join = ''.join(sub_domain_url)
               if not sub:
                  break
               else:  
                  try:
                      requests.get(sub_domain_url_join) 
                  except requests.ConnectionError:
                      print"[+]Sub-Domain ...........| ",sub_domain_url_join
                      sys.stdout.write('\x1b[1A')
                      sys.stdout.write('\x1b[2K')
                  else:
                     print"[+]Sub-Domain ...........| ",sub_domain_url_join
                     output_13 = self.output.writelines( '\n'+"[+]Sub-Domain ...........| "+ sub_domain_url_join +'\n')
                     list_domain = []
                     if sub_domain_url_join not in list_domain :
                        list_domain.append(sub_domain_url_join)
                        string_list= ''.join(list_domain)
                        append_list = append_list.write(string_list+'\n')
                          

      except KeyboardInterrupt: 
               print self.panner
               exit()                                      
  def Email_Scan(self):
      try:
       
          with open('.data.txt','r') as read_line:
                   self.line_read = read_line.readlines() 
          print "\n###-Discover Emails "
          print("="*25)
          print 
          output_14 = self.output.write('\n'+"###-Discover Emails " +'\n'+ '='*25 +'\n')
          for self.line in self.line_read:
              replace_spaces = self.line.replace('\n','')
              response = requests.get(replace_spaces)
              emails = re.findall("[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}",response.content)
              email_list = []
              for email in emails :
                 if email not in email_list:
                      email_list.append(email)
                      email_final = ''.join(email)
                      slice_email = email_final[-4:]
                      list_out = ['.png','.jpg','.jpeg','.gif','.zip']
                      if slice_email in  list_out :
                         pass
                      else:	  
                          print"[+]Email ...........| ",email_final
                          output_13 = self.output.writelines( "[+]Email ...........| "+ email_final+'\n')
              else:
                print"[+]Email ...........| ",replace_spaces
                sys.stdout.write('\x1b[1A')
                sys.stdout.write('\x1b[2K')        
          else:
            print "[-]Email ...........| No Email Discover"
            output_20 = self.output.write("[-]Email ...........| No Email Discover"+'\n')
      except KeyboardInterrupt: 
               print self.panner
               exit()           
  def robotstxt_read(self) :
   
      try:
      	 with open('.domain','r') as read_line_sub:
              self.line_domain = read_line_sub.readlines()
              print "\n###-Discover Robots.txt"
              print("="*25)
         output_15 = self.output.write('\n'+"###-Discover Robots.txt" +'\n'+'='*25 +'\n')     
         for robots in self.line_domain :
              if not robots : 
                 break
              else:      
	              self.link_robot  = urlparse.urljoin(robots ,'/robots.txt')
	              self.link_robot_str = str( self.link_robot)
	              response_robots  =  requests.get(self.link_robot,data =None)
	              Beautiful_robots = str(BeautifulSoup(response_robots.content,'lxml'))
	              Beautiful_robots = Beautiful_robots.replace('<html>','')
	              Beautiful_robots = Beautiful_robots.replace('<body>','')
	              Beautiful_robots = Beautiful_robots.replace('<p>','')
	              Beautiful_robots = Beautiful_robots.replace('</p>','')
	              Beautiful_robots = Beautiful_robots.replace('</body>','')
	              Beautiful_robots1 = Beautiful_robots.replace('</html>','')
	              time.sleep(0.25)
	              print "\n###-Discover Robots.txt"
	              print("="*25)
	              output_15 = self.output.write('\n'+"###-Discover Robots.txt" +'\n'+'='*25 +'\n')
	              print
	              print "[*]link ..........|" ,self.link_robot
	              print
	              print ('*'*30)
	              print Beautiful_robots1 
	              print ('*'*30) 
	              output_16 = self.output.write("[*]link ..........|" +self.link_robot+'\n')
	              output_17 = self.output.writelines(Beautiful_robots1+'*'*25 +'\n') 
         else:
            print "[*]Robots.txt ..........| NO Robots.txt Discover "        
            output_21 = self.output.write("[*]Robots.txt ..........| NO Robots.txt Discover "+'\n')           
         try:
             if os.path.isfile(".domain"):         
                os.remove(".domain")        
             if os.path.isfile('.data.txt'):
                os.remove('.data.txt')
         except IOError :
            pass      
      except KeyboardInterrupt: 
               print self.panner
               exit()         
        


  def control(self):
    
      parser = argparse.ArgumentParser( description="Usage: [OPtion] [arguments]  [length]  [arguments] Example: ./webshop.py --URL https://www.site.com/ -o outbut ")
      parser.add_argument("--URL" , metavar='' , action=None  ,help ="url target website ") 
      parser.add_argument("-o","--output" , metavar='' , action=None  ,help ="save the outbut into file ") 
      self.args = parser.parse_args()
      if len(sys.argv)!=1 :
           pass
      else:
         parser.print_help()
         exit()
  
  def main(self):
     if self.args.output:   
        self.output = open(self.args.output,'a')
     if self.args.URL:
     	with open ('.domain','a')as append_list :
     		pass     		
        self.extract_links_form()
        self.discover_link()
        self.form_Check()
        self.Email_Scan()
        self.sub_domain() 
        self.robotstxt_read()  
                                 
if __name__ == "__main__":      
    Shopping()
        
    
    
    
    
