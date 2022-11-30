# -*- coding: utf-8 -*-

# core pkgs
import streamlit as st

# data pkgs
import pandas as pd

def main() :
    """코드작성"""
    # Select / Slider

    # 프로그래밍 언어
    proLan = ["파이썬", "자바", "R", "SQL"]
    choice = st.selectbox("휴먼 프로그래밍 언어", proLan) 
    st.write(f"{choice} 언어를 선택함")

    mulChoice = st.multiselect("언어 선택", proLan, default="SQL")
    st.write("선택:", mulChoice)


if __name__ == "__main__":
    main()

# streamlit run 파일명.py