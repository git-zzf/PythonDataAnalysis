[TOC]

# 数据的排序

## 对一组数据的理解：运算过程

摘要：采用有损的方式提取数据特征的过程，获得：

+ 基本统计值（含排序）
+ 分布/累计统计
+ 数据特征：相关性、周期性
+ 数据挖掘（形成知识）



## Pandas库的数据排序

### 索引排序

对索引进行排序：

`.sort_index()`方法在指定轴上根据索引进行排序，默认升序

参数：

`.sort_index(axis=0, ascending=True)`



#### 例子

```python
>>> import pandas as pd
>>> import numpy as np
>>> b = pd.DataFrame(np.arange(20).reshape(4,5), index=['c', 'a', 'd', 'b'])
>>> b
    0   1   2   3   4
c   0   1   2   3   4
a   5   6   7   8   9
d  10  11  12  13  14
b  15  16  17  18  19

>>> b.sort_index()
    0   1   2   3   4
a   5   6   7   8   9
b  15  16  17  18  19
c   0   1   2   3   4
d  10  11  12  13  14

>>> b.sort_index(ascending=False)
    0   1   2   3   4
d  10  11  12  13  14
c   0   1   2   3   4
b  15  16  17  18  19
a   5   6   7   8   9
```

原数据的索引是`cadb`，经过排序变成了`abcd`和`dcba`，默认是在0轴上操作（排列行）

 修改参数后，可以对1轴排序：

```python
>>> c = b.sort_index(axis=1, ascending=False)
>>> c
    4   3   2   1   0
c   4   3   2   1   0
a   9   8   7   6   5
d  14  13  12  11  10
b  19  18  17  16  15

>>> c = c.sort_index() #默认对0轴（行索引）进行排序操作
>>> c
    4   3   2   1   0
a   9   8   7   6   5
b  19  18  17  16  15
c   4   3   2   1   0
d  14  13  12  11  10
```



### 数据值排序

`.sort_value()`方法在指定轴上根据数值进行排序，默认升序

对于Series对象，使用：

`Series.sort_values(axis=0, ascending=True)`

对于DataFrame，使用：

`DataFrame.sort_values(by, axis=0, ascending=True)`

`by`参数表示axis轴上的某个索引或索引列表



#### 例子

```python
>>> import pandas as pd
>>> import numpy as np
>>> b = pd.DataFrame(np.arange(20).reshape(4,5), index=['c', 'a', 'd', 'b'])
>>> b
    0   1   2   3   4
c   0   1   2   3   4
a   5   6   7   8   9
d  10  11  12  13  14
b  15  16  17  18  19

>>> c = b.sort_values(2, ascending=False)
    0   1   2   3   4
b  15  16  17  18  19
d  10  11  12  13  14
a   5   6   7   8   9
c   0   1   2   3   4
```

由于默认对0轴（行）排序，所以指定`by`参数为2，在第二列按照元素值对行排序

同样可以指定按照某一行对列进行排序

```python
>>> c = c.sort_values('a', axis=1, ascending=False)
>>> c
    4   3   2   1   0
b  19  18  17  16  15
d  14  13  12  11  10
a   9   8   7   6   5
c   4   3   2   1   0
```

这里按照`a`这一行的数字对各列进行排序



#### 例子：对空值的处理

空值`NaN`统一放到排序的末尾

```python
>>> import pandas as pd
>>> import numpy as np
>>> a = pd.DataFrame(np.arange(12).reshape(3,4), index=['a', 'b', 'c'])
>>> a
   0  1   2   3
a  0  1   2   3
b  4  5   6   7
c  8  9  10  11

>>> b = pd.DataFrame(np.arange(20).reshape(4,5), index=['c', 'a', 'd', 'b'])
>>> b
    0   1   2   3   4
c   0   1   2   3   4
a   5   6   7   8   9
d  10  11  12  13  14
b  15  16  17  18  19

>>> c = a + b
      0     1     2     3   4
a   5.0   7.0   9.0  11.0 NaN
b  19.0  21.0  23.0  25.0 NaN
c   8.0  10.0  12.0  14.0 NaN
d   NaN   NaN   NaN   NaN NaN
```

生成一个DataFrame数据`c`，由于运算的时候，行列数量不同，`c`中包含`NaN`空值

```python
>>> c.sort_values(2, ascending=False)
      0     1     2     3   4
b  19.0  21.0  23.0  25.0 NaN
c   8.0  10.0  12.0  14.0 NaN
a   5.0   7.0   9.0  11.0 NaN
d   NaN   NaN   NaN   NaN NaN

>>> c.sort_values(2, ascending=True)
      0     1     2     3   4
a   5.0   7.0   9.0  11.0 NaN
c   8.0  10.0  12.0  14.0 NaN
b  19.0  21.0  23.0  25.0 NaN
d   NaN   NaN   NaN   NaN NaN
```

