
# WebShop Tool

`WebShop` is a Python-based tool designed for analyzing websites and gathering critical information such as links, forms, subdomains, emails, and `robots.txt` files. It also uses the Whois API to fetch domain-related data for in-depth analysis.

## Requirements

To use `WebShop`, the following dependencies must be installed:
- `requests`
- `BeautifulSoup` (from `bs4`)
- `argparse`
- `json`
- `socket`

You can install the necessary dependencies by running:

```bash
pip install requests beautifulsoup4
```

## Usage

To use the tool, run it with the following options:

```bash
./webshop_P3.py --URL https://example.com [options]
```
----------------------------------------------------------------------------
### Command-Line Arguments

- `--URL`: **Required.** Target website URL.
- `-w`, `--wordlist`: Optional. Path to the wordlist for subdomain discovery.
- `-E`, `--email`: Optional. Discover email addresses from the target website.
- `-S`, `--subdomain`: Optional. Discover subdomains of the target website.
- `-A`, `--all`: Optional. Discover all available options (links, forms, emails, subdomains, etc.).
- `-V`, `--APIKEY`: Optional. API key to fetch domain analysis from the Whois API.
- `-C`, `--callapi`: Optional. Flag to call the API if set.
-----------------------------------------------------------------------------------
## Features
### 1. Domain and WHOIS Info (`APIKEY`)
The tool can fetch and display WHOIS and domain-related information using the host.io API. The information includes:
- Domain name
- URL
- Rank
- GTM (Google Tag Manager)
- IP address, city, and country
- DNS and server details
- Social media links
The API key is stored locally in `.APIKEY.KEY`. If the API key is provided via the `--APIKEY` option or through a stored file, the tool will fetch the domain analysis.
- Create account to use apikey [host.io](https://host.io)
----------------------------------------------------------------------

### 2. Link Discovery (`extract_links_form`)
The tool crawls the provided website to discover and extract all available links from the HTML content.

### 3. Form Discovery (`form_Check`)
The tool searches for forms on the website and extracts details such as:
- Form actions and methods
- Input fields and their types and values

### 4. Subdomain Discovery (`sub_domain`)
The tool discovers subdomains of the provided domain using a wordlist and checks if the subdomain is valid by sending requests.

### 5. Email Discovery (`Email_Scan`)
The tool scans the website content and looks for any email addresses mentioned, excluding those ending in image or archive formats (e.g., `.png`, `.jpg`, `.zip`).

### 6. Robots.txt Reader (`robotstxt_read`)
The tool reads and displays the contents of the `robots.txt` file from the discovered subdomains.

## Example


To Store Host.io API key in the local to use in WebShop tool 
./webshop_P3.py --URL https://example.com -E -K follow by APIKEY 
```bash
./webshop_P3.py --URL https://example.com -E -K 223374939933
```
To call the API Key use  -C option

```bash
./webshop_P3.py --URL https://example.com -E -C 
```
To scan for emails on a website:


```bash
./webshop_P3.py --URL https://example.com -E
```
To scan for emails on a website with whois domain call api:

```bash
./webshop_P3.py --URL https://example.com -E -C
```
To discover subdomains using a wordlist:

```bash
./webshop_P3.py --URL https://example.com -S -w wordlist.txt
```
To discover all available options for a website, use the following command with whois API:

```bash
./webshop_P3.py --URL https://example.com -A -w wordlist.txt -C 
```
To discover all available options for a website, use the following command without API
```bash
./webshop_P3.py --URL https://example.com -A -w wordlist.txt 
```
