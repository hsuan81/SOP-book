# download file from web
import requests
res = requests.get('http://automatetheboringstuff.com/files/rj.txt')

# verify the request to the server
'''if res.status_code == requests.codes.ok:
    print(len(res.text))
    print(res.text[:300])'''

# alternative way to verify and deal with the exception
try:
    res.raise_for_status()
except Exception as exc:
    print("There was a problem: %s" % exc)

playFile = open('RomeoandJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
print("File is established")

playFile.close()


