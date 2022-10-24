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

#btVal=TRUE #대소문자를 구분해야 한다(오류)
#bfVal=FALSE

#btVal=true #대소문자를 구분해야 한다(오류)
#bfVal=false

#연산자
10==11
10!=11
10>=11
10<=11
10>11
10<11
nBig=100
nSmall=10
print(nBig==nSmall)
print(nBig!=nSmall)
print(nBig>=nSmall)
print(nBig<=nSmall)
print(nBig>nSmall)
print(nBig<nSmall)


#print(nBig=<nSmall) #부등호 순서에 유의해야 한다(오류)
#print(nBig=>nSmall) 

strData='data' #문자열 선언
strSci="Science"
strLecture=strData+strSci #+연산자로 문자열 합치기
strLecture

strLecture=strData+" "+strSci #""로 공백 넣어서 합치기
strLecture

strLecture.split() #split()으로 문자열 구분
lSeperate=strLecture.split()
type(lSeperate)

strHello="안녕하세요. 반갑습니다"
strHello.find("반갑") #반갑 찾아주는 함수
strHello.find("hello") #문자열 없으면 -1리턴
"반갑" in strHello #in명령어로 확인 가능. if조건문에서 활용
