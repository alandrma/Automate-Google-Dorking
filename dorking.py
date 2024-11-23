import sys
from googlesearch import search
import time
import random

def google_dorking(domain):
    """
    Perform Google Dorking searches based on a domain.
    :param domain: Target domain entered as an argument.
    :return: List of URLs from the search results.
    """
    try:
        print(f"Searching for dorks on domain: {domain}\n")
        
        # List of dork queries
        dork_queries = [
           f"site:{domain} filetype:pdf",
           f"site:{domain} intitle:'index of'",
           f"site:{domain} ext:conf | ext:cnf | ext:config | ext:ini",
           f"site:{domain} ext:sql | ext:db | ext:dbf | ext:mdb",
           f"site:{domain} ext:log",
           f"site:{domain} ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup",
           f"site:{domain} ext:doc | ext:docx | ext:pdf | ext:xls | ext:xlsx | ext:ppt | ext:pptx",
           f"site:{domain} intext:username | intext:password | intext:passwd",
           f"site:{domain} ext:env | ext:yaml | ext:json",
           f"site:{domain} ext:php intext:'phpinfo()' | intext:'PHP Version'",
           f"site:{domain} 'parent directory'",
        ]
        
        results = []
        for query in dork_queries:
            print(f"Searching with dork: {query}\n")
            
            # Perform the search for each query
            for url in search(query, lang="id"):
                print(f"Found: {url}")
                results.append(url)
            
            # Delay between searches to avoid excessive requests
            delay = random.randint(5, 15)  # Delay between 5-15 seconds
            print(f"Waiting for {delay} seconds before continuing...\n")
            time.sleep(delay)  # Random delay
            
            print("-" * 50)
        
        return results
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 dorking.py <domain>")
        sys.exit(1)
    
    # Get the domain from the command-line arguments
    target_domain = sys.argv[1]
    
    print("Google Dorking Tool")
    print("===================")
    
    # Run the Dorking process
    results = google_dorking(target_domain)
    
    # Display the complete search results
    print("\nComplete search results:")
    for index, url in enumerate(results, start=1):
        print(f"{index}. {url}")
