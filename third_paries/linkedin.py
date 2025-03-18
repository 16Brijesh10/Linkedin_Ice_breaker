import os
import requests
from dotenv import load_dotenv

load_dotenv()

def scrape_linledin_profile(linkedin_profile_url: str,mock: bool= False):
    """ scrape information from LinkedIn profile,
    Manually Scrape the information from linkedIn profile"""
    
    if mock:
        linkedin_profile_url="https://gist.githubusercontent.com/16Brijesh10/ef40522f65d057c6e789dc6756acbae0/raw/70ed1ee0421795a71d2be8d2a26c3ea31f51a050/brijesh-a-scrapping.json"
        response = requests.get(linkedin_profile_url,timeout=10,)
    else:
        api_endpoint= "https://api.scrapin.io/enrichment/profile"
        params={
                "apikey":os.environ["SCRAPIN_API_KEY"],
                "linkedInUrl":linkedin_profile_url,
        }
        response=requests.get(
            api_endpoint,
            params=params,
            timeout=10,
        )
    data=response.json().get("person")
    return data
if __name__ == "__main__":
    print(
        scrape_linledin_profile(linkedin_profile_url="www.linkedin.com/in/brijesh-arumuganainar/",)
    )
    