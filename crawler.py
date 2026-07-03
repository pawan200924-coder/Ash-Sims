import urllib.request
import urllib.parse
import os
import re
import ssl

# Avoid SSL errors for scraping
ssl._create_default_https_context = ssl._create_unverified_context

PAGES = {
    "home": "https://www.ashandsims.com/",
    "about": "https://www.ashandsims.com/about/",
    "services": "https://www.ashandsims.com/services/",
    "vehicle_branding": "https://www.ashandsims.com/services/large-format-digital-printing/vehicle-branding/",
    "large_format_digital_printing": "https://www.ashandsims.com/services/large-format-digital-printing/",
    "fabrication": "https://www.ashandsims.com/services/fabrication/",
    "flags_fabric_printing": "https://www.ashandsims.com/services/flags-fabric-printing/",
    "signage": "https://www.ashandsims.com/services/signage/",
    "corporate_gifts": "https://www.ashandsims.com/services/corporate-gifts/",
    "designing": "https://www.ashandsims.com/services/designing/",
    "offset_printing": "https://www.ashandsims.com/services/offset-printing/",
    "clients": "https://www.ashandsims.com/clients/",
    "blog": "https://www.ashandsims.com/blog/",
    "contact": "https://www.ashandsims.com/contact/"
}

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

RAW_HTML_DIR = r"c:\Users\pawan\Videos\Ash&Sims\raw_html"
IMAGES_DIR = r"c:\Users\pawan\Videos\Ash&Sims\public\assets\images"

os.makedirs(RAW_HTML_DIR, exist_ok=True)
os.makedirs(IMAGES_DIR, exist_ok=True)

def fetch_url(url):
    print(f"Fetching: {url}")
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            return response.read()
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
        return None

def download_image(url, local_path):
    if os.path.exists(local_path):
        return True
    print(f"Downloading image: {url} -> {local_path}")
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            with open(local_path, 'wb') as f:
                f.write(response.read())
        return True
    except Exception as e:
        print(f"Failed to download image {url}: {e}")
        return False

# List of downloaded image names to avoid duplicates
downloaded_images = {}

def extract_and_download_images(html_content, base_url):
    # Regex to find all URLs containing wp-content/uploads/
    pattern = r'https?://[a-zA-Z0-9.-]+/wp-content/uploads/[a-zA-Z0-9_./%-]+'
    urls = re.findall(pattern, html_content)
    
    # Also find background images or other media ending with jpg/png/jpeg/svg
    img_extensions = r'[a-zA-Z0-9_./%-]+\.(?:jpg|jpeg|png|gif|svg|webp)'
    more_urls = re.findall(r'https?://[a-zA-Z0-9.-]+/' + img_extensions, html_content)
    
    all_img_urls = set(urls + more_urls)
    
    for img_url in all_img_urls:
        # Get filename
        filename = os.path.basename(urllib.parse.urlparse(img_url).path)
        if not filename:
            continue
        
        # Clean filename from %20, etc.
        filename = urllib.parse.unquote(filename)
        # Ensure it has a valid extension
        if not any(filename.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp']):
            continue
            
        local_path = os.path.join(IMAGES_DIR, filename)
        
        # Download
        success = download_image(img_url, local_path)
        if success:
            downloaded_images[img_url] = f"/assets/images/{filename}"

print("=== Starting Scraping ===")
scraped_data = {}

for name, url in PAGES.items():
    content = fetch_url(url)
    if content:
        html_str = content.decode('utf-8', errors='ignore')
        # Save raw HTML
        html_path = os.path.join(RAW_HTML_DIR, f"{name}.html")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_str)
        print(f"Saved HTML to {html_path}")
        
        # Download images
        extract_and_download_images(html_str, url)

# Save image mapping
import json
mapping_path = os.path.join(RAW_HTML_DIR, "image_mapping.json")
with open(mapping_path, "w") as f:
    json.dump(downloaded_images, f, indent=4)

print("=== Scraping Completed ===")
