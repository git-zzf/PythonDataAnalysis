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

## DataFrame类型的定义

Pandas库的二维数据类型

DataFrame类型由共用相同索引的数据组成，包含一个索引和多列数据

类似一个表格，第一列和第一行是索引，其余是数据

索引方式包含行索引和列索引

纵向在0轴，axis=0

横向在1轴，axis=1

### DataFrame类型的特点

DataFrame是一个表格型的数据类型，每列值类型可以不同

DataFrame既有行索引，也有列索引

DataFrame常用于表达二维数据，但也可以表达多维数据



## DataFrame类型的创建

DataFrame可以由如下类型创建：

+ 二维ndarray对象

+ 由一维ndarray、列表、字典、元组或Series构成的字典

+ Series类型
+ 其它的DataFrame类型



### 从二维ndarray对象创建

#### 示例

```python
>>> import pandas as pd
>>> import numpy as np
>>> d = pd.DataFrame(np.arange(10).reshape(2,5))
>>> d
   0  1  2  3  4
0  0  1  2  3  4
1  5  6  7  8  9
```

生成一个10个元素的ndarray类型如何变为2*5的维度

在d中除了0~9的元素本身外，还有两部分自动生成的索引，从0开始



### 从一维ndarray对象字典创建

```python
>>> import pandas as pd
>>> dt = {'one':pd.Series([1, 2, 3], index=['a', 'b', 'c']),
          'two':pd.Series([9, 8, 7, 6], index=['a', 'b', 'c', 'd'])}
>>> d = pd.DataFrame(dt)
>>> d
   one  two
a  1.0    9
b  2.0    8
c  3.0    7
d  NaN    6
```

从一个字典中创建DataFrame类型

第一个元素的键是one，值是Series类型，这个Series类型包含数据[1,2,3]和索引['a','b','c']

第二个元素的键是two，值也是Series类型

从这个字典中创建的DataFrame类型包含两个自动索引部分，`a b c d`和`one two`

其中字典的一个元素就是一列，而这个元素的键就是列索引的名字，分别是one和two

键值对的值就是行数据，第一个元素的值是一个Series类型，包含3个数据和索引，第二个元素的值包含4个数据和索引



```python
>>> pd.DataFrame(dt, index=['b', 'c', 'd'], columns=['two', 'three'])
   two three
b    8   NaN
c    7   NaN
d    6   NaN
```

这里试图从字典中创建一个DataFrame类型，包含行索引`bcd`和列索引`two three`

由于字典中不存在three的元素，所以创建出的DataFrame类型的第二列为空，数据会用NaN补齐



### 从列表类型的字典创建

生成DataFrame类型一般都需要使用字典，不过字典中的元素的值可以使用不同的数据类型，这里使用列表来创建

```python
>>> import pandas as pd
>>> dl = {'one': [1, 2, 3, 4], 'two': [9, 8, 7, 6]}
>>> d = pd.DataFrame(dl, index = ['a', 'b', 'c', 'd'])
>>> d
   one  two
a    1    9
b    2    8
c    3    7
d    4    6
```

在这里生成DataFrame类型的时候，使用dl字典同时自定义索引为`abcd`



## 例子：从房价表单生成DataFrame类型

| 城市 | 环比  | 同比  | 定基  |
| ---- | ----- | ----- | ----- |
| 北京 | 101.5 | 120.7 | 121.4 |
| 上海 | 101.2 | 127.3 | 127.8 |
| 广州 | 101.3 | 119.4 | 120.0 |
| 深圳 | 102.0 | 140.9 | 145.5 |
| 沈阳 | 100.1 | 101.4 | 101.6 |

### 引入库

```python
>>> import pandas as pd
```



### 生成字典

```python
>>> dl = {'城市': ['北京', '上海', '广州', '深圳', '沈阳'], 
          '环比': [101.5, 101.2, 101.3, 102.0, 100.1 ], 
          '同比': [120.7, 127.3, 119.4, 140.9, 101.4 ], 
          '定基': [121.4, 127.8, 120.0, 145.5, 101.6 ]}
```



### 生成DataFrame类型

```python
>>> d = pd.DataFrame(dl, index=['c1', 'c2', 'c3', 'c4', 'c5'])
>>> d
    城市     环比     同比     定基
c1  北京  101.5  120.7  121.4
c2  上海  101.2  127.3  127.8
c3  广州  101.3  119.4  120.0
c4  深圳  102.0  140.9  145.5
c5  沈阳  100.1  101.4  101.6
```



### 查看DataFrame类型

分别查看0轴索引，1轴索引和数据

