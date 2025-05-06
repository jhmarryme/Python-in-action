import logging
import os
import re
from functools import wraps

from dotenv import load_dotenv
from flask import Flask, request, jsonify

from dify_dataset_sdk import DifySDK

# 配置日志记录
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)
load_dotenv(dotenv_path='.env')
API_KEY = os.getenv('DIFY_API_KEY')
if not API_KEY:
    raise ValueError("DIFY_API_KEY is not set in the .env file.")
API_URL = os.getenv('DIFY_API_URL')
if not API_URL:
    raise ValueError("DIFY_API_URL is not set in the .env file.")
sdk = DifySDK(API_KEY, API_URL)


# 日志和异常处理装饰器
def log_and_handle_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        operation_name = func.__name__
        logging.info(f"开始操作: {operation_name}，参数: args={args}, kwargs={kwargs}")
        try:
            result = func(*args, **kwargs)
            logging.info(f"操作 {operation_name} 成功完成。")
            return result
        except Exception as e:
            logging.error(f"操作 {operation_name} 失败。错误信息: {str(e)}")
            return jsonify({"error": str(e)}), 500

    return wrapper


# 提取关键词函数，并移除 content 中的关键词部分
def extract_keywords(content):
    start_index = content.find("K：")
    if start_index != -1:
        # 从 "K：" 后面开始提取关键词
        keyword_str = content[start_index + 2:]
        # 使用中文顿号分割关键词
        keywords = re.split(r'[、，,]', keyword_str)
        # 移除 content 中的关键词部分
        new_content = content[:start_index].strip()
        return keywords, new_content
    return [], content


# 公共的更新分段关键词逻辑
def update_segments_keywords_common(dataset_id, document_id):
    # 获取文档的所有分段
    segments_data = sdk.get_document_segments(dataset_id, document_id)
    for segment in segments_data.get('data', []):
        enabled = segment.get("enabled")
        if not enabled:
            continue
        segment_id = segment["id"]
        content = segment["content"]
        answer = segment.get("answer")
        old_keywords = segment.get("keywords")
        # 提取关键词
        new_keywords, new_content = extract_keywords(content)
        # 暂时不考虑 regenerate_child_chunks 的情况，可根据实际情况修改
        regenerate_child_chunks = None
        if old_keywords is not None and len(old_keywords) > 0:
            final_keywords = []
            for keyword in old_keywords:
                if ',' in keyword or '，' in keyword:
                    # 重新切割关键词
                    sub_keywords = re.split(r'[、，,]', keyword)
                    final_keywords.extend([kw.strip() for kw in sub_keywords if kw.strip()])
                else:
                    final_keywords.append(keyword.strip())
            new_keywords = final_keywords
        # 调用 SDK 方法更新关键词
        sdk.update_segment_keywords(
            dataset_id,
            document_id,
            segment_id,
            new_content,
            answer=answer,
            keywords=new_keywords,
            enabled=enabled,
            regenerate_child_chunks=regenerate_child_chunks
        )
        logging.info(f"已更新数据集 {dataset_id} 中文档 {document_id} 的分段 {segment_id} 的关键词。")
    return segments_data


# 通过文本创建文档
@app.route('/datasets/<dataset_id>/document/create-by-text', methods=['POST'])
@log_and_handle_errors
def create_document_by_text(dataset_id):
    data = request.get_json()
    return jsonify(sdk.create_document_by_text(dataset_id, data))


# 通过文件创建文档
@app.route('/datasets/<dataset_id>/document/create-by-file', methods=['POST'])
@log_and_handle_errors
def create_document_by_file(dataset_id):
    data = request.form.get('data')
    file = request.files.get('file')
    return jsonify(sdk.create_document_by_file(dataset_id, data, file))


# 创建空知识库
@app.route('/datasets', methods=['POST'])
@log_and_handle_errors
def create_empty_dataset():
    data = request.get_json()
    return jsonify(sdk.create_empty_dataset(data))


# 知识库列表
@app.route('/datasets', methods=['GET'])
@log_and_handle_errors
def get_dataset_list():
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 20, type=int)
    return jsonify(sdk.get_dataset_list(page, limit))


# 删除知识库
@app.route('/datasets/<dataset_id>', methods=['DELETE'])
@log_and_handle_errors
def delete_dataset(dataset_id):
    return jsonify(sdk.delete_dataset(dataset_id))


