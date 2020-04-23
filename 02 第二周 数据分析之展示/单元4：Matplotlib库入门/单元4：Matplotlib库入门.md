[TOC]

本周课程导学

## 学习内容

展示数据的基本方法

介绍第三方库，Matplotlib库：

+ 基本使用方法
+ 绘制坐标系，极坐标系，饼图，直方图，散点图
+ 实例：根据原始文件绘制引力波



****

# Matplotlib库的介绍

## Matplotlib库

Python中最优秀的数据可视化第三方库

## Matplotlib库的使用

Matplotlib库由各种可视化类构成，内部结构复杂，受Matlab启发

为了用户使用方便，Matplotlib库提供了一个子库

## pyplot子库

`matplotlib.pyplot`是绘制各种可视化图形的命令子库，相当于快捷方式

pyplot库用简单的方式调用matplotlib库中的各种可视化方式

在使用matplotlib库的时候，重点使用pyplot这个子库

## 使用pyplot子库

```python
import matplotlib.pyplot as plt
```

## 测试pyplot库

```python
import matplotlib.pyplot as plt
plt.plot([3, 1, 4, 5, 2])
plt.ylabel("grade")
plt.show()
```

将列表[3, 1, 4, 5, 2]作为y轴的值

### `plt.plot()`函数

**当参数只有一个列表或数组时，那么这个列表或数组会被当做y轴来处理**

**x轴是这个列表的索引，也就是0~4的数字，自动生成**

### 保存绘制的文件

```python
import matplotlib.pyplot as plt
plt.plot([3, 1, 4, 5, 2])
plt.ylabel("grade")
plt.savefig('test', dpi=600)  # PNG文件
plt.show()
```

使用`plt.savefig()`保存图片，默认为PNG格式

可以在属性中设置dpi的值修改输出质量，dpi是每一英寸空间中包含的点的数量

设置dip = 600，就是每一英寸包含600个像素点，这个质量已经非常高了

### `plt.plot()`函数多个列表作为输入

```python
import matplotlib.pyplot as plt
plt.plot([0, 2, 4, 6, 8], [3, 1, 4, 5, 2])
plt.ylabel("grade")
plt.axis([-1, 10, 0, 6])
plt.show()
```

当`plt.plot(x,y)`函数有两个以上参数时，按照x轴和y轴顺序绘制数据点

### `plt.axis()`函数

使用`plt.axis()`函数可以设定横纵坐标尺度

它的参数是一个包含4个元素的列表：

+ x轴的起始值
+ x轴的终止值
+ y轴的起始值
+ y轴的终止值

所以`plt.axis([-1, 10, 0, 6])`生成的坐标系横轴是-1到10，纵轴是0到6



## pyplot绘图区域

使用pyplot绘制两个或两个以上的图形

### 分割绘图区域

使用`plt.subplot()`函数：

```python
plt.subplot(nrows, ncols, plot_number)
```

+ `nrows`：行数
+ `ncols`：列数
+ `plot_number`：绘图的位置

举例：

```python
plt.subplot(3, 2, 4)
```

就是把绘图区域划分成3行2列的6个区域，同时在第4个区域绘图，顺序是从左到右，从上到下

简写也可以省略逗号：

```python
plt.subplot(324)
```

### 实例：

```python
import numpy as np
import matplotlib.pyplot as plt


def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

a = np.arange(0.0, 5.0, 0.02)

plt.subplot(211)
plt.plot(a, f(a))

plt.subplot(212)
plt.plot(a, np.cos(2*np.pi*a), 'r--')
plt.show()
```



****

# pyplot的plot()函数

## 格式

```python
plt.plot(x, y, format_string, **kwargs)
```

+ `x`：X轴数据，列表或数组，可选
+ `y`：X轴数据，列表或数组
+ `format_striing`：控制曲线格式字符串，可选
+ `**kwargs`：第二组或更多的`(x, y, format_string)`参数，也就是可以同时绘制多条曲线

**当绘制多条曲线时，各条曲线的x都不能省略**

当绘制一条曲线的时候，可以省略x的参数

### 例子（绘制4条曲线）

```python
import numpy as np
import matplotlib.pyplot as plt

a = np.arange(10)
plt.plot(a, a*1.5, a, a*2.5, a, a*3.5, a, a*4.5)
plt.show()
```

画的四条曲线都是以a为x轴的曲线



## 修改曲线的格式

由3种字符构成：

+ 颜色字符
+ 风格字符
+ 标记字符



**颜色字符：**

| 颜色字符    | 说明        | 颜色字符 | 说明           |
| ----------- | ----------- | -------- | -------------- |
| `'b'`       | 蓝色        | `'m'`    | 洋红色 magenta |
| `'g'`       | 绿色        | `'y'`    | 黄色           |
| `'r'`       | 红色        | `'k'`    | 黑色           |
| `'c'`       | 青绿色 cyan | `'w'`    | 白色           |
| `'#008000'` | RGB某颜色   | `'0.8'`  | 灰度值字符串   |



