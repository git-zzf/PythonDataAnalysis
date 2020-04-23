[TOC]

# 本周内容导学

介绍`Pands`库，介绍两个数据类型：

+ `series`
+ `DataFrame`

学习使用Pandas对数据进行摘要，提取数据的基本特征

使用Pandas对房价进行分析

****



# Pandas库的介绍

## Pandas库的引用

Pandas是Python第三方库，提供了：

+ 高性能易用数据类型
+ 分析工具

```python
import pandas as pd
```

`Pandas`基于`Numpy`实现，常与`Numpy`和`Matplotlib`一同使用

### 测试

```python
>>> import pandas as pd
>>> d = pd.Series(range(20))
>>> d

0      0
1      1
2      2
3      3
4      4
5      5
6      6
7      7
8      8
9      9
10    10
11    11
12    12
13    13
14    14
15    15
16    16
17    17
18    18
19    19
dtype: int64
```

左边的一列是索引，右边的是值

```python
>>> d.cumsum()

0       0
1       1
2       3
3       6
4      10
5      15
6      21
7      28
8      36
9      45
10     55
11     66
12     78
13     91
14    105
15    120
16    136
17    153
18    171
19    190
dtype: int64
```

计算前N项的累加和



## Pandas库的理解

两个数据类型：`Series`, `DataFrame`

`Series`是一个一维数据类型

`DataFrame`是一个二维到多维的数据类型

围绕这两个数据类型，Pandas库提供了很多的操作功能：

+ 基本操作
+ 运算操作
+ 特征类操作
+ 关联类操作



### 对比Numpy和Pandas库

| Numpy                                                        | Pandas                                                       |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 基础数据类型`ndarray`，用来表示n维数组                       | 提供了两种基于`ndarray`的扩展数据类型                        |
| 关注数据的结构表达，数据的维度，用多少维度的数据结构存储这些数据 | 关注数据的应用表达，在使用这些数据的时候，如何更有效地提取数据和进行运算 |
| 关注维度：数据间关系                                         | 关注数据与索引间关系                                         |

****



# Pandas库的Series类型

## Series类型

Series类型由一组数据与之相关的数据索引组成

每一个数据都有一个索引对应

### 自动索引

在生成一个Series数据类型的同时，自动生成的索引

```python
>>> import panda as pd
>>> a = pd.Series([9, 8, 7, 6])
>>> a
0    9
1    8
2    7
3    6
dtype: int64

```

使用列表构造一个Series对象，赋值给a

输出a，发现右边的每个元素都有一个在左边的索引对应，这个索引是自动生成的自动索引

数据类型是int64



### 自定义索引

```python
>>> import panda as pd
>>> b = pd.Series([9, 8, 7, 6], index=['a', 'b', 'c', 'd'])
>>> b
a    9
b    8
c    7
d    6
dtype: int64

```

`pd.Series()`有两个参数，第一个是一组数据，第二个是索引

这时，索引列变成了自定义索引

在使用`pd.Series()`函数的时候，如果索引放在了第二个参数的位置，就可以省略`"index="`



## 创建Series类型

Series类型可以由以下类型创建：

+ Python列表
+ 标量值
+ Python字典
+ ndarray
+ 其它函数



### 从标量值创建

```python
>>> import panda as pd
>>> s = pd.Series(25, index=['a', 'b', 'c'])
>>> s
a    25
b    25
c    25
dtype: int64
```

在第一个参数位置只使用一个数字25来创建

这时为了创建一个Series类型，必须在第二个位置增加index的参数，不然就只能创建一个数字的Series，不过`"index="`标识符可以省略。



### 从字典类型创建

#### 直接从字典中构造

```python
>>> import panda as pd
>>> d = pd.Series({'a':9, 'b':8, 'c':7})
>>> d
a    9
b    8
c    7
dtype: int64
```

直接将一个字典类型赋值给`pd.Series()`函数生成Series



#### 在字典之后指定index挑选数据

```python
>>> import panda as pd
>>> e = pd.Series({'a':9, 'b':8, 'c':7}, index=['c', 'a', 'b', 'd'])
>>> e
c    7.0
a    9.0
b    8.0
d    NaN
dtype: float64
```

在另外给出索引参数的时候，会按照索引的顺序输出字典中的数据，分别输出c，a，b，d四个索引对应的数据，这里d索引在字典中没有对应的数据所以输出的是空`NaN`



### 从ndarray类型创建

从numpy类型ndarray创建

#### 自动索引

```python
>>> import panda as pd
>>> import numpy as np
>>> n = pd.Series(np.arange(5))
>>> n
0    0
1    1
2    2
3    3
4    4
dtype: int32
```



#### 使用ndarray索引

```python
>>> import panda as pd
>>> import numpy as np
>>> m = pd.Series(np.arange(5), index=np.arange(9,4,-1))
>>> m
9    0
8    1
7    2
6    3
5    4
dtype: int32
```



## Series类型的基本操作

Series类型包括index和values两部分

Series类型的操作类似`ndarray`和字典类型

### 示例

```python
>>> import panda as pd
>>> b = pd.Series([9, 8, 7, 6], ['a', 'b', 'c', 'd'])
>>> b
a    9
b    8
c    7
d    6
dtype: int64
```



#### 获得索引

