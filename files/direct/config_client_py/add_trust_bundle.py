from suds.client import Client
from trust_bundle import TrustBundle
import sys

client = Client("http://localhost:8081/config-service/ConfigurationService?wsdl")
tb = TrustBundle(*sys.argv[1:])
tb.add_to_config(client)
