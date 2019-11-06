#<<<<<최대한 수업시간에 배운 것 들을 활용하여 코드를 짜는게 목표>>>>>
#1 숫자가 그대로 나오고 공백을 인식하여 숫자가 채워지는 것을 해결하기 ==> 해결
#2 파일을 가져와서 파일의 내용들을 암호화하는 것 해보기

#1 caeser cipher Algorithm

from caesarfunction2 import encryption, decryption

while(True):
    signal= input('암호화 or 복호화')
    if signal=='암호화':
        Fn = input('암호화하려는 파일이름')
        N=int(input('key number'))
        encryption(Fn,N)
        print("성공")
    elif signal=='복호화':
        Fn = input('복호화하려는 파일이름')
        N = int(input('key number'))
        decryption(Fn,N)
        print("성공")
    elif signal == 'end':
        break


































'''
#2
from caesarfunction2 import encryption, decryption

while(True):
    signal= input('암호화 or 복호화')
    if signal=='암호화':
        P = input('원문')
        N=int(input('key number'))
        encryption(P,N)
    elif signal=='복호화':
        C = input('암호문')
        N = int(input('key number'))
        decryption(C,N)
    elif signal == 'end':
        break
'''
