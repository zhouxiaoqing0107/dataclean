import jieba
jieba.initialize()
import jieba.analyse

s=' 来源：中国科学报人本报讯（记者肖洁）又有一位中国科学家喜获小行星命名殊荣！4月19日下午，中国科学院国家天文台在京举行“周又元星”颁授仪式，" \
           "我国天文学家、中国科学院院士周又元的弟子与后辈在欢声笑语中济济一堂。国家天文台党委书记、" \
           "副台长赵刚在致辞一开始更是送上白居易的诗句：“令公桃李满天下，何须堂前更种花。”" \
           "据介绍，这颗小行星由国家天文台施密特CCD小行星项目组于1997年9月26日发现于兴隆观测站，" \
           "获得国际永久编号第120730号。2018年9月25日，经国家天文台申报，" \
           "国际天文学联合会小天体联合会小天体命名委员会批准，国际天文学联合会《小行星通报》通知国际社会，" \
           "正式将该小行星命名为“周又元星'

sentence_cut=jieba.lcut(s)

# 人工去停用词
def delete_stopword(x, stopword_path, encoding):
    stopwords = []
    for word in open(stopword_path, 'r', encoding=encoding):
        stopwords.append(word.strip())

    stayed_line = ''
    words_delete_stopword = []
    for word in x:
        if word not in stopwords:
            stayed_line += word + ' '  # 去停用词后sentence展示
            words_delete_stopword.append(word)  # 去停用词后更新词语

    return words_delete_stopword

stopword_deleted = delete_stopword(sentence_cut,'hit_stopwords.txt','utf-8')
f=','.join(stopword_deleted)
#output=open('stopword_deleted.txt','w')
#output.write(f)
#output.close()
#input1=open('stopword_deleted.txt','r')
#input1.read()

# 按词性提取
import jieba.posseg as pseg

def select_by_char(x,char_list):
    words=[]
    w=pseg.cut(x)
    for word,flag in w:
        if flag in char_list:
            words.append(word)
    return words

spec_char=select_by_char(f,['n'])

# 替换同义词
def word_substitute(x,synonym_word_path,encoding):
    combine_dict = {}
    for line in open(synonym_word_path,'r',encoding=encoding):
        seperate_word=line.strip().split(' ')
        num=len(seperate_word)
        for i in range(1,num):
            combine_dict[seperate_word[i]]=seperate_word[1]

    final_sentence = ''
    substituted_word=[]
    for word in x:
        if word in combine_dict:
            word = combine_dict[word]
            final_sentence += word # 更改原文
            substituted_word.append(word) #替换同义词后更新词语
        else:
            final_sentence += word
            substituted_word.append(word)
    return substituted_word

synonym_substituted=word_substitute(words_delete_stopword,'dict_synonym.txt','utf-8')

# 词频统计
def word_count(x):
    word_freq={} # dict
    for word in x:
        if word in word_freq:
            word_freq[word]+=1 #对字典key映射的第一个值（频率）+1
        else:
            word_freq[word]=1
    return word_freq

word_count=word_count(synonym_substituted)


# 词语提及率统计
def word_fred_count(x):
    total_freq = sum(word_freq.values())  # 词语总数求和

    word_freq_1 = {}
    for word, freq in x.items():
        freq2 = round((float(freq) / float(total_freq)), 2)  # 求提及率
        word_freq_1[word] = freq2

    return word_freq_1

word_freq_1=word_fred_count(word_freq)


# 降序排序
def sort_word(x):
    word_sort = []
    for word, freq in x.items():
        word_sort.append((word, freq))  # 字典变list
    word_sort.sort(key=lambda x: x[1], reverse=True)  # 按词频排序

    return word_sort

word_sort=sort_word(word_freq)
top_ranked_word=word_sort[:5]


