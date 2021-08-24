import requests

def main():
    url = input('Enter URL address: ')
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content

if __name__ == '__main__':
    main()