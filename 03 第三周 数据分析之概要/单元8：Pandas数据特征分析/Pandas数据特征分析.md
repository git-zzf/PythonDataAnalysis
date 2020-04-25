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