使用`.index`获得索引

```python
>>> b.index
Index(['a', 'b', 'c', 'd'], dtype='object')
```

Pandas中的索引的类型就是Index



#### 获得数据

使用`.values`获得数据

```python
>>> b.values
array([9, 8, 7, 6], dtype=int64)
```

数据是`numpy`类型array



#### 索引Series

```python
>>> b['b']
8

>>> b[1]
8
```

使用方括号['b']获取对应的值，也可以通过数字的索引来得到同样的值，这说明自动索引和自定义索引是共同存在的



#### 混合使用索引

```python
>>> b[['c', 'd', 0]]
报错
```

不能同时使用两套索引方法，混用会报错

在索引Series的时候，必须使用一致的索引方式，如果混合使用就会被当作自定义索引，如果找不到这给索引标签就会报错

```python
>>> b[['c', 'd', 'a']]
c    7
d    6
a    9
dtype: int64
```



### 与ndarray类型相似的操作方法

1. 索引方法相同，采用方括号[]
2. `Numpy`中运算和操作可用于Series类型
3. 可以通过自定义索引的列表进行切片
4. 可以通过自动索引进行切片，如果存在自定义索引，则会一同切片



#### 切片

```python
>>> import pandas as pd
>>> b = pd.Series([9, 8, 7, 6], ['a', 'b', 'c', 'd'])
>>> b
a    9
b    8
c    7
d    6
dtype: int64

>>> b[3]
6

>>> b[:3]
a    9
b    8
c    7
dtype: int64
```

由于Series存在自定义索引，所以索引也会被一同保留

注意：

+ 如果是索引一个元素，那返回的就是那个索引对应的值
+ 如果做的是切片，那么切出的依然是Series类型，包含之前的索引



#### 使用比较关系切片

```python
>>> b[b>b.median()]
a    9
b    8
dtype: int64
```

把所有大于中位数的元素输出



#### 对Series做运算

```python
>>> np.exp(b)
a    8103.083928
b    2980.957987
c    1096.633158
d     403.428793
dtype: float64
```

理解：Series类型是索引加值的一种类型，对它的切片和运算全都是生成Series类型，即包含索引和值两部分。不过如果只选取Series中的一个值，那么返回的就是一个值而不是Series类型



### 与字典类型相似的操作

1. 通过自定义索引访问
2. 保留字in操作
3. 使用`.get()`方法



#### 示例

```python
>>> import pandas as pd
>>> b = pd.Series([9, 8, 7, 6], ['a', 'b', 'c', 'd'])
>>> b['b']
8

>>> 'c' in b
True

>>> 0 in b
False

>>> 8 in b
False

>>> b.get('f', 100)
100
```

在字典的操作中，有保留字in，用来判断一个键在不在字典中，对于Series同理，可以判断一个索引在不在Series自定义的索引中，保留字in不会判断自动索引，因此`0 in b`返回的是False

这里不是判断值，因此`8 in b`返回的是False

`.get()`函数指的是从b中提取标签'f'对应的值，如果这个值不存在，就把100返回回来，如果存在就返回'f'对应的值



### Series类型对齐操作

#### 对齐

```python
>>> import pandas as pd
>>> a = pd.Series([1, 2, 3], ['c', 'd', 'e'])
>>> b = pd.Series([9, 8, 7, 6], ['a', 'b', 'c', 'd'])
>>> a + b
a    NaN
b    NaN
c    8.0
d    8.0
e    NaN
dtype: float64
```

生成了两个Series对象，一个是3个元素，一个是4个元素

Series运算的时候考虑的是对应的索引，索引相同的值进行运算，不同的值不进行运算

所以最终的结果是一个5个元素的Series对象，包含所有的索引

因此Series类型在运算中会自动对齐不同索引的数据



#### 对比Numpy

在`Numpy`中，数据的运算是维度的运算，而在Series中，数据的运算要考虑索引



### Series类型的name属性

Series对象和索引都可以有一个名字，存储在属性`.name`中

```python
>>> import pandas as pd
>>> b = pd.Series([9, 8, 7, 6], ['a', 'b', 'c', 'd'])
>>> b.name

```

输入`b.name`没有返回，说明现在b没有名字



#### 添加名字

```python
>>> b.name = 'Series对象'
>>> b.index.name = '索引列'
>>> b
索引列
a    9
b    8
c    7
d    6
Name: Series对象, dtype: int64
```

如果给b指定名字之后，输入b，返回的结果中会出现名字



### Series类型的修改

Series对象可以随时修改并即刻生效

#### 修改示例

```python
>>> import pandas as pd
>>> b = pd.Series([9, 8, 7, 6], ['a', 'b', 'c', 'd'])
>>> b['a'] = 15
>>> b.name = 'Series'
>>> b
a    15
b     8
c     7
d     6
Name: Series, dtype: int64
```

再次修改

```python
>>> b.name = 'New Series'
>>> b['b', 'c'] = 20
>>> b
a    15
b    20
c    20
d     6
Name: New Series, dtype: int64
```

修改之后就可以看到b的名字和值发生了变化



## 理解Series类型

Series 类型是一个一维带标签的数组

存在索引和值两部分

操作类似`ndarray`和字典，根据索引对齐

****



# Pandas库的DataFrame类型