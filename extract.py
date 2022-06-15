import requests
import time
from csv import writer
from datetime import datetime
import pandas as pd

#for timer
starttime = time.time()

while True:
    #specify URL
    target_url_BTC = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD"
    target_url_ETH = "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD"
    target_url_SOL = "https://min-api.cryptocompare.com/data/price?fsym=SOL&tsyms=USD"
    target_url_BNB = "https://min-api.cryptocompare.com/data/price?fsym=BNB&tsyms=USD"
    target_url_XRP = "https://min-api.cryptocompare.com/data/price?fsym=XRP&tsyms=USD"
    target_url_ADA = "https://min-api.cryptocompare.com/data/price?fsym=ADA&tsyms=USD"
    target_url_DOGE = "https://min-api.cryptocompare.com/data/price?fsym=DOGE&tsyms=USD"
    target_url_DOT = "https://min-api.cryptocompare.com/data/price?fsym=DOT&tsyms=USD"
    target_url_TRX = "https://min-api.cryptocompare.com/data/price?fsym=TRX&tsyms=USD"
    target_url_AVAX = "https://min-api.cryptocompare.com/data/price?fsym=AVAX&tsyms=USD"

    #request responses
    response_BTC = requests.get(target_url_BTC)
    response_ETH = requests.get(target_url_ETH)
    response_SOL = requests.get(target_url_SOL)
    response_BNB = requests.get(target_url_BNB)
    response_XRP = requests.get(target_url_XRP)
    response_ADA = requests.get(target_url_ADA)
    response_DOGE = requests.get(target_url_DOGE)
    response_DOT = requests.get(target_url_DOT)
    response_TRX = requests.get(target_url_TRX)
    response_AVAX = requests.get(target_url_AVAX)

    data_BTC = response_BTC.text 
    data_ETH = response_ETH.text
    data_SOL = response_SOL.text
    data_BNB = response_BNB.text
    data_XRP = response_XRP.text
    data_ADA = response_ADA.text 
    data_DOGE = response_DOGE.text
    data_DOT = response_DOT.text
    data_TRX = response_TRX.text 
    data_AVAX = response_AVAX.text 

    #establish timestamp
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d-%b-%Y %H:%M:%S.%f")

    #remove unnecessary characters
    for char in '""{}':  
        data_BTC = data_BTC.replace(char,'')
        data_ETH = data_ETH.replace(char,'')
        data_SOL = data_SOL.replace(char,'')
        data_BNB = data_BNB.replace(char,'')
        data_XRP = data_XRP.replace(char,'')
        data_ADA = data_ADA.replace(char,'')
        data_DOGE = data_DOGE.replace(char,'')
        data_DOT = data_DOT.replace(char,'')
        data_TRX = data_TRX.replace(char,'')
        data_AVAX = data_AVAX.replace(char,'')

    #convert string into list
    data_list_BTC = data_BTC.split(":") 
    data_list_ETH = data_ETH.split(":") 
    data_list_SOL = data_SOL.split(":") 
    data_list_BNB = data_BNB.split(":") 
    data_list_XRP = data_XRP.split(":") 
    data_list_ADA = data_ADA.split(":") 
    data_list_DOGE = data_DOGE.split(":") 
    data_list_DOT = data_DOT.split(":") 
    data_list_TRX = data_TRX.split(":") 
    data_list_AVAX = data_AVAX.split(":") 

    #add timestamp into list 
    data_list_BTC += [timestampStr]
    data_list_ETH += [timestampStr]
    data_list_SOL += [timestampStr]
    data_list_BNB += [timestampStr]
    data_list_XRP += [timestampStr]
    data_list_ADA += [timestampStr]
    data_list_DOGE += [timestampStr]
    data_list_DOT += [timestampStr]
    data_list_TRX += [timestampStr]
    data_list_AVAX += [timestampStr]
    
    #append into BTC csv
    with open('BTC.csv', 'a', newline='') as f_object:
    
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)
    
        # Pass the list as an argument into
        # the writerow()
        writer_object.writerow(data_list_BTC)
    
        #Close the file object
        f_object.close()
    
    #remove any blank rows
    df = pd.read_csv('BTC.csv')
    df.to_csv('BTC.csv', index=False)

    #append into ETH csv
    with open('ETH.csv', 'a', newline='') as f_object:
    
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)
    
        # Pass the list as an argument into
        # the writerow()
        writer_object.writerow(data_list_ETH)
    
        #Close the file object
        f_object.close()
    
    #remove any blank rows
    df = pd.read_csv('ETH.csv')
    df.to_csv('ETH.csv', index=False)

    #append into SOL csv
    with open('SOL.csv', 'a', newline='') as f_object:
    
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)
    
        # Pass the list as an argument into
        # the writerow()
        writer_object.writerow(data_list_SOL)
    
        #Close the file object
        f_object.close()
    
    #remove any blank rows
    df = pd.read_csv('SOL.csv')
    df.to_csv('SOL.csv', index=False)

    #append into BNB csv
    with open('BNB.csv', 'a', newline='') as f_object:
    
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)
    
        # Pass the list as an argument into
        # the writerow()
        writer_object.writerow(data_list_BNB)
    
        #Close the file object
        f_object.close()
    
    #remove any blank rows
    df = pd.read_csv('BNB.csv')
    df.to_csv('BNB.csv', index=False)

    #append into XRP csv
    with open('XRP.csv', 'a', newline='') as f_object:
    
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)
    
        # Pass the list as an argument into
        # the writerow()
        writer_object.writerow(data_list_XRP)
    
        #Close the file object
        f_object.close()
    
    #remove any blank rows
    df = pd.read_csv('XRP.csv')
    df.to_csv('XRP.csv', index=False)

    #append into ADA csv
    with open('ADA.csv', 'a', newline='') as f_object:
    
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)
    
        # Pass the list as an argument into
        # the writerow()
        writer_object.writerow(data_list_ADA)
    
        #Close the file object
        f_object.close()
    
    #remove any blank rows
    df = pd.read_csv('ADA.csv')
    df.to_csv('ADA.csv', index=False)

    #append into DOGE csv
    with open('DOGE.csv', 'a', newline='') as f_object:
    
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)
    
        # Pass the list as an argument into
        # the writerow()
        writer_object.writerow(data_list_DOGE)
    
        #Close the file object
        f_object.close()
    
    #remove any blank rows
    df = pd.read_csv('DOGE.csv')
    df.to_csv('DOGE.csv', index=False)

    #append into DOT csv
    with open('DOT.csv', 'a', newline='') as f_object:
    
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)
    
        # Pass the list as an argument into
        # the writerow()
        writer_object.writerow(data_list_DOT)
    
        #Close the file object
        f_object.close()
    
    #remove any blank rows
    df = pd.read_csv('DOT.csv')
    df.to_csv('DOT.csv', index=False)

    #append into TRX csv
    with open('TRX.csv', 'a', newline='') as f_object:
    
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)
    
        # Pass the list as an argument into
        # the writerow()
        writer_object.writerow(data_list_TRX)
    
        #Close the file object
        f_object.close()
    
    #remove any blank rows
    df = pd.read_csv('TRX.csv')
    df.to_csv('TRX.csv', index=False)

    #append into AVAX csv
    with open('AVAX.csv', 'a', newline='') as f_object:
    
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)
    
        # Pass the list as an argument into
        # the writerow()
        writer_object.writerow(data_list_AVAX)
    
        #Close the file object
        f_object.close()
    
    #remove any blank rows
    df = pd.read_csv('AVAX.csv')
    df.to_csv('AVAX.csv', index=False)
    
    time.sleep(15.0 - ((time.time() - starttime) % 15.0))
        