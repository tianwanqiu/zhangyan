"""
统计一篇文章中英文单词出现的数量
sort 用于排序列表
sorted 可以用于对字典进行排序
"""


class WordsCount:

    def __init__(self):
        self.words_count = {}

    def count_words(self):
        with open('D:\记事本\英文单词统计.txt', encoding='utf-8') as fine:
            for line in fine:
                # 去掉换行
                line = line[:-1]
                words_list = line.split()
                for word in words_list:
                    # 操作字典
                    # if判断初始化一个字典的键和值
                    if word not in self.words_count:
                        self.words_count[word] = 0
                    self.words_count[word] += 1
        print(
            sorted(
                self.words_count.items(),  # items是字典中的一个方法，返回由元组组成的列表。sorted对元组的列表进行排序
                key=lambda x: x[1],  # 根据哪个值排序
                reverse=True
            )[:5]
        )


if __name__ == "__main__":
    test = WordsCount()
    test.count_words()
