#!/usr/bin/env python3
import matplotlib 
matplotlib.use('Agg');
from matplotlib import pyplot
from matplotlib import cm
from numpy import arange
import bisect
import io 
import base64 
import sys
#pyplot.use('Agg')

def scatterplot(x,y):
    pyplot.plot(x,y,'b.')
    pyplot.xlim(min(x)-1,max(x)+1)
    pyplot.ylim(min(y)-1,max(y)+1)
    pyplot.show()

def barplot(labels,data,username):
    pos=arange(len(data))
    c=[];
    for i in data:
     c.append(cm.gist_heat(i/100,20));
     
    pyplot.ylim(0,100);
    pyplot.xticks(pos+0.4,labels,color="black")
    pyplot.bar(pos,data,color=c);
    pyplot.xlabel("Class",fontsize="14",color="black");
    pyplot.ylabel("Percentage",fontsize="14",color="black");
    pyplot.title("Performance",fontsize="16",color="black");
    imn="../student/graphs/"+username+".png";
    pyplot.savefig(imn)
    pyplot.close()
    #pyplot.show(block=False);
   
    
def histplot(data,bins=None,nbins=5):
    minx,maxx=min(data),max(data)
    space=(maxx-minx)/float(nbins)
    if not bins: bins=arange(minx,maxx,space)
    binned=[bisect.bisect(bins,x) for x in data]
    l=['%.1f'%x for x in list(bins)+[maxx]] if space<1 else [str(int(x)) for x in list(bins)+[maxx]]
    displab=[x+'-'+y for x,y in zip(l[:-1],l[1:])]
    barplot(displab,[binned.count(x+1) for x in range(len(bins))])

def barchart(x,y,username,numbins=5):
    datarange=max(x)-min(x)
    bin_width=float(datarange)/numbins
    pos=min(x)
    bins=[0 for i in range(numbins+1)]

    for i in range(numbins):
        bins[i]=pos
        pos+=bin_width
    bins[numbins]=max(x)+1
    binsum=[0 for i in range(numbins)]
    bincount=[0 for i in range(numbins)]
    binaverage=[0 for i in range(numbins)]

    for i in range(numbins):
        for j in range(len(x)):
            if x[j]>=bins[i] and x[j]<bins[i+1]:
                bincount[i]+=1
                binsum[i]+=y[j]

    for i in range(numbins):
        binaverage[i]=float(binsum[i])/bincount[i]
    barplot(['10th','12th','1st','2-1','2-2','3-1','3-2','4-1','4-2','overall'],binaverage,username)

def piechart(labels,data):
    fig=pyplot.figure(figsize=(7,7))
    pyplot.pie(data,labels=labels,autopct='%1.2f%%')
    pyplot.show()
