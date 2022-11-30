# -*- coding: utf-8 -*-

# core pkgs
import streamlit as st

# data pkgs
import pandas as pd

# 이미지 라이브러리
from PIL import Image

def main() :
    """코드작성"""
    # 텍스트 Input
    fname = st.text_input("이름 입력")
    # st.title(fname)
    st.write(fname)

    # 텍스트 영역
    message = st.text_area("입력해주세요!", height=100)
    st.write(message)

if __name__ == "__main__":
    main()

# streamlit run 파일명.py