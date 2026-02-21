import subprocess
import requests
from bs4 import BeautifulSoup
import re

p = subprocess.Popen(
    ["rofi", "-dmenu", "-p", "DE -> EN (Cambridge):"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    text=True
)
word, _ = p.communicate()
word = word.strip().lower()

if not word:
    exit(0)

url = f"https://dictionary.cambridge.org/dictionary/german-english/{word}"
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"}

try:
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    
    headword = soup.select_one("span.hw.dhw")
    pos = soup.select_one("span.pos.dpos")
    gram = soup.select_one("span.gram.dgram") 

    out = f"--- {headword.text.upper() if headword else word.upper()} ---\n"
    if pos or gram:
        out += f"({pos.text if pos else ''} {gram.text if gram else ''})\n\n"

    def_blocks = soup.select("div.def-block.ddef_block")
    
    if not def_blocks:
        subprocess.run(["rofi", "-e", "Kelime bulunamadı veya sayfa yapısı farklı."])
        exit()

    for i, block in enumerate(def_blocks[:3], 1): 
        
        definition = block.select_one("div.def.ddef_d")
        
        translation = block.select_one("span.trans.dtrans")
        
        if definition:
            out += f"{i}. DEF: {definition.text.strip()}\n"
        if translation:
            out += f"   EN: {translation.text.strip()}\n"
        
        
        examples = block.select("div.examp.dexamp")
        for ex in examples[:2]: 
            out += f"   • {ex.text.strip()}\n"
        
        out += "\n"

    
    subprocess.run(["rofi", "-e", out])

except Exception as e:
    subprocess.run(["rofi", "-e", f"Hata: {str(e)}"])
