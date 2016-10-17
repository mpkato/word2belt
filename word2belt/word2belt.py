import requests
import json
from requests.auth import HTTPBasicAuth

class Word2Belt(object):
    def __init__(self, url, username, password, filename):
        self.url = url
        self.username = username
        self.password = password
        self.filename = filename

    def get(self, word):
        auth = HTTPBasicAuth(self.username, self.password)
        params = {'w': word, 'filename': self.filename}
        res = requests.get(self.url, params=params, auth=auth)
        if res.status_code == requests.codes.ok:
            data = json.loads(res.text)
            if "vector" in data:
                return data["vector"]
            elif "error" in data:
                raise Exception(data["error"])
            else:
                raise Exception("Unknown Error: %s" % self)
        else:
            res.raise_for_status()
