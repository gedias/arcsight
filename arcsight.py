import requests
import json
import time
import warnings
import xml.etree.ElementTree as ET
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import pandas as pd
class arcsight(object):
    
    def __init__(self, idconecta,url):
        self.idconecta = idconecta
        self.url=url
        print(self.idconecta)
    def logon(self,user,password):
        warnings.simplefilter('ignore', InsecureRequestWarning)
        parametro={}
        parametro["login"]=user
        parametro["password"]=password
        resp = requests.get(self.url+"/core-service/rest/LoginService/login",verify=False, params=parametro)
        try:
            self.idconecta=ET.fromstring(resp.content.decode("utf8"))[0].text
        except:
            print("falha no login")
    def busca(self,busca,ini="",fim="",dataframe=False):
        if self.idconecta=="":
            print("Necessario fazer login antes")
        else:
            warnings.simplefilter('ignore', InsecureRequestWarning)
            parametro={}
            parametro["search_session_id"]=int(time.time())
            parametro["user_session_id"]=self.idconecta
            parametro["query"]=busca
            if ini != "" and fim != "":
                parametro["start_time"]=ini
                parametro["end_time"]=fim
            print(parametro)
            resp = requests.post(self.url+"/server/search",verify=False,json=parametro)
            result=json.loads(resp.content.decode("utf8"))
            print(result)
            time.sleep(1)
            print(resp.content.decode("utf8"))
            resp = requests.post(self.url+"/server/search/status",verify=False,json=parametro)
            result=json.loads(resp.content.decode("utf8"))
            print(result)
            while result["status"]=='running':
                time.sleep(10)
                print("Aguardando retorno..."+result["status"])
                resp = requests.post(self.url+"/server/search/status",verify=False,json=parametro)
                result=json.loads(resp.content.decode("utf8"))
            resp = requests.post(self.url+"/server/search/events",verify=False,json=parametro)
            if dataframe:
                dicionario=json.loads(resp.content.decode("utf8"))
                cabecalho=[]
                for campos in dicionario['fields']:
                    cabecalho.append(campos["name"])
                dados=[]
                for campos in dicionario['results']:
                    dados.append(campos)
                return pd.DataFrame(data=dados,columns=cabecalho)
            else:
                return json.loads(resp.content.decode("utf8"))
    
    
    
    
    
    #message CONTAINS \"Low disk\""
    
