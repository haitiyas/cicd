import requests

print("hello world")
print("testing CI/CD")

response = requests.get("https://www.google.com")

print(response.text)
