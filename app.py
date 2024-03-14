import streamlit as st

st.title("ランナーなし")

straight = st.number_input("ストレート", value=0)
curve = st.number_input("カーブ", value=0)
slider = st.number_input("スライダー", value=0)
changeup = st.number_input("チェンジアップ", value=0)
fork = st.number_input("フォーク", value=0)