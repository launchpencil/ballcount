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

sumnorun = straight + curve + slider + changeup + fork + cutball + two + sinka + shoot

if sumnorun != 0:
    data = {
        'ストレート' : [straight, straight/sumnorun],
        'カーブ' : [curve, curve/sumnorun],
        'スライダー' : [slider, slider/sumnorun],
        'チェンジアップ' : [changeup, changeup/sumnorun],
        'フォーク' : [fork, fork/sumnorun],
        'カットボール' : [cutball, cutball/sumnorun],
        'ツーシーム' : [two, two/sumnorun],
        'シンカー' : [sinka, sinka/sumnorun],
        'シュート' : [shoot, shoot/sumnorun],
        '合計' : [sumnorun, 1]
        }

    df = pd.DataFrame(data, index=["球数", "割合"])
    st.dataframe(df.T)