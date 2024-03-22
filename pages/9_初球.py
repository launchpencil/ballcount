import streamlit as st
import pandas as pd
import math

st.title("初球")

if 'df9' in st.session_state:
    straight = st.number_input("ストレート", value=math.floor(st.session_state.df9.loc["球数", "ストレート"]))
    curve = st.number_input("カーブ", value=math.floor(st.session_state.df9.loc["球数", "カーブ"]))
    slider = st.number_input("スライダー", value=math.floor(st.session_state.df9.loc["球数", "スライダー"]))
    changeup = st.number_input("チェンジアップ", value=math.floor(st.session_state.df9.loc["球数", "チェンジアップ"]))
    fork = st.number_input("フォーク", value=math.floor(st.session_state.df9.loc["球数", "フォーク"]))
    cutball = st.number_input("カットボール", value=math.floor(st.session_state.df9.loc["球数", "カットボール"]))
    two = st.number_input("ツーシーム", value=math.floor(st.session_state.df9.loc["球数", "ツーシーム"]))
    sinka = st.number_input("シンカー", value=math.floor(st.session_state.df9.loc["球数", "シンカー"]))
    shoot = st.number_input("シュート", value=math.floor(st.session_state.df9.loc["球数", "シュート"]))

else:
    straight = st.number_input("ストレート", value=0, key="ストレート1")
    curve = st.number_input("カーブ", value=0, key="カーブ1")
    slider = st.number_input("スライダー", value=0, key="スライダー1")
    changeup = st.number_input("チェンジアップ", value=0, key="チェンジアップ1")
    fork = st.number_input("フォーク", value=0, key="フォーク1")
    cutball = st.number_input("カットボール", value=0, key="カットボール1")
    two = st.number_input("ツーシーム", value=0, key="ツーシーム1")
    sinka = st.number_input("シンカー", value=0, key="シンカー1")
    shoot = st.number_input("シュート", value=0, key="シュート1")

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

    df9 = pd.DataFrame(data, index=["球数", "割合"])
    st.dataframe(df9.T)

    st.session_state['df9'] = df9