import requests
from requests.exceptions import RequestException


class DifySDKException(Exception):
    """自定义 SDK 异常类"""

    def __init__(self, message, status_code=None):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class DifySDK:
    def __init__(self, api_key, api_url):
        self.api_key = api_key
        self.base_url = api_url

    def _add_auth_header(self, headers):
        headers["Authorization"] = f"Bearer {self.api_key}"
        return headers

    def _send_request(self, method, url, headers=None, json=None, data=None, files=None):
        headers = self._add_auth_header(headers or {})
        try:
            response = requests.request(method, url, headers=headers, json=json, data=data, files=files)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            try:
                error_data = response.json()
                error_message = error_data.get('message', str(e))
                status_code = response.status_code
            except (KeyError, ValueError):
                error_message = str(e)
                status_code = response.status_code if hasattr(response, 'status_code') else None
            raise DifySDKException(error_message, status_code)

    # 通过文本创建文档
    def create_document_by_text(self, dataset_id, data):
        url = f"{self.base_url}/datasets/{dataset_id}/document/create-by-text"
        return self._send_request('POST', url, headers={"Content-Type": "application/json"}, json=data)

    # 通过文件创建文档
    def create_document_by_file(self, dataset_id, data, file):
        url = f"{self.base_url}/datasets/{dataset_id}/document/create-by-file"
        files = {'file': file}
        data_dict = {'data': data}
        return self._send_request('POST', url, data=data_dict, files=files)

    # 创建空知识库
    def create_empty_dataset(self, data):
        url = f"{self.base_url}/datasets"
        return self._send_request('POST', url, headers={"Content-Type": "application/json"}, json=data)

    # 知识库列表
    def get_dataset_list(self, page=1, limit=20):
        url = f"{self.base_url}/datasets?page={page}&limit={limit}"
        return self._send_request('GET', url)

    # 删除知识库
    def delete_dataset(self, dataset_id):
        url = f"{self.base_url}/datasets/{dataset_id}"
        return self._send_request('DELETE', url)

    # 通过文本更新文档
    def update_document_by_text(self, dataset_id, document_id, data):
        url = f"{self.base_url}/datasets/{dataset_id}/documents/{document_id}/update-by-text"
        return self._send_request('POST', url, headers={"Content-Type": "application/json"}, json=data)

    # 通过文件更新文档
    def update_document_by_file(self, dataset_id, document_id, data, file):
        url = f"{self.base_url}/datasets/{dataset_id}/documents/{document_id}/update-by-file"
        files = {'file': file}
        data_dict = {'data': data}
        return self._send_request('POST', url, data=data_dict, files=files)

    # 获取文档嵌入状态（进度）
    def get_document_indexing_status(self, dataset_id, batch):
        url = f"{self.base_url}/datasets/{dataset_id}/documents/{batch}/indexing-status"
        return self._send_request('GET', url)

    # 删除文档
    def delete_document(self, dataset_id, document_id):
        url = f"{self.base_url}/datasets/{dataset_id}/documents/{document_id}"
        return self._send_request('DELETE', url)

    # 知识库文档列表
    def get_dataset_document_list(self, dataset_id):
        url = f"{self.base_url}/datasets/{dataset_id}/documents"
        return self._send_request('GET', url)

    # 新增分段
    def add_segments(self, dataset_id, document_id, data):
        url = f"{self.base_url}/datasets/{dataset_id}/documents/{document_id}/segments"
        return self._send_request('POST', url, headers={"Content-Type": "application/json"}, json=data)

    # 查询文档分段
    def get_document_segments(self, dataset_id, document_id):
        url = f"{self.base_url}/datasets/{dataset_id}/documents/{document_id}/segments"
        return self._send_request('GET', url, headers={"Content-Type": "application/json"})

    # 删除文档分段
    def delete_document_segment(self, dataset_id, document_id, segment_id):
        url = f"{self.base_url}/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}"
        return self._send_request('DELETE', url, headers={"Content-Type": "application/json"})

    # 更新文档分段
    def update_document_segment(self, dataset_id, document_id, segment_id, data):
        url = f"{self.base_url}/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}"
        return self._send_request('POST', url, headers={"Content-Type": "application/json"}, json=data)

    # 检索知识库
    def retrieve_dataset(self, dataset_id, data):
        url = f"{self.base_url}/datasets/{dataset_id}/retrieve"
        return self._send_request('POST', url, headers={"Content-Type": "application/json"}, json=data)

    def _process_documents_for_dataset(self, dataset_id, all_datasets_docs):
        doc_list = self.get_dataset_document_list(dataset_id)
        documents = doc_list.get('data', [])
        simplified_docs = []
        for doc in documents:
            simplified_doc = {
                'document_id': doc.get('id'),
                'document_name': doc.get('name')
            }
            simplified_docs.append(simplified_doc)
        if dataset_id not in all_datasets_docs:
            all_datasets_docs[dataset_id] = {
                'dataset_id': dataset_id,
                'documents': simplified_docs
            }
        else:
            all_datasets_docs[dataset_id]['documents'].extend(simplified_docs)
        return all_datasets_docs

    def get_all_documents_in_all_datasets(self, dataset_ids=None):
        all_datasets_docs = {}
        if dataset_ids is None or len(dataset_ids) == 0:
            page = 1
            while True:
                dataset_list = self.get_dataset_list(page=page)
                datasets = dataset_list.get('data', [])
                if not datasets:
                    break
                for dataset in datasets:
                    dataset_id = dataset.get('id')
                    all_datasets_docs = self._process_documents_for_dataset(dataset_id, all_datasets_docs)
                page += 1
        else:
            for dataset_id in dataset_ids:
                all_datasets_docs = self._process_documents_for_dataset(dataset_id, all_datasets_docs)
        return list(all_datasets_docs.values())

    # 更新文档分段关键词
    def update_segment_keywords(self, dataset_id, document_id, segment_id, content, answer=None, keywords=None,
                                enabled=None, regenerate_child_chunks=None):
        url = f"{self.base_url}/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}"
        data = {
            "segment": {
                "content": content
            }
        }
        if answer is not None:
            data["segment"]["answer"] = answer
        if keywords is not None:
            data["segment"]["keywords"] = keywords
        if enabled is not None:
            data["segment"]["enabled"] = enabled
        if regenerate_child_chunks is not None:
            data["segment"]["regenerate_child_chunks"] = regenerate_child_chunks

        return self._send_request('POST', url, headers={"Content-Type": "application/json"}, json=data)
