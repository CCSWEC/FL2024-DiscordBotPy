import urllib.request
import requests
import webbrowser
import random
from bs4 import BeautifulSoup

def get_random_bash_post():
    """Opens a random Wikipedia article in the web browser."""
    #post_id = str(random.randint(0, 9999))

  
#"350529"
    post_id = "browse&p="+str(random.randint(1,11))
    url = f"https://bash-org-archive.com/?{post_id}"

    req = urllib.request.Request(url=url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"})
    page = urllib.request.urlopen(req)
    
    soup = BeautifulSoup(page, "html.parser")
    elements = soup.find_all("p", class_="qt")
    all_elements = []
    for e in elements:
        all_elements.append(e.text.strip())
    
    rindex = random.randint(0, len(all_elements)-1)
    return all_elements[rindex]    
    #response = requests.get(url)
    #response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
    #webbrowser.open(response.url)
    



