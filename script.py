import json
import requests

response_json = json.loads( requests.get("https://raw.githubusercontent.com/gorhill/uBlock/master/assets/assets.json").text )

list_of_urls = []

for group in response_json:
    if response_json[group]['content'] == "filters" and response_json[group]["group"] != "regions":
        if "cdnURLs" not in response_json[group]:
            if type(response_json[group]["contentURL"]) is list:
                list_of_urls.append(response_json[group]["contentURL"][0])
            else:
                list_of_urls.append(response_json[group]["contentURL"])
        else:
            list_of_urls.append(response_json[group]["cdnURLs"][0])

concat_list = ""

for url in list_of_urls:
    concat_list += requests.get(url).text
    concat_list += "\n\n\n"

with open("concatenated_list.txt", 'w') as file:
    file.write(concat_list)