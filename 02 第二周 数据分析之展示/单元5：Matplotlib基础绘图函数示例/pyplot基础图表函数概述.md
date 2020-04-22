[TOC]

# pyplot基础图表函数概述

## 16种图表函数

| 函数                                    | 说明                           |
| --------------------------------------- | ------------------------------ |
| `plt.plot(x,y,fmt...)`                  | 绘制一个坐标图                 |
| `plt.boxplot(data, notch, position)`    | 绘制一个箱型图                 |
| `plt.bar(left, height, width, bottom)`  | 绘制一个条形图                 |
| `plt.barh(width, bottom, left, height)` | 绘制一个横向条形图             |
| `plt.polar(theta, r)`                   | 绘制极坐标图                   |
| `plt.pie(data, explode)`                | 绘制饼图                       |
| `plt.psd(x, NFFT=256, pad_to, Fs)`      | 绘制功率谱密度图               |
| `plt.specgram(x, NFFT=256, Fs)`         | 绘制谱图                       |
| `plt.cohere(x, y, NFFT=256, Fs)`        | 绘制X-Y的相干性函数            |
| `plt.scatter(x,y)`                      | 绘制散点图，其中，x和y长度相同 |
| `plt.step(x, y, where)`                 | 绘制步阶图                     |
| `plt.hist(x, bins, normed)`             | 绘制直方图                     |
| `plt.contour(X, Y, Z, N)`               | 绘制等值图                     |
| `plt.vlines()`                          | 绘制垂直图                     |
| `plt.stem(x, y, linefmt, markerfmt)`    | 绘制柴火图                     |
| `plt.plot_date()`                       | 绘制数据日期                   |

****



# pyplot饼图的绘制

适合展示带有百分比的数据

## 实例

```python
import matplotlib.pyplot as plt

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)

plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)

plt.show()

```

