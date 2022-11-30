# -*- coding: utf-8 -*-

# core pkgs
import streamlit as st

# data pkgs
import pandas as pd

# 이미지 라이브러리
from PIL import Image

def main() :
    """코드작성"""
    # 이미지 추가
    img = Image.open("data/image_03.jpg")
    st.image(img)

    # URL 이미지 삽입
    st.image("https://res.cloudinary.com/dyd911kmh/image/upload/v1640050215/image27_frqkzv.png")

if __name__ == "__main__":
    main()

# streamlit run 파일명.py