from pickle import FALSE, TRUE


strVal = 'data science'        
nVal = 12345                
fVal = 1.2                         
lVal = ['data', 'science']            
dVal = {'lecture' : 'data science'}   
bVal = True
#기본적인 주석은 이렇게
'''
이런 형태도 사용한다.
'''                  
strVal
nVal
fVal
lVal
dVal
bVal
print('strVal:',strVal)     
print('nVal:',nVal)    
print('fVal:',fVal)    
print('lVal:',lVal)    
print('dVal:',dVal)    
print('bVal:',bVal)        
print('strVal:',type(strVal))     
print('nVal:',type(nVal))    
print('fVal:',type(fVal))    
print('lVal:',type(lVal))    
print('dVal:',type(dVal))    
print('bVal:',type(bVal))  

'''
같은 변수명인 경우 이전 데이터를 덮어쓴다
'''
nVal=16
fVal=3.14
print('10진수 표현: ',nVal)
print('2진수 표현: ',bin(nVal))
print('8진수 표현: ',oct(nVal))
print('16진수 표현: ',hex(nVal))

btVal=True
bfVal=False

btVal=TRUE #대소문자를 구분해야 한다
bfVal=FALSE

btVal=true #대소문자를 구분해야 한다
bfVal=False
