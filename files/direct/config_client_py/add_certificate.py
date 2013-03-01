from suds.client import Client
from certificate import Certificate
import sys

client = Client("http://localhost:8081/config-service/ConfigurationService?wsdl")

cert = Certificate(sys.argv[1])
cert.add_to_config(client)
