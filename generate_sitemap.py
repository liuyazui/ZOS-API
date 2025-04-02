import os
from datetime import datetime
import re

# GitHub Pages 基础URL
base_url = "https://liuyazui.github.io/ZOS-API/"

# 当前日期，用于lastmod字段
today = datetime.now().strftime("%Y-%m-%d")

# 打开输入文件（包含所有HTML文件的列表）
with open('html_files_list.txt', 'r') as f:
    html_files = f.readlines()

# 创建sitemap.xml文件
with open('sitemap.xml', 'w', encoding='utf-8') as sitemap:
    # 写入XML头部和根元素
    sitemap.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    sitemap.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    
    # 处理每个HTML文件
    for file_path in html_files:
        file_path = file_path.strip()
        if not file_path:
            continue
            
        # 使用正则表达式提取相对路径
        match = re.search(r'C:\\Users\\liuya\\Desktop\\ZOS-API\\(.*)', file_path)
        if match:
            relative_path = match.group(1)
            # 将Windows反斜杠转换为前斜杠，用于URL
            relative_path = relative_path.replace('\\', '/')
            
            # 构建完整URL
            url = base_url + relative_path
            
            # 写入URL条目
            sitemap.write('  <url>\n')
            sitemap.write(f'    <loc>{url}</loc>\n')
            sitemap.write(f'    <lastmod>{today}</lastmod>\n')
            sitemap.write('    <changefreq>monthly</changefreq>\n')
            sitemap.write('    <priority>0.8</priority>\n')
            sitemap.write('  </url>\n')
    
    # 关闭根元素
    sitemap.write('</urlset>')

print("sitemap.xml 文件已生成完毕，包含了所有HTML文件的URL。") 