import requests

# StingBox Info
url = "https://stingbox.twocyber.com/threat2/api/stingbox_api.php?api_key=UW42WXFoOHBBOXlMZkNsZ0QzWFRvZGF2cy0=&api_data=%7B%22action%22%3A%22getStingBoxDetails%22%7D"

response = requests.get(url)
data = response.json()

all_boxes = []

for stingbox in data:
    all_boxes.append(stingbox['code'])

# StingBox Alerts
alert_url = "https://stingbox.twocyber.com/threat2/api/stingbox_api.php?api_key=UW42WXFoOHBBOXlMZkNsZ0QzWFRvZGF2cy0=&api_data={%22action%22%3A%22getLatestAlerts%22}"

response = requests.get(alert_url)
alerts = response.json()

# Discovered Hosts
hosts_url = "https://stingbox.twocyber.com/threat2/api/stingbox_api.php?api_key=UW42WXFoOHBBOXlMZkNsZ0QzWFRvZGF2cy0=&api_data={%22action%22%3A%22getActiveHosts%22}"

response = requests.get(hosts_url)
hosts = response.json()