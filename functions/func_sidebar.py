import streamlit as st


# keyを指定して，対応するsession_stateに入力値を格納する関数
def set_value_to_the_session_state(key, value):
    if key not in st.session_state:
        st.session_state[key] = []

    if value:
        st.session_state[key] = value


# keyを指定して，対応するsession_stateから入力値を取得する関数
def get_value_from_the_session_state(key):
    return st.session_state[key]


# navigationの入力欄を設置し，入力値を返す関数
def input_navigation():
    navigation = st.multiselect(
        "What's your favorite navigation?",
        ["Movie", "Image", "Sequentially", "Whole"],
        ["Movie", "Image", "Sequentially", "Whole"],
    )  # st.multiselect(label, selected, first-value)

    return navigation
