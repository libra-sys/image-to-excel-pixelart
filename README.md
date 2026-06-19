# 图片转 Excel 像素画工具

将任意图片转换为 Excel 格式的像素画，每个像素对应 Excel 中的一个单元格，通过设置单元格颜色来还原图片效果。

## 功能特点

- 支持常见图片格式（JPG、PNG、BMP 等）
- 自动缩放图片到合理尺寸
- 可自定义像素大小和最大尺寸
- 生成标准 `.xlsx` 文件，用 Excel 即可打开查看

## 效果展示

项目包含两个示例成品：

- `luotina_pixelart.xlsx` - 基础质量版本
- `luotina_pixelart_highquality.xlsx` - 高质量版本

## 环境要求

- Python 3.6+
- 依赖库：`pillow`、`openpyxl`

## 安装

```bash
pip install pillow openpyxl
```

## 使用方法

```bash
python image_to_excel_pixelart.py
```

运行后按提示输入：

1. **图片路径** - 要转换的图片文件路径
2. **输出 Excel 路径** - 生成文件的保存路径（默认 `output.xlsx`）
3. **像素大小** - 每个像素块的大小（默认 20，值越大像素块越大）
4. **最大尺寸** - 图片最大边长（默认 100，防止文件过大）

## 参数建议

| 参数 | 推荐值 | 说明 |
|------|--------|------|
| 像素大小 | 10-50 | 值越大文件越大 |
| 最大尺寸 | 50-200 | 防止 Excel 性能问题 |

## 注意事项

- 图片分辨率过高时建议减小最大尺寸
- 生成的 Excel 文件打开时可能需要启用编辑功能
- 大图片转换时请耐心等待

## License

MIT License
