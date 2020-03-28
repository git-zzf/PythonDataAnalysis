# Anaconda IDE的基本使用

+ 开源免费

+ 支持近800个第三方库

+ 包含多个主流开发调试环境

+ 适合数据处理和科学计算领域的使用

+ 支持Win/Linux/OS X上使用

下载：`https://www.continuum.io`

`Anaconda`是一个集成各类`Python`工具的集成平台，本身并不是一个开发和调试环境，开始将很多第三方的开发和调试环境集成到一起。



## `Conda`

+ 一个工具，用于包管理和环境管理
+ 包管理（安装，卸载）与`Python`自带的`pip`工具类似，用于管理`Python`第三方库
+ 环境管理能够允许用户使用不同版本的`Python`，并能灵活切换版本



## `Anaconda`

一个基于`conda`这样的管理工具的集合，包含`conda`、某版本的`Python`以及一批第三方库等

`conda`由于是个第三方工具，它很好地将第三方库、`Python`的不同版本、以及`conda`自身都当作包来对待，十分强大。



## 使用`conda`

`conda`有命令行的使用方式

在`cmd`中：

+ 执行`conda --version`来获取`conda`的版本号
+ 执行`conda update conda`升级`conda`



`conda`也有图形界面的使用方式

在“`Anaconda Navigator`”中，`Enviroments`下，`conda`默认生成了一个叫`root`的环境空间，在这个环境空间中，包含了很多已经安装的或未安装的包。在这里可以创建新的`conda`环境，并且在

新的`conda`环境中增加我们需要的`conda`包



## `Spyder`工具

编写和调试`Python`的工具

分为编辑区、文件导航和帮助以及`Ipython`区（包含运行结果和获得输入）

配置`Spyder`外观

`Tools` --> `Preference` --> `Syntax coloring` --> `Monokai`



## 交互式编程环境：`IPython`

功能强大的交互式shell

使得输出和输入变得非常清晰

适合进行交互式的数据可视化以及GUI的相关开发

小技巧：

`IPython`中的问号：

+ 对于函数和变量，在变量之前或之后增加一个问号来获得这个函数和变量的通用信息
+ 比如对于变量来说可以知道它的类型、值以及描述信息，对于函数可以知道它的源代码

`Ipython`中的提示字段：

+ 非常明确的`In`，`Out`字段以及输入命令的序号（在当前`IPython`启动之后）

`IPython`的`run`执行`.py`程序命令：

+ 使用`%run`后面加上一个`Python`文件，这个文件可以在系统的任何一个目录下，通过输入路径来执行这个文件
+ 注意：`%run`在一个空的命名空间执行`%`，也就是说这个程序必须在它的内部包含足够的`import`变量使得这个程序可以不借助于现有的命名空间来执行

`IPython`的`%`魔术命令：

| 常用命令            | 说明                                        |
| ------------------- | ------------------------------------------- |
| `%magic`            | 显示所有魔术命令                            |
| `%hist`             | `IPython`命令的输入历史                     |
| `%pdb`              | 异常发生后自动进入调试器                    |
| `%reset`            | 删除当前命名空间中的全部变量或名称          |
| `%who`              | 显示`IPython`当前命名空间中已经定义的变量   |
| `%time statement`   | 给出代码的执行时间，`statement`表示一段代码 |
| `%timeit statement` | 多次执行代码，计算综合平均执行时间          |

`IPthon`通过调用`Python`解释器核心的交互式环境，这个环境能够显示很多的图形图像，让用户理解，而程序本身是在后台内核执行，`IPython`只是一个前台的显示脚本。

魔术命令例子：

```python
>>> import numpy as np

>>> a = np.random.randn(1000,1000)

>>> %timeit np.dot(a,a)
31.3 ms ± 370 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)

>>> %who
a        np      

>>> %hist
import numpy as np
a = np.random.randn(1000,1000)
%timeit np.dot(a,a)
%who
%hist

```

