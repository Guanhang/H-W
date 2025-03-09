import os
import xml.etree.ElementTree as ET
from datetime import datetime

# 配置
base_url = "https://hangnwen.com"  # 替换为你的 GitHub Pages URL
root_dir = "."  # 根目录（当前目录）
xml_output_file = "sitemap.xml"
html_output_file = "sitemap.html"

# 获取当前日期
lastmod_date = datetime.now().strftime("%Y-%m-%d")

# 创建 XML 结构
urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")

# 创建 HTML 内容
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sitemap</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        h1 { color: #333; }
        ul { list-style-type: none; padding: 0; }
        li { margin: 10px 0; }
        a { color: #007BFF; text-decoration: none; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <h1>Sitemap</h1>
    <ul>
"""

# 遍历根目录下的所有文件
for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith(".html"):  # 只处理 HTML 文件
            # 获取文件的相对路径
            filepath = os.path.join(dirpath, filename)
            relative_path = os.path.relpath(filepath, root_dir)

            # 将路径转换为 URL
            url = base_url + "/" + relative_path.replace("\\", "/")  # 确保路径格式正确

            # 创建 XML URL 条目
            url_element = ET.SubElement(urlset, "url")
            ET.SubElement(url_element, "loc").text = url
            ET.SubElement(url_element, "lastmod").text = lastmod_date
            ET.SubElement(url_element, "changefreq").text = "weekly"
            ET.SubElement(url_element, "priority").text = "0.8"

            # 添加 HTML 内容
            html_content += f'<li><a href="{url}">{url}</a></li>\n'

# 完成 HTML 内容
html_content += """
    </ul>
</body>
</html>
"""

# 保存 XML Sitemap
tree = ET.ElementTree(urlset)
tree.write(xml_output_file, encoding="utf-8", xml_declaration=True)

# 保存 HTML Sitemap
with open(html_output_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Sitemap generated: {xml_output_file} and {html_output_file}")