from suds.client import Client
import sys

setting_name = sys.argv[1]
setting_value = sys.argv[2]

client = Client("http://localhost:8081/config-service/ConfigurationService?wsdl")

client.service.deleteSetting(names=[setting_name])
client.service.addSetting(name=setting_name, value=setting_value)
