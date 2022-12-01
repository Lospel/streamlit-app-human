# -*- coding: utf-8 -*-
import streamlit as st
import streamlit.components.v1 as stc

html_temp = '''
<div style="background-color:#3872fb;padding:10px;border-radius:10px">
    <h1 style="color:white;text-align:center;">IRIS 머신러닝 모형</h1>
</div>
'''

dec_temp = '''
### IRIS 예측 모델 개발
- 시각화, ML앱 개발.
### 데이터 소스
- 어디서 가져옴.
'''

def main():
    stc.html(html_temp)

if __name__ == "__main__":
    main()