**风格字符：**

| 风格字符      | 说明   |
| ------------- | ------ |
| `'-'`         | 实线   |
| `'--'`        | 破折线 |
| `'-.'`        | 点划线 |
| `':'`         | 虚线   |
| `' '`（空格） | 无线条 |



**标记字符：**

| 标记字符 | 说明               |
| -------- | ------------------ |
| `'.'`    | 点标记             |
| `','`    | 像素标记（极小点） |
| `'o'`    | 实心圈标记         |
| `'v'`    | 倒三角标记         |
| `'^'`    | 上三角标记         |
| `'>'`    | 右三角标记         |
| `'<'`    | 左三角标记         |

| 标记字符 | 说明         |
| -------- | ------------ |
| `'1'`    | 下花三角标记 |
| `','`    | 上花三角标记 |
| `'3'`    | 左花三角标记 |
| `'4'`    | 右花三角标记 |
| `'s'`    | 实心方块标记 |
| `'p'`    | 实心五角标记 |
| `'*'`    | 星形标记     |

| 标记字符 | 说明         |
| -------- | ------------ |
| `'h'`    | 竖六边形标记 |
| `'H'`    | 横六边形标记 |
| `'+'`    | 十字标记     |
| `'x'`    | x标记        |
| `'D'`    | 菱形标记     |
| `'d'`    | 瘦菱形标记   |
| `'|'`    | 垂直线标记   |



### 例子

```python
import numpy as np
import matplotlib.pyplot as plt

a = np.arange(10)
plt.plot(a, a*1.5, 'go-', a, a*2.5, 'rx', a, a*3.5, '*', a, a*4.5, 'b-.')
plt.show()
```



修改风格除了使用标记字符，还可以使用其它的参数命令，如： 

+ `color`：控制颜色，`color = 'green'`
+ `linestyle`：线条风格，`linestyle = 'dashed'`
+ `marker`：标记风格，`marker = 'o'`
+ `markerfacecolor`：改变标记颜色，`markerfacecolor = 'blue'`
+ `markersize`：标记尺寸，`markersize = 20`

以及其它参数来更改参数



****

# pyplot的中文显示

pyplot默认不支持中文，如果想要显示中文，需要添加额外的代码辅助

## 修改`rcParams`字体实现

例子：

```python
import matplotlib.pyplot as plt

matplotlib.rcParams['font.family'] = 'SimHei'
plt.plot([3, 1, 4, 5, 2])
plt.ylabel("纵轴(值)")
plt.savefig('test', dpi=600)
plt.show()
```

`SimHei`是黑体

### `rcParams`的属性

| 属性          | 说明                                    |
| ------------- | --------------------------------------- |
| `font.family` | 用于显示字体的名字，如`SimHei`          |
| `font.style`  | 字体风格，正常`normal`或斜体`italic`    |
| `font.size`   | 字体大小，整数字号或者`large`、`xsmall` |

### `font.family`中文字体

| 中文字体   | 说明     |
| ---------- | -------- |
| `SimHei`   | 中文黑体 |
| `Kaiti`    | 中文楷体 |
| `LiSu`     | 中文隶书 |
| `FangSong` | 中文仿宋 |
| `YouYuan`  | 中文幼圆 |
| `STSong`   | 华文宋体 |

## 示例：显示正弦波

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family']='STSong'
matplotlib.rcParams['font.size']=20

a = np.arange(0.0, 5.0, 0.02)
plt.xlabel('横轴：时间')
plt.ylabel('纵轴：振幅')
plt.plot(a, np.cos(2*np.pi*a), 'r--')
plt.show()

```

这种方法改变的是全局字体



## 增加属性`fontproperties`

如果只希望在某一个地方有中文输出，不想改变其它的输出（建议使用），可以在有中文输出的地方，增加一个属性：`fontproperties`

### 示例：绘制正弦波

```python
import numpy as np
import matplotlib.pyplot as plt

a = np.arange(0.0, 5.0, 0.02)

plt.xlabel('横轴：时间', fontproperties='SimHei', fontsize=20)
plt.ylabel('纵轴：振幅', fontproperties='SimHei', fontsize=20)
plt.plot(a, np.cos(2*np.pi*a), 'r--')
plt.show()

