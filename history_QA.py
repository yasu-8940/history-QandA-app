import streamlit as st

# プルダウンの選択肢
subject_options = ["日本史", "世界史", "地理"]
level_options = ["初級", "中級", "上級"]
format_options = ["○×式" , "3択式", "語句記述" , "記述式"]

# 各入力欄
subject = st.selectbox("範囲選択", subject_options)          # 日本史など
topic = st.text_input("語句入力1", "江戸時代")               # 江戸時代など
level = st.selectbox("レベル選択", level_options)             # 中級など
format_text = st.selectbox("形式選択", format_options)       # 記述式など
# extra = st.text_input("語句入力2", "人物")                   # 語句入力

# 出力
# st.write(f"{subject}の範囲で{topic}について{level}レベルで{format_text}形式の問題を３問作って下さい。")

# 出力される質問プロンプト
prompt1 = f"{subject}の範囲で{topic}について{level}レベルで{format_text}形式の問題を3問作って下さい。"

st.write(prompt1)

# コピー用ボタン
if st.button("コピー用に表示（質問）"):
    st.code(prompt1, language="text")

#　回答作成
answer1 = st.text_input("回答1", "A") 
answer2 = st.text_input("回答2", "B") 
answer3 = st.text_input("回答3", "C") 

# 出力される解凍プロンプト
prompt2 = f"回答1：{answer1}、回答2：{answer2}、回答3：{answer3}です。正誤判定とそれぞれに対する簡単な解説をお願いします。"

st.write(prompt2)

# コピー用ボタン
if st.button("コピー用に表示（回答）"):
    st.code(prompt2, language="text")

