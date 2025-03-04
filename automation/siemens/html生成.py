import pandas as pd

# 读取 Excel 文件
excel_file = "data.xlsx"  # 确保 data.xlsx 在当前目录
df = pd.read_excel(excel_file, usecols=["描述", "订货号"], engine="openpyxl")

# 生成 HTML 代码
html_output = ""
start_index = 4  # 商品框从 4 开始编号

for i, row in enumerate(df.itertuples(), start=start_index):
    order_number = str(row.订货号).upper()  # 订货号转换为大写
    product_desc = str(row.描述)  # 产品描述

    html_template = f"""
                    <!-- 商品框{i} -->
                    <div class="product-item" data-brand="Siemens" style="border: 1px solid #ddd; border-radius: 8px; padding: 10px; text-align: center; background-color: #fff;">
                        <a href="{order_number}.html"><img src="../siemens/{order_number}.png" style="width: 100%; border-radius: 4px;"></a>
                        <h4 style="margin: 10px 0 5px;">
                            <a href="{order_number}.html">{order_number}</a>
                        </h4>
                        <p style="margin: 0; color: #888;">{product_desc}</p>
                    </div>
    """
    html_output += html_template

# 保存到 HTML 文件
output_file = "output.html"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(html_output)

print(f"HTML 文件已生成: {output_file}")
