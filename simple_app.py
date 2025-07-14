"""
[実行方法] Anaconda Promptで対象の環境を起動して以下を実行
steamlit run simple_app.py
"""

import streamlit as st

# タイトル表示
st.title("簡単な Streamlit アプリ")

# ユーザーからテキスト入力を受ける
name = st.text_input("あなたの名前を入力してください：")

# ユーザーからスライダー入力を受ける (最小値, 最大値, デフォルト値)
age = st.slider("あなたの年齢を選択してください:", 0, 100, 25)

# 結果表示
if name:   #もし、name変数が空(null)ではなかったら
    st.write(f"こんにちは{name}さん！ あなたは{age}歳ですね。")
    st.write(f"{age-5}歳に見えますけどね")
else:
    st.write("上記の入力欄に名前を入力してください。")