对第2列中的元素进行排序，无论是升序还是降序，`NaN`都在这一列的末尾

所以，当对值进行排序的时候，`NaN`不参与排序，所以如果需要对`NaN`的位置排序，需要替换`NaN`的值，否则，将一直在末尾

****



# 数据的基本统计分析

## 统计分析函数

适用于Series和DataFrame类型：

| 方法                  | 说明                             |
| --------------------- | -------------------------------- |
| `.sum()`              | 计算数据的总和，按0轴计算，下同  |
| `.count()`            | 非`NaN`值的数量                  |
| `.mean()` `.median()` | 计算数据的算术平均值、算术中位数 |
| `.var()` `.std()`     | 计算数据的方差、标准差           |
| `.min()` `.max()`     | 计算数据的最小值、最大值         |

适用于Series类型：

| 方法                    | 说明                                                 |
| ----------------------- | ---------------------------------------------------- |
| `.argmin()` `.argmax()` | 计算数据最大值、最小值所在位置的索引位置（自动索引） |
| `.idxmin()` `.idxmax()` | 计算数据最大值、最小值所在位置的索引（自定义索引）   |

除此以外，还有一个通用的方法：

| 方法          | 说明                      |
| ------------- | ------------------------- |
| `.describe()` | 针对0轴（各列）的统计汇总 |



### 例子：describe方法

#### 一维Series对象

```python
>>> import pandas as pd
>>> a = pd.Series([9, 8, 7, 6], index=['a', 'b', 'c', 'd'])
>>> a
a    9
b    8
c    7
d    6
dtype: int64

>>> a.describe()
count    4.000000
mean     7.500000
std      1.290994
min      6.000000
25%      6.750000
50%      7.500000
75%      8.250000
max      9.000000
dtype: float64
```

`a.describe()`将各种统计值一起输出出来

```python
>>> type(a.describe())
pandas.core.series.Series
```

`a.describe()`生成的是一个Series类型

所以可以对这个生成的结果使用Series类型的方法，获得其中某一个值

例如，使用方括号获取其中的一个值：

```python
>>> a.describe()['count']
4.0

>>> a.describe()['max']
9.0
```



#### 二维DataFrame对象

```python
>>> import pandas as pd
>>> import numpy as np
>>> b = pd.DataFrame(np.arange(20).reshape(4,5), index=['c', 'a', 'd', 'b'])
>>> b.describe()
               0          1          2          3          4
count   4.000000   4.000000   4.000000   4.000000   4.000000
mean    7.500000   8.500000   9.500000  10.500000  11.500000
std     6.454972   6.454972   6.454972   6.454972   6.454972
min     0.000000   1.000000   2.000000   3.000000   4.000000
25%     3.750000   4.750000   5.750000   6.750000   7.750000
50%     7.500000   8.500000   9.500000  10.500000  11.500000
75%    11.250000  12.250000  13.250000  14.250000  15.250000
max    15.000000  16.000000  17.000000  18.000000  19.000000
```

所有的值都是按照0轴来计算的，也就是统计每一列的元素的信息

```python
>>> type(b.describe())
pandas.core.frame.DataFrame

>>> b.describe().loc['max']
0    15.0
1    16.0
2    17.0
3    18.0
4    19.0
Name: max, dtype: float64
        
>>> b.describe()[2]
count     4.000000
mean      9.500000
std       6.454972
min       2.000000
25%       5.750000
50%       9.500000
75%      13.250000
max      17.000000
Name: 2, dtype: float64
```

获取每一列的最大值，可以使用`b.describe().loc['max']`（`.ix['max']`无效）来获取，返回值是一个Series对象

****



# 数据的累计统计分析

能够对序列中的前1到N个数进行累计运算，对大量数据的处理减少`for`循环的使用

使得数据的运算变得更加灵活

## 累计统计分析函数

### 基本累计计算函数

适用于Series和DataFrame类型

| 函数         | 说明                      |
| ------------ | ------------------------- |
| `.cumsum()`  | 依次给出前1~n个数的和     |
| `.cumprod()` | 依次给出前1~n个数的积     |
| `.cummax()`  | 依次给出前1~n个数的最大值 |
| `.cummin()`  | 依次给出前1~n个数的最小值 |



#### 例子

```python
>>> import pandas as pd
>>> import numpy as np
>>> b = pd.DataFrame(np.arange(20).reshape(4,5), index=['c', 'a', 'd', 'b'])
>>> b
    0   1   2   3   4
c   0   1   2   3   4
a   5   6   7   8   9
d  10  11  12  13  14
b  15  16  17  18  19

>>> b.cumsum()
    0   1   2   3   4
c   0   1   2   3   4
a   5   7   9  11  13
d  15  18  21  24  27
b  30  34  38  42  46
```

使用`.cumsum()`函数，按照0轴的方向，对于每列进行累计加法，比如第`0`列的第`d`行的元素15，就是原先第`0`列的`c`行加上`a`行加上`d`行的总和

