"""
🌱 ESG 好物种草助手
基于 DeepSeek API 的产品 ESG 评分和种草文案生成工具
"""

import streamlit as st
import os
from dotenv import load_dotenv
from utils.deepseek_client import DeepSeekClient


def main():
    """主函数：Streamlit 应用入口"""
    
    # 页面配置
    st.set_page_config(
        page_title="ESG 好物种草助手",
        page_icon="🌱",
        layout="centered"
    )
    
    # 加载环境变量
    load_dotenv()
    api_key = os.getenv("DEEPSEEK_API_KEY")
    
    # 标题
    st.title("🌱 ESG 好物种草助手")
    st.markdown("---")
    
    # 侧边栏 - API Key 提示
    with st.sidebar:
        st.header("⚙️ 设置")
        if not api_key:
            st.error("❌ 未找到 DEEPSEEK_API_KEY\n\n请在项目根目录创建 `.env` 文件并填入有效的 API Key")
        else:
            st.success("✅ API Key 已配置")
        st.markdown("---")
        st.markdown("**使用说明：**\n1. 输入产品名称和品牌\n2. 点击'生成内容'\n3. 获取 ESG 评分和种草文案")
    
    # 输入区域
    col1, col2 = st.columns(2)
    with col1:
        product = st.text_input("产品名称", placeholder="例如：Nike Air Force 1")
    with col2:
        brand = st.text_input("品牌", placeholder="例如：Nike")
    
    # 生成按钮
    generate_button = st.button("生成内容", type="primary", use_container_width=True)
    
    # 处理生成逻辑
    if generate_button:
        if not product or not brand:
            st.warning("⚠️ 请填写产品名称和品牌")
        elif not api_key:
            st.error("❌ 请先配置 DeepSeek API Key（见左侧边栏）")
        else:
            # 初始化客户端
            client = DeepSeekClient(api_key)
            
            # 显示加载状态
            with st.spinner("🔍 正在分析产品 ESG 表现..."):
                # 1. 获取 ESG 评分
                esg_result = client.get_esg_score(product, brand)
                
                if esg_result is None:
                    st.error("❌ ESG 评分获取失败，请稍后重试")
                    return
                
                esg_score = esg_result["score"]
                esg_reason = esg_result["reason"]
                
                # 2. 生成种草文案
                copywriting = client.generate_copywriting(product, brand, esg_score, esg_reason)
                
                if copywriting is None:
                    st.error("❌ 文案生成失败，请稍后重试")
                    return
                
                # 3. 如果评分为"差"，获取替代推荐
                alternatives = None
                if esg_score == "差":
                    with st.spinner("💡 正在寻找更可持续的替代品..."):
                        alternatives = client.get_alternative(product)
            
            # 输出结果区域
            st.markdown("---")
            
            # 📊 ESG 评价
            st.subheader("📊 ESG 评价")
            
            # 根据评分显示不同颜色
            score_colors = {
                "优": "green",
                "中": "orange", 
                "差": "red"
            }
            score_emoji = {"优": "✅", "中": "⚠️", "差": "❌"}
            
            color = score_colors.get(esg_score, "gray")
            emoji = score_emoji.get(esg_score, "❓")
            
            st.markdown(f"**{emoji} ESG 评分：<span style='color:{color};font-weight:bold;font-size:1.2em'>{esg_score}</span>**", unsafe_allow_html=True)
            st.write(f"**理由：** {esg_reason}")
            
            # 📝 种草文案
            st.subheader("📝 种草文案")
            st.markdown(copywriting)
            
            # 💡 替代推荐（仅当评分为"差"时显示）
            if esg_score == "差" and alternatives:
                st.subheader("💡 替代推荐")
                st.info("以下产品在功能和品类上相似，但更具可持续性：")
                for alt in alternatives:
                    st.markdown(f"- {alt}")
            
            # 成功提示
            st.success("✨ 内容生成完成！")


if __name__ == "__main__":
    main()
