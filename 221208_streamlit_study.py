# -*- coding: utf-8 -*-

import streamlit as st

def main() :
    """코드작성"""
    st.title("Hello World!")
    st.subheader("임시...")

    # text
    num = 1
    st.text(f'숫자는 {num}')

    # 마크다운
    st.markdown("## 마크다운 제목2")

    # 색상
    st.success("성공")
    st.warning("경고")
    st.info("정보")
    st.error("에러")
    st.exception("예외")

    # superfunction
    st.write("문자열")
    st.write(1+2)
    st.write(dir(int))

if __name__ == "__main__":
    main()

# streamlit run 파일명.py

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

def main() :
    """코드작성"""
    # 버튼 입력
    name = 'Held'

    if st.button("대문자"):
        st.write(f'이름 : {name.upper()}')
    if st.button("소문자"):
        st.write(f'이름 : {name.lower()}')
    
    # 활성화, 비활성화
    status = st.radio('Status', ("활성화", "비활성화"))
    if status == "활성화":
        st.success("활성화 상태")
    else:
        st.error("비활성화 상태")

    # 체크박스
    if st.checkbox("Show/Hide"):
        st.text("무언가를 보여줘요")
        
    with st.expander('python'):
        st.text("Hello Python")

def main() :
    """코드작성"""
    # Select / Slider

    # 프로그래밍 언어
    proLan = ["파이썬", "자바", "R", "SQL"]
    choice = st.selectbox("휴먼 프로그래밍 언어", proLan) 
    st.write(f"{choice} 언어를 선택함")

    mulChoice = st.multiselect("언어 선택", proLan, default="SQL")
    st.write("선택:", mulChoice)

    # 슬라이더
    age = st.slider("나이", 1, 120)
    st.write(age)

    # Select Slider
    color = st.select_slider("색상 선택",
                            options=["노란색","빨간색","파란색","흰색"]
                            , value=("노란색","흰색"))
    st.write(color)

    start_color, end_color = st.select_slider("색상 선택",
                        options=["노란색","빨간색","파란색","흰색", "검정색"]
                        , value=("노란색","흰색"))
    st.write(start_color, end_color)

# 이미지 라이브러리
from PIL import Image

def main() :
    """코드작성"""
    # 이미지 추가
    img = Image.open("data/image_03.jpg")
    st.image(img)

    # URL 이미지 삽입
    st.image("https://res.cloudinary.com/dyd911kmh/image/upload/v1640050215/image27_frqkzv.png")

    # 비디오 출력
    with open("data/secret_of_success.mp4","rb") as rb :
        video_file = rb.read()
        st.video(video_file, start_time=1)

    # 오디오 출력
    with open("data/song.mp3","rb") as rb :
        audio_file = rb.read()
        st.video(audio_file, format="audio/mp3")

def main() :
    """코드작성"""
    # 텍스트 Input
    fname = st.text_input("이름 입력")
    # st.title(fname)
    st.write(fname)

    # 텍스트 영역
    message = st.text_area("입력해주세요!", height=100)
    st.write(message)

    # 숫자 입력
    number = st.number_input("숫자 입력")
    st.write(number)

    # 날짜
    myDate = st.date_input("날짜")
    st.write(myDate)

    # 시간
    myTime = st.time_input("시간")
    st.write(myTime)

    # Color Picker
    color = st.color_picker("색상 선택")
    st.write(color)