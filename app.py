import streamlit as st

st.set_page_config(page_title="서울 도시 경관 디자인 도우미")

st.title("🎨 도시 경관 디자인 도우미")
st.write("파일을 업로드하고 원하는 스타일을 선택하세요. 업로드된 자료는 자동 분석되어 적절한 경관 제안을 제공합니다.")

# 1. 파일 업로드
uploaded_file = st.file_uploader("📤 경관 자료 업로드 (PDF, 이미지 등)", type=["pdf", "png", "jpg", "jpeg"])

# 2. 스타일 선택
style_option = st.selectbox(
    "디자인 스타일을 선택하거나 직접 입력하세요:",
    ["모던한", "차분한", "화려한", "전통적인", "미니멀", "직접 입력"]
)

custom_style = ""
if style_option == "직접 입력":
    custom_style = st.text_area("원하는 스타일을 자유롭게 입력하세요:", placeholder="예: 자연친화적이고 따뜻한 분위기의 거리...")

# 3. 출력
if uploaded_file:
    st.success(f"✅ 파일 '{uploaded_file.na_
