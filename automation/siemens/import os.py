import os
import pandas as pd

# 获取当前目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 读取 Excel 文件
excel_file = os.path.join(current_dir, "输出结果.xlsx")
df = pd.read_excel(excel_file, engine='openpyxl')

# 获取当前文件夹下的所有图片文件（忽略后缀）
valid_extensions = (".png", ".jpg", ".jpeg")
folder_images = {os.path.splitext(f.lower())[0] for f in os.listdir(current_dir) if f.lower().endswith(valid_extensions)}

# 处理 Excel 里的订货号（去空格 & 转小写）
df["订货号"] = df["订货号"].astype(str).str.strip().str.lower()

# 计算匹配结果
df["图片是否存在"] = df["订货号"].apply(
    lambda x: "✅ 存在" if x in folder_images else "❌ 不存在"
)

# 保存更新后的 Excel
updated_excel_file = os.path.join(current_dir, "更新后的_输出结果.xlsx")
df.to_excel(updated_excel_file, index=False, engine='openpyxl')

# 输出结果
print("📄 Excel 已更新，新增‘图片是否存在’列")
print(f"✅ 在 Excel 里的订货号: {df[df['图片是否存在'] == '✅ 存在']['订货号'].tolist()}")
print(f"❌ 不在 Excel 里的订货号: {df[df['图片是否存在'] == '❌ 不存在']['订货号'].tolist()}")
print(f"✅ Excel 文件已保存: {updated_excel_file}")
