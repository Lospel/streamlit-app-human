# -*- coding: utf-8 -*-

# core pkgs
import streamlit as st

# data pkgs
import pandas as pd

def main() :
    """코드작성"""
    # 버튼 입력
    name = 'Held'

    if st.button("대문자"):
        st.write(f'이름 : {name.upper()}')
    if st.button("소문자"):
        st.write(f'이름 : {name.lower()}')
    
    # 활성화, 비활성화
    status = st.radio('Status', ("활성화", "비활성화"))
    if status == "활성화":
        st.success("활성화 상태")
    else:
        st.error("비활성화 상태")

    # 체크박스
    if st.checkbox("Show/Hide"):
        st.text("무언가를 보여줘요")
        
    with st.expander('python'):
        st.text("Hello Python")

if __name__ == "__main__":
    main()

# streamlit run 파일명.py