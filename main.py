import streamlit as st
import pandas as pd

st.title("全体")

adddf = pd.DataFrame(pd.DataFrame(columns=['ストレート', 'カーブ', 'スライダー', 'チェンジアップ', 'フォーク', 'カットボール', 'ツーシーム', 'シンカー', 'シュート', '合計'], index=["球数", "割合"]))

if 'df1' in st.session_state:
    adddf = adddf.add(st.session_state.df1, fill_value=0)

if 'df2' in st.session_state:
    adddf = adddf.add(st.session_state.df2, fill_value=0)

if 'df3' in st.session_state:
    adddf = adddf.add(st.session_state.df3, fill_value=0)

if 'df4' in st.session_state:
    adddf = adddf.add(st.session_state.df4, fill_value=0)

if 'df5' in st.session_state:
    adddf = adddf.add(st.session_state.df5, fill_value=0)

if 'df6' in st.session_state:
    adddf = adddf.add(st.session_state.df6, fill_value=0)

if 'df7' in st.session_state:
    adddf = adddf.add(st.session_state.df7, fill_value=0)

if 'df8' in st.session_state:
    adddf = adddf.add(st.session_state.df8, fill_value=0)

if not ["割合", "合計"] == 1:
    adddf.loc["割合"] = adddf.loc["割合"] / adddf.loc["割合", "合計"]

st.dataframe(adddf.T)