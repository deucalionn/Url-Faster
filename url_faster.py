import sys
import requests
import urllib.request


def SpamUrl(url, fichier):
    f = open(fichier, "r")
    print("---------------------------------\n")
    for line in f.readlines():
        requete = requests.post(url+line)
        try:
            urllib.request.urlopen(url+line).read()
            print(" [!] Found " + url + line)
        except:
            continue
    
    print("---------------------------------")


def main():
    print()
    print("           Url Faster")
    print("          By Deucalion\n")   
    try:
        url = sys.argv[1]
        fichier = sys.argv[2]
        SpamUrl(url, fichier)
    except:
        print("To use the script : \n")
        print("python url_faster.py <url> <wordlist>")


main()