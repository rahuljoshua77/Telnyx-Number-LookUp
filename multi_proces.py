import requests,os
from multiprocessing import Pool
cwd = os.getcwd()
 
def check(number):
    if "+1" in number:
        number = number.replace("+1","")
    apiKey="KEY01817170596E5033BC23D3ED6A42F1B4_MFxUOHPTfulvUmcHn4Bola"

    header = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {apiKey}" 
    }
        
    check = requests.get(f"https://api.telnyx.com/v2/number_lookup/1{number}?type=carrier&type=caller-name",headers=header).json()
    try:
        get_carrier_name = check["data"]["carrier"]["name"]
        if get_carrier_name != "":
            print(f"+1{number}: {get_carrier_name}")
            # GANTI get_carrier_name ke valid klu mau nama file nya valid
            with open(f'{get_carrier_name}.txt','a') as f: f.write(f'+1{number}|{get_carrier_name}\n')
            #with open(f'valid.txt','a') as f: f.write(f'+1{number}|{get_carrier_name}\n')
        else:
            print(f"+1{number}: Not Found")
            with open('not_valid.txt','a') as f: f.write(f'+1{number}\n')
    except:
        print(f"+1{number}: Not Found")
        with open('not_valid.txt','a') as f: f.write(f'+1{number}\n')
        
if __name__ == '__main__':
 
    file_list_akun = "data.txt"
    myfile_akun = open(f"{cwd}/{file_list_akun}","r")
    akun = myfile_akun.read()
    list_accountsplit = akun.split("\n")
    jumlah = int(input("[*] Multi Proccesing: "))
    with Pool(jumlah) as p:  
        p.map(check, list_accountsplit)