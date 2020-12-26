import hashlib
import hmac
#based on primedice roll
#serverSeed is the key
#clientseed-Nonce is the message
def roll(serverSeed, clientSeed, Nonce):
    msg = clientSeed+"-"+str(Nonce)
    result = hmac.new(key=serverSeed.encode(),msg=msg.encode(),digestmod=hashlib.sha512)
    result = result.hexdigest()
    value = int(result[:5],16)*1.0
    while value>=1000000 and len(result)>=5:
        result = result[5:]
        value = int(result[:5],16)*1.0
    if value>=1000000:
        value = 999999
    value = value%10000
    value = value/100.0
    return round(value,2)

#print(roll("88d5af39a8c6d70e63743b4754e75b606b7bf49021498f522c5e409711da284f","55cb2fcb7d",1239))     