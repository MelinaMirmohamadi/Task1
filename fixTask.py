import requests
import re
import json
import pandas as pd

url = "https://www.kaggle.com/datasets/amirpourmand/fa-wikipedia"
headers = {"username":"melimimo","key":"59850ce834e145e521e19566abf4f176"}
response = requests.get(url, headers=headers)
with open("wikipedia.csv", "wb") as f:
    f.write(response.content)

df = pd.read_csv("wikipedia.csv", encoding="utf-8", error_bad_lines=False)

persian_letters = re.compile(r"[ء-ی]")
persian_words = 0
for text in df["wikipedia"]:
    words = re.findall(r"\w+", text)
    persian_words += sum(persian_letters.match(word) for word in words)
print(f"تعداد کلمات فارسی: {persian_words}")