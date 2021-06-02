"""
统计文档中成绩的最高分、最低分和平均分
101,小张, 88
102,小王, 77
103,小李, 99
104,小赵, 66
105,小强, 55
"""


def get_scores():
    score = []
    with open('D:\记事本\学分.txt', encoding='utf-8') as f:
        for line in f:
            line = line[:-1]  # 去掉换行符
            fileds = line.split(',')
            score.append(int(fileds[-1]))
    max_scores = max(score)
    min_scores = min(score)
    avg_scores = sum(score) / len(score)
    return max_scores, min_scores, avg_scores

max_scores,  min_scores,  avg_scores=get_scores()
print(f"max_scores={max_scores},min_scores={min_scores},avg_scores={avg_scores}")