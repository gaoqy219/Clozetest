#  Created by Bryan on 25/10/2018.
#  Copyright © 2018 Bryan. All rights reserved.
#  ClozeTese V1.2beta
#  File paths need to be modified first!
#  Testfiles with 22 in its name are for this test.

import time
f = open("/Users/gaoqy/Documents/test22file.txt", "r")
w = open("/Users/gaoqy/Documents/test22result.txt", "w")
sp = "\n"
print(sp)
print("————————————————————————————Notice———————————————————————————————")
print("         在本测试中，请根据给出的内容选择你认为最恰当的选项")
print("                 并按数字键 1 2 3 和 4 选择                 ")
print("本测试同时会记录你的答题时间，请选择完毕后，立即按回车键停止计时")
print("—————————————————————————————————————————————————————————————————")
print(sp)
input("现在，请按任意键开始测试。")
print(sp)
while f.readline() != '':
    st = f.readline()
    co = f.readline()
    print(st)
    print(co)
    time0 = time.time()
    an = input("请按 1 2 3 或 4 并按回车键完成:")
    time1 = time.time() - time0
    tm = str(time1)
    w.write(an)
    w.write(sp)
    w.write(tm)
    w.write("\n")
    print(sp)
    input("请按任意键开始下一题～")
    print(sp)
f.close()
w.close()
input("测试已完成，感谢参与！")
print(sp)


"""
Testfile.txt
---start below this line---
#
Sentence1
1.aa    2.bb    3.cc    4.dd
#
Sentence2
1.aa    2.bb    3.cc    4.dd
#
Sentence3
1.aa    2.bb    3.cc    4.dd
......

"""
