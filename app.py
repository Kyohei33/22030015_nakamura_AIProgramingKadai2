"""
[実行方法] Anaconda Promptで対象の環境を起動して以下を実行
steamlit run simple_app.py
"""

import streamlit as st
from analyzer import analyze_text, analyze_file

st.set_page_config(page_title="日本語テキスト解析くん", layout="wide")

st.title("📊 日本語テキスト解析くん")
st.write("日本語テキストを形態素解析して、単語頻度などを表示するアプリです。")

option = st.radio("入力方法を選んでください", ["テキストを入力", "ファイルをアップロード"])

if option == "テキストを入力":
    text_input = st.text_area("ここに日本語の文章を入力してください", height=200)
    if st.button("解析実行") and text_input.strip():
        with st.spinner("解析中..."):
            result = analyze_text(text_input)
            st.success("解析完了！")
            st.dataframe(result)
elif option == "ファイルをアップロード":
    uploaded_file = st.file_uploader("txtファイルをアップロード", type=["txt"])
    if uploaded_file is not None:
        content = uploaded_file.read().decode("utf-8")
        with st.spinner("解析中..."):
            result = analyze_file(content)
            st.success("解析完了！")
            st.dataframe(result)
