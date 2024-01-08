import requests
import re

url = "https://fa.wikipedia.org/"
response = requests.get(url)

if response.status_code == 200:
    data = response.text

    data = re.sub(r'<.*?>', '', data)
    words = data.split(' ')
    word_count = len(words)

    print(f"تعداد کلمات در داده متنی ویکی پدیا فارسی: {word_count}")

else:
    print("دریافت اطلاعات با شکست مواجه شد")
