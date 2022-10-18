------------------------分隔符-------------------------
#  一种分隔符
a = 'name-age-hobby'

b1=a.split()
print(b1)

b2=a.split('-')
print(b2)

b3=a.split('-',1)
print(b3)

b4=a.split('age')
print(b4)

------------------------re模块-------------------------
import re

a = 'name-age-work/habby?salary'
b = 'dfdklfjaldc----++fj' #包含特殊字符
print(re.escape(b))
# 多种分隔符
# split
print('split : %s' % re.split('[-/?]',a))

# match：在目标文本的开头进行匹配
print('match : %s ' % re.match('salary',a))

# search：在整个目标文本中进行匹配
print('search : %s ' %re.search('salary',a))

# findall：扫描整个目标文本，返回所有与规则匹配的子串组成的列表，如果没有匹配的返回空列表
t='test tey fkdi'
print('findall: %s ' %re.findall('te',t))

# fullmatch：要求目标文本要完全匹配规则，否则返回None
re.escape(a) #  'name\\-age\\-work/habby\\?salary'
print('fullmatch : %s ' %re.fullmatch('name\\-age\\-work/habby\\?salary',a))

# sub：将与规则匹配的子串替换为其他文本
test='a-a-b-b-b'
print('sub : %s ' %re.sub('a','c',test))

# 预定义字符
re.findall('\d','8ddaa3')    #匹配所有的十进制数字  0-9
re.findall('\D','8ddaa3')    #匹配所有的非数字，包含下划线
re.findall('\s','8-- d;daa3')   #匹配所有空白字符（空格、TAB等）
re.findall('\S','8-- d;daa3')   #匹配所有非空白字符，包含下划线
re.findall('\w', '8-- d;da__a3')   # 匹配所有字母、汉字、数字    a-z A-Z 0-9
re.findall('\W','8-- d;da__a3')    # 匹配所有非字母、汉字、数字，包含下划线

#特殊字符
a='d8xnq_l;(///00'
re.search('l',a)
re.search('^l',a)  # ^：匹配一行的开头（必须放在正则表达式最前面）
re.search('0$',a)  # $：匹配一行的结尾（必须放在正则表达式最后面）
re.search('c*',a)  # * ：前面的字符可以出现0次或多次（0~无限）
re.search('0+',a)  # +：前面的字符可以出现1次或多次（1~无限）

#  ？ 变"贪婪模式"为"勉强模式"，前面的字符可以出现0次或1次
#  .  匹配除了换行符"\n" 之外的任意单个字符
re.search('a.*x', 'abbbbbxxxxxxx').group()       # Out[]: 'abbbbbxxxxxxx'
re.search('a.*?x', 'abbbbbxxxxxxx').group()      # Out[]: 'abbbbbx'
re.search('a.*?x','abb5xbbbxx823jxxxxx').group() # Out[]: 'abb5x'
re.search('a.?x','abb5xbbbxx823jxxxxx')          # Out[]:  None

# |：两项都进行匹配
re.findall('[a-z]|[0-3]', 'ii34.55')     # Out[]: ['i', 'i', '3']
#  [ ]：代表一个集合
re.findall('[a-z][0-9]+', 'ii34.55')     # Out[]:['i34']
# { }：用于标记前面的字符出现的频率：
re.findall('[a-z]|[0-3]{2}', 'ii34.55')  # Out[]: ['i', 'i']
#用于查看指定分组匹配到的内容
re.search('\w',a).group()                # Out[]:  'd'