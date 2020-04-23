import requests
import os
url = ["http://python123.io/dv/H1_Strain.wav", "http://python123.io/dv/L1_Strain.wav", "http://python123.io/dv/wf_template.txt"]
root = "E:/Notes/PythonDataAnalysis/02 第二周 数据分析之展示/单元6：实例2：引力波的绘制/引力波数据/"
for i in range(len(url)):
    path = root + url[i].split('/')[-1]
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url[i])
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
                print("文件保存成功")
        else:
            print("文件已存在")
    except:
        print("爬取失败")
              