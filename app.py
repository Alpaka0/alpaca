# app.py — 이 파일만 실행
import streamlit as st
def home(): # ① 함수로
    st.title("🏠 홈")
def data():
    st.title("📊 데이터")
pg = st.navigation([ # ② 등록
    st.Page(home, title="홈",
        icon="🏠", default=True),
    st.Page(data, title="데이터",
        icon="📊"),
])
pg.run() # ③ 실