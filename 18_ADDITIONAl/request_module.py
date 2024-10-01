import requests

resourse = requests.get("https://curriculum-vitae-naveen.w3spaces.com/")
print(resourse.text)
# dir(resourse.txt)