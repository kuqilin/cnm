# Use the API of Hitokoto to get a random quote.
# https://hitokoto.cn/


import requests, subprocess

def get_hitokoto():
    url = 'https://v1.hitokoto.cn/?encode=json'
    
    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        hitokoto = data.get('hitokoto', 'NULL')
        from_ = data.get('from', 'NULL')
        from_who = data.get('from_who', 'NULL')
        return f"{hitokoto}\n \t —— {from_who}《{from_}》"
    
    except requests.exceptions.RequestException as e:
        return f'Error: {e}'

def main():
    # print(get_hitokoto())
    process = subprocess.Popen(['lolcat'], stdin=subprocess.PIPE)
    process.communicate(get_hitokoto().encode())
    print()

if __name__ == '__main__':
    main()