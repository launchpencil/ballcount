import streamlit as st
import pandas as pd

st.title("ランナーなし")

straight = st.number_input("ストレート", value=0)
curve = st.number_input("カーブ", value=0)
slider = st.number_input("スライダー", value=0)
changeup = st.number_input("チェンジアップ", value=0)
fork = st.number_input("フォーク", value=0)
cutball = st.number_input("カットボール", value=0)
two = st.number_input("ツーシーム", value=0)
sinka = st.number_input("シンカー", value=0)
shoot = st.number_input("シュート", value=0)

data = {
    'ストレート' : [straight],
    'カーブ' : [curve],
    'スライダー' : [slider],
    'チェンジアップ' : [changeup],
    'フォーク' : [fork],
    'カットボール' : [cutball],
    'ツーシーム' : [two],
    'シンカー' : [sinka],
    'シュート' : [shoot]
    }
df = pd.DataFrame(data, columns=["ストレート", "カーブ", "スライダー", "チェンジアップ", "フォーク", "カットボール", "ツーシーム", "シンカー", "シュート"])
df