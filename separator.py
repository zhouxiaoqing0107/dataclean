# 分隔符
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

## re模块
#  多种分隔符
a = 'name-age-work/habby?salary'

b=re.
1、$：匹配一行的结尾（必须放在正则表达式最后面）

2、^：匹配一行的开头（必须放在正则表达式最前面）

3、*：前面的字符可以出现0次或多次（0~无限）

4、+：前面的字符可以出现1次或多次（1~无限）

5、？：变"贪婪模式"为"勉强模式"，前面的字符可以出现0次或1次

6、.：匹配除了换行符"\n"之外的任意单个字符

7、|：两项都进行匹配

8、[ ]：代表一个集合，有如下三种情况

[abc]：能匹配其中的单个字符
[a-z0-9]：能匹配指定范围的字符，可取反（在最前面加入^）
[2-9] [1-3]：能够做组合匹配
9、{ }：用于标记前面的字符出现的频率，有如下情况：

{n，m}：代表前面字符最少出现n次，最多出现m次
{n，}：代表前面字符最少出现n次，最多不受限制
{，m}：代表前面字符最多出现n次，最少不受限制
{n}：前面的字符必须出现n次