# 通过文本更新文档
@app.route('/datasets/<dataset_id>/documents/<document_id>/update-by-text', methods=['POST'])
@log_and_handle_errors
def update_document_by_text(dataset_id, document_id):
    data = request.get_json()
    return jsonify(sdk.update_document_by_text(dataset_id, document_id, data))


# 通过文件更新文档
@app.route('/datasets/<dataset_id>/documents/<document_id>/update-by-file', methods=['POST'])
@log_and_handle_errors
def update_document_by_file(dataset_id, document_id):
    data = request.form.get('data')
    file = request.files.get('file')
    return jsonify(sdk.update_document_by_file(dataset_id, document_id, data, file))


# 获取文档嵌入状态（进度）
@app.route('/datasets/<dataset_id>/documents/<batch>/indexing-status', methods=['GET'])
@log_and_handle_errors
def get_document_indexing_status(dataset_id, batch):
    return jsonify(sdk.get_document_indexing_status(dataset_id, batch))


# 删除文档
@app.route('/datasets/<dataset_id>/documents/<document_id>', methods=['DELETE'])
@log_and_handle_errors
def delete_document(dataset_id, document_id):
    return jsonify(sdk.delete_document(dataset_id, document_id))


# 知识库文档列表
@app.route('/datasets/<dataset_id>/documents', methods=['GET'])
@log_and_handle_errors
def get_dataset_document_list(dataset_id):
    return jsonify(sdk.get_dataset_document_list(dataset_id))


# 新增分段
@app.route('/datasets/<dataset_id>/documents/<document_id>/segments', methods=['POST'])
@log_and_handle_errors
def add_segments(dataset_id, document_id):
    data = request.get_json()
    return jsonify(sdk.add_segments(dataset_id, document_id, data))


# 查询文档分段
@app.route('/datasets/<dataset_id>/documents/<document_id>/segments', methods=['GET'])
@log_and_handle_errors
def get_document_segments(dataset_id, document_id):
    return jsonify(sdk.get_document_segments(dataset_id, document_id))


# 删除文档分段
@app.route('/datasets/<dataset_id>/documents/<document_id>/segments/<segment_id>', methods=['DELETE'])
@log_and_handle_errors
def delete_document_segment(dataset_id, document_id, segment_id):
    return jsonify(sdk.delete_document_segment(dataset_id, document_id, segment_id))


# 更新文档分段
@app.route('/datasets/<dataset_id>/documents/<document_id>/segments/<segment_id>', methods=['POST'])
@log_and_handle_errors
def update_document_segment(dataset_id, document_id, segment_id):
    data = request.get_json()
    return jsonify(sdk.update_document_segment(dataset_id, document_id, segment_id, data))


# 检索知识库
@app.route('/datasets/<dataset_id>/retrieve', methods=['POST'])
@log_and_handle_errors
def retrieve_dataset(dataset_id):
    data = request.get_json()
    return jsonify(sdk.retrieve_dataset(dataset_id, data))


@app.route('/all-documents', methods=['GET'])
@log_and_handle_errors
def get_all_documents_in_all_datasets():
    dataset_ids_str = request.args.get('dataset_ids')
    if dataset_ids_str:
        dataset_ids = dataset_ids_str.split(',')
    else:
        dataset_ids = None
    return jsonify(sdk.get_all_documents_in_all_datasets(dataset_ids))


# 更新指定 dataset_id 和 document_id 下所有分段的关键词
@app.route('/datasets/<dataset_id>/documents/<document_id>/update-segments-keywords', methods=['GET'])
@log_and_handle_errors
def update_segments_keywords(dataset_id, document_id):
    segments_data = update_segments_keywords_common(dataset_id, document_id)
    return jsonify(segments_data)


# 更新指定数据集下所有文档中所有分段的关键词
@app.route('/datasets/<dataset_id>/update-all-segments-keywords', methods=['GET'])
@log_and_handle_errors
def update_all_segments_keywords_in_dataset(dataset_id):
    # 获取指定数据集下的所有文档
    document_list = sdk.get_dataset_document_list(dataset_id)
    documents = document_list.get('data', [])
    all_segments_data = []
    for document in documents:
        document_id = document.get('id')
        segments_data = update_segments_keywords_common(dataset_id, document_id)
        all_segments_data.append(segments_data)
    return jsonify({"message": f"所有分段关键词在数据集 {dataset_id} 中已更新。",
                    "segments_data": all_segments_data})


if __name__ == '__main__':
    app.run(debug=True)
