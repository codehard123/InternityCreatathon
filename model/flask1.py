from flask import Flask
from flask import jsonify, request

from sklearn.externals import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import pandas as pd
import sklearn
from sklearn.cross_validation import cross_val_score
import string
from sklearn import preprocessing ,cross_validation,svm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from sklearn.cross_validation import cross_val_score
from sklearn.linear_model import LinearRegression,LogisticRegression
import seaborn as sns
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
import string


app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def pred():
    
    '''classifier=joblib.load('linear_regression_model.pkl')
    X1=joblib.load('x1.pkl')
    y1=joblib.load('y1.pkl')
    String1 =cross_val_score(clf,X1,y1,cv=10,scoring='accuracy').mean()
    
    return jsonify({"result":String1[0]}),220'''
    df=pd.read_csv('dataset5.csv')
    #print(df.head())
    X=df.iloc[0:8000,[1,2,3]].values.astype(int)
    y=df.iloc[0:8000,4].values.astype(int)
    #print(X)
    #print(y)
    #plt.figure(figsize=(10,8))
    #sns.heatmap(df.corr(),annot=True)
    #plt.plot(X_train,clf.predict(X_train))
    #plt.show()
    X_train ,X_test,y_train, y_test=cross_validation.train_test_split(X,y,test_size=0.2)
    clf=svm.SVC()
    clf.fit(X_train,y_train)

    xy=np.array([13 , 2 ,5]).reshape(1,-1)
    #print(Xtest)
    prdection=clf.predict(xy)
    #x_test will be containg time and day for checking
    #now we will see at present time which of dustbins are above 75%
    print(prdection)
    set1=set()
    for i in range(len(prdection)):
        if prdection[i]>75:#threshold value 75%
            set1.add(i%25)
    xy[0][0]=xy[0][0]+1
    print(xy[0])
    prdection=clf.predict(xy)
#x_test will be containg time + one hourrr   and day for checking

#now we will see at present time which of dustbins are above 90% predection for completion of bin
    for i in range(len(prdection)):
        if prdection[i]>90:#threshold value 90%
            set1.add(i%25)
    print(prdection)

    from priodict import priorityDictionary

    from collections import defaultdict

    def Dijkstra(G, start, end=None):
   

        D = {}  # dictionary of final distances
        P = {}  # dictionary of predecessors
        Q = priorityDictionary()  # estimated distances of non-final vertices
        Q[start] = 0

        for v in Q:
            D[v] = Q[v]
            if v == end:
                break

            for w in G[v]:
                vwLength = D[v] + G[v][w]
                if w in D:
                    if vwLength < D[w]:
                        raise ValueError("Dijkstra: found better path to already-final vertex")
                elif w not in Q or vwLength < Q[w]:
                    Q[w] = vwLength
                    P[w] = v

        return (D, P)


    def shortestPath(G, start, end):
    """
    Find a single shortest path from the given start vertex to the given
    end vertex. The input has the same conventions as Dijkstra(). The
    output is a list of the vertices in order along the shortest path.
    """
    D, P = Dijkstra(G, start, end)
    Path = []
    while 1:
        Path.append(end)
        if end == start:
            break
        end = P[end]
    Path.reverse()
    return Path

    def least(c,graph_to_visit,n,completed,cost):
        nc=999
        min_x=999
        kmin=0
        for i in range(n):
            if graph_to_visit[c][i]!=0 and completed[i]==0:
                if graph_to_visit[c][i]+graph_to_visit[i][c]<min_x:
                    min_x=graph_to_visit[i][0]+graph_to_visit[c][i]
                    kmin=graph_to_visit[c][i]
                    nc=i
        if min_x!=999:
            cost+=kmin
            
        return (nc,cost)

    def mincost(city,graph_to_visit,n,completed,cost=0,path=[]):
    completed[city]=1
#     print(city+1,"--> ",end=" " )
    path.append(city)

    ncity,cost=least(city,graph_to_visit,n,completed,cost)
    
    if ncity==999:
        ncity=0
        print(ncity+1)
        cost+=graph_to_visit[city][ncity]
        return (cost,path,completed)
    cost,path,completed=mincost(ncity,graph_to_visit,n,completed,cost,path)
    return (cost,path,completed)

    if __name__ == "__main__":
    # n = int(input())
    # m = int(input())

    n = 7
    m = 8

    location_with_distance= [['1', '2', 3],
                             ['2', '3', 1],
                             ['4', '1', 10],
                             ['3', '4', 2],
                             ['4', '6', 7],
                             ['7', '5', 2],
                             ['3', '5', 1],
                             ['4', '5', 5]]
    
    set1.add('1')
    set1.add('4')
    set1.add('7')
    location_to_visit=list(set1)


    dustbins_location=[]
    main_graph=defaultdict(dict)
    gtime={}
    for i in range(0,m):
    #     input_path=input().split()

        input_path=location_with_distance[i]

    #     will store the time from one path to other path
        if(input_path[0]==input_path[1]):
            continue

        main_graph[input_path[0]][input_path[1]]=input_path[2]
        main_graph[input_path[1]][input_path[0]]=input_path[2]

    main_graph=dict(main_graph)
    print(main_graph)

    for i in main_graph:
        dustbins_location.append(i)


    number_of_location_to_visit=len(location_to_visit)
    graph_to_visit=[]  
    for i in range(number_of_location_to_visit):
        arr=[]
        for j in range(number_of_location_to_visit):
            arr.append(0)
        graph_to_visit.append(arr)
            
#     check all the combinations
    for i in range(number_of_location_to_visit-1):
        for j in range(i+1,number_of_location_to_visit):

            minimum_distance_list=shortestPath(main_graph,location_to_visit[i],location_to_visit[j])
#             print(minimum_distance_list)
            minimum_distance=0
            for x in range(len(minimum_distance_list)-1):
                minimum_distance+=main_graph[minimum_distance_list[x]][minimum_distance_list[x+1]]
#             print(total_dist)
            
            graph_to_visit[i][j]=graph_to_visit[j][i]=minimum_distance
        
    print("Graph to visit:" ,graph_to_visit)
        
    # graph_to_visit=[[0, 4, 1, 3],[4, 0, 2, 1],[1, 2, 0, 5],[3, 1, 5, 0]]
    completed=[]
    for i in range(number_of_location_to_visit):
        completed.append(0)
    cost,final_path,completed=mincost(0,graph_to_visit,3,completed)
    print("Total Cost(back to src):",cost)
    for i in range(len(final_path)): final_path[i]=location_to_visit[i]
    print("Sequence of path: ",final_path)
    
    final_full_path=[final_path[0]]
    for i in range(len(final_path)-1):
        minimum_distance_list=shortestPath(main_graph,final_path[i],final_path[i+1])
        print("aaaa: ",minimum_distance_list)
        final_full_path+=minimum_distance_list[1:-1]
        final_full_path+=[final_path[i+1]]
        
    print("Final Path to return: ")
    print(final_full_path)

    df2=df=pd.read_csv('locations.csv')
    X1=df.iloc[0:,[0,1,2]].values.astype(str)
    we=np.array(['1','2',3,5,7,5,3,4])
    d = dict()
    for i in range (len(we)):
    
        d[we[i]]=X[i]


    return jsonify({"result":d}),220
    
    
if  __name__=="__main__":
    app.run(port=8000,debug=True)
