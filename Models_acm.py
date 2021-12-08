import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score
from django.shortcuts import render
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly as py
import plotly.graph_objs as go
from plotly.subplots import make_subplots
#from plotly.offline import iplot, init_notebook_mode
#init_notebook_mode(connected = True)


df = pd.read_csv('Copy of Responses.csv')

df.drop('Timestamp',inplace = True,axis=1)
df.drop('Age',inplace = True,axis=1)
df.drop('Gender',inplace = True,axis=1)
df.drop('Level of education',inplace = True,axis=1)

for col in df.columns:
    for i in range(len(df)):
        if df[col][i] == 'Never':
            df[col][i] = 0
        elif df[col][i] == 'Rarely':
            df[col][i] = 1
        elif df[col][i] == 'Sometimes':
            df[col][i] = 2
        elif df[col][i] == 'Often':
            df[col][i] = 3
        elif df[col][i] == 'Always':
            df[col][i] = 4
        elif df[col][i] == 'Yes':
            df[col][i] = 4
        elif df[col][i] == 'No':
            df[col][i] = 0
        else:
            pass

for i in range(len(df)):
    df[df.columns[10]][i] = abs(df[df.columns[10]][i] - 4)
    df[df.columns[17]][i] = abs(df[df.columns[17]][i] - 4)

df['wq1'] = df[df.columns[0]] * 0.2
df['wq2'] = df[df.columns[1]] * 0.5
df['wq3'] = df[df.columns[2]] * 0.2
df['wq4'] = df[df.columns[3]] * 0.3
df['wq5'] = df[df.columns[4]] * 0.3
df['wq6'] = df[df.columns[5]] * 0.2
df['wq7'] = df[df.columns[6]] * 0.5
df['wq8'] = df[df.columns[7]] * 0.5
df['wq9'] = df[df.columns[8]] * 0.2
df['wq10'] = df[df.columns[9]] * 0.2
df['wq11'] = df[df.columns[10]] * 0.3
df['wq12'] = df[df.columns[11]] * 0.5
df['wq13'] = df[df.columns[12]] * 0.3
df['wq14'] = df[df.columns[13]] * 0.5
df['wq15'] = df[df.columns[14]] * 0.3
df['wq16'] = df[df.columns[15]] * 0.5
df['wq17'] = df[df.columns[16]] * 0.5
df['wq18'] = df[df.columns[17]] * 0.3

df['wsum'] = df['wq1']+df['wq2']+df['wq3']+df['wq4']+df['wq5']+df['wq6']+df['wq7']+df['wq8']+df['wq9']+df['wq10']+df['wq11']+df['wq12']+df['wq13']+df['wq14']+df['wq15']+df['wq16']+df['wq17']+df['wq18']
df['w%']=(df['wsum']/25.6)*100

XX = df.iloc[:,0:18]
YY = df['w%']

X_train,X_test,Y_train,Y_test=train_test_split(XX,YY,test_size=0.2,random_state=1)
print ("train data shape:")
print (X_train.shape)
print ("test data shape:")
print (X_test.shape)
print ("train label shape:")
print (Y_train.shape)
print ("test label shape:")
print (Y_test.shape)

pipefinal = Pipeline([('poly', PolynomialFeatures(degree=1)),('scaler',StandardScaler()),('fit', Ridge(alpha=4.0))])

pipefinal.fit(X_train,Y_train)
predictions = pipefinal.predict(X_test)

def home(request):
    return render(request,'home.html')

def frequency(request):
    return render(request,'statistic.html')

def homepage(request):
    return render(request,'homepage.html')

def calculate(request):
    Q1 = request.GET['Q1']
    q1 = int(Q1)
    Q2 = request.GET['Q2']
    q2 = int(Q2)
    Q3 = request.GET['Q3']
    q3 = int(Q3)
    Q4 = request.GET['Q4']
    q4 = int(Q4)
    Q5 = request.GET['Q5']
    q5 = int(Q5)
    Q6 = request.GET['Q6']
    q6 = int(Q6)
    Q7 = request.GET['Q7']
    q7 = int(Q7)
    Q8 = request.GET['Q8']
    q8 = int(Q8)
    Q9 = request.GET['Q9']
    q9 = int(Q9)
    Q10 = request.GET['Q10']
    q10 = int(Q10)
    Q11 = request.GET['Q11']
    q11 = int(Q11)
    Q12 = request.GET['Q12']
    q12 = int(Q12)
    Q13 = request.GET['Q13']
    q13 = int(Q13)
    Q14 = request.GET['Q14']
    q14 = int(Q14)
    Q15 = request.GET['Q15']
    q15 = int(Q15)
    Q16 = request.GET['Q16']
    q16 = int(Q16)
    Q17 = request.GET['Q17']
    q17 = int(Q17)
    Q18 = request.GET['Q18']
    q18 = int(Q18)

    score = pipefinal.predict([[q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18]])

    diagnosis = ""
    explaination =""
    diagram = ""
    if score[0] >=55:
        diagram +="https://www.voicesofyouth.org/sites/voy/files/images/2020-12/stress_2.gif"
        diagnosis += "Very Highly Vulnerable"
        explaination +="You need to visit a mental health professional or seek help from a professional at the earliest."
    elif score[0] >=40 and score[0] <55:
        diagram +=  "https://1.bp.blogspot.com/-6TJbKQ-nOf4/XERqB3C3GzI/AAAAAAAADv0/LCPQHnaEX3IpotGSx_MOWYThEpK1nz28ACLcBGAs/s1600/mood02.gif"
        diagnosis += "Highly Vulnerable"
        explaination +="You need to look into this at depth as you are not away from being there at very highly vulnerability and hence it is recommended that you do not take your routine lightly and not take that date today stressors in a casual form."
    elif score[0] >=20 and score[0] <40:
        diagram += "https://monophy.com/media/l378dlnLfAbviROAE/monophy.gif"
        diagnosis += "Mildy Vulnerable"
        explaination += "You need to visit a psychologist and share your day to day concerns so that you do not get affected at major level later on."
    elif score[0] <20:
        diagram += "https://www.voicesofyouth.org/sites/voy/files/images/2020-12/wellness_2.gif"
        diagnosis += "Low Vulnerable"
        explaination += "You still need to be vigilant even though you are low on the same as we all are vulnerable and hence it is recommended for you to be vigilant more often."
    else:
        pass

    final_score = round(score[0],2)

    return render(request,'results.html',{"diag":diagnosis,"ex":explaination,"score":final_score,"Diagram":diagram})








