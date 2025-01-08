The first file is to organize the format of WeChat reading export notes and convert them to excel format
The second file is an optimized version of the first. Compared with the first file, you can directly copy your notes from WeChat reading and paste them into a txt file to run.
3/4/5 test files for different books
wordcloud.py can generate word clouds.


The main purpose of the code
The code reads a text file (1.txt) containing chapters, original text, comments, and dates, parses the data according to the rules, and then organizes the results into a table and saves it as an Excel file (formatted.xlsx).

steps to use
Prepare input file

In the code, the input file path is: (find the location of the txt file on your computer).
Please ensure that the input file exists.

If the path or file name is different, you need to change the value input_file variable in your code to your file path.
Prepare output folder

The output file path is: (enter the location you want to export to).
Make sure the folder path exists, or change the value output_file variable in your code to the appropriate output path.
run code

Copy the code to a Python file such as parse_text_to_excel.py.
Run in an environment with Python installed.

After the program runs, it will save the extracted content to the specified Excel file and prompt:
Makefile
Copy code
The file has been successfully saved!

Open the Excel file to view the formatted content.
Code input and output parsing
Input content (text file format)
Chapter title:

Format example: Chapter 1: How to learn efficiently
Will be extracted into the section column.

Original content:
Format example: Original text: This is a paragraph of original text.
Will be extracted to the Content column.

Comment content:
Format example: 2023/01/01 post an idea: This is a comment.
The date will be extracted to the Date column, and the comments will be extracted to the Comments column.

General content:
Format example: • This is a normal piece of content.
Will be extracted to the Contents column, but the Comments and Date columns are empty.

Output content (Excel spreadsheet)
List:
Chapter: Save the chapter title.
Content: Save the original or ordinary content under the section.
Comments: Save comments corresponding to the original text.
Date: Save the date of publication of the comment.


Detailed explanation of code logic

Initialize input and output paths
input_file and output_file define the file path. The user needs to ensure that the path is correct.
Define the data storage structure


Regular Expression Matching Rules
Match chapter title: chapter\ d +：(.+)。
Match the original content: Original: (. +).
Match comment and date: (\ d {4}/\ d {2}/\ d {2}) \ s * Post an idea: (. *).
Matches normal content (content with a • symbol): •\ s * (. +).



Convert data to a DataFrame object using pandas.
Use the to_excel () method to save the DataFrame as an Excel file.


Dependent installation:
The program relies on the pandas library. Please ensure that the library is installed before running.
PIP install pandas

Coding issues:
Make sure the input file is UTF-8 encoded, otherwise garbled characters may appear.

第一个文件是为了整理微信读书导出笔记的格式，将其转化为excel格式
第二个文件是第一个的优化版，相比第一个文件，可以直接从微信读书复制笔记，粘贴到txt文件中运行。
3/4/5为不同书籍的测试文件
wordcloud.py 可以生成词云。


代码的主要用途
该代码读取一份包含章节、原文内容、评论和日期的文本文件 (1.txt)，按照规则解析数据，然后将结果整理成表格并保存为 Excel 文件 (格式化.xlsx)。

使用步骤
准备输入文件

在代码中，输入文件路径是：（找到txt文件在你电脑中的位置）。
请确保输入文件存在。

如果路径或文件名不同，需要修改代码中变量 input_file 的值为你的文件路径。
准备输出文件夹

输出文件路径是：（输入你想要导出的位置）。
确保文件夹路径存在，或者修改代码中变量 output_file 的值为合适的输出路径。
运行代码

将代码复制到一个 Python 文件（例如 parse_text_to_excel.py）中。
在安装好 Python 的环境下运行。

程序运行后会将提取的内容保存到指定的 Excel 文件中，并提示：
makefile
复制代码
文件已成功保存！

打开该 Excel 文件即可查看格式化后的内容。
代码的输入和输出解析
输入内容（文本文件格式）
章节标题：

格式示例：章节1：如何高效学习
会被提取到 章节 列。

原文内容：
格式示例：原文：这是一段原文。
会被提取到 内容 列。

评论内容：
格式示例：2023/01/01 发表想法：这是一个评论。
日期会被提取到 日期 列，评论会被提取到 评论 列。

普通内容：
格式示例：• 这是一条普通内容。
会被提取到 内容 列，但 评论 和 日期 列为空。

输出内容（Excel 表格）
列名：
章节：保存章节标题。
内容：保存章节下的原文或普通内容。
评论：保存与原文对应的评论。
日期：保存评论的发表日期。

		
代码逻辑的详细解释

初始化输入与输出路径
input_file 和 output_file 定义了文件路径。用户需确保路径正确。
定义数据存储结构


正则表达式匹配规则
匹配章节标题：章节\d+：(.+)。
匹配原文内容：原文：(.+)。
匹配评论和日期：(\d{4}/\d{2}/\d{2})\s*发表想法：(.*)。
匹配普通内容（带 • 符号的内容）：•\s*(.+)。



使用 pandas 将 data 转换为 DataFrame 对象。
使用 to_excel() 方法将 DataFrame 保存为 Excel 文件。


依赖安装：
程序依赖 pandas 库，请确保在运行前已安装该库：
pip install pandas

编码问题：
确保输入文件为 UTF-8 编码，否则可能会出现乱码。
