class Solution:
    def reverse(self, x: int) -> int:
        if(x==0):
            return 0
        else:
            z=0
            x=str(x)
            if(x[0]=='-'):
                x=x.replace('-','')
                z=1
            x=list(x)
            p=copy.deepcopy(x)
            while(1): 
                o=p.pop()
                if(o!='0'):
                    break
                else:
                    x=copy.deepcopy(p)
            x=x[::-1]
            x=''.join(x)
            if(z==1):
                x='-'+x
            if((int(x)>-2147483648)and(int(x)<2147483647)):
                return x
            else:
                return 0
