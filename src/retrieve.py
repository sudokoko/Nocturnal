import os

def pidlist(cccc):
  os.system("curl -X 'GET' \
    'https://mesonet.agron.iastate.edu/api/1/nws/afos/list.json?cccc=" + cccc + "' \
    -H 'accept: application/json'")
  
def gettext(pid):
  os.system("curl -X 'GET' \
  'https://mesonet.agron.iastate.edu/api/1/nwstext/" + pid + "' \
  -H 'accept: application/json'")
  
def mnettime():
  os.system("curl -X 'GET' \
  'https://mesonet.agron.iastate.edu/api/1/servertime' \
  -H 'accept: application/json'")
