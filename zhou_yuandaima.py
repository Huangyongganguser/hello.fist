import pandas as pd
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform
dt=pd.read_csv('F:\h\data_convert(1).csv',encoding = "utf-8",header=None)
xyDisMat=squareform(pdist(dt.values[:,7:8]))
tMat=squareform((pdist(dt.values[:,9].reshape(-1,1))))#reshape是想让他变成一列，但是不知道有多少行，-1就是自动计算
# print(tMat)
# stay=open(r'E:\zyj_experiment\test3.csv',mode='a')
N=len(dt)
i=0
S=[]
M=[]
#构造函数更新潜在停留集合Q（把Q中不满足条件的点去掉)
def stay_update(Q,xyDisMat):
    n=len(Q)
    i=0
    while i<n-1:
        j=i+1
        while j<n:
            if xyDisMat[Q[i],Q[j]]>200:
                # for r in range(j,n-1):#这两句代码会报错，显示超出范围，然而没有找到原因。。。
                #     del Q[r]
                newQ=[]  #这四句代码的作用等同于delQ[j：n]
                for idx in range(j):
                    newQ.append(Q[idx])
                Q=newQ
                # del Q[j:n]
                n=len(Q)
                break
            else:
                j=j+1
        i=i+1
    return Q

while(i<N-1):
    Q=[]
    Q.append(i)
    for j in range(i+1,N):
        if xyDisMat[i,j]<=200:
            Q.append(j)
        else:
            break
    #判断潜在停留集合Q中各点之间的空间距离是否都满足小于300的条件
    I= stay_update(Q, xyDisMat)
#    判断时间是否满足条件
    if (len(I)>1):
        if (tMat[I[0],I[-1]]>14400):
            S.append(I)
            for s in S:
                M=[s[0],s[-1]]
                res=dt.loc[M]
                S.pop()
                #print(res)
                res.to_csv(r'F:\h\data60.csv',index=None,header=None,mode='a')
    i=j
#             # print(S)
#             # for s in S:
#             #     for j in range(len(s)):
#             #         res=dt.ix[[s[j]]
#             #         print(res)
#                     # res.to_csv(r'F:\h\data17.csv',index=None,header=None,mode='a')
#                 # S.pop()
#
# print(S)
# for w in S:
#     print(w)
#     res=dt.ix[[w-1]]
#     print(res)
#     res.to_csv(r'F:\h\data23.csv',index=None,header=None,mode='a')
#     S.pop()
#构造函数提取出行
# def move(dt):
#     xyDisMat = squareform(pdist(dt.values[:,7:8]))
#     tMat = squareform((pdist(dt.values[:,9].reshape(-1, 1))))
#     N = len(dt)
#     i = 0
#     S1 = []
#     S2 = []
#
#     while (i < N - 1):
#         Q = []
#         Q.append(i)
#         for j in range(i + 1, N):
#             if xyDisMat[i, j] <= 200:
#                 Q.append(j)
#             else:
#                 break
#             # 判断潜在停留集合Q中各点之间的空间距离是否都满足小于300的条件
#         I = stay_update(Q, xyDisMat)
#         # 判断时间是否满足条件
#         if (len(I) > 1):
#             # print(tMat[I[0], I[-1]])
#             if (tMat[I[0], I[-1]] > 1800):
#                 S1.append(I)
#
#                 del I[1:-1]
#
#                 S2.append(I)
#
#         i = j
# # move(dt)
#
#
# #print(S)
#     S = list(flatten(S2))  # 将二维list将为一维list
#     if len(S) !=0:
#         if S[0] == 0:
#             # 删除首个元素0
#             S.pop(0)
#             # print(S)
#             if S[-1] == len(dt) - 1:
#                 S.pop(-1)
#             else:
#                 S.append(len(dt) - 1)
#         else:
#             # 添加首个元素0
#             S.insert(0, 0)
#             if S[-1] == len(dt) - 1:
#                 # 删除末尾元素
#                 S.pop(-1)
#                 # print(S)
#             else:
#                 S.append(len(dt) - 1)
#     print(S)
# move(dt)