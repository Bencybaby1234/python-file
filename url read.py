# programe to read content of url
import urllib.request

# getting content of the speciifed url
page_content = urllib.request.urlopen(
    "https://www.hackerrank.com/dashboard").read()

# print the content of the url
print(page_content)
