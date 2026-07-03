import os
import json
from bs4 import BeautifulSoup

RAW_HTML_DIR = r"c:\Users\pawan\Videos\Ash&Sims\raw_html"
OUTPUT_DIR = r"c:\Users\pawan\Videos\Ash&Sims\raw_html\parsed"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def parse_file(filepath):
    filename = os.path.basename(filepath)
    print(f"Parsing: {filename}")
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    
    # Extract title
    title = soup.title.string if soup.title else ""
    
    # Extract SEO meta description
    desc_meta = soup.find('meta', attrs={'name': 'description'})
    description = desc_meta['content'] if desc_meta else ""
    
    # Remove header, footer, script, styles, navigation, widgets to isolate main body content
    for elem in soup(['script', 'style', 'header', 'footer', 'nav', 'noscript']):
        elem.extract()
    
    # Find all headings and paragraphs
    content_elements = []
    
    # We can search inside the main content wrapper e.g. div with id="ajax-content-wrap" or class="container-wrap"
    main_content = soup.find('div', id='ajax-content-wrap') or soup.find('div', class_='container-wrap') or soup
    
    for elem in main_content.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'li']):
        text = elem.get_text().strip()
        # Clean up double spacing and newlines
        text = re.sub(r'\s+', ' ', text)
        if len(text) > 3:
            content_elements.append({
                'tag': elem.name,
                'text': text
            })
            
    # Also find all image tags and their sources
    images = []
    for img in main_content.find_all('img'):
        src = img.get('src')
        alt = img.get('alt', '')
        if src:
            images.append({
                'src': src,
                'alt': alt
            })

    output_data = {
        'title': title,
        'description': description,
        'elements': content_elements,
        'images': images
    }
    
    out_name = filename.replace('.html', '_parsed.json')
    out_path = os.path.join(OUTPUT_DIR, out_name)
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2)
    print(f"Saved parsed data to {out_path}")

import re
for file in os.listdir(RAW_HTML_DIR):
    if file.endswith('.html'):
        parse_file(os.path.join(RAW_HTML_DIR, file))
