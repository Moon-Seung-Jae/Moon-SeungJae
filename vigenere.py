# Vigenere
# 띄어쓰기하기--->완성,파일찾기

'''
#파일 찾기
import string, os ,sys
lower = string.ascii_lowercase

def encrypt(filename,key):
    final1=[]
    final2=''
    l=len(key)
    line=''
    if not os.path.isfile(filename):
        print("해당 경로에 파일이 없습니다")
        sys.exit(1)
        
    replace = line.replace(" ","")
    f= open(filename,"r")
    output=open(input('암호화 된 파일 이름'),"w")
    
    for line in f:

        if l < len(replace):
            result = len(replace)/l
            rest = len(replace)%l
            key = key * int(result)
            for q in range(rest):
                key += key[q]
                
            for i,k in zip(replace,key):
                a = lower.find(i)
                b = lower.find(k)
                final1 += lower[(a+b)%26]

            for c in range(len(line)):
                if line[c]==' ':
                    final1.insert(c," ")

            for i in final1:
                final2 += i
            print(final2)
    else:
            
            for i,k in zip(line,key):
                a = lower.find(i)
                b = lower.find(k)
                final2 += lower[(a+b)%26]
                
            
    output.write(final2)
    f.close()
    output.close()

def decrypt(cipher,key):
    pass

P = input('암호화하려는 파일이름')
K=input('키')
encrypt(P,K)

C = input('암호문')
K=input('키')
decrypt(C,K)
'''


#1 띄어쓰기
import string
lower = string.ascii_lowercase

def encrypt(plain_text,key):
    final1=[]
    final2=''
    l=len(key)

    replace = plain_text.replace(" ","")

    if l < len(replace):
            result = len(replace)/l
            rest = len(replace)%l
            key = key * int(result)
            for q in range(rest):
                key += key[q]
                
            for i,k in zip(replace,key):
                a = lower.find(i)
                b = lower.find(k)
                final1 += lower[(a+b)%26]

            for c in range(len(plain_text)):
                if plain_text[c]==' ':
                    final1.insert(c," ")

            for i in final1:
                final2 += i
            print(final2)
    else:
            
            for i,k in zip(plain_text,key):
                a = lower.find(i)
                b = lower.find(k)
                final2 += lower[(a+b)%26]
                
            print(final2)
def decrypt(cipher,key):
    final1=[]
    final2=''
    l=len(key)

    replace = cipher.replace(" ","")

    if l < len(replace):
            result = len(replace)/l
            rest = len(replace)%l
            key = key * int(result)
            for q in range(rest):
                key += key[q]
                
            for i,k in zip(replace,key):
                a = lower.find(i)
                b = lower.find(k)
                final1 += lower[(a-b)%26]

            for c in range(len(cipher)):
                if cipher[c]==' ':
                    final1.insert(c," ")

            for i in final1:
                final2 += i
            print(final2)
    else:
            
            for i,k in zip(cipher,key):
                a = lower.find(i)
                b = lower.find(k)
                final2 += lower[(a-b)%26]
                
            print(final2)

P = input('원문')
K=input('키')
encrypt(P,K)

C = input('암호문')
K=input('키')
decrypt(C,K)



'''
import string, os ,sys
lower = string.ascii_lowercase

def encrypt(filename,key):
    final=''
    l=len(key)

    if not os.path.isfile(filename):
        print("해당 경로에 파일이 없습니다")
        sys.exit(1)
        
    f= open(filename,"r")
    output=open(input('암호화 된 파일 이름'),"w")
    for line in f:
        for i in line:
            if l < len(line):
                result = len(line)/l
                rest = len(line)%l
                key = key * int(result)

                for q in range(rest):
                    key += key[q]
                for i,k in zip(line,key):
                    a = lower.find(i)
                    b = lower.find(k)
                    final += lower[(a+b)%26]
                print(final)

            else:
                for i,k in zip(line,key):
                    a = lower.find(i)
                    b = lower.find(k)
                    final += lower[(a+b)%26]
                print(final)
    output.write(final)
    f.close()
    output.close()

def decrypt(cipher,key):
    pass
    final=''
    l = len(key)
    
    if l < len(cipher):
        result = len(cipher)/l
        rest = len(cipher)%l
        key = key * int(result)
        
        for q in range(rest):
            key += key[q]
            
        for i,k in zip(cipher,key):
            a = lower.find(i)
            b = lower.find(k)
            final += lower[(a-b)%26]
            
        print(final)
        
    else:
        
        for i,k in zip(cipher,key):
            a = lower.find(i)
            b = lower.find(k)
            final += lower[(a-b)%26]
            
        print(final)

P = input('암호화하려는 파일이름')
K=input('키')
encrypt(P,K)

C = input('암호문')
K=input('키')
decrypt(C,K)
'''







'''
import string
lower = string.ascii_lowercase

def encrypt(plain_text,key):
    final=''
    l=len(key)
    
    if l < len(plain_text):
        result = len(plain_text)/l
        rest = len(plain_text)%l
        key = key * int(result)
        
        for q in range(rest):
            key += key[q]
            
        for i,k in zip(plain_text,key):
            a = lower.find(i)
            b = lower.find(k)
            final += lower[(a+b)%26]
            
        print(final)
        
    else:
        
        for i,k in zip(plain_text,key):
            a = lower.find(i)
            b = lower.find(k)
            final += lower[(a+b)%26]
            
        print(final)

def decrypt(cipher,key):
    final=''
    l = len(key)
    
    if l < len(cipher):
        result = len(cipher)/l
        rest = len(cipher)%l
        key = key * int(result)
        
        for q in range(rest):
            key += key[q]
            
        for i,k in zip(cipher,key):
            a = lower.find(i)
            b = lower.find(k)
            final += lower[(a-b)%26]
            
        print(final)
        
    else:
        
        for i,k in zip(cipher,key):
            a = lower.find(i)
            b = lower.find(k)
            final += lower[(a-b)%26]
            
        print(final)

P = input('원문')
K=input('키')
encrypt(P,K)

C = input('암호문')
K=input('키')
decrypt(C,K)
'''
