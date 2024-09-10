import requests
from dotenv import load_dotenv
import os
import base64

url = "https://www.udemy.com/api-2.0/courses/"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(f'{BASE_DIR}/../.env')
API_USERNAME = os.getenv("UDEMY_API_USERNAME")
API_PASSWORD = os.getenv("UDEMY_API_PASSWORD")
credentials = f'{API_USERNAME}:{API_PASSWORD}'
encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

payload = {}
headers = {
  'Authorization': f'Basic {encoded_credentials}',
  'Cookie': '__cf_bm=bkcu.jOEU62Dn0R9tuph4QpaMBjLhprS__CtBoX81e8-1725378876-1.0.1.1-9nT7EpfNzJUsYbIs9.2awjX_ovrS.07ZPdQjjSfENSpEFmf7nHFbYJ0e7vRSrSZvLBxVeBhCFT_dM4NYz9MdRQ; __cfruid=b13a7c58e7febb79cba9413823146d0f118d0107-1725378876; __udmy_2_v57r=a4bd15e40cae48aebf8a910d7d5dda27; evi="3@G9OL4xRI1D8uAwbSA3OgfjwjeqPZ0fiUYHKj03UBQZNOHfPK0XVVjdLC"; ud_cache_brand=IDen_US; ud_cache_device=None; ud_cache_language=en; ud_cache_logged_in=0; ud_cache_marketplace_country=ID; ud_cache_price_country=ID; ud_cache_release=2190cdef910ade129e64; ud_cache_user=""; ud_cache_version=1; ud_rule_vars="eJx9jcEOgyAQBX_FcG01i0JBvsWErLBa0qakgF6M_16TNk1Pvb68mdlYwTRTIW_XkEOJyaAYPZckwCEJjTROGnsOXnnpPbbKuBhvgZip2DawKaRc3qz1WGg49oG10Ioa-hq6iksjhelko5RWip8ADMDAzsfrjgda4uKutiScpuBsjktyZFdMAcf7xxbTjI_gfqBEz4Xy_-Kl6Vqt-be4s_0Fk2tJAQ==:1slVrY:62swpsX0epPV39SUzRCfUzZKfQ6QAkEk55YT3KbGZzM"'
}

def fetch_udemy(keyword):
    
    response = requests.request("GET", f'{url}?search={keyword}', headers=headers, data=payload)
    response_json = response.json()

    # Access the 'result' property
    return response_json.get('results')