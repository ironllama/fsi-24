import requests
import json
import time
import random

page = 1
max = 0

results = []

while True:
    print("Getting page: ", page)

    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'Cookie': '_cfuvid=MBsr6QpvSzq6_gx8ROHvpZFcfwgKVvMgTuDjLge7qLs-1716446197786-0.0.1.1-604800000; cf_clearance=P.00rGeuYQd84mR6TH2ZBe0NJShZq52mDKHJaNa7Lqk-1716446240-1.0.1.1-g17mMhl.KQDqG7B4P5YycvD_cvpi69a0QAJ2QLS6RFtf32Z4Qvh9xRvwf.24VC3dCxwdD33_C.L4ulP_GF6dkg; __cf_bm=VTdaSLytFdT4TocGVfnVhOtW7dJFG7P_Wsb1dxE9g80-1716447349-1.0.1.1-.GsSNf7teNrRPH_rIzrnhZhhk8j161yt0mVO_2vUbCOzjH543D3R46YyQa9tje_GHow5PW5P0xDbyJ6pVAzkaw'
        }

    try:
        first_page = requests.get(
            "https://api.fbi.gov/wanted/v1/list?page=" + str(page),
            headers=headers
            )
        first_page = first_page.json()
    except Exception as e:
        print("ERROR:", e, first_page.text)

    results += first_page["items"]

    if max == 0:
        max = first_page["total"]
    
    if len(results) >= max:
        break

    page += 1
    time.sleep(random.randint(1, 5))

with open("allMostWanted.json", "w") as f:
    json.dump(results, f)
