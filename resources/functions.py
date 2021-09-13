def geturl(self, url):
    return self.get(url)


def getjson(self):
    return self.json()


def getstatuscode(self):
    return self.status_code


def getname(self):
    return self['name']


def getid(self):
    return self['id']


def getcount(self):
    return self["info"]["count"]


def getcharactercount(self):
    return len(self['characters'])


def getepisodecount(self):
    return len(self['episode'])
