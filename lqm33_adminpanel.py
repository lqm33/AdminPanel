import requests
import os
renk="\033[96m"


os.system("cls")
print(renk+"""
██╗      ██████╗ ███╗   ███╗██████╗ ██████╗ 
██║     ██╔═══██╗████╗ ████║╚════██╗╚════██╗
██║     ██║   ██║██╔████╔██║ █████╔╝ █████╔╝
██║     ██║▄▄ ██║██║╚██╔╝██║ ╚═══██╗ ╚═══██╗
███████╗╚██████╔╝██║ ╚═╝ ██║██████╔╝██████╔╝
╚══════╝ ╚══▀▀═╝ ╚═╝     ╚═╝╚═════╝ ╚═════╝
instagram:lqm33.py

LQM33 Tarafından M3T4L'in isteği üzerine kodlanmıştır.


""")
      
print(renk+"""
1 Http var / yok
2 http var / var
3 http yok / yok
4 http yok / var


LQM33


""")
islem=input("Listenizin özelliğini seçiniz...:")

if islem=="1":
    with open("admin.txt","r") as admin:
        for ad in admin:
                ad=ad.replace('\n','')
    with open("siteler.txt","r") as siteler:
        for site in siteler:
            with open("admin.txt","r") as admin:
                for ad in admin:
                    ad=ad.replace('\n','')
                    site= site.replace('\n','')
                    url=(site+"/"+ad)
                
                
                    try:
                        try:
                            r=requests.post(url,timeout=1,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"})
                            a=r.status_code
                            a=str(a)
    
                            if "wp-submit" in r.text:
                                print(url+" [ WordPress ]")
                                
                                with open("wordpress.txt","a") as f:
                                    f.write(url + "\n")
                            
                            
                            elif "joomla" in r.text:
                                print(url +" [ Joomla ]")
                                with open("joomla.txt","a") as j:
                                    j.write(url + "\n")
                            
                            else:
                                if a=="200":
                                    print(url)
                                    with open("cıktılar.txt","a") as n:
                                        n.write(url + "\n")
                                else:
                                    pass
                        except:
                            pass
                        
                    except:
                           pass

    

elif islem=="2":
    with open("admin.txt","r") as admin:
        for ad in admin:
                ad=ad.replace('\n','')
    with open("siteler.txt","r") as siteler:
        for site in siteler:
            with open("admin.txt","r") as admin:
                for ad in admin:
                    ad=ad.replace('\n','')
                    site= site.replace('\n','')
                    url=(site+ad)
                
                
                    try:
                        try:
                            r=requests.post(url,timeout=1,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"})
                            a=r.status_code
                            a=str(a)
    
                            if "wp-submit" in r.text:
                                print(url+" [ WordPress ]")
                                
                                with open("wordpress.txt","a") as f:
                                    f.write(url + "\n")
                            
                            elif "joomla" in r.text:
                                print(url +" [ Joomla ]")
                                with open("joomla.txt","a") as j:
                                    j.write(url + "\n")
                            else:
                                if a=="200":
                                    print(url)
                                    with open("cıktılar.txt","a") as n:
                                        n.write(url + "\n")
                                else:
                                    pass
                            
                        except:
                            pass
                        
                    except:
                           pass
elif islem=="3":
   
                

    with open("admin.txt","r") as admin:
        for ad in admin:
                ad=ad.replace('\n','')
    with open("siteler.txt","r") as siteler:
        for site in siteler:
            with open("admin.txt","r") as admin:
                for ad in admin:
                    ad=ad.replace('\n','')
                    site= site.replace('\n','')
                    url=("http://"+site+"/"+ad)
                
                
                    try:
                        try:
                            r=requests.post(url,timeout=1,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"})
                            a=r.status_code
                            a=str(a)
    
                            if "wp-submit" in r.text:
                                print(url+" [ WordPress ]")
                                
                                with open("wordpress.txt","a") as f:
                                    f.write(url + "\n")
                            
                            elif "joomla" in r.text:
                                print(url +" [ Joomla ]")
                                with open("joomla.txt","a") as j:
                                    j.write(url + "\n")
                            else:
                                if a=="200":
                                    print(url)
                                    with open("cıktılar.txt","a") as n:
                                        n.write(url + "\n")
                                else:
                                    pass

                        except:
                            pass
                        
                    except:
                           pass
elif islem=="4":
    with open("admin.txt","r") as admin:
        for ad in admin:
                ad=ad.replace('\n','')
    with open("siteler.txt","r") as siteler:
        for site in siteler:
            with open("admin.txt","r") as admin:
                for ad in admin:
                    ad=ad.replace('\n','')
                    site= site.replace('\n','')
                    url=("http://"+site++ad)
                
                
                    try:
                        try:
                            r=requests.post(url,timeout=1,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"})
                            a=r.status_code
                            a=str(a)
    
                            if "wp-submit" in r.text:
                                print(url+" [ WordPress ]")
                                
                                with open("wordpress.txt","a") as f:
                                    f.write(url + "\n")
                            
                            elif "joomla" in r.text:
                                print(url +" [ Joomla ]")
                                with open("joomla.txt","a") as j:
                                    j.write(url + "\n")
                            else:
                                if a=="200":
                                    print(url)
                                    with open("cıktılar.txt","a") as n:
                                        n.write(url + "\n")
                                else:
                                    pass
                           
                        except:
                            pass
                        
                    except:
                           pass
                    
