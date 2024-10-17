import json
import os

from langfuse import Langfuse

# get keys for your project from https://cloud.langfuse.com
os.environ["LANGFUSE_PUBLIC_KEY"] = "pk-lf-78a056fb-a591-45fd-90af-f968267ae458"
os.environ["LANGFUSE_SECRET_KEY"] = "sk-lf-61e7bff0-ea0f-4992-8c28-2b7a43cc41eb"
os.environ["LANGFUSE_HOST"] = "http://localhost:3010"


def load_config(file_path):
    """从文件中加载数据集配置信息"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


if __name__ == '__main__':
    # 配置文件路径
    config_file = 'dataset_config.json'

    # 加载配置文件
    config = load_config(config_file)

    # 初始化Langfuse
    langfuse = Langfuse()

    # 从配置中获取数据集名称和描述
    dataset_name = config.get('dataset_name', 'default_dataset')
    description = config.get('description', 'My first dataset')

    # 创建数据集
    langfuse.create_dataset(
        name=dataset_name,
        description=description,
        metadata=config.get('dataset_metadata', {})
    )

    # 创建数据集条目
    for item in config.get('dataset_items', []):
        langfuse.create_dataset_item(
            dataset_name=dataset_name,
            input=item.get('input', {}),
            expected_output=item.get('expected_output', {}),
            metadata=item.get('metadata', {})
        )
