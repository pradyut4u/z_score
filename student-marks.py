import pandas as pd
import csv
import plotly.figure_factory as pff
import statistics
import random
import plotly.graph_objects as pgo

df = pd.read_csv(r"D:/python/py/studentMarks.csv")

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

smean = statistics.mean(mainlist)
ssd = statistics.stdev(mainlist)

sd_start1, sd_end1 = smean - ssd, smean + ssd
sd_start2, sd_end2 = smean - 2*ssd, smean + 2*ssd
sd_start3, sd_end3 = smean - 3*ssd, smean + 3*ssd

fig = pff.create_distplot([mainlist],["Score"],show_hist=False)
fig.add_trace(pgo.Scatter(x=[smean,smean],y=[0,0.2],mode="lines",name="mean"))
fig.add_trace(pgo.Scatter(x=[sd_start1,sd_start1],y=[0,0.2],mode="lines",name="sd_start1"))
fig.add_trace(pgo.Scatter(x=[sd_end1,sd_end1],y=[0,0.2],mode="lines",name="sd_end1"))
fig.add_trace(pgo.Scatter(x=[sd_start2,sd_start2],y=[0,0.2],mode="lines",name="sd_start2"))
fig.add_trace(pgo.Scatter(x=[sd_end2,sd_end2],y=[0,0.2],mode="lines",name="sd_end2"))
fig.add_trace(pgo.Scatter(x=[sd_start3,sd_start3],y=[0,0.2],mode="lines",name="sd_start3"))
fig.add_trace(pgo.Scatter(x=[sd_end3,sd_end3],y=[0,0.2],mode="lines",name="sd_end3"))

#mean of the first data (ipad given)

df = pd.read_csv(r"D:/python/py/data1.csv")
d1 = df["Math_score"].tolist()

d1_mean = statistics.mean(d1)
zd1 = (d1_mean-smean)/ssd
print("z score for data 1 ",zd1)

fig.add_trace(pgo.Scatter(x=[d1_mean,d1_mean],y=[0,0.2],mode="lines",name="d1_mean"))

#mean of the second data (extra classes)

df = pd.read_csv(r"D:/python/py/data2.csv")
d2 = df["Math_score"].tolist()

d2_mean = statistics.mean(d2)
zd2 = (d2_mean-smean)/ssd
print("z score for data 2 ",zd2)

fig.add_trace(pgo.Scatter(x=[d2_mean,d2_mean],y=[0,0.2],mode="lines",name="d2_mean"))

#mean of the second data (worksheets)

df = pd.read_csv(r"D:/python/py/data3.csv")
d3 = df["Math_score"].tolist()

d3_mean = statistics.mean(d3)
zd3 = (d3_mean-smean)/ssd
print("z score for data 3 ",zd3)

fig.add_trace(pgo.Scatter(x=[d3_mean,d3_mean],y=[0,0.2],mode="lines",name="d3_mean"))
#fig.show()