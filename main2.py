import requests
import re
import json

r = requests.get("https://alexwohlbruck.github.io/cat-facts/docs/endpoints/facts.html")
l = re.findall('</span><span class="nl">"(.*?)"</span><span class="p">:</span><span class="w"> </span><span class="(.*?)">(.*?)</span><span class="p">,</span><span class="w">', r.text)
dict_for_json = {}
for i in l:
    dict_for_json.update({i[0]: i[2]})
x = json.dumps(dict_for_json)