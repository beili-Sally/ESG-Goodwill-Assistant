# 🌱 ESG 好物种草助手

基于 DeepSeek API 的产品 ESG 评分和种草文案生成工具。

## ✨ 功能特点

- **ESG 评分**：自动评估产品的环境、社会和治理表现（优/中/差）
- **种草文案**：生成小红书/抖音风格的推广文案，带 emoji 和话题标签
- **替代推荐**：当产品 ESG 评级为"差"时，推荐更可持续的替代品

## 📋 前置要求

- Python 3.9+
- DeepSeek API Key（从 [DeepSeek 官网](https://platform.deepseek.com/) 获取）

## 🚀 快速开始

### 1. 克隆或下载项目

```bash
cd ESGprogramme
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 配置 API Key

复制示例文件并填入你的 DeepSeek API Key：

```bash
cp .env.example .env
```

编辑 `.env` 文件：

```
DEEPSEEK_API_KEY=your_actual_api_key_here
```

### 4. 运行应用

```bash
streamlit run app.py
```

浏览器会自动打开 http://localhost:8501

## 📁 项目结构

```
ESGprogramme/
├── app.py                 # 主程序（Streamlit 应用）
├── requirements.txt       # Python 依赖
├── README.md             # 本文件
├── .env.example          # 环境变量示例
├── .gitignore            # Git 忽略文件
└── utils/
    ├── __init__.py
    └── deepseek_client.py # DeepSeek API 客户端封装
```

## 💡 使用示例

### 示例 1：高 ESG 评分产品
- **产品名称**：Allbirds Tree Runners
- **品牌**：Allbirds
- **预期结果**：评分"优"，突出天然材料和碳中和认证

### 示例 2：中等 ESG 评分产品
- **产品名称**：Nike Air Force 1
- **品牌**：Nike
- **预期结果**：评分"中"，提及再生材料计划但指出碳足迹问题

### 示例 3：低 ESG 评分产品
- **产品名称**：Shein 连衣裙
- **品牌**：Shein
- **预期结果**：评分"差"，显示替代推荐

## ⚙️ 技术栈

- **前端**：Streamlit
- **后端**：Python 3.9+
- **API**：DeepSeek Chat API (deepseek-chat 模型)
- **HTTP 客户端**：Requests
- **环境管理**：python-dotenv

## 🔧 自定义配置

### 修改 Prompt

编辑 `utils/deepseek_client.py` 中的三个 Prompt 函数：
- `get_esg_score()` - ESG 评分 Prompt
- `generate_copywriting()` - 文案生成 Prompt
- `get_alternative()` - 替代推荐 Prompt

### 调整重试机制

在 `DeepSeekClient._call_api()` 方法中修改：
- `max_retries`：最大重试次数（默认 2 次）
- `time.sleep(2)`：重试间隔（默认 2 秒）

## ❓ 常见问题

### Q: API 调用失败怎么办？
A: 检查以下几点：
1. `.env` 文件中 API Key 是否正确
2. 网络连接是否正常
3. API Key 是否有足够的余额

### Q: 如何更改生成的文案风格？
A: 修改 `generate_copywriting()` 函数中的 Prompt，调整语气、长度或格式要求。

### Q: 可以批量处理多个产品吗？
A: 当前版本为单用户设计，如需批量处理可扩展代码添加循环调用逻辑。

## 📝 注意事项

- 本项目仅供学习和演示用途
- API 调用会产生费用，请注意用量
- 不要将 `.env` 文件提交到 Git 仓库

## 📄 许可证

MIT License
