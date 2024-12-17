import os

from datasets import Dataset
from dotenv import load_dotenv
from langchain_community.embeddings.dashscope import DashScopeEmbeddings
from langchain_community.llms.tongyi import Tongyi
from ragas import evaluate, RunConfig
from ragas.metrics import faithfulness, answer_relevancy, context_recall, context_precision, answer_similarity, \
    answer_correctness, context_entity_recall

load_dotenv()
os.environ["DASHSCOPE_API_KEY"] = os.getenv("DASHSCOPE_API_KEY")
llm = Tongyi(model_name="qwen-turbo")
embeddings = DashScopeEmbeddings()

data_samples = {
    'question': ['四川面积是多少', '四川有多少人'],
    'answer': ['四川省总面积48.6万平方千米', '四川有9071.4万人'],
    'contexts': [
        [
            '四川省总面积48.6万平方千米，辖21个[地级行政区]，其中18个[地级市]、3个[自治州]。共55个[市辖区]、19个[县级市]，105个[县]，4个[自治县]，合计183个县级区划。街道459个、镇2016个、乡626个，合计3101个乡级区划。']
        , ['截止2023年末，四川省户籍人口9071.4万人']
    ],
    'ground_truth': ['四川省总面积48.6万平方千米', '四川省户籍人口9071.4万人']
}

dataset = Dataset.from_dict(data_samples)
run_config = RunConfig(
    max_retries=5,
    max_wait=120,
    log_tenacity=True
)
print("开始计算。。。。。")
correctness_ = metrics = [
    faithfulness,
    answer_relevancy,
    context_recall,
    context_precision,
    answer_similarity,
    context_entity_recall,
    answer_correctness]

score = evaluate(dataset, correctness_,
                 llm=llm, embeddings=embeddings,
                 raise_exceptions=False, run_config=run_config)
print("计算完成。。。。。。")
print(score)

# 评估结果
{'faithfulness': 1.0000, 'answer_relevancy': 0.6457, 'context_relevancy': 0.6667, 'context_recall': 1.0000,
 'context_precision': 1.0000, 'answer_similarity': 0.9262, 'answer_correctness': 0.9816}
