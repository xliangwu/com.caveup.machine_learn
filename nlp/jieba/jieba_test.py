import jieba

segs = jieba.cut("我来到北京清华大学", cut_all=True)
print("Full mode:", '/'.join(segs))

segs = jieba.cut("我来到北京清华大学", cut_all=False)
print("Default mode:", '/'.join(segs))

seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")
print("Search mode:", '/'.join(seg_list))

segs = jieba.cut("我来自北栗村")
print("Default mode:", '/'.join(segs))
