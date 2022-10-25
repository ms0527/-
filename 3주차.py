#변수
strVal='data science'
nVal=12345
fVal=1.2
lVal=['data','science']
dVal={'lecture','science'}
bVal=True
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

#자료형
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

#문자열
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

strHello.replace('.','?')
strHello.replace("하세요","하셔유")
strHello #이렇게만 하면 원본 데이터는 변하지 않음

strNewHello=strHello.replace('.','?')
strNewHello=strNewHello.replace("하세요","하셔유")
strNewHello #이렇게 하면 안녕하셔유? 반갑습니다 라고 나온다.
strHello.strip('반갑습니다') #strip은 ()안에 제거하는 함수
strHello #이렇게만 하면 원본 데이터는 변하지 않음. strNewHello처럼 만들어줘야함

#리스트 기본개념
lnData=[1,2,3,4,5]
print(lnData)
print('type: ',type(lnData))

#인덱싱
print(lnData[0])
print(lnData[3])
lnData[0]=lnData[4] #4번인덱스 값을 0번인덱스에 저장
print(lnData)

#슬라이싱
print(lnData[2:4]) #2번인덱스부터 4번인덱스 미만까지(3,4만 출력)

#기본연산
lnData=[1,2,3,4,5]
lstrData=['a','b','c']

lnData+lstrData #다른 자료형 리스트끼리 합침
lnData.append(10) #10을 맨 뒤에 추가
lnData
lnData.insert(0,'python') #0번인덱스에 문자열 추가
lnData

lnData.remove('python')
lnData

del lnData[5] #인덱스를 지정하여 삭제
lnData

lnData
lnData.pop(0) #0번인덱스 데이터 삭제
lnData.pop() #()비어있으면 마지막 인덱스 삭제
lnData
lnData.clear() #리스트의 모든 데이터 삭제
lnData

#튜플
tVal=("사과","딸기","바나나","토마토","키위")
print(tVal)
print(type(tVal))
# tVal[0]="포도" 튜플에 저장된 데이터는 변경이 안된다.

tData=(1,2,3,1,2,3,4,5,1,2,7)
tData.count(1) #1이 몇개 있는지 세어준다

len(tVal) #전체 데이터 개수 확인
len(tData)

print(tData[2:5]) #튜플 슬라이싱
tTuple=tVal+tData
print(tTuple)

tData*2
tData

tData2=tData*2
print(tData2)

print("tVal memory=",hex(id(tVal)))
tVal=tVal*2
print("tVal memory=",hex(id(tVal)))
print(tVal)

print("tVal memory=",hex(id(tVal)))
tVal=tVal+tVal
print("tVal memory=",hex(id(tVal)))
print(tVal)

#set
sVal={1,2,3,4,5}
print(sVal)
print(type(sVal))

#sVal[1:2] #리스트나 튜플같은 인덱스가 없기 때문에 인덱싱 연산은 불가함(오류)
sVal.add(100) #add함수로 데이터 추가하기
print(sVal)

sVal.update([200,300]) #update함수로 여러 개의 데이터 추가
print(sVal)

sVal.remove(200) #remove함수로 삭제하기
print(sVal)

sVal.clear()
print(sVal) #데이터 초기화

sVal={100,200,300,400,500}
sData={"a","b","c","c",100,300}
print(sVal)
print(sData) #c는 한개로 나옴

sVal.intersection(sData) #교집합 함수
sVal.difference(sData) #차집합 함수
sVal-sData #차집합 -로도 표현 가능
sVal.union(sData) #합집합 함수
#sVal+sData #합집합 +로 표현 불가
sVal.symmetric_difference(sData) #합집합에서 교집합을 뺀 집합

#딕셔너리 (key, value로 표현한 구조)
dVal={
    'name':'이컴공',
    'email':'computer@hoseo.edu',
    'address':'충남 아산시'
}
print(dVal)
print(type(dVal))

dData={
    "사과":300,
    "포도":200,
    "배":500,
    "키위":100
}
print(dData["배"]) #키를 이용한 검색
dData.get("배") #get함수로 검색

dData["딸기"]=100 #항목 추가
print(dData)

dData.pop("사과") #항목 삭제
dData
#dData.pop() #오류
sorted(dData) #정렬
sorted(dData.values()) #정렬
dData #위에처럼 정렬해도 실제 dData에는 변화가 없다.

#함수
def f(x):
    return x+10
f(2) #들여쓰기 중요함

#내장함수
strText=input("아무 문장이나 입력하세요: ")
print(strText)

#list를 사용한 다차원 배열
flVal=[1.0,2.0,3.14,4.2,5.1]
arVal=[flVal,flVal,flVal]
arVal
arVal[0]
arVal[1]
arVal[1][2] #1번에 2번인덱스

arVal[0]='python'
arVal #0번이 아예 python이 됨

arVal[0][2] #t만 출력됨
arVal[0]='python programming'
arVal

#numpy배열
import numpy as np
arData=np.array([1.0,2.0,3.14,4.2,5.1])
arData

arData.sum()
#에러 arVal.sum()
print(type(arVal))
print(type(arData))
arData.std() #배열의 표준편차 출력
arData.cumsum() #누적 합 출력

arData*2
arData**2
np.sqrt(arData)

arVal=np.array([arData,arData**2])
arVal
arVal.sum(axis=0)
arVal.sum(axis=1)
np.array([0,0,0],[0,0,0])
arZero=np.zeros((2,3),dtype='i')
arZero

#시리즈
import pandas as pd
pandas_series=pd.Series([30,20,10],index=['국어','영어','수학'])
print(type(pandas_series))
pandas_series #세로로 국어 영어 수학 / 30 20 10

pandas_series[1:] #영어, 수학, 타입
pandas_series[0]
#에러 pandas_series[0][1] 