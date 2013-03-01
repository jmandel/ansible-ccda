from suds.client import Client
from dns_entry import A, MX

client = Client("http://localhost:8081/config-service/ConfigurationService?wsdl")

import sys
record_type = sys.argv[1]

dns_class = A if record_type =="A" else MX

dns_entry = dns_class(*sys.argv[2:])

dns_entry.add_to_config(client)