```

这里的黑体仅对`xlabel`起作用，而不影响其它的文本，比如y轴或坐标系



****

# pyplot的文本显示

## pyplot的文本显示函数

| 函数             | 说明                     |
| ---------------- | ------------------------ |
| `plt.xlabel()`   | 对X轴增加文本标签        |
| `plt.ylabel()`   | 对Y轴增加文本标签        |
| `plt.title()`    | 对图形整体增加文本标签   |
| `plt.text()`     | 在任意位置增加文本       |
| `plt.annotate()` | 在图形中增加带箭头的注解 |

### 示例：绘制正弦波

专业的表示，有标示和注释

```python
import numpy as np
import matplotlib.pyplot as plt

a = np.arange(0.0, 5.0, 0.02)
plt.plot(a, np.cos(2*np.pi*a), 'r--')

plt.xlabel('横轴：时间', fontproperties='SimHei', fontsize=15, color='green')
plt.ylabel('纵轴：振幅', fontproperties='SimHei', fontsize=15)
plt.title(r'正弦波实例 $y=cos(2\pi x)$', fontproperties='SimHei', fontsize=25)
plt.text(2, 1, r'$\mu=100$', fontsize=15)

plt.axis([-1, 6, -2, 2])
plt.grid(True)
plt.show()

```

`r'正弦波实例 $y=cos(2\pi x)$'`加上标题

双`$`标识，是Latex语法，可以表示公式

`plt.text(2, 1, r'$\mu=100$', fontsize=15)`

在对应坐标的位置显示文本

`plt.axis([-1, 6, -2, 2])`

设定坐标范围



## annotate函数

`plt.annotate(s, xy=arrpw_crd, xytext=text_crd, arrowprops=dict)`

`s`是需要显示的字符串

`xy`是箭头所在位置	

`xytext`表示文本显示的位置

`arrowprps`是一个字典类型定义了整个箭头显示的属性

### 实例

```python
import numpy as np
import matplotlib.pyplot as plt

a = np.arange(0.0, 5.0, 0.02)
plt.plot(a, np.cos(2*np.pi*a), 'r--')

plt.xlabel('横轴：时间', fontproperties='SimHei', fontsize=15, color='green')
plt.ylabel('纵轴：振幅', fontproperties='SimHei', fontsize=15)
plt.title(r'正弦波实例 $y=cos(2\pi x)$', fontproperties='SimHei', fontsize=25)
plt.annotate( r'$\mu=100$', xy=(2,1), xytext=(3, 1.5),
              arrowprops=dict(facecolor='black', shrink=0.1, width=2))

plt.axis([-1, 6, -2, 2])
plt.grid(True)
plt.show()

```

annotate函数的参数分别是：字符串，箭头位置，备注位置，备注属性

其中备注属性分别是：箭头颜色，缩进比例，宽度

缩进比例指的是箭头两端和指定位置的距离，有的时候不希望箭头直接指到对应位置上，所以要留出一段空白（缩进小于0.5是箭头头部留出空白，大于0.5是尾部留出空白）

更多关于注释的说明，可参考：

`https://blog.csdn.net/u013457382/article/details/50956459`

****



# pyplot的子绘图区域

## `subplot`函数

只能简单分割绘图区域，如果想要在自定义的复杂绘图区域绘制图形需要使用辅助函数`plt.subplot2grid()`

`plt.subplot2grid(GridSpec, CurSpec, colspan=1, rowspan=1)`

理念：设定网络，选中网络，确定选中行列区数量，编号从0开始

### 例子

```python
plt.subplot2grid((3,3),(1,0),colspan=2)
```

第一个参数元组(3,3)表示将一个区域分割成3x3的网格形状

第二个参数(1,0)表示当前为subplot选定的位置在第1行第0列

第三个参数`colspan`表示列的延伸，也就是从选定位置开始，在列的方向上延伸两个长度，也就是选定的位置以及选定位置右侧两个长度的位置（同理也有`rowspan`）

如果在`plt.subplot2grid`后面加上绘制图形的函数，那么这个图形就会在这个区域显示出来

之后可以再调用`subplot2grid`，改变新的位置，切换到新的区域



##  `GridSpec`类

避免每次都重新定义分割区域

`GridSpec`是`Matplotlib`中一个专门用于子区域设定的类

```python
import matplotlib.gridspec as gridspec

gs = gridspec.GridSpec(3,3)

ax1 = plt.subplot(gs[0, :]) #在第一行，占全部列
ax2 = plt.subplot(gs[1, :-1]) #在第二行，到倒数第二列为止
ax3 = plt.subplot(gs[1:, -1])
ax4 = plt.subplot(gs[2, 0])
ax5 = plt.subplot(gs[2, 1])
```

****



# 单元小结

介绍了pyplot子库的基本使用

+ 如何绘制一个坐标系，以及如何确定一个曲线的风格
+ 进一步讲解了在绘制区域中，如何形成子绘制区域的方法，`subplot`和`subplot2grid`函数
+ 介绍了如何在绘制图中增加文本显示和增加中文显示的方法

关键：选取恰当的图形展示数据含义

