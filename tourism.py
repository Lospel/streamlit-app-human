import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def Data_Load(path):
    df = pd.read_csv(path,encoding="euc-kr")
    return df

def runApp():
    st.subheader("자료분석")

    data_path = "data/전라북도 남원시_광한루원입장객_20220928.csv"
    tourism_data = Data_Load(data_path)
    tourism_data.columns = ["year","Paid_admission","Free_admission","All_visitors","Month"]
    tourism_data['year'] = pd.to_datetime(tourism_data['year'],infer_datetime_format=True)
    tourism_data['Month'] = tourism_data['year'].dt.month
    tourism_data['year'] = tourism_data['year'].dt.year

    submenu = st.sidebar.selectbox("서브메뉴", ['통계', '그래프'])
    if submenu == "통계":
        with st.expander("데이터_상세정보"):
            st.dataframe(tourism_data, width=700, height=300)

        with st.expander("데이터_타입"):
            tourism_dtype = pd.DataFrame(tourism_data.dtypes).transpose()
            tourism_dtype.index = ['유형']
            st.dataframe(tourism_dtype, width=300)

        with st.expander('데이터요약'):
            st.dataframe(pd.DataFrame(tourism_data.describe()).transpose(), width=300)

    elif submenu == "그래프":
        st.subheader('그래프')
        admission = st.selectbox('유형별_고객',('유료입장객', '무료입장객', '전체입장객'))
            
        if admission == '유료입장객':
            select_am = "Paid_admission"
        elif admission == '무료입장객':
            select_am = "Free_admission"
        else:
            select_am = "All_visitors"

        sns.set_theme(style="whitegrid")
        # Tabs
        산점도, 라인플롯, 바_플롯 = st.tabs(['산점도', '라인플롯', '바_플롯'])
        with 산점도:
            fig, ax = plt.subplots()
            sns.scatterplot(tourism_data
                , x="Month"
                , y=select_am
                , hue="year")
            st.pyplot(fig)

        with 라인플롯:        
            fig, ax = plt.subplots()
            sns.lineplot(tourism_data
                , x="Month"
                , y=select_am
                , hue="year")
            st.pyplot(fig)

        with 바_플롯:
            barPlot = sns.catplot(tourism_data
                , x="Month"
                , y=select_am
                , hue="year"
                , kind="bar")
            st.pyplot(barPlot)

    else:
        pass