import matplotlib.pyplot as plt
import numpy as np
from sklearn.manifold import TSNE
from tensorflow.keras.datasets import mnist

from matplotlib.offsetbox import OffsetImage, AnnotationBbox

class tSNE_on_image:
    #dataは3D,labelは1Dとする
    def __init__(self,data,label=0):
        
        #データ処理部分
        self.data=data
        self.label=label
        self.data_anal=np.array([self.unite(self.data[i]) for i in range(len(self.data))])

        x_embedded = TSNE(n_components=2).fit_transform(self.data_anal)


        #図作成部分
        self.fig, self.ax=plt.subplots()
        #labelをlist(set())してindexを色付けに使用しては
        self.color=self.l2c(label)
        cmap = plt.cm.RdYlGn

        
        img = np.array([0]*1*1).reshape((1, 1))
        self.imagebox = OffsetImage(img, zoom=1.0)
        self.imagebox.image.axes = self.ax
        cmap = plt.cm.RdYlGn

        width=7
        self.sc = plt.scatter(x_embedded[:, 0], x_embedded[:, 1], c=self.color/(len(self.color)), cmap=cmap, s=3)
        self.annot = AnnotationBbox(self.imagebox, xy=(0,0), xybox=(width,width),
                            xycoords="data", boxcoords="offset points", pad=0.5,
                            arrowprops=dict( arrowstyle="->", connectionstyle="arc3,rad=-0.3"))
        self.annot.set_visible(False)
        self.ax.add_artist(self.annot)

        self.fig.canvas.mpl_connect("motion_notify_event", self.hover)

        print("この文字列が見えてて図が出ないってことはshowされてないってこと")
        plt.show()

    def unite(self,list_2d):
        rev=[]
        for list_1d in list_2d:
            for item in list_1d:
                rev.append(item)

        return np.array(rev)

    def l2c(self,label):
        temp=list(set(label))
        dic={}
        for index,item in enumerate(temp):
            dic[item]=index

        color=[dic[label[i]] for i in range(len(label))]

        return np.asarray(color, dtype=int)
    
    def update_annot(self,ind):
        i = ind["ind"][0]
        pos = self.sc.get_offsets()[i]
        self.annot.xy = (pos[0], pos[1])
        #img = X_train[i][:].reshape((width, width))
        img=self.data[i][:]
        height,width=len(self.data[i]),len(self.data[i][0])
        self.imagebox.set_data(img)

    def hover(self,event):
        vis = self.annot.get_visible()
        if event.inaxes == self.ax:
            cont, ind = self.sc.contains(event)
            if cont:
                self.update_annot(ind)
                self.annot.set_visible(True)
                self.fig.canvas.draw_idle()
            else:
                if vis:
                    self.annot.set_visible(False)
                    self.fig.canvas.draw_idle()

if __name__=="__main__":
    (X_train, y_train), (X_test, y_test) = mnist.load_data()
    nskip = 35
    X_train=X_train[::nskip]
    y_train=y_train[::nskip]

    A=tSNE_on_image(X_train,y_train)

