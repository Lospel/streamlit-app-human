# -*- coding: utf-8 -*-
import streamlit as st
import streamlit.components.v1 as stc

# 파일 함수
from eda_app import run_eda_app

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

    # 메뉴 만들기
    menu = ['Home', '탐색적 자료분석', '머신러닝', 'About']
    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == 'Home':
        st.subheader('Home')
        st.markdown(dec_temp, unsafe_allow_html=True)
    elif choice == "탐색적 자료분석":
        # st.subheader('탐색적 자료분석')
        run_eda_app()
    elif choice == "머신러닝":
        st.subheader('머신러닝')
    elif choice == "About":
        st.subheader('About')
    else:
        pass

if __name__ == "__main__":
    main()


import streamlit as st
import utils
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

def Data_Load(path):
    path2, ext = os.path.splitext(path)

    if ext == '.csv':
        # CSV 파일 가져올 시
        df = pd.read_csv(path)
    elif ext =='.xml':
        # DB에서 가져올 경우
        df = pd.read_xml(path)
    elif ext == '.html':
        # 크롤링해서 가져올 경우
        df = pd.read_html(path)

    return df

def run_app():
    st.subheader("탐색적_자료_분석")
    # with st.expander('데이터셋_정보'):
    #     st.markdown(utils.attrib_info)

    # 데이터셋 불러오기
    data_path = "data/iris.csv"
    iris_data = Data_Load(data_path)

    # 서브메뉴 지정
    submenu = st.sidebar.selectbox("서브메뉴", ['기술통계량', '그래프'])
    if submenu == "기술통계량":
        with st.expander("데이터_상세정보"):
            st.dataframe(iris_data, width=700, height=300)

        with st.expander("데이터_타입"):
            iris_dtype = pd.DataFrame(iris_data.dtypes).transpose()
            iris_dtype.index = ['유형']
            st.dataframe(iris_dtype, width=300)

        with st.expander('데이터요약'):
            st.dataframe(pd.DataFrame(iris_data.describe()).transpose(), width=300)

        with st.expander("종_갯수") :
            st.dataframe(iris_data['species'].value_counts())

    elif submenu == "그래프":
        st.subheader('그래프')

        # with st.expander('산점도'):
            
        #     # plotly 그래프
        #     fig1 = px.scatter(iris_data
        #         , x='sepal_width'
        #         , y='sepal_length'
        #         , color= "species"
        #         , size= 'petal_width'
        #         , hover_data=['petal_length']
        #         , title= 'IRIS 산점도')
        #     st.plotly_chart(fig1)

        # # layouts
        # col1, col2 = st.columns(2)
        # with col1:
        #     st.subheader('col1')

        #     # seaborn 그래프
        #     fig, ax = plt.subplots()
        #     sns.boxplot(iris_data, x="species", y="sepal_length", ax= ax)
        #     st.pyplot(fig)
        #     st.write("위 그래프는 ~를 의미합니다.")

        # with col2:
        #     st.subheader('col2')

        #     # 히스토그램 (Matplotlib)
        #     fig, ax = plt.subplots()
        #     ax.hist(iris_data['sepal_length'], color= 'green')
        #     st.pyplot(fig)
        #     st.write("위 그래프는 ~를 의미합니다.")

        # Tabs
        산점도, 박스플롯, 스트립플롯, 페어플롯 = st.tabs(['산점도', '박스플롯', '스트립플롯', '페어플롯'])
        with 산점도:
            # st.write('Welcome Tab1')
            val_species = st.selectbox('종_선택', ('Iris-setosa', 'Iris-versicolor', 'Iris-virginica'))
            st.write('종 선택:', val_species)
            
            result = iris_data[iris_data['species'] == val_species]
            st.dataframe(result)

            fig1 = px.scatter(result
                , x='sepal_width'
                , y='sepal_length'
                , size= 'petal_width'
                , hover_data=['petal_length'])
            st.plotly_chart(fig1)

        with 박스플롯:
            st.write('Welcome Tab2')

    else:
        pass

    