同理：

```python
>>> b.cumprod()
   0     1     2     3     4
c  0     1     2     3     4
a  0     6    14    24    36
d  0    66   168   312   504
b  0  1056  2856  5616  9576

>>> b.cummin()
   0  1  2  3  4
c  0  1  2  3  4
a  0  1  2  3  4
d  0  1  2  3  4
b  0  1  2  3  4

>>> b.cummax()
    0   1   2   3   4
c   0   1   2   3   4
a   5   6   7   8   9
d  10  11  12  13  14
b  15  16  17  18  19
```



### 滚动计算（窗口计算）函数

适用于Series和DataFrame类型，计算相邻w个元素的值

| 方法                                    | 说明                                |
| --------------------------------------- | ----------------------------------- |
| `.rolling(w).sum()`                     | 依次计算相邻w个元素的和             |
| `.rolling(w).mean()`                    | 依次计算相邻w个元素的算术平均值     |
| `.rolling(w).var()`                     | 依次计算相邻w个元素的方差           |
| `.rolling(w).std()`                     | 依次计算相邻w个元素的标准差         |
| `.rolling(w).min()` `.rolling(w).max()` | 依次计算相邻w个元素的最小值和最大值 |



#### 例子

```python
>>> import pandas as pd
>>> import numpy as np
>>> b = pd.DataFrame(np.arange(20).reshape(4,5), index=['c', 'a', 'd', 'b'])
>>> b
    0   1   2   3   4
c   0   1   2   3   4
a   5   6   7   8   9
d  10  11  12  13  14
b  15  16  17  18  19

>>> b.rolling(2).sum()
      0     1     2     3     4
c   NaN   NaN   NaN   NaN   NaN
a   5.0   7.0   9.0  11.0  13.0
d  15.0  17.0  19.0  21.0  23.0
b  25.0  27.0  29.0  31.0  33.0
```

在0轴方向上，对每列中的元素，以两个元素作为一个窗口进行加法运算，例如，`a`行的元素就是`c`行加上`a`行的元素，`d`行的元素就是`a`行加上`d`行的元素

由于`c`行之前没有元素，所以`c`行的值是空值

同理，如果选取窗口选为3：

```python
>>> b.rolling(3).sum()
      0     1     2     3     4
c   NaN   NaN   NaN   NaN   NaN
a   NaN   NaN   NaN   NaN   NaN
d  15.0  18.0  21.0  24.0  27.0
b  30.0  33.0  36.0  39.0  42.0
```

****



# 数据的相关分析

## 概念

相关分析：对于两个事物，表示为X和Y，如何判断它们之间的相关性？

+ X增大，Y增大，两个变量**正相关**
+ X增大，Y减小，两个变量**负相关**
+ X增大，Y无视，两个变量**不相关**



## 度量相关性

### 协方差

两个元素分别和它们的均值做差，然后累加起来，再计算平均值

$cov(X,Y) = \frac{\sum_{k=1}^n (X_i - \overline{X}) (Y_i - \overline{Y})}{n-1}$

+ 如果协方差>0，X和Y正相关
+ 如果协方差<0，X和Y负相关
+ 如果协方差=0，X和Y独立无关

协方差的缺点是不是很精确



### Pearson相关系数

$r = \frac{\sum_{i=1}^n (x_i - \overline{x}) (y_i - \overline{y})}{\sqrt{\sum_{i=1}^n (x_i - \overline{x})^2})\sqrt{\sum_{i=1}^n (y_i - \overline{y})^2})}$

在这里，x和y可以是一组数据，或者随机变量，或者随机变量的观测值

`r`的取值范围是-1到1

对`r`取绝对值：

+ 0.8~1极强相关
+ 0.6~0.8强相关
+ 0.4~0.6中等程度相关
+ 0.2~0.4弱相关
+ 0.0~0.2极弱相关或无相关



## 相关分析函数

| 方法      | 说明                                               |
| --------- | -------------------------------------------------- |
| `.cov()`  | 计算协方差矩阵                                     |
| `.corr()` | 计算相关系数矩阵，Pearson、Spearman、Kendall等系数 |



### 例子

```python
>>> import pandas as pd
>>> hprice = pd.Series([3.04, 22.93, 12.75, 22.6, 12.33], index=['2008', '2009', '2010', '2011', '2012'])
>>> m2 = pd.Series([8.18, 18.38, 9.13, 7.82, 6.69], index=['2008', '2009', '2010', '2011', '2012'])
>>> hprice.corr(m2)
0.5239439145220387
```

0.52表示存在中等相关性

****



# 单元小结

一组数据的摘要：

+ 排序
  + `.sort_index()`
  + `.sort_values()`
+ 基本统计函数
  + `.describe()`
+ 累计统计函数
  + `.cum*()`
  + `.rolling().*()`
+ 相关性分析
  + `.corr()`
  + `.cov()`

