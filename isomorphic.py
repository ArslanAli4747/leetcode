def isIsomorphic(s: str, t: str) -> bool:
        found = True
        dic = {}
        dic2 = {}

        for a,b in zip(s,t):
            if (a in dic and dic[a]!=b) or(b in dic2 and dic2[b]!=a):
                found = False
                break
            dic[a]=b
            dic2[b] =a
        return found