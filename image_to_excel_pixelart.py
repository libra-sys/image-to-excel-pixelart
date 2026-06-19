from PIL import Image
from openpyxl import Workbook
from openpyxl.styles import PatternFill
import os
import argparse

def image_to_excel_pixelart(image_path, output_path, pixel_size=10, max_size=200, dpi=300, smooth=True):
    # 打开图片
    img = Image.open(image_path)
    
    # 转换为RGB模式
    img = img.convert('RGB')
    
    # 调整图片大小
    width, height = img.size
    aspect_ratio = height / width
    
    # 确保图片不超过最大尺寸
    if width > max_size:
        width = max_size
        height = int(width * aspect_ratio)
    if height > max_size:
        height = max_size
        width = int(height / aspect_ratio)
    
    # 使用高质量插值进行缩放
    resample_method = Image.LANCZOS if smooth else Image.NEAREST
    img = img.resize((width, height), resample_method)
    
    # 可选的图像增强
    if smooth:
        from PIL import ImageFilter
        img = img.filter(ImageFilter.SMOOTH)
    
    print(f"处理后的图片尺寸: {width}x{height}")
    
    # 创建Excel工作簿
    wb = Workbook()
    ws = wb.active
    
    # 遍历像素并设置单元格颜色
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            # 转换为aRGB格式（FF表示完全不透明）
            hex_color = f"FF{r:02x}{g:02x}{b:02x}"
            
            # 获取单元格
            cell = ws.cell(row=y+1, column=x+1)
            
            # 设置单元格颜色
            cell.fill = PatternFill(start_color=hex_color, end_color=hex_color, fill_type="solid")
    
    # 调整单元格大小
    for col in ws.columns:
        ws.column_dimensions[col[0].column_letter].width = pixel_size / 7
    for row in ws.rows:
        ws.row_dimensions[row[0].row].height = pixel_size
    
    # 保存Excel文件
    wb.save(output_path)
    print(f"Excel像素画已生成：{output_path}")

def main():
    parser = argparse.ArgumentParser(description='图片转Excel像素画工具')
    parser.add_argument('image_path', help='图片路径')
    parser.add_argument('-o', '--output', default='output.xlsx', help='输出Excel路径')
    parser.add_argument('-p', '--pixel_size', type=int, default=10, help='像素大小（值越小越精细）')
    parser.add_argument('-m', '--max_size', type=int, default=200, help='最大尺寸（值越大细节越多）')
    parser.add_argument('-d', '--dpi', type=int, default=300, help='DPI设置（影响质量）')
    parser.add_argument('-s', '--smooth', action='store_true', help='启用平滑处理（提高质量）')
    parser.add_argument('-i', '--interactive', action='store_true', help='交互式模式')
    
    args = parser.parse_args()
    
    if args.interactive or not args.image_path:
        # 交互式模式
        print("图片转Excel像素画工具")
        print("=" * 30)
        
        # 获取用户输入
        image_path = input("请输入图片路径：")
        if not os.path.exists(image_path):
            print("图片路径不存在！")
            return
        
        output_path = input("请输入输出Excel路径（默认：output.xlsx）：")
        if not output_path:
            output_path = "output.xlsx"
        
        try:
            pixel_size = int(input("请输入像素大小（默认：10）："))
        except ValueError:
            pixel_size = 10
        
        try:
            max_size = int(input("请输入最大尺寸（默认：200）："))
        except ValueError:
            max_size = 200
        
        try:
            dpi = int(input("请输入DPI设置（默认：300）："))
        except ValueError:
            dpi = 300
        
        smooth_input = input("是否启用平滑处理？(y/n，默认：y)：").lower()
        smooth = smooth_input != 'n'
    else:
        # 命令行模式
        image_path = args.image_path
        output_path = args.output
        pixel_size = args.pixel_size
        max_size = args.max_size
        dpi = args.dpi
        smooth = args.smooth
    
    if not os.path.exists(image_path):
        print(f"图片路径不存在：{image_path}！")
        return
    
    print("\n开始转换...")
    image_to_excel_pixelart(image_path, output_path, pixel_size, max_size, dpi, smooth)
    print("转换完成！")

if __name__ == "__main__":
    main()