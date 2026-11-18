import numpy as np
'''
m=np.array([[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]])
print(m[0:2, 1:3])
print(m[:, ::2])
print(m[::-1])
print(m[1:, :2])
'''
'''
v=np.array([10,20,30,40,50])
sl=v[1:3]
sl[0]=999
print(v)
'''
'''
x=np.arange(12)
print(x.reshape(3,4))
print(x.reshape(2,-1).shape)
print(x.reshape(3,4).flatten())
print(x.reshape(3,4).T.shape)
try:
    x.reshape(5,3)
except ValueError as e:
    print(e)
'''
'''
p=np.array([[1,2],[3,4]])
q=np.array([[5,6],[7,8]])
print(np.concatenate((p,q),axis=0))
print(np.concatenate((p,q),axis=1))
print(np.vstack((p,q)).shape)
print(np.hstack((p,q)).shape)
'''
'''
print(np.split(np.arange(6),3))
print(np.split(np.arange(8),[2,5]))
s=np.arange(12).reshape(3,4)
left, right=np.hsplit(s,2)
print(left)
print(right)
t=np.arange(8).reshape(4,2)
top, bottom=np.vsplit(t,2)
print(top)
print(bottom)
'''
'''
d=np.array([[1,2,3],[4,5,6]])
print(d.sum(), d.mean(), d.min(), d.max())
print(d.std().round(4), d.prod())
print(d.argmax())
print(d.cumsum())
'''
'''
d=np.array([[1,2,3],[4,5,6]])
print(d.sum(axis=0))
print(d.sum(axis=1))
print(d.mean(axis=0))
print(d.max(axis=1))
'''
'''
mat=np.array([[1,2,3],[4,5,6],[7,8,9]])
row=np.array([10,20,30])
col=np.array([[1],[2],[3]])
print(mat+10)
print(mat+row)
print(mat+col)
print(np.array([[0],[10],[20]])+np.array([[1,2,3]]))
try:
    np.ones((3,2))+np.ones(3)
except ValueError as e:
    print(e)
'''
v=np.array([10,20,30,40,50])
m=np.array([[10,20,30,40],[50,60,70,80],[90,100,110,120]])
print(v[[0,2,4]])
print(m[[0,2],[1,3]])
print(m[np.ix_([0,2],[1,3])])
vv=v.copy()
vv[[0,1]]=0
print(vv)