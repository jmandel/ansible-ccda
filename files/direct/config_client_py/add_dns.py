from suds.client import Client
from dns_entry import A, MX, NS

client = Client("http://localhost:8081/config-service/ConfigurationService?wsdl")

import sys
record_type = sys.argv[1]

types = {
'A': A,
'MX':MX,
'NS':NS
}

dns_class = types[record_type]

dns_entry = dns_class(*sys.argv[2:])
dns_entry.add_to_config(client)
