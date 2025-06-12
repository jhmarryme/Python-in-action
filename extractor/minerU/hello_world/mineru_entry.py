import os

from dotenv import load_dotenv
from magic_pdf.config.enums import SupportedPdfParseMethod
# 导入必要的模块和类
from magic_pdf.data.data_reader_writer import FileBasedDataWriter, FileBasedDataReader
from magic_pdf.data.dataset import PymuDocDataset
from magic_pdf.model.doc_analyze_by_custom_model import doc_analyze

load_dotenv()
file_location = os.getenv('FILE_LOCATION')

if not file_location:
    raise ValueError("FILE_LOCATION 环境变量未在 .env 文件中设置")

# 参数设置
pdf_file_name = os.path.basename(file_location)  # 获取文件名
name_without_suff = os.path.splitext(pdf_file_name)[0]  # 去除文件扩展名

# 准备环境
local_image_dir, local_md_dir = "output/images", "output"  # 图片和输出目录
image_dir = str(os.path.basename(local_image_dir))  # 获取图片目录名

# 创建输出目录（如果不存在）
os.makedirs(local_image_dir, exist_ok=True)

# 初始化数据写入器
image_writer, md_writer = FileBasedDataWriter(local_image_dir), FileBasedDataWriter(
    local_md_dir
)

# 读取PDF文件内容
reader1 = FileBasedDataReader("")  # 初始化数据读取器
pdf_bytes = reader1.read(file_location)  # 读取PDF文件内容为字节流

# 处理流程
## 创建PDF数据集实例
ds = PymuDocDataset(pdf_bytes)  # 使用PDF字节流初始化数据集

## 推理阶段
if ds.classify() == SupportedPdfParseMethod.OCR:
    # 如果是OCR类型的PDF（扫描件/图片型PDF）
    infer_result = ds.apply(doc_analyze, ocr=True)  # 应用OCR模式的分析

    ## 处理管道
    pipe_result = infer_result.pipe_ocr_mode(image_writer)  # OCR模式的处理管道

else:
    # 如果是文本型PDF
    infer_result = ds.apply(doc_analyze, ocr=False)  # 应用普通文本模式的分析

    ## 处理管道
    pipe_result = infer_result.pipe_txt_mode(image_writer)  # 文本模式的处理管道

### 绘制模型分析结果到每页PDF
infer_result.draw_model(os.path.join(local_md_dir, f"{name_without_suff}_model.pdf"))

### 获取模型推理结果
model_inference_result = infer_result.get_infer_res()

### 绘制布局分析结果到每页PDF
pipe_result.draw_layout(os.path.join(local_md_dir, f"{name_without_suff}_layout.pdf"))

### 绘制文本块(span)分析结果到每页PDF
pipe_result.draw_span(os.path.join(local_md_dir, f"{name_without_suff}_spans.pdf"))

### 获取Markdown格式的内容
md_content = pipe_result.get_markdown(image_dir)  # 包含图片相对路径

### 保存Markdown文件
pipe_result.dump_md(md_writer, f"{name_without_suff}.md", image_dir)

### 获取内容列表（JSON格式）
content_list_content = pipe_result.get_content_list(image_dir)

### 保存内容列表到JSON文件
pipe_result.dump_content_list(md_writer, f"{name_without_suff}_content_list.json", image_dir)

### 获取中间JSON格式数据
middle_json_content = pipe_result.get_middle_json()

### 保存中间JSON数据
pipe_result.dump_middle_json(md_writer, f'{name_without_suff}_middle.json')
