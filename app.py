import streamlit as st
import pandas as pd

st.title("全体")

st.subheader("球種別")
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

adddf.loc["割合"] = adddf.loc["球数"] / adddf.loc["球数", "合計"]

st.dataframe(adddf.T)


st.subheader("コース別")
adddf2 = pd.DataFrame(pd.DataFrame(columns=['ストレート', 'カーブ', 'スライダー', 'チェンジアップ', 'フォーク', 'カットボール', 'ツーシーム', 'シンカー', 'シュート', '合計'], index=["球数", "割合"]))

if 'df9' in st.session_state:
    adddf2 = adddf2.add(st.session_state.df9, fill_value=0)

if 'df10' in st.session_state:
    adddf2 = adddf2.add(st.session_state.df10, fill_value=0)

if 'df11' in st.session_state:
    adddf2 = adddf2.add(st.session_state.df11, fill_value=0)

if 'df12' in st.session_state:
    adddf2 = adddf2.add(st.session_state.df12, fill_value=0)

adddf2.loc["割合"] = adddf2.loc["球数"] / adddf2.loc["球数", "合計"]
st.dataframe(adddf2.T)


st.subheader("コース別")
adddf3 = pd.DataFrame(pd.DataFrame(columns=['ストレート', 'カーブ', 'スライダー', 'チェンジアップ', 'フォーク', 'カットボール', 'ツーシーム', 'シンカー', 'シュート', '合計'], index=["球数", "割合"]))

if 'df13' in st.session_state:
    adddf3 = adddf3.add(st.session_state.df13, fill_value=0)

if 'df14' in st.session_state:
    adddf3 = adddf3.add(st.session_state.df14, fill_value=0)

if 'df15' in st.session_state:
    adddf3 = adddf3.add(st.session_state.df15, fill_value=0)

if 'df16' in st.session_state:
    adddf3 = adddf3.add(st.session_state.df16, fill_value=0)

if 'df17' in st.session_state:
    adddf3 = adddf3.add(st.session_state.df17, fill_value=0)

if 'df18' in st.session_state:
    adddf3 = adddf3.add(st.session_state.df18, fill_value=0)

if 'df19' in st.session_state:
    adddf3 = adddf3.add(st.session_state.df19, fill_value=0)

if 'df20' in st.session_state:
    adddf3 = adddf3.add(st.session_state.df20, fill_value=0)

if 'df21' in st.session_state:
    adddf3 = adddf3.add(st.session_state.df21, fill_value=0)

adddf3.loc["割合"] = adddf3.loc["球数"] / adddf3.loc["球数", "合計"]

st.dataframe(adddf3.T)