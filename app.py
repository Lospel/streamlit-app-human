# -*- coding: utf-8 -*-

# core pkgs
import streamlit as st

# data pkgs
import pandas as pd

def main() :
    """코드작성"""
    iris_df = pd.read_csv("data/iris.csv")
    st.dataframe(iris_df)
    st.dataframe(iris_df, width=500, height=200)

    # 색상 추가
    st.title("데이터 프레임에 색상 입히기")
    st.dataframe(iris_df.style.highlight_max(axis=0))

    # 코드 보여주기
    myCode = """
    def hello():
        print("Hello World")
    end
    """
    st.code(myCode, language="python")
    
if __name__ == "__main__":
    main()

# streamlit run 파일명.py