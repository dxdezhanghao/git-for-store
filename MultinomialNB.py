# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 10:28:41 2018

@author: 704423953
"""
import matplotlib.pyplot as plt
import numpy as np
from NaiveBayes import NativeBayes
class MultinomialNB(NativeBayes):
    def feed_data(self,dic,label,x):
        for i in range(len(x)):
            if label.__contains__(x[i][-1]):
                label[x[i][-1]]+=1
            for j in range(len(x[0])-1):
                   if dic.__contains__(x[i][-1]):
                       if dic[x[i][-1]].__contains__(j):
                           if dic[x[i][-1]][j].__contains__(x[i][j]):
                               dic[x[i][-1]][j][x[i][j]]+=1
                           else:
                               dic[x[i][-1]][j][x[i][j]]=1        
                       else:
                           dic[x[i][-1]][j]={x[i][j]:1}
                   else:
                       dic[x[i][-1]]={j:{x[i][j]:1}}
                       label[x[i][-1]]=1
        print(dic)
        print(label)   
    def predict(self,lb,x,label,dic,jieguo):
        probility=1
        result=0.0
        predictlabel=""
        ratio=0
        allsum=0
        for key in label:
            allsum+=label[key]
        for i in range(len(x)):
           result=0 
           for key in label:
               num=label[key]
               for j in range(0,len(x[0])-1):
                   if dic[key][j].__contains__(x[i][j]):
                      probility*=((dic[key][j][x[i][j]]+lb)/(num+lb*len(label)))
                   else:
                      probility*=((0+lb)/(num+lb*len(label)))
               probility*=(num/allsum)       
               if probility>result:
                   result=probility
                   predictlabel=key     
               probility=1    
           if(predictlabel==x[i][-1]):
               ratio+=1
           jieguo.append(predictlabel)
        print("Acc: {:12.6} %".format(100*ratio/len(x)))
if __name__=='__main__':
        x=[]
        with open("_Data/mushroom.txt","r",encoding="utf8") as file:
            for sample in file:
                print(sample)
                x.append(sample.strip().split(","))
        for i in range(len(x)):
            x[i].reverse() 
        nb=MultinomialNB()
        dic={}
        label={}
        list1=[]
        nb.feed_data(dic,label,x)
        nb.predict(1,x,label,dic,list1)
colors={"e":"lightSkyBlue","p":"orange"}
for i in range(len(dic["p"])-10):
     plt.figure()
     m=0
     for key in label:
        s=[]
        index =np.arange(1,len(dic[key][i])+1)
        print(index)
        for values in dic[key][i].values():
            s.append(values/label[key])   
        print(s)    
        plt.bar(index+m,s,width=0.35,facecolor=colors[key],edgecolor="white",label="class: {}".format(key),tick_label=list(dic[key][i].keys()))
        m+=0.35
     plt.ylim(0,1.0)     







            