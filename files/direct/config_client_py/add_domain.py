from suds.client import Client
from domain import Domain
import sys

domain_name = sys.argv[1]
postmaster = sys.argv[2]

client = Client("http://localhost:8081/config-service/ConfigurationService?wsdl")

d = Domain(domain_name,postmaster)
d.add_to_config(client)
