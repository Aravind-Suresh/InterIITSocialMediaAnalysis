from instagram.client import InstagramAPI
from random import randint
import sys
from collections import OrderedDict

class InstagramExtract:
    def authenticate(self, cred):
        return InstagramAPI(client_id=cred["client_id"],
        client_secret=cred["client_secret"], client_ips= cred["client_ip"],
        access_token=cred["access_token"])

    def __init__(self, cred):
        self.api = self.authenticate(cred)

    def fetchData(self, keywords, limit=80, maxPages=3):
        mediaAllIds = []
        # TODO: Check if Instagram API accepts array of keywords
        mediaIds, nextUrl = self.api.tag_recent_media(tag_name=keywords, count=limit)
        _, maxTagId = nextUrl.split('max_tag_id=')
        maxTagId = str(maxTagId)

        for idObj in mediaIds:
            mediaAllIds.append(idObj.id)

        ctr = 1

        while nextUrl and ctr < maxPages:
            mediaNewIds, nextUrl = api.tag_recent_media(tag_name=keywords, max_tag_id=maxTagId)
            _, maxTagId = nextUrl.split('max_tag_id=')
            maxTagId = str(maxTagId)

            for idObj in mediaNewIds:
                mediaAllIds.append(idObj.id)

            ctr += 1

        return list(OrderedDict.fromkeys(mediaAllIds))
