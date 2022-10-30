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

#4주차
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
from cProfile import label
import imp
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

#DATAFRAME
df=pd.DataFrame([30,20,10],columns=['score'],index=['국어','영어','수학'])
df
df.index #index표시
df.columns #colums표시
df.loc['국어']
df.sum()
df.score**2 #columns값 제곱 출력인데 그럼 df.columns**2 아닌가 질문하기
df['score2']=(50,50,50)
df
df['score2']=pd.DataFrame([90,90,90],index=['국어','영어','수학'])
df #score2만든거임

del df['score']
df['score2']=(90,90,90,100) #에러

df['score2']=pd.DataFrame([90,90,90,100],index=['국어','영어','수학','윤리'])
df

df1=pd.DataFrame([1,2,3],columns=['A'])
df2=pd.DataFrame([10,11,12,13],columns=['B'])
df=df1.join(df2,how='outer')
df #join함수로 2개 DataFrame 합치기

df_inner=df1.join(df2,how='inner')
df_inner

df=pd.DataFrame(np.random.randn(5,5))
df.columns=['A','B','C','D','E']
df #난수로 임의의 값 생성
df.max()
df.min()
df.mean()#평균
df.std()#표준편차
df.cumsum()#누적값
df.describe()#통계적 요약
df['division']=['X','Y','X','Y','Z']
df #그룹화
df.groupby(['division']).mean()

#5주차
#pandas dataframe(각각 행, 열로 출력되는 것)
import pandas as pandas
sr=pd.Series([100,200,300,400])
sr.index=['A','B','O','AB']
sr

sr1=pd.Series([10,20,30])
sr1

df=pd.DataFrame({'키':[170,180,175],'몸무게':[65,78,70]})
df.index=['스파이더맨','닥터스트레인지','아이언맨']
df
#CSV파일 읽기
df=pd.read_csv('scores.csv',encoding='cp949')
df
#csv파일에서 불러온 파일의 정보 읽기
df.head()
df.tail()
df.sample(3)
df.info()
df.shape
len(df)
df.isnull().sum()

df_dropna=df.dropna()
df.dropna()

df_fillna=df.fillna(50)
df_fillna

df.describe()

df['국어'].sum()
df.value_counts('영어')
df['국어']
df[['국어','영어']]
df.loc[[1,2,3]]
df.loc[2]
df.iloc[2:5] #2~4번까지
df.loc[2:5] #2~5번까지
df

df.iloc[1,3]
df.iloc[1:3,1:3]

#6주차
!sudo apt-get install -y fonts-nanum
!sudo fc-cache -fv
!rm ~/.cache/matplotlib -rf
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline
plt.rc('font',family='NanumBarunGothic')
plt.rc('axex',unicode_minus=False) #여기까지 한글폰트로 출력하기 설정

#꺾은 선 그래프
x=['1월','2월','3월','4월','5월']
y=[7,10,17,20,23]
plt.plot(x,y)
plt.show()

#그래프 옵션
x=['1월','2월','3월','4월','5월']
y=[7,10,17,20,23]
plt.plot(x,y,color="blue",marker='o',linestyle=':')
plt.title('월별 평균 온도',fontsize=15)
plt.ylabel('온도(도)')
plt.grid(linestyle=':')
plt.show()

aVal=np.random.standard_normal(40) #표준정규분포 따르는 랜덤 값 생성
aVal
type(aVal)

#lineplot 그리기
index=range(len(aVal))
plt.plot(index,aVal) #선, 마커
plt.xlim(0,20) #x축 범위
plt.ylim(np.min(aVal)-1,np.max(aVal)+1) #y축 범위
plt.show()
type(index)

#plot 옵션 설정 및 꾸미기
plt.figure(figsize=(7,4)) #새로운 모양 생성
plt.plot(aVal.cumsum(),'b',lw=1.5) #누적 합계 구함
plt. plot(aVal.cumsum(),'ro')
plt.xlabel('index') #x축 이름 설정
plt.ylabel('aVal')
plt.title('Line Plot') #플롯 제목 설정
plt.show()

#랜덤으로 lineplot 그리기
value=np.random.standard_normal((30,2)) #30,2 행렬 랜덤으로 가져옴
value
value[0] #0번째 랜덤값

#그래프 여러개 겹쳐 그리기
plt.figure(figsize=(10,4))
plt.plot(value[:,0],lw=1.5)
plt.plot(value[:,1],lw=1.5)
plt.plot(value,'ro')
plt.grid(True)
#plt.legend(loc=0)
plt.xlabel('index')
plt.ylabel('value')
plt.title('Line Plot')

