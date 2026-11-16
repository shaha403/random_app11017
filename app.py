import streamlit as st
import random

# 페이지 기본 설정
st.set_page_config(page_title="점심 메뉴 추천기", page_icon="🍱")

# 제목 및 설명
st.title("오늘의 점심 메뉴 추천기 🍚")
st.write("메뉴 고르기 힘드신가요? 아래 버튼을 눌러 오늘의 점심을 결정해 보세요!")

# 추천할 메뉴 리스트
menus = [
    "김치찌개", "된장찌개", "제육볶음", "순대국", "비빔밥",
    "돈까스", "초밥", "우동", "라멘", "돈부리",
    "짜장면", "짬뽕", "마라탕", "볶음밥", "탕수육",
    "파스타", "피자", "햄버거", "샌드위치", "샐러드"
]

# 버튼을 눌렀을 때 실행되는 동작
if st.button("오늘의 점심 추천받기 🎲", type="primary"):
    selected_menu = random.choice(menus)
    st.balloons()  # 축하 풍선 효과
    st.success(f"오늘의 추천 메뉴는 **{selected_menu}** 입니다! 😋")
