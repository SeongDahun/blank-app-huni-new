import streamlit as st

st.title("🎈Huni's new streamlit app")
st.write(
    "가보자구~ For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)


# st.markdown(): 마크다운 문법 지원 (굵게, 기울임, 목록 등)
st.markdown("**굵은 텍스트**, *기울임 텍스트*")
st.markdown("""- 첫 번째 항목
- 두 번째 항목
- 여러 줄을 쓸 때""")


# 정보성 메시지 박스
st.info("ℹ️ 정보 메시지입니다.")
st.warning("⚠️ 경고 메시지입니다.")
st.success("✅ 성공 메시지입니다.")
st.error("❌ 오류 메시지입니다.")


# 이미지 출력
st.image("https://i.namu.wiki/i/kHCs0iQbAYxBlqeY4eKZxns1X7k4dZH7Qd8Zh_e52n86a9oj5R0Zh0sYhQ5BGrC4069d4AVIW7y7-nOh8w8rGlgAr72XXUS1JT8R6GT8L65oVGgMtSwxVm6s6qGitIYCOjCUawXnFRi0ZS_J7QYNfNvSh0OD2bJ9LEiQUI7-ffA.webp", caption="귀여운 고양이", use_container_width=True)
st.image("https://via.placeholder.com/300", caption="예시 이미지")

# 영상 출력
st.video("https://www.youtube.com/watch?v=4nU-Fp96p8E")
st.video("https://www.youtube.com/watch?v=B1J6Ou4q8vE")

# 오디오 출력
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

# 지도 출력
import pandas as pd
df = pd.DataFrame({"lat": [37.5], "lon": [127.0]})
st.map(df, zoom=12)

# 데이터프레임 테이블 출력
st.dataframe(pd.DataFrame({
    "이름": ["홍길동", "김철수"],
    "점수": [85, 92]
}))

# st.expander("제목"): 내용을 접었다 펼 수 있는 컨테이너입니다
with st.expander("ℹ️ 자세한 설명 보기"):
    st.write("여기에 상세 설명이나 보조 정보를 넣을 수 있습니다.")



# st.tabs(["이름1", "이름2", ...]): 탭 인터페이스 생성
tab1, tab2 = st.tabs(["탭 1", "탭 2"])  # 2개의 탭 생성

with tab1:
    st.write("탭 1에 해당하는 내용입니다.")  # 첫 번째 탭에 표시할 내용
with tab2:
    st.write("탭 2에 해당하는 내용입니다.")  # 두 번째 탭에 표시할 내용


# st.sidebar: 사이드바 영역에 콘텐츠를 배치합니다
st.sidebar.title("📌 사이드바 메뉴")
option = st.sidebar.selectbox("옵션을 선택하세요", ["A", "B", "C"])
st.write("선택한 옵션:", option)


# 버튼 클릭 여부에 따라 실행
if st.button("클릭하세요"):
    st.write("버튼이 클릭되었습니다!")



import pandas as pd

st.title("1️⃣ ✅ 공개 Google Sheet 읽기")
st.info("📘 누구나 볼 수 있도록 공개된 시트를 Pandas로 직접 불러오는 가장 간단한 방법입니다.\n📎 링크는 반드시 `export?format=csv` 형태로 설정하세요.")



csv_url1 = public_url
df1 = pd.read_csv(csv_url1)
st.dataframe(df1)

# 막대 그래프로 df1["choice"] 표시
st.bar_chart(df1['choice'].value_counts())