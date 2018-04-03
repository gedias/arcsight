# arcsight
Api python para acesso ao logger do arcsight

---
metodos
=
arcsight
-
Este é o metodo de criação do objeto, e possui dois parâmetros:
* **id conexão** um numero inteiro para servir de id da conexão.
* **url**: URL do servidor.

Metodos do objeto arcsight
=
Estes metodos serão usados no objeto criado apartir do metodo arcsight.

logon
-
Este metodo é usado para efetuar login no logger, e possui dois parâmetros:
* user: usuario para login
* password: senha para login.

busca
-
Este metodo é usado para efetuar a busca no logger (arcsight ), e possui 4 parâmetros:
* **busca**: string da busca exemplo: **"categoryBehavior=/Authentication/Verify and categoryOutcome=/Failure"** para busca de falha de login.
* **ini**: Data inicial do intervalo da busca.
* **fim**: Data final do intervalo da busca.
* **dataframe**: Define se retorna um dataframe do pandas ou não,aceita True ou False ( o default é False) 

Obs.: deve usar o formato de data "AAAA-MM-DDTHH:mm:ss.ms-TZHH:TZmm":
* **AAAA**: Ano com 4 digitos.
* **MM**: Mês com 2 digitos.
* **DD**: Dia com 2 digitos.
* **T**: Padrão do formato, indica que irá ser passado a hora ( deve-se usar a letra "T" mesmo ).
* **HH**: hora com 2 digitos ( formato 24h).
* **mm**: minutos com 2 digitos.
* **ss**: segundos com 2 digitos.
* **ms**: mili segundos.
* **+/-**: serve para especificar o timezone, se é positivo ou negativo
* **TZHH**: hora do time zone.
* **TZmm**: hora do time zone.

Ex.: para especificar dia 27 de março de 2018 as 07:15:00 no Brasil ( GMT-3 ):
    **2018-03-27T07:15:00.000-03:00**

Programa de exemplo usando esta classe:
==

    import arcsight
    import time
    #Devemos passar um numero como id de conexão e url do servidor
    logger=arcsight.arcsight(int(time.time()),"https://192.168.3.14:9000/")
    logger.logon("geisler","senha")
    busca="categoryBehavior=/Authentication/Verify and categoryOutcome=/Failure"    
    #retornando a busca em um dicionario
    dicionario=logger.busca(busca,ini="2018-03-27T00:00:00.000-03:00", fim="2018-03-28T00:00:00.000-03:00")
    #retornando a busca em um dataframe
    df=logger.busca(busca,ini="2018-03-27T00:00:00.000-03:00", fim="2018-03-28T00:00:00.000-03:00",dataframe=True)

Instalação de requisitos:
=
    pip3 install -r requirements.txt

*Obs.: o pip deve ser referente ao python3.*
