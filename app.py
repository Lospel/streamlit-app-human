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

if __name__ == "__main__":
    main()

# streamlit run 파일명.py