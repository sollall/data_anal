from re import A
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

#タイトルで漢字が使えるようフォントを設定
plt.rcParams['font.family'] = 'Meiryo'
 
#描画エリアの作成
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
 
#グラフタイトルを設定
ax.set_title("３D散布図",size=20)
 
#軸ラベルのサイズと色を設定
ax.set_xlabel("x軸",size=15,color="black")
ax.set_ylabel("y軸",size=15,color="black")
ax.set_zlabel("z軸",size=15,color="black")

#x,yデータの作成
x_data = np.linspace(0,10,50)
y_data = np.linspace(1500,3000,50)
x, y = np.meshgrid(x_data,y_data)

z=np.zeros_like(x)

def f(x,y):
    #ストレス
    a=70+(x-6)/6+(y-2250)/2250
    #脳
    b=70-(x-6)/6
    #糖尿
    c=70-(y-2250)/2250

    ans=min(a,b,c)
    label=""
    if ans==a:
        label="red"
    elif ans==b:
        label="blue"
    elif ans==c:
        label="green"

    return ans,label
# zデータの作成
for i in range(50):
    for j in range(50):
        ans,label=f(x[i][j],y[i][j])
        z[i][j]=ans
        
        #散布図の作成
        ax.scatter(x[i][j],y[i][j],z[i][j],s=1,c=label)

#描画
plt.show()