import re
import pandas as pd
from docx import Document

# 打开文件
file_path = r"C:\Users\sugarzhao\Desktop\数据库\微信读书整理\供词与放逐.docx"

# 使用 python-docx 读取 .docx 文件内容
doc = Document(file_path)

# 定义章节、原文和想法正则匹配
chapter_pattern = r"所属章节名称：\s*(.+)"
quote_pattern = r"原文摘录：\s*(.+)"
thought_pattern = r"我的想法：\s*(.+)"

# 数据存储结构
data = []

current_chapter = None
current_quote = None
current_thought = None

# 遍历文档内容
for paragraph in doc.paragraphs:
    line = paragraph.text.strip()
    
    # 匹配章节
    chapter_match = re.match(chapter_pattern, line)
    if chapter_match:
        current_chapter = chapter_match.group(1)
        continue

    # 匹配原文摘录
    quote_match = re.match(quote_pattern, line)
    if quote_match:
        current_quote = quote_match.group(1)
        current_thought = None  # 重置想法
        data.append({"章节": current_chapter, "原文摘录": current_quote, "我的想法": current_thought})
        continue

    # 匹配我的想法
    thought_match = re.match(thought_pattern, line)
    if thought_match and len(data) > 0:
        current_thought = thought_match.group(1)
        data[-1]["我的想法"] = current_thought

# 转换为 DataFrame
df = pd.DataFrame(data)

# 保存为 Excel 文件
output_file = r"D:\0APYTHON\xhs projects\for WeChat reading\0106\results\1结果.xlsx"
df.to_excel(output_file, index=False)

print(f"文件已保存为 {output_file}")
