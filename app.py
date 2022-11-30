# -*- coding: utf-8 -*-

# core pkgs
import streamlit as st

# data pkgs
import pandas as pd

def main() :
    """코드작성"""
    iris_df = pd.read_csv("data/iris.csv")
    st.dataframe(iris_df)

if __name__ == "__main__":
    main()

# streamlit run 파일명.py