from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import re

# 文件路径
file_path = r"C:\Users\sugarzhao\Desktop\数据库\微信读书整理\6《冰岛往事.1，狂暴海》.txt"

# 读取文件内容
with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

# 数据清理 - 删除指定词语（如"发表想法"）
text = re.sub(r"发表想法", "", text)  # 删除所有"发表想法"
text = re.sub(r"原文", "", text)  # 删除所有"原文"

# 定义停止词
stopwords = set(STOPWORDS)
stopwords.update(["发表想法", "原文", "发音为", "意思是"])  # 添加自定义停止词

# 生成词云
wordcloud = WordCloud(
    width=800,
    height=400,
    background_color="white",
    font_path=r"c:\USERS\SUGARZHAO\APPDATA\LOCAL\MICROSOFT\WINDOWS\FONTS\汇文明朝体.TTF",  # 字体文件路径，确保支持中文
    stopwords=stopwords  # 设置停止词
).generate(text)

# 显示词云
plt.figure(figsize=(12, 6), dpi=300)  # 设置更高的 DPI 值，如 300
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
