#1
#대문자, 숫자가 암호화가 안됌-->해결

import string, os , sys
upper=string.ascii_uppercase
lower=string.ascii_lowercase
number=string.digits
def encryption(filename,num):
    a=0
    cipher=''
    
    if not os.path.isfile(filename):
        print("해당 경로에 파일이 없습니다")
        sys.exit(1)

    f= open(filename,"r")
    output=open(input('암호화 된 파일 이름'),"w")

    for line in f:
        for i in line:
            if i in lower:
                a = lower.find(i)
                b = (a+num)%26
                cipher += lower[b]
            elif i in upper:
                a = upper.find(i)
                b = (a+num)%26
                cipher += upper[b]
            else:
                if ord(i) == 32:
                    cipher += ' '
                elif ord(i)>=48 and ord(i)<=57:
                     a = number.find(i)
                     b = (a+num)%10
                     cipher += number[b]
                else:
                    cipher += i

                
    output.write(cipher)
    f.close()
    output.close()

            

def decryption(filename,num):
    a = 0
    plain_text = ''
    

    if not os.path.isfile(filename):
        print("해당 경로에 파일이 없습니다")
        sys.exit(1)

    f= open(filename,"r")
    output=open(input('복호화 된 파일 이름'),"w")

    for line in f:
        for i in line:
            if i in lower:
                a = lower.find(i)
                b = (a-num)%26
                plain_text += lower[b]
            elif i in upper:
                a = upper.find(i)
                b = (a-num)%26
                plain_text += upper[b]
            
            else:
                if ord(i) == 32:
                    plain_text += ' '
                elif ord(i)>=48 and ord(i)<=57:
                     a = number.find(i)
                     b = (a-num)%10
                     plain_text += number[b]
                else:
                    plain_text += i
   
    output.write(plain_text)
    f.close()
    output.close()


















'''
#2
import string
upper=string.ascii_uppercase
lower=string.ascii_lowercase
number=string.digits
def encryption(plain_text,num):
    a=''
    cipher=''
    for i in plain_text:
        if i in lower:
            a = lower.find(i) #lower에서 plain_text[i]와 같은 알파벳을 찾고 그것의 인덱스 값을 도출
            b = (a+num)%26
            cipher += lower[b]
            
        elif i in upper:
            a = upper.find(i)
            b = (a+num)%26
            cipher += upper[b]
            
        else:
            if ord(i) == 32:
                cipher += ' '
            elif ord(i)>=48 and ord(i)<=57:
                a = number.find(i)
                b = (a+num)%10
                cipher += number[b]
            else:
                cipher += i
                
            
    print(cipher)

def decryption(cipher,num):
    a = ''
    plain_text = ''
    for i in cipher:
        if i in lower:
            a = lower.find(i)
            b = (a-num)%26
            plain_text += lower[b]
            
        elif i in upper:
            a = upper.find(i)
            b = (a-num)%26
            plain_text += upper[b]
            
        else:
            if ord(i) == 32:
                plain_text += ' '
            elif ord(i)>=48 and ord(i)<=57:
                a = number.find(i)
                b = (a-num)%10
                plain_text += number[b]
            else:
                plain_text += i

    print(plain_text)

'''


'''
import string
upper=string.ascii_uppercase
lower=string.ascii_lowercase
number=string.digits
def encryption(plain_text,num):
    a=''
    cipher=''
    for i in range(len(plain_text)):
        if plain_text[i] in lower:
            a = lower.find(plain_text[i]) #lower에서 plain_text[i]와 같은 알파벳을 찾고 그것의 인덱스 값을 도출
            b = (a+num)%26
            cipher += lower[b]
            
        elif plain_text[i] in upper:
            a = upper.find(plain_text[i])
            b = (a+num)%26
            cipher += upper[b]
            
        else:
            if ord(plain_text[i]) == 32:
                cipher += ' '
            elif ord(plain_text[i])>=48 and ord(plain_text[i])<=57:
                a = number.find(plain_text[i])
                b = (a+num)%10
                cipher += number[b]
            
    print(cipher)

def decryption(cipher,num):
    a = ''
    plain_text = ''
    for i in range(len(cipher)):
        if cipher[i] in lower:
            a = lower.find(cipher[i])
            b = (a-num)%26
            plain_text += lower[b]
            
        elif cipher[i] in upper:
            a = upper.find(cipher[i])
            b = (a-num)%26
            plain_text += upper[b]
            
        else:
            if ord(cipher[i]) == 32:
                plain_text += ' '
            elif ord(cipher[i])>=48 and ord(cipher[i])<=57:
                a = number.find(cipher[i])
                b = (a-num)%10
                plain_text += number[b]

    print(plain_text)
'''
