import streamlit as st

# 1. 문제와 정답 데이터
ask = ["과__", "동학 __ 운동", "9주 5__", "돈오__", "정혜__", "이_신"]
re = ["전법", "농민", "소경", "점수", "쌍수", "순"]

# 2. 세션 상태(session_state) 초기화
# 페이지가 다시 로드되어도 현재 문제 번호(index), 점수(score), 피드백 메시지를 유지합니다.
if 'index' not in st.session_state:
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.feedback = None
    st.session_state.feedback_type = None

st.title("역사 용어 빈칸 채우기 퀴즈 📝")
st.write("---")

# 3. 퀴즈 진행 로직
if st.session_state.index < len(ask):
    current_idx = st.session_state.index
    current_ask = ask[current_idx]
    current_ans = re[current_idx]

    # 이전 문제에 대한 피드백(정답/오답) 출력
    if st.session_state.feedback:
        if st.session_state.feedback_type == "success":
            st.success(st.session_state.feedback)
        else:
            st.error(st.session_state.feedback)

    st.subheader(f"문제 {current_idx + 1} / {len(ask)}")
    st.write(f"다음 **'{current_ask}'** 중 밑줄에 들어갈 말로 알맞은 것은?")

    # 입력 폼 생성 (엔터키나 제출 버튼을 누르면 작동)
    with st.form(key=f"quiz_form_{current_idx}"):
        user_input = st.text_input("정답을 입력하세요:")
        submit_button = st.form_submit_button(label="제출")

        if submit_button:
            # 정답 확인 로직
            if user_input == current_ans:
                st.session_state.score += 1
                st.session_state.feedback = f"'{user_input}' - 정답입니다! 🎉"
                st.session_state.feedback_type = "success"
            else:
                st.session_state.feedback = f"오답입니다. 밑줄에 들어갈 정답은 **'{current_ans}'**입니다."
                st.session_state.feedback_type = "error"
            
            # 다음 문제로 넘어가기 위해 인덱스 증가 후 화면 새로고침
            st.session_state.index += 1
            st.rerun()

# 4. 퀴즈 종료 및 최종 결과 출력
else:
    st.header("퀴즈 종료! 🏁")
    
    # 마지막 문제에 대한 피드백 출력
    if st.session_state.feedback:
        if st.session_state.feedback_type == "success":
            st.success(st.session_state.feedback)
        else:
            st.error(st.session_state.feedback)

    st.write("---")
    # 최종 점수 출력 (st.info 또는 st.metric 활용)
    st.info(f"최종 점수는 **{st.session_state.score}개** 맞았습니다. (총 {len(ask)}문제)")
    
    # 다시 풀기 버튼
    if st.button("처음부터 다시 풀기 🔄"):
        st.session_state.index = 0
        st.session_state.score = 0
        st.session_state.feedback = None
        st.session_state.feedback_type = None
        st.rerun()
