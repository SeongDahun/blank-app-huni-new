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