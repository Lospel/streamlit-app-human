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

        # Tabs
        산점도, 박스플롯, 스트립플롯, 페어플롯 = st.tabs(['산점도', '박스플롯', '스트립플롯', '페어플롯'])
        with 산점도:
            st.success("파란색: Setosa, 주황색: Versicolor, 녹색: Virginica")
            
            # species_select = st.selectbox('종_선택', ('Iris-setosa', 'Iris-versicolor', 'Iris-virginica'))
            # choise_sp = iris_data[iris_data['species'] == species_select]

            x_select = st.selectbox('산점도_가로',('sepal_width', 'petal_width'))
            y_select = st.selectbox('산점도_세로',('sepal_length', 'petal_length'))

            fig, ax = plt.subplots()
            sns.scatterplot(iris_data
                , x=x_select
                , y=y_select
                , hue='species')
            st.pyplot(fig)

        with 박스플롯:
            st.success("파란색: Setosa, 주황색: Versicolor, 녹색: Virginica")
            box_Y = st.selectbox('박스플롯_세로',('sepal_width', 'sepal_length', 'petal_width', 'petal_length'))

            fig, ax = plt.subplots()
            sns.boxplot(iris_data
                , x='species'
                , y=box_Y
                , hue='species')
            st.pyplot(fig)

        with 스트립플롯 :
            st.success("파란색: Setosa, 주황색: Versicolor, 녹색: Virginica")
            strip_Y = st.selectbox('스트립플롯_세로',('sepal_width', 'sepal_length', 'petal_width', 'petal_length'))

            fig, ax = plt.subplots()
            sns.stripplot(iris_data
                , x='species'
                , y=strip_Y
                , jitter=True
                , edgecolor="gray"
                , hue='species')
                
            st.pyplot(fig)

        with 페어플롯 :
            st.success("파란색: Setosa, 주황색: Versicolor, 녹색: Virginica")
            fig = sns.pairplot(iris_data
                , hue="species"
                , height=3
                , diag_kind="hist")
            st.pyplot(fig)
            
    else:
        pass