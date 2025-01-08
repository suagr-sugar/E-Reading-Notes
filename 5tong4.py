import re
import pandas as pd

# 输入和输出文件路径
input_file = r"C:\Users\sugarzhao\Desktop\数据库\微信读书整理\5.txt"
output_file = r"D:\0APYTHON\xhs projects\for WeChat reading\0106\results\5结果.xlsx"

# 初始化数据存储结构
data = {
    "内容": [],
    "评论": [],
    "日期": []
}

# 定义正则表达式匹配逻辑
date_pattern = re.compile(r"◆\s*(\d{4}/\d{2}/\d{2})\s*发表想法")  # 匹配日期
content_pattern = re.compile(r"原文：(.*)")  # 匹配原文内容
general_content_pattern = re.compile(r"^◆\s*(.+)")  # 匹配普通内容（无日期和评论的行）
comment_accumulator = []  # 临时存储评论的多行内容

current_date = None
current_comment = None

# 读取文件并解析
with open(input_file, "r", encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()

        # 匹配日期
        date_match = date_pattern.match(line)
        if date_match:
            # 保存当前记录到数据集（如果有未保存的数据）
            if current_date or comment_accumulator:
                data["内容"].append("")  # 如果没有原文则为空
                data["评论"].append(" ".join(comment_accumulator).strip())  # 合并评论行
                data["日期"].append(current_date)
            # 更新当前日期，并清空临时变量
            current_date = date_match.group(1).strip()
            comment_accumulator = []  # 重置评论
            continue

        # 匹配原文
        content_match = content_pattern.match(line)
        if content_match:
            # 保存当前记录
            content = content_match.group(1).strip()
            data["内容"].append(content)
            data["评论"].append(" ".join(comment_accumulator).strip())  # 合并评论行
            data["日期"].append(current_date)
            # 清空临时变量
            current_comment = None
            comment_accumulator = []
            continue

        # 匹配普通内容（没有评论和日期）
        general_content_match = general_content_pattern.match(line)
        if general_content_match:
            content = general_content_match.group(1).strip()
            data["内容"].append(content)
            data["评论"].append("")  # 无评论
            data["日期"].append("")  # 无日期
            continue

        # 收集评论行（处理评论的多行情况）
        if current_date:
            comment_accumulator.append(line)

# 如果文件结束时还有未保存的记录，保存最后一条
if current_date or comment_accumulator:
    data["内容"].append("")
    data["评论"].append(" ".join(comment_accumulator).strip())
    data["日期"].append(current_date)

# 转换为 DataFrame
df = pd.DataFrame(data)

# 导出为 Excel
df.to_excel(output_file, index=False)

print(f"文件已成功保存到：{output_file}")
