import pandas as pd
import csv
import plotly.figure_factory as pff
import statistics
import random
import plotly.graph_objects as pgo

df = pd.read_csv(r"D:/python/py/studentMarks.csv")
fig = pff.create_distplot([df["Math_score"].tolist()],["Math Score"],show_hist=False)
fig.show()

Math_score_list = df["Math_score"].tolist()

pmean = statistics.mean(Math_score_list)
psd = statistics.stdev(Math_score_list)

print(pmean)
print(psd)

def randomly(counter):
    newlist = []
    for i in range(0,counter):
        randomindex = random.randint(0,len(Math_score_list)-1)
        value = Math_score_list[randomindex]
        newlist.append(value)

    smean = statistics.mean(newlist)
    return smean

mainlist = []
for i in range(0,1000):
    mainindex = randomly(100)
    mainlist.append(mainindex)

sd_mainlist = statistics.stdev(mainlist)
mean_mainlist = statistics.mean(mainlist)

print(sd_mainlist)
print("mean of sampling distributuion ",mean_mainlist)

dig = pff.create_distplot([mainlist],["Math Score"],show_hist=False)
dig.add_trace(pgo.Scatter(x=[mean_mainlist,mean_mainlist],y=[0,0.2],mode="lines",name="mean"))
dig.show()