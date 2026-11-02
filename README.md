# 图片转 Excel 像素画工具

## 图文演示

![32乘32测试图生成填色单元格的实际结果](docs/images/runtime-20261102.png)

将一张自制 32×32 几何图交给本仓库脚本，实际生成 1024 个填色单元格的 XLSX。右侧预览读取生成的文件，不是 Microsoft Excel 应用截图。展示页不是项目自带界面；截图中的副本脚本名与仓库文件名不同，运行时以下方命令为准。


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

脚本需要图片路径参数，不能直接无参数运行。

```bash
python image_to_excel_pixelart.py input.png -o output.xlsx --max_size 100
```

如需交互输入，仍需提供位置参数：

```bash
python image_to_excel_pixelart.py input.png --interactive
```

用 `python image_to_excel_pixelart.py --help` 查看选项。

## 参数建议

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--pixel_size` | 10 | 控制单元格显示尺寸，不增加图片采样细节 |
| `--max_size` | 200 | 限制图片最大边长；建议先用 50–100，避免工作簿过大 |
| `--smooth` | 关闭 | 启用平滑处理 |
| `--dpi` | 300 | 当前脚本接收该参数，但没有在输出逻辑中使用，不影响生成效果 |

最大边长决定输出单元格数量，单元格显示尺寸主要影响外观。

## 注意事项

- 图片分辨率过高时建议减小最大尺寸
- 生成的 Excel 文件打开时可能需要启用编辑功能
- 大图片转换时请耐心等待

## License

MIT License
