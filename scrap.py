import requests, json, yaml
from seleniumwire import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options  

config = yaml.load(open('config.yaml', 'r'), Loader=yaml.FullLoader)
match_id = config['full-url'].split('/')[-1].split('.')[-1]
web_name = config['full-url'].split('/')[-1].split('.')[0]
url_ = "https://shopee.co.id/api/v2/search_items/?by=relevancy&limit=" + str(config['data-per-page']) + "&match_id=" + match_id + "&newest="
_url = "&order=desc&page_type=search&version=2"
store_data = open(config['file-store-location'] + web_name + '.json', 'w')
chrome_options = Options()  
chrome_options.add_argument("--headless")  

store_data.write('[')
total = 0
for i in range(config['max-page']):
    headers = {}
    browser = webdriver.Chrome(config['webdriver-path'], chrome_options=chrome_options)
    # sleep(1)
    url = url_ + str(i * config['data-per-page']) + _url
    while 1:
        try:
            browser.get(config['full-url'] + '?page=' + str(i))
            for _ in range(100):
                for request in browser.requests:
                    if request.path == url:
                        try:
                            headers = request.headers
                            break
                        except:
                            pass
                if headers != {}:
                    break
            break
        except:
            pass
    if headers == {}:
        continue
    requestResult = requests.get(url=url, headers=headers).text
    requestResultParsed = json.loads(requestResult)
    for x in requestResultParsed['items']:
        if i + 1 == config['max-page'] and x == requestResultParsed['items'][-1]:
            store_data.write(json.dumps(x) + "\n")
        else:
            store_data.write(json.dumps(x) + ",\n")
    browser.close()
    total += len(requestResultParsed['items'])
    print('Page', i + 1, 'done, Total', len(requestResultParsed['items']), 'data')
store_data.write(']')
print('Done, Total', len(requestResultParsed['items']), 'data')