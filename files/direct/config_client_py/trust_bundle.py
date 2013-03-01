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
        
        existing= client.service.getTrustBundleByName(self.name)
        if (existing): client.service.deleteTrustBundles(existing.id)
        
        client.service.addTrustBundle(tb)
        bundles = client.service.getTrustBundles()
        domains = client.service.listDomains()
        
        for domain, bundle in itertools.product(domains, bundles):
            dass = {}
            dass['incoming']=True
            dass['outgoing']=True
            dass['domainId']=domain._id
            dass['trustBundleId']=bundle.id
            client.service.associateTrustBundleToDomain(**dass)
