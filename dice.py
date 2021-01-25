import hashlib
import hmac
DEFAULT_SERVER_SEED = "88d5af39a8c6d70e63743b4754e75b606b7bf49021498f522c5e409711da284f"
DEFAULT_CLIENT_SEED = "55cb2fcb7d"
#based on primedice roll
#serverSeed is the key
#clientseed-Nonce is the message

class dice:
    def __init__(self,serverSeed=DEFAULT_SERVER_SEED, clientSeed=DEFAULT_CLIENT_SEED):
        self.serverSeed = serverSeed
        self.clientSeed = clientSeed
        self.nonce = 0
        
    def roll(self):
        msg = self.clientSeed+"-"+str(self.nonce)
        result = hmac.new(key=self.serverSeed.encode(),msg=msg.encode(),digestmod=hashlib.sha512)
        result = result.hexdigest()
        value = int(result[:5],16)*1.0
        while value>=1000000 and len(result)>=5:
            result = result[5:]
            value = int(result[:5],16)*1.0
        if value>=1000000:
            value = 999999
        value = value%10000
        value = value/100.0
        self.nonce += 1
        return round(value,2)

    def getserverSeed(self):
        return self.serverSeed
    
    def setserverSeed(self, serverSeed):
        self.serverSeed = serverSeed
    
    def getclientSeed(self):
        return self.clientSeed
    
    def setclientSeed(self, clientSeed):
        self.clientSeed = clientSeed

    def getnonce(self):
        return self.nonce
        
    def setnonce(self, nonce):
        self.nonce = nonce
    

if __name__ == '__main__':
    ROLL = dice()
    print(ROLL.roll())
