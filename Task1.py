import requests
from bs4 import BeautifulSoup
import re

def get_all_wikipedia_titles():
    base_url = 'https://fa.wikipedia.org/w/api.php'
    params = {
        'action': 'query',
        'list': 'allpages',
        'aplimit': 'max',
        'format': 'json'
    }

    titles = []

    while True:
        response = requests.get(base_url, params=params)
        data = response.json()
        
        for page in data['query']['allpages']:
            titles.append(page['title'])

        if 'continue' in data:
            params['apcontinue'] = data['continue']['apcontinue']
        else:
            break

    return titles

def count_words_in_wikipedia_page(page_title):
    url = f'https://fa.wikipedia.org/wiki/{page_title}'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')

        total_words = 0
        for paragraph in paragraphs:
            text = paragraph.get_text()
            words = re.findall(r'\b\w+\b', text)
            total_words += len(words)

        return total_words
    else:
        return 0

all_titles = get_all_wikipedia_titles()

total_word_count = 0 

for title in all_titles:
    word_count = count_words_in_wikipedia_page(title)
    total_word_count += word_count
    print(f"تعداد کلمات در صفحه '{title}': {word_count}")

# چاپ جمع کل کلمات تمام صفحات
print(f"تعداد کلمات در تمام صفحات: {total_word_count}")
