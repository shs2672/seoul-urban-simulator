import streamlit as st

# 페이지 설정
st.set_page_config(page_title="서울 도시 시뮬레이터")

st.title("🏙️ 서울 도시 시뮬레이터")
st.write("안녕하세요! 서울의 도시 경관을 시각화하고 제안하는 프로젝트입니다.")

# 파일 업로드
uploaded_file = st.file_uploader("📤 경관 관련 자료를 업로드하세요 (예: 사진, PDF 등)", type=["png", "jpg", "jpeg", "pdf"])

if uploaded_file is not None:
    st.success(f"✅ 파일 '{uploaded_file.name}' 이 업로드되었습니다.")

    # 디자인 스타일 선택
    style = st.selectbox(
        "🎨 원하는 경관 스타일을 선택하세요:",
        ["모던한", "차분한", "화려한", "전통적인", "미니멀", "직접 입력"]
    )

    if style == "직접 입력":
        custom_style = st.text_input("원하는 스타일을 직접 입력하세요:")
    else:
        custom_style = style

    # 제출 버튼
    if st.button("변경안 생성하기"):
        st.write(f"선택한 스타일: **{custom_style}**")
        st.image("before_example.jpg", caption="변경 전 이미지", use_column_width=True)
        st.image("after_example.jpg", caption="변경 후 이미지 (AI 시뮬레이션 예시)", use_column_width=True)
        st.markdown("💡 이 변경안은 업로드한 자료와 선택한 스타일을 바탕으로 생성된 예시입니다. 자료를 기반으로 더 정교하게 조정할 수 있습니다.")
