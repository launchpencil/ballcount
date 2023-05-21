import streamlit as st
import requests as r

st.title('todo')

with st.form(key='login_form'):
    username = st.text_input('ユーザー名')
    password = st.text_input('パスワード', type='password')
    name = st.text_input('タスク名')
    date = st.date_input('提出期限')
    submit_button = st.form_submit_button(label='実行')

if submit_button:

    if  not (name == ''):
        response = r.get(f'https://api.launchpencil.f5.si/todo/add?user={username}&pass={password}&name={name}&date={date}')

        if response.status_code == 200:
            st.write(response.text)
        else:
            st.error(response.status_code)
    
    else:
        response = r.get(f'https://api.launchpencil.f5.si/todo/?user={username}&pass={password}')
        if response.status_code == 200:
            
            a = response.text.split(',')

            if a[0] == 'エラー':
                if str(a[1]).startswith("Access denied for user"):
                    st.error('認証に失敗しました。ユーザー名またはパスワードが間違っているか設定されていません。')
                else:
                    st.error(a[1])
                st.stop()

            for i in range(len(a) -1):
                st.markdown('* ' + a[i])
            st.write('タスクは以上です')
        else:
            # エラーが発生した場合はエラーメッセージを表示する
            st.error(response.status_code)