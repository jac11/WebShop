#!/usr/bin/env python3

import subprocess
import sys

class ManPage:
    def __init__(self, **kwargs):
        self.man_info()

    def man_info(self, **kwargs):
        try:
            INFO = """


            NAME
              WEBSHOP - Links - Forms input - Subdomain - robots.txt and Email Discovery Tool
              

              usage: webshop_P3.py [-h] [-K APIKEY] [--URL URL] [-w WORDLIST] [-E] [-S] [-a]
                     [-R] [--api] [-s] [--pdf]

              WebShop: Subdomain and Email Discovery Tool

              Modes:
                1. Scan Mode → requires --URL
                2. API Key Mode → only -K is needed

              options:
                -h, --help            show this help message and exit

              Scan Options:
                Options for scanning a target domain (require --URL).

                --URL URL             Target website URL (e.g., https://www.example.com)
                -w, --wordlist WORDLIST
                                      Path to wordlist file for subdomain brute-force discovery
                -E, --email           Discover email addresses from the target domain
                -S, --subdomain       Discover subdomains using a wordlist
                -a, --all             Run all discovery modules (subdomains, emails, APIs).
                                      If combined with --api, wordlist-based subdomain discovery is skipped.
                -R, --robots          Discover robots.txt file.
                                      If combined with --api, wordlist-based subdomain discovery is skipped.
                --api                 Use API-based subdomain discovery (crt.sh, RapidDNS, Hackertarget).
                                      When used with --all, disables wordlist brute-force and only uses APIs.
                -s, --subapi          Fetch subdomains specifically using the crt.sh, RapidDNS, Hackertarget API
                --pdf                 Generate output report in PDF format

              API Key Options:
                Options for managing/storing API keys.

                -K, --APIKEY APIKEY   API key for domain analysis (optional in scans, or can be used alone to just store the key)

              It supports:
                  - Subdomain brute-force discovery with wordlists
                  - Subdomain discovery via APIs (crt.sh, RapidDNS, Hackertarget)
                  - Email harvesting from target domains
                  - API key management and storage (host.io WHOIS info)
                  - PDF report generation

              Two primary modes are available:

                  1. Scan Mode → requires --URL
                  2. API Key Mode → only -K is needed to analyze WHOIS info via host.io API

       

       SYNOPSIS

              webshop.py --URL https://www.example.com [OPTIONS]

       DESCRIPTION
              WebShop is a Links Forms input subdomain and email discovery tool designed for
              penetration testers, bug bounty hunters, and security researchers.

       OPTIONS
              -h, --help
                     Show this help message and exit.

              --URL URL
                     Target website URL.
                     Example: --URL https://www.example.com

              -w, --wordlist FILE
                     Path to wordlist file for brute-force subdomain discovery.
                     The tool includes 4 lists:
                        small_list.txt, medium_list.txt, large_list.txt, big_large.txt
                     If not specified, the default is small_list.txt (100 subdomains).

                     Example: -w medium_list.txt or -w /path/to/wordlist.txt

              -S, --subdomain
                     Discover subdomains using a wordlist.  
                     Example: -S -w medium_list.txt     

              -E, --email
                     Discover email addresses from the target domain by scraping.
                     It extracts all links and regex-matches email addresses.

              -a, --all
                     Run all discovery modules (subdomains, emails, Forms input, links).
                     If combined with --api, skips wordlist brute-force.

              --api
                     Use API-based subdomain discovery (crt.sh, RapidDNS, Hackertarget).
                     When used with --all, disables brute-force.

              -s, --subapi
                     Fetch subdomains specifically via APIs.
                     Does not run email discovery or brute-force.

              --pdf
                     Generate a professional PDF report of the scan results.
                     The report will include:
                        - Scan metadata (date, target, options used)
                        - Discovered subdomains
                        - Found email addresses
                        - Links and forms information
                        - API results (if used)
                     
                     Example: --URL https://example.com -a --pdf

              -K, --APIKEY APIKEY

                     Provide or store an API key for domain analysis (WHOIS info via host.io).
                     Can be used alongside scans or standalone.
                     Store an API key for later use:

                            1. Go to: https://host.io
                            2. Click: Sign Up (GitHub or Google login works).
                            3. After login: Open your Dashboard.
                            4. Copy your API key (token).
                            5. Use it in your script like this:

                     python webshop_P3.py -K YOUR_API_KEY
                     webshop_P3.py -K fdad56b78bcff


       EXAMPLES
              Scan a target domain for emails:
                     webshop_P3.py --URL https://example.com -E

              Run subdomain brute-force with a wordlist:
                     webshop_P3.py --URL https://example.com -S -w subdomains.txt

              Use APIs only for subdomain discovery:
                     webshop_P3.py --URL https://example.com -s

              Run everything (Forms, links, emails, subdomains) with API-based discovery:
                     webshop_P3.py --URL https://example.com -a --api

              Run everything (Forms, links, emails, subdomains) using brute-force:
                     Using default wordlist:
                        webshop_P3.py --URL https://example.com -a 
                     Using custom wordlist:
                        webshop_P3.py --URL https://example.com -a -w medium_list.txt

              Generate PDF report:
                     webshop_P3.py --URL https://example.com -a --pdf
                     webshop_P3.py --URL https://example.com -E -S --pdf

             
       EXIT STATUS
              0      Successful execution.
              1      General error, such as invalid command input.
              2      Misuse of command options.

       FILES
              Wordlist files for subdomain discovery.

                  small_list.txt
                  medium_list.txt
                  large_list.txt
                  big_large.txt
                     
       AUTHOR
              Developed by jac11.
              https://github.com/jac11

       LICENSE
              Licensed for ethical use only.
            """
            subprocess.run(['echo', INFO], text=True, check=True, stdout=subprocess.PIPE)
            subprocess.run(['more'], input=INFO, text=True)
        except KeyboardInterrupt:
            sys.exit(0)

if __name__ == '__main__':
    ManPage()