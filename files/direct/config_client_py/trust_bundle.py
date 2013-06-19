import OpenSSL.crypto as crypto
from datetime import datetime
import itertools


class TrustBundle(object):

    def __init__(self, name, url, refresh_interval=86400):
        self.name=name
        self.url=url
        self.refresh_interval=refresh_interval

    def add_to_config(self, client):
        tb = client.factory.create("ns0:trustBundle")
        tb.id = 0 # TODO: not sure why but this avoids err.
        tb.bundleName = self.name
        tb.bundleURL = self.url
        tb.refreshInterval = self.refresh_interval
       	print "adding %s"%self.name 
        existing= client.service.getTrustBundleByName(self.name)
        if (existing): 
            client.service.deleteTrustBundles(existing.id)
            print "Deleted existing %s"%existing.id
        
        client.service.addTrustBundle(tb)
        bundle= client.service.getTrustBundleByName(self.name)
        domains = client.service.listDomains()
        
        for domain in domains:
            print "and adding %s to %s %s"%(self.name, domain, bundle)
            dass = {}
            dass['incoming']=True
            dass['outgoing']=True
            dass['domainId']=domain._id
            dass['trustBundleId']=bundle.id
            client.service.associateTrustBundleToDomain(**dass)
