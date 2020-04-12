[TOC]

# 本周课程导学

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

