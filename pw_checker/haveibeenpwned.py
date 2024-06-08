import hashlib
import urllib3
import getpass
import re

passwrd = getpass.getpass("Gesuchtes Passwort eingeben:  ")
hashedPW = hashlib.sha1(passwrd.encode("utf-8"))

print ("Produced SHA-1 hash")
print(hashedPW.hexdigest())

hashDigit = hashedPW.hexdigest()
firstFive = hashDigit[0:5]
print ("\nRequesting Password-Checker-API (haveibeenpwned.com): \n")
makeRequest = urllib3.request("GET","https://api.pwnedpasswords.com/range/"+firstFive)

if makeRequest.status == 200:
    print("Anfrage ok!")
    responeData = makeRequest.data
    
    data = responeData.split()

    found = 0
    foundHash = []
    pat = hashedPW.hexdigest() + ":\\d.*"
    for entry in data:
        if re.search(pat,bytes.decode(entry)):
            found += 1
            foundHash.append(bytes.decode(entry))

    if found > 0:
        print("Oh nein! Dieses Passwort ist gefunden worden! Passwort umgehend ändern und nicht mehr verwenden!\n")
        print(foundHash)
    else:
        print("Alles ok. Dieses Passwort scheint sich aktuell in keinem bekannten Leak (bei haveibeenpwned) zu befinden! \n")
     
    

    