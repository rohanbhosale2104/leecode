class Solution:
    def decodeString(self, s: str) -> str:
        num_stack=[]
        str_stack=[]
        current=""
        number=0
        for ch in s:
            if ch.isdigit():
                number=number*10+int(ch)
            elif ch=="[":
                num_stack.append(number)
                str_stack.append(current)
                number=0
                current=""
            elif ch=="]":
                repeat=num_stack.pop()
                previous=str_stack.pop()
                current=previous+current*repeat
            else:
                current+=ch
        return current

        