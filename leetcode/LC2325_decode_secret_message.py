class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        key = key.replace(" ", "")
        key = "".join(OrderedDict.fromkeys(key))
        unlock = {}
        for i in range(len(key)): unlock[key[i]] = alphabet[i]
        secret = ""
        for i in range(len(message)): 
            if message[i] != " ": secret += unlock[message[i]]
            else: secret += " "
        return secret