#그래프 여러개 따로따로 그리기
#첫번째 그래프
plt.figure(figsize=(10,5))
plt.subplot(211)
plt.plot(value[:,0],lw=1.5,label='1st')
plt.plot(value[:,0],'ro')
plt.grid(True)
plt.legend(loc=0)
plt.ylabel("value")
plt.title('Line Plot 3')
#두번째 그래프
plt.subplot(212)
plt.plot(value[:,1],'g',lw=1.5,label='2nd')
plt.grid(True)
plt.legend(loc=0)
plt.axis('tight')
plt.ylabel('value')

#그래프 엄청 많이 그리기
#첫번째
plt.figure(figsize=(13,5))
plt.subplot(231)
plt.plot(value[:,0],lw=1.5,label='1st')
plt.plot(value[:,0],'co')
plt.grid(True)
plt.legend(loc=0)
plt.ylabel("value")
plt.title('Line Plot 3')
#두번째
plt.subplot(232)
plt.plot(value[:,0],'g-.',lw=1.5,label='1st')
plt.grid(True)
plt.legend(loc=0)
plt.axis('tight')
plt.ylabel('value')
#세번째
plt.subplot(233)
plt.plot(value[:,0],'g',lw=1.5,label='1st')
plt.plot(value[:,0],'bD')
plt.grid(True)
plt.legend(loc=0)
plt.axis('tight')
plt.ylabel('value')
#네번째
plt.subplot(234)
plt.plot(value[:,1],'*',lw=1.5,label='2nd')
plt.grid(True)
plt.legend(loc=0)
plt.axis('tight')
plt.ylabel('value')
#다섯번째
plt.subplot(235)
plt.plot(value[:,1],'b',lw=1.5,label='2nd')
plt.plot(value[:,1],'ms')
plt.grid(True)
plt.legend(loc=0)
plt.axis('tight')
plt.ylabel('value')
#여섯번째
plt.subplot(236)
plt.plot(value[:,1],'r--',lw=1.5,label='2nd')
plt.grid(True)
plt.legend(loc=0)
plt.axis('tight')
plt.ylabel('value')

#세로막대그래프
x=['1월','2월','3월','4월','5월']
y=[7,10,17,20,23]
plt.bar(x,y)
plt.show()
#가로막대그래프
x=['1월','2월','3월','4월','5월']
y=[7,10,17,20,23]
plt.barh(x,y)
plt.show()
#그래프 옵션
x=['1월','2월','3월','4월','5월']
y=[7,10,17,20,23]
plt.bar(x,y,color="orange",width=0.5,edgecolor='black',hatch='/')
plt.title('월별 평균 온도',fontsize=15)
plt.ylabel('온도(도)')
plt.grid(linestyle=':',axis='y')
plt.show()

#csv파일 읽어오기(계속 파일 있다는 가정 하에 코드 진행)
import pandas as pd
df=pd.read_csv('scores.csv',encoding='cp949')
df
x=df['이름']
y_kor=df['국어']
plt.bar(x,y_kor)
plt.show()
#바 그래프로 항목 비교해서 보기
x=df['이름']
y_kor=df['국어']
y_eng=df['영어']
plt.bar(x,y_kor,width=-0.4,align='edge',label='국어')
plt.bar(x,y_eng,width=0.4,align='edge',label='영어')
plt.title('국어/영어 점수 비교',fontsize=15)
plt.ylabel('점수')
plt.legend()
plt.show()

#산점도(scatter plot)
value=np.random.standard_normal((500,2))
plt.plot(value[:,0],value[:,1],'ro')
plt.grid(False)
plt.xlabel('value 1')
plt.ylabel('value 2')
plt.title('Scatter Plot 1')
#산점도 배경으로 칸 만들기
plt.figure(figsize=(7,5))
plt.scatter(value[:,0],value[:,1],marker='o')
plt.grid(True)
plt.xlabel('value 1')
plt.ylabel('value 2')
plt.title('Scatter Plot 2')
#여러가지 산점도 색깔 다르게 해서 보기
color=np.random.randint(0,10,len(value))
plt.figure(figsize=(10,5))
plt.scatter(value[:,0],value[:,1],c=color,marker='o')
plt.colorbar() #산점도 옆에 색깔 막대기 추가
plt.xlabel('value 1')
plt.ylabel('value 2')
plt.title('Scatter Plot 3')

#Seaborn
import seaborn as sns
df=sns.load_dataset('tips')
df
df.head()
df.describe()
df.info()
x=df['total_bill']
y=df['tip']
sns.scatterplot(x,y)
sns.boxplot(x="day",y="tip",hue="sex",data=df,palette="muted")

#7주차
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
%matplotlib inline
iris=sns.load_dataset('iris')
iris

iris.groupby('species').size()
iris.describe()
type(iris)

sns.pairplot(iris)
plt.title("Iris Data Analysis") #산점도, 막대그래프
sns.pairplot(iris,hue="species",diag_kind='kde') #산점도, 확률분포표
sns.boxplot(x='species',y="petal_length",data=iris) #박스형
sns.boxplot(x='species',y="petal_width",data=iris)
iris.boxplot(by="species",figsize=(16,8))