import jieba
# 分词
## 精确模式
jieba.cut()
jieba.lcut()
## 全模式
jieba.cut(cut_all=True))
jieba.lcut(cut_all=True))
## 搜索引擎模式
jieba.cut_for_search()
jieba.lcut_for_search()
-----------------------------------------------
# 添加自定义词典
## 与初始化词库一同使用
jieba.load_userdict(dict_path)
## 替换初始化词库
jieba.set_dictionary(filename)
## 增加词
add_word(self, word, freq=None, tag=None)
## 删除词
del_word(word)
##建议词频
suggest_freq(segment, tune=False)
-----------------------------------------------
# 关键词提取
## extract_tags
import jieba.analyse
jieba.analyse.TFIDF(idf_path=None)
jieba.analyse.extract_tags(sentence, topK=20, withWeight=False,allowPOS=())
  # IDF文本语料库切换成自定义语料库 jieba.analyse.set_idf_path(file_name)
  # Stop Words文本语料库可以切换成自定义语料库jieba.analyse.set_stop_words(file_name)
## TextRank
jieba.analyse.textrank()
## 词性标注
import jieba.posseg
pt = jieba.posseg.POSTokenizer()
pt = jieba.posseg
pt.lcut(s)
## Tokenize
jieba.Tokenizer(dictionary=DEFAULT_DICT)
tokenize(unicode_sentence, mode="default", HMM=True)
-----------------------------------------------
# 手动初始化
jieba.initialize()
-----------------------------------------------
#获取前缀词典词频
##
jieba.get_FREQ(word)
##
tokenizer = jieba.Tokenizer()
tokenizer.initialize()
tokenizer.FREQ[] #dict
-----------------------------------------------