```python
>>> d.index
Index(['c1', 'c2', 'c3', 'c4', 'c5'], dtype='object')

>>> d.columns
Index(['城市', '环比', '同比', '定基'], dtype='object')

>>> d.values
array([['北京', 101.5, 120.7, 121.4],
       ['上海', 101.2, 127.3, 127.8],
       ['广州', 101.3, 119.4, 120.0],
       ['深圳', 102.0, 140.9, 145.5],
       ['沈阳', 100.1, 101.4, 101.6]], dtype=object)
```



### 获得DataFrame对象的元素

#### 获取列

```python
>>> d['同比']
c1    120.7
c2    127.3
c3    119.4
c4    140.9
c5    101.4
Name: 同比, dtype: float64
```



#### 获取行

```python
>>> d.ix['c2'] #从pandas1.0.0版本开始，移除了ix操作，现在使用loc操作
>>> d.loc['c2']
城市       上海
环比    101.2
同比    127.3
定基    127.8
Name: c2, dtype: object
```



#### 获取某一个位置的数据

```python
>>> d['同比']['c2']
127.3
```

这里不要使用`d.`，直接使用d后面跟上行索引和列索引



## 理解DataFrame类型

DataFrame是二维带“标签”的数组

所有的数据都是用行列索引来组织起来

DataFrame基本操作类似Series，依据行列索引

****



# Pandas库的数据类型操作

## 改变Series和DataFrame对象：增加，删除或重排

增加和重排：使用重新索引

删除：使用drop



## 重新索引

`.reindex()`能够改变或重排Series和DataFrame索引

#### 例子

```python
>>> import pandas as pd
>>> dl = {'城市': ['北京', '上海', '广州', '深圳', '沈阳'], 
          '环比': [101.5, 101.2, 101.3, 102.0, 100.1 ], 
          '同比': [120.7, 127.3, 119.4, 140.9, 101.4 ], 
          '定基': [121.4, 127.8, 120.0, 145.5, 101.6 ]}
>>> d = pd.DataFrame(dl, index=['c1', 'c2', 'c3', 'c4', 'c5'])
>>> d
    城市     环比     同比     定基
c1  北京  101.5  120.7  121.4
c2  上海  101.2  127.3  127.8
c3  广州  101.3  119.4  120.0
c4  深圳  102.0  140.9  145.5
c5  沈阳  100.1  101.4  101.6
```

调整行的顺序

```python
>>> d = d.reindex(index=['c5', 'c4', 'c3', 'c2', 'c1'])
>>> d
    城市     环比     同比     定基
c5  沈阳  100.1  101.4  101.6
c4  深圳  102.0  140.9  145.5
c3  广州  101.3  119.4  120.0
c2  上海  101.2  127.3  127.8
c1  北京  101.5  120.7  121.4
```

调整列的顺序

```python
>>> d = d.reindex(columns=['城市', '同比', '环比', '定基'])
>>> d
    城市     同比     环比     定基
c5  沈阳  101.4  100.1  101.6
c4  深圳  140.9  102.0  145.5
c3  广州  119.4  101.3  120.0
c2  上海  127.3  101.2  127.8
c1  北京  120.7  101.5  121.4
```



### 其它参数

| 参数               | 说明                                             |
| ------------------ | ------------------------------------------------ |
| `index`, `columns` | 新的行列自定义索引                               |
| `fill_value`       | 重新索引中，用于填充缺失位置的值，默认`NaN`      |
| `method`           | 填充方法，`ffill`当前值向前填充，`bfill`向后填充 |
| `limit`            | 最大填充值                                       |
| `copy`             | 默认True，生成新的对象，False时，新旧相等不复制  |



#### 示例

```python
>>> d
    城市     环比     同比     定基
c1  北京  101.5  120.7  121.4
c2  上海  101.2  127.3  127.8
c3  广州  101.3  119.4  120.0
c4  深圳  102.0  140.9  145.5
c5  沈阳  100.1  101.4  101.6
>>> newc = d.columns.insert(4, '新增')
>>> newd = d.reindex(columns=newc, fill_value=200)
>>> newd
    城市     环比     同比     定基   新增
c1  北京  101.5  120.7  121.4  200
c2  上海  101.2  127.3  127.8  200
c3  广州  101.3  119.4  120.0  200
c4  深圳  102.0  140.9  145.5  200
c5  沈阳  100.1  101.4  101.6  200
```

使用`d.columns.insert()`在4的位置增加一个列索引

使用`d.reindex()`生成一个新的DataFrame对象，增加一个列索引，并用200填充这一列的元素

```python
>>> d.index
Index(['c1', 'c2', 'c3', 'c4', 'c5'], dtype='object')
>>> d.columns
Index(['城市', '环比', '同比', '定基'], dtype='object')
```

