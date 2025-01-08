import re
import pandas as pd

# 输入和输出文件路径
input_file = r"C:\Users\sugarzhao\Desktop\数据库\微信读书整理\1.txt"
output_file = r"D:\0APYTHON\xhs projects\for WeChat reading\0106\results\格式化.xlsx"

# 初始化数据存储结构
data = {
    "章节": [],
    "内容": [],
    "评论": [],
    "日期": []
}

# 定义正则表达式匹配逻辑
chapter_pattern = re.compile(r"章节\d+：(.+)")
content_pattern = re.compile(r"原文：(.+)")
comment_pattern = re.compile(r"(\d{4}/\d{2}/\d{2})\s*发表想法：(.*)")
chapter_name = ""

# 读取文件并解析
with open(input_file, "r", encoding="utf-8") as file:
    lines = file.readlines()
    current_date = None  # 当前日期记录
    current_comment = None  # 当前评论内容
    for line in lines:
        line = line.strip()
        if not line:
            continue
        # 匹配章节
        chapter_match = chapter_pattern.match(line)
        if chapter_match:
            chapter_name = chapter_match.group(1).strip()
            continue
        # 匹配日期和评论
        comment_match = comment_pattern.match(line)
        if comment_match:
            current_date = comment_match.group(1)
            current_comment = comment_match.group(2).strip()
            continue
        # 匹配原文内容（评论的内容）
        content_match = content_pattern.match(line)
        if content_match and current_comment:
            content = content_match.group(1).strip()
            data["章节"].append(chapter_name)
            data["内容"].append(content)
            data["评论"].append(current_comment)
            data["日期"].append(current_date)
            current_comment = None  # 处理完当前评论，重置为 None
            continue
        # 匹配普通内容
        content_match = re.match(r"•\s*(.+)", line)
        if content_match:
            content = content_match.group(1).strip()
            data["章节"].append(chapter_name)
            data["内容"].append(content)
            data["评论"].append("")
            data["日期"].append(current_date)

# 转换为 DataFrame
df = pd.DataFrame(data)

# 导出为 Excel
df.to_excel(output_file, index=False)

print(f"文件已成功保存到：{output_file}")

#内容清晰后可以成功输出。