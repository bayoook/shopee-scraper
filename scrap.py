import requests, json, yaml

config = yaml.load(open('config.yaml', 'r'), Loader=yaml.FullLoader)
url_ = "https://shopee.co.id/api/v2/search_items/?by=relevancy&limit=" + str(config['data-per-page']) + "&match_id=" + str(config['match-id']) + "&newest="
_url = "&order=desc&page_type=search&version=2"
store_data = open(config['file-store-location'], 'w')

for i in range(config['max-page']):
    userAgent = 'curl'
    url = url_ + str(i * config['data-per-page']) + _url
    requestResult = requests.get(url, headers={"user-agent": userAgent}).text
    requestResultParsed = json.loads(requestResult)['items']
    for x in requestResultParsed:
        store_data.writelines(json.dumps(x))