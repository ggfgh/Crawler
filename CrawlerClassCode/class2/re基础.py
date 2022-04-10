import re

# #findall:匹配字符串中所有符合正则的内容
# list = re.findall(r"\d+", "我的电话是10010,我朋友的电话是10086")
# print(list)

# #finditer
# it = re.finditer(r"\d+","我的电话是10010,我朋友的电话是10086")
# for i in it:
#     print(i.group())

#search:找到一个结果就返回，返回的结果是match对象，拿数据要用.group()
# s = re.search(r"\d+", "我的电话是10010,我朋友的电话是10086")
# print(s.group())

# #match:从头开始匹配
# s = re.match(r"\d+","10010,我朋友的电话是10086")
# print(s.group())

#compile:预加载正则表达式
# obj = re.compile(r"\d+")
# ret = obj.finditer("我的电话是10010,我朋友的电话是10086")
# for i in ret:
#     print(i.group())

# ret = obj.findall("sdjfjsfl43432839")
# print(ret)

s = """
<div class='jay'><span id='1'>金鸡奖</span></div>
<div class='apple'><span id='2'>广告歌</span></div>
<div class='haker'><span id='3'>咕咕咕</span></div>
<div class='tom'><span id='4'>嘎嘎嘎</span></div>
"""

#(?P<分组名字>正则) 可以单独从正则匹配的内容中进一步提取内容
obj = re.compile(r"<div class='(?P<a>.*?)'><span id='(?P<b>\d+)'>(?P<c>.*?)</span></div>",re.S)
result = obj.finditer(s)
for i in result:
    print(i.group("a"))
    print(i.group("b"))
    print(i.group("c"))