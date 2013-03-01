class Domain(object):

    def __init__(self, domain_name, postmaster_email):
        self.domain_name = domain_name
        self.postmaster_email = postmaster_email

    def add_to_config(self, client):
        client.service.removeDomain(self.domain_name)

        d = client.factory.create("ns0:domain")
        d.domainName = self.domain_name
        d.postMasterEmail = self.postmaster_email
        d._status = "ENABLED"
        client.service.addDomain(d)
