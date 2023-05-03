import streamlit as st
import requests as r

st.title('todo')

with st.form(key='login_form'):
    username = st.text_input('ユーザー名')
    password = st.text_input('パスワード', type='password')
    submit_button = st.form_submit_button(label='表示')

if submit_button:
    response = r.get(f'https://api.launchpencil.f5.si/todo/?user={username}&pass={password}')
    if response.status_code == 200:
        
        a = response.text.split(',')

        for i in range(len(a) -1):
            st.markdown('* ' + a[i])
    else:
        # エラーが発生した場合はエラーメッセージを表示する
        print("Error: {}".format(response.status_code))