获取索引，索引都是Index类型，这种类型属于不可修改的类型



### 索引类型的常用方法

| 方法                 | 说明                                   |
| -------------------- | -------------------------------------- |
| `.append(idx)`       | 连接另一个Index对象，产生新的Index对象 |
| `.diff(idx)`         | 计算差集，产生新的Index对象            |
| `.intersection(idx)` | 计算交集                               |
| `.union(idx)`        | 计算并集                               |
| `.delete(loc)`       | 删除`loc`位置处的元素                  |
| `.insert(loc,e)`     | 在`loc`位置增加一个元素e               |

#### 例子

```python
>>> nc = d.columns.delete(2)
>>> ni = d.index.insert(5, 'c6')
>>> nd = d.reindex(index=ni, columns=nc).ffill()
>>> nd
    城市     环比     定基
c1  北京  101.5  121.4
c2  上海  101.2  127.8
c3  广州  101.3  120.0
c4  深圳  102.0  145.5
c5  沈阳  100.1  101.6
c6  沈阳  100.1  101.6
```

在DataFrame中可以通过操作索引可以修改数据值



## 删除指定索引对象

使用`.drop()`删除Series和DataFrame指定行或列索引

### 示例

```python
>>> a = pd.Series([9, 8, 7, 6], index=['a', 'b', 'c', 'd'])
>>> a
a    9
b    8
c    7
d    6
dtype: int64

>>> a.drop(['b', 'c'])
a    9
d    6
dtype: int64

>>> a
a    9
b    8
c    7
d    6
dtype: int64
```

使用`.drop()`方法可以删除对应的索引，不过对象本身不发生变化

`.drop()`可以删除行索引和列索引

```python
>>> d.drop('c5')
    城市     环比     同比     定基
c1  北京  101.5  120.7  121.4
c2  上海  101.2  127.3  127.8
c3  广州  101.3  119.4  120.0
c4  深圳  102.0  140.9  145.5

>>> d.drop('同比', axis=1)
    城市     环比     定基
c1  北京  101.5  121.4
c2  上海  101.2  127.8
c3  广州  101.3  120.0
c4  深圳  102.0  145.5
c5  沈阳  100.1  101.6
```

当希望删除列索引的时候，需要在参数中加上`axis=1`，不然函数默认删除行索引，如果找不到就会报错

****



# Pandas库的数据类型运算

## 算术运算法则

Series和DataFrame类型在运算的时候需要符合的法则：

+ 算术运算是根据行列索引进行运算的，索引补齐后开始运算，不同索引之间不进行运算，只有索引值相同的行或列才进行运算，运算默认产生**浮点数**

+ 补齐时缺项填充`NaN`(空)

+ 当维度不同的数据进行运算的时候，采用广播运算，比如：
  + 用二维的DataFrame和一维的Series进行运算的时候，采用广播运算的逻辑
  + 用一维的Series和零维的数据（一个数）进行运算的时候，零维的数会与一维的Series中的每个数进行运算，这就是广播运算
+ 采用+、-、*、/的符号进行的二元运算将产生新的对象



### 例子

创建两个DataFrame数据

```python
>>> import pandas as pd
>>> import numpy as np
>>> a = pd.DataFrame(np.arange(12).reshape(3,4))
>>> a
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11

>>> b = pd.DataFrame(np.arange(20).reshape(4,5))
>>> b
    0   1   2   3   4
0   0   1   2   3   4
1   5   6   7   8   9
2  10  11  12  13  14
3  15  16  17  18  19
```

数据a和b都是二维DataFrame的数据，不过横纵数量不相同

```python
>>> a + b
      0     1     2     3   4
0   0.0   2.0   4.0   6.0 NaN
1   9.0  11.0  13.0  15.0 NaN
2  18.0  20.0  22.0  24.0 NaN
3   NaN   NaN   NaN   NaN NaN

>>> a * b
      0     1      2      3   4
0   0.0   1.0    4.0    9.0 NaN
1  20.0  30.0   42.0   56.0 NaN
2  80.0  99.0  120.0  143.0 NaN
3   NaN   NaN    NaN    NaN NaN
```

标签相同的值进行运算，标签不同的值用`NaN`填充自动补齐



## 方法形式的算术运算

优点是可以增加可选参数

| 方法              | 说明                     |
| ----------------- | ------------------------ |
| `.add(d,**argws)` | 类型间加法运算，可选参数 |
| `.sub(d,**argws)` | 类型间减法运算，可选参数 |
| `.mul(d,**argws)` | 类型间乘法运算，可选参数 |
| `.div(d,**argws)` | 类型间除法运算，可选参数 |



### 例子

```python
>>> import pandas as pd
>>> import numpy as np
>>> a = pd.DataFrame(np.arange(12).reshape(3,4))
>>> a
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11

>>> b = pd.DataFrame(np.arange(20).reshape(4,5))
>>> b
    0   1   2   3   4
0   0   1   2   3   4
1   5   6   7   8   9
2  10  11  12  13  14
3  15  16  17  18  19

>>> b.add(a, fill_value = 100)
       0      1      2      3      4
0    0.0    2.0    4.0    6.0  104.0
1    9.0   11.0   13.0   15.0  109.0
2   18.0   20.0   22.0   24.0  114.0
3  115.0  116.0  117.0  118.0  119.0

>>> a.mul(b, fill_value = 0)
      0     1      2      3    4
0   0.0   1.0    4.0    9.0  0.0
1  20.0  30.0   42.0   56.0  0.0
2  80.0  99.0  120.0  143.0  0.0
3   0.0   0.0    0.0    0.0  0.0
```

`fill_value = 100`的作用是将运算中缺少的参数用100来补齐，补齐后再进行运算，可以替代`NaN`



### 例子：不同维度数据的运算

DataFrame数据类型和Series数据类型之间的运算

```python
>>> import pandas as pd
>>> import numpy as np
>>> b = pd.DataFrame(np.arange(20).reshape(4,5))
>>> b
    0   1   2   3   4
0   0   1   2   3   4
1   5   6   7   8   9
2  10  11  12  13  14
3  15  16  17  18  19

>>> c = pd.Series(np.arange(4))
>>> c
0    0
1    1
2    2
3    3
dtype: int32
    
>>> c - 10
0   -10
1    -9
2    -8
3    -7
dtype: int32

>>> b - c
      0     1     2     3   4
0   0.0   0.0   0.0   0.0 NaN
1   5.0   5.0   5.0   5.0 NaN
2  10.0  10.0  10.0  10.0 NaN
3  15.0  15.0  15.0  15.0 NaN
```

当一维数据和零维数据（10）进行运算的时候，Series中的每个数都和10进行运算

不同维度间做广播运算，即当低维数据和高维数据进行运算的时候，低维会作用到高维的每一个元素上，一维Series默认在轴1参与运算

同样的，当运算`b - c`时，低维的`c`也作用到了`b`的每一个维度上，`c`默认作用到`b`的1轴上，也就是说，`b`的每一行都与`c`做了运算

如果希望运算发生在零轴上，也就是让`b`的每一列都减去`c`，需要使用`.sub()`函数

```python
>>> b.sub(c, axis=0)
    0   1   2   3   4
0   0   1   2   3   4
1   4   5   6   7   8
2   8   9  10  11  12
3  12  13  14  15  16
```



## 比较运算

### 法则

比较运算只能比较相同索引的元素，不进行补齐

二维和一维、一维和零维间为广播运算

采用>、<、>=、<=、==、!=等符号进行的二元运算产生布尔对象

### 例子：相同维度

```python
>>> import pandas as pd
>>> import numpy as np
>>> a = pd.DataFrame(np.arange(12).reshape(3,4))
>>> a
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11

>>> d = pd.DataFrame(np.arange(12, 0, -1).reshape(3,4))
>>> d
    0   1   2  3
0  12  11  10  9
1   8   7   6  5
2   4   3   2  1

>>> a > d
       0      1      2      3
0  False  False  False  False
1  False  False  False   True
2   True   True   True   True

>>> a == d
       0      1      2      3
0  False  False  False  False
1  False  False   True  False
2  False  False  False  False
```

同维度运算（都是DataFrame），要求尺寸一致，不存在填充，如果尺寸不同，就会报错



### 例子：不同维度

```python
>>> import pandas as pd
>>> import numpy as np
>>> a = pd.DataFrame(np.arange(12).reshape(3,4))
>>> a
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11

>>> c = pd.Series(np.arange(4))
>>> c
0    0
1    1
2    2
3    3
dtype: int32
    
>>> a > c
       0      1      2      3
0  False  False  False  False
1   True   True   True   True
2   True   True   True   True

>>> c > 0
0    False
1     True
2     True
3     True
dtype: bool
```

不同维度，广播运算，默认在1轴（行索引）

****



# 单元小结

## 两个数据类型

+ Series
  + 索引 + 一维数据

+ DataFrame
  + 行列索引 + 二维数据

强调数据和索引之间的关联关系



## 基本方法

重新索引、删除数据、算术运算、比较运算

同样维度的数据运算考虑对齐和填充

不同维度的数据运算要考虑广播运算

像对待单一数据一样对待Series和DataFrame对象

