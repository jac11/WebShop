# Webshop Security Scanner

## Description
`Webshop Security Scanner` is a Python-based reconnaissance tool for auditing websites.  
It can crawl links, discover forms, scan for email addresses, find subdomains, and analyze `robots.txt`.  
Useful for **security researchers, penetration testers, and bug bounty hunters** to gather information from target websites.

---

## Requirements

Dependencies:

- `requests`
- `beautifulsoup4`
- `argparse`
- `json`
- `socket`

Install with:

```bash
pip install requests beautifulsoup4
```

---

## Why Use Webshop?
- 🔍 Automates **link and hidden endpoint discovery**  
- 📨 Finds **email addresses** exposed on the site  
- 🌐 Discovers **subdomains** (wordlist + API methods)  
- 🤖 Reads and parses **robots.txt**  
- 🔑 Supports **API key management** for domain WHOIS/analysis  
- 📂 Saves results to output files for later analysis  

---

## Usage

Run with:

```bash
python webshop.py --URL https://example.com [options]
```

---

## Command-Line Arguments

| Option              | Description                                                           |
|---------------------|-----------------------------------------------------------------------|
| `--URL`             | **Required.** Target website URL (e.g., `https://example.com`).       |
| `-w`, `--wordlist`  | Path to wordlist file for subdomain brute-force discovery.            |
| `-E`, `--email`     | Discover email addresses from the target domain.                      |
| `-S`, `--subdomain` | Discover subdomains using a wordlist.                                 |
| `-a`, `--all`       | Run all modules (subdomains, emails, robots, APIs). <br>If combined with `--api`, brute-force is skipped. |
| `-R`, `--robots`    | Fetch and display `robots.txt`. <br>If combined with `--api`, brute-force is skipped. |
| `--api`             | Discover subdomains using APIs (`crt.sh`, `RapidDNS`, `Hackertarget`). <br>When used with `--all`, disables brute-force. |
| `-s`, `--subapi`    | Fetch subdomains specifically via Hackertarget API.                   |
| `-K`, `--APIKEY`    | Provide or store an API key for domain analysis. Stored in `.APIKEY.KEY`. |

---

## Features
###  🔑 How to Get API Key from Host.io

## Steps

1. **Open the Host.io website**  
   👉 Go to [https://host.io](https://host.io)

2. **Sign Up / Create an Account**  
   - Click **Sign Up** (top-right corner).  
   - Choose to register with **Email & Password**, or sign in with **GitHub** or **Google**.  

3. **Verify Your Email**  
   - Host.io will send you a confirmation email.  
   - Open it and click the verification link.  

4. **Log in to Dashboard**  
   - After verification, log in at [https://host.io](https://host.io).  
   - Go to your **Dashboard** or **Account Settings**.  

5. **Get Your API Key**  
   - In the dashboard, look for **API Key** (usually shown as `sk_XXXXXXXXXXXXXXXX`).  
   - Copy this key.  

6. **Choose Your Plan (Optional)**  
   - Host.io offers a **Free plan** with limited API calls.  
   - Paid plans allow more requests per month.  
   - See: [https://host.io/pricing](https://host.io/pricing).  

---

### 1. WHOIS & Domain Info (`--APIKEY`)
- Domain name, URL, rank  
- IP address, city, and country  
- DNS and server details  
- Social media links  

API key is stored in `.APIKEY.KEY` and used when provided with `-K`.

---

### 2. Link Discovery
Extracts static and hidden links from HTML.

### 3. Form Discovery
Finds forms, actions, methods, and input fields.

### 4. Subdomain Discovery
- Brute-force using wordlist (`-S -w`)  
- API discovery (`-s`)
- discover all option include api subdomain discover -a --api

### 5. Email Discovery
Finds email addresses exposed on the site (ignores media/archive extensions).

### 6. Robots.txt Reader
Fetches and displays entries from `robots.txt`.

---

## Examples

Store API key for later use:
```bash
python webshop.py -K 223374939933
```
Scan for emails:
```bash
python webshop.py --URL https://example.com -E
```

Subdomain discovery with wordlist:
```bash
python webshop.py --URL https://example.com -S -w wordlist.txt
```


Subdomain discovery with api:
```bash
python webshop.py --URL https://example.com -s 
```


robote.txt  discovery :
```bash
python webshop.py --URL https://example.com -R
```


Run all modules with API:
```bash
python webshop.py --URL https://example.com -a --api
```

Run all modules without API:
```bash
python webshop.py --URL https://example.com -a -w wordlist.txt
```

---

## Connect
📧 jac11devel@gmail.com
