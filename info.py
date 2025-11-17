#!/usr/bin/env python3

import subprocess
import sys

class ManPage:
    def __init__(self, **kwargs):
        self.man_info()

    def man_info(self, **kwargs):
        try:
            INFO = """

            usage: webshop.py [-h] [--man] [-K APIKEY] [--URL URL] [-w WORDLIST] [-E] [-S] [-a] [-R] [--api] [-s] [--pdf] [-D] [-d DIRPATH]

            WebShop: Subdomain and Email Discovery Tool

            Modes:
              1. Scan Mode → requires --URL
              2. API Key Mode → only -K is needed

            options:
              -h, --help            show this help message and exit
              --man                 display man page

            Scan Options:
              Options for scanning a target domain (require --URL).

              --URL URL             Target website URL (e.g., https://www.example.com)
              -w, --wordlist WORDLIST
                                    Path to wordlist file for subdomain brute-force discovery
                                    By default the tool uses the small built-in list (small_list.txt) — ~100 words
                                    The tool also includes three additional built-in lists and accepts either a
                                    list number (1-3) or a full file path:
                                    -w 1    Use the medium list (medium_list.txt) — ~1,000 words
                                    -w 2    Use the large list (large_list.txt)  — ~5,000 words
                                    -w 3    Use the very large list (big_large.txt) — ~10,000 words
                                    Alternatively, provide a custom path to a wordlist file:
                                    -w /path/to/wordlist.txt
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
              -D, --DIRLIST         Discover the web directories using the built-in dir wordlist
              -d, --dirpath DIRPATH
                                    Custom directory wordlist file for directory discovery

            API Key Options:
              Options for managing/storing API keys.

              -K, --APIKEY APIKEY   API key for domain analysis (optional in scans, or can be used alone to just store the key)


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

                     By default the tool uses the small built-in list (small_list.txt) — ~100 words.

                     The tool also includes three additional built-in lists and accepts either a
                     list number (1-3) or a full file path:

                       -w 1            Use the medium list (medium_list.txt) — ~1,000 words
                       -w 2            Use the large list (large_list.txt)  — ~5,000 words
                       -w 3            Use the very large list (big_large.txt) — ~10,000 words

                     Alternatively, provide a custom path to a wordlist file:
                       -w /path/to/wordlist.txt

                     If -w is omitted the tool defaults to the small list (equivalent to no -w, or
                     you may also explicitly pass -w small_list.txt).

                     Examples:
                       webshop --URL https://example.com -S
                           (runs default small wordlist ~100 words)

                       webshop --URL https://example.com -S -w 1
                           (runs medium_list.txt ~1,000 words)

                       webshop --URL https://example.com -S -w 2
                           (runs large_list.txt ~5,000 words)

                       webshop --URL https://example.com -S -w 3
                           (runs big_large.txt ~10,000 words)

                       webshop --URL https://example.com -S -w /home/user/lists/subs.txt
                           (runs a custom user-provided wordlist)
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
              -D, --DIRLIST
                     Discover directories using the built-in WebShop directory
                     wordlist.
                     Directory discovery runs automatically when using --all,
                     or manually when this option is provided.

              -d DIRPATH, --dirpath DIRPATH
                     Use a custom directory wordlist for directory discovery.
                     This option also triggers directory discovery, even
                     without --all.
                     Example:
                         webshop --URL https://example.com -d /path/to/dirs.txt      

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

                     python webshop -K YOUR_API_KEY
                     webshop -K fdad56b78bcff


       EXAMPLES
              Scan a target domain for emails:
                     webshop --URL https://example.com -E

              Run subdomain brute-force with a wordlist:
                     webshop --URL https://example.com -S -w subdomains.txt

              Use APIs only for subdomain discovery:
                     webshop --URL https://example.com -s

              Run everything (Forms, links, emails, subdomains) with API-based discovery:
                     webshop --URL https://example.com -a --api

              Run everything (Forms, links, emails, subdomains) using brute-force:
                     Using default wordlist:
                        webshop --URL https://example.com -a 
                     Using custom wordlist:
                        webshop --URL https://example.com -a -w medium_list.txt

              Generate PDF report:
                     webshop --URL https://example.com -a --pdf
                     webshop --URL https://example.com -E -S --pdf

             
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
                 MIT-NoMod License
                Copyright (c) 2025 jac11
                
                Permission is hereby granted, free of charge, to any person obtaining a copy
                of this software and associated documentation files (the “Software”), to use,
                copy, and distribute the Software, including for commercial purposes,
                subject to the following conditions:
                
                1. Modification of the source code is NOT permitted without the express
                   written permission of the copyright holder (jac11).
                
                2. Redistribution of the Software, whether modified or unmodified, must
                   include this license and the above copyright notice.
                
                3. The Software may not be sold or distributed under a different name
                   or with altered functionality without written approval from jac11.
                
                THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
                IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
                FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
                AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
                LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
                OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
                SOFTWARE.
                
                Author: jac11  
                Project: WebShop Tool  
                GitHub: https://github.com/jac11

            """
            subprocess.run(['echo', INFO], text=True, check=True, stdout=subprocess.PIPE)
            subprocess.run(['more'], input=INFO, text=True)
        except KeyboardInterrupt:
            sys.exit(0)

if __name__ == '__main__':
    ManPage()
