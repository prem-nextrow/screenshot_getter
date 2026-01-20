import requests
from urllib.parse import urlparse

def safe_name(url):
    return urlparse(url).netloc.replace(".", "_").replace(":", "_")

def download_media(url, folder, name):
    try:
        response = requests.get(url, timeout=10, stream=True)
        if response.status_code == 200:
            ext = url.split('.')[-1].split('?')[0][:4]
            filepath = f"{folder}/{name}.{ext}"
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            return filepath
    except Exception as e:
        print(f" Error downloading {url}: {e}")
    return None
