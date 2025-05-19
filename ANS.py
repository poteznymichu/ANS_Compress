
import math
from typing import Optional
class ANS:

    def __init__(self):
        self.text: str = ""
        self.encoded: float = 0
        self.decoded: str = ""  
    
    # def is_text(self) -> bool:
    #     return isinstance(self.text, str) and all(c in '01' for c in self.text)

    def encode_uABS(self, text: str="",p1: float=0.5) -> int:
        x:float = 1
        for bit in text:
            if bit == '0':
                x = math.ceil((x+1) / (1-p1)) - 1
            elif bit == '1':
                x = math.floor(x / p1)
            else:
                raise ValueError("Invalid character in text. Only '0' and '1' are allowed.")
        return x
    
    def decode_uABS(self, x: float = 0,p1: float=0.5) -> str:
        print(f"Jaki wejsciowy x: {x}")
        result:str = ""
        while x > 1:
            s = math.ceil((x+1) * p1) - math.ceil(x*p1)
            print(f"X+1 : {x+1}")
            print(f"X : {x}")
            print(f"Jakie s: {s}")
            result += str(s)
            if s == 0:
                x -= math.ceil(x * p1)
            elif s == 1:
                x = math.ceil(x * p1)
            else:
                raise ValueError("Invalid value for s. Only 0 and 1 are allowed.")
        decoded_text:str = result[::-1]
        return decoded_text
    

ans = ANS()
print("Encoding:", ans.encode_uABS("0100",0.6))
res = ans.encode_uABS("0100",0.6)
print(res)
print(f"Decoding:",ans.decode_uABS(res,0.6))