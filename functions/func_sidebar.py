import streamlit as st


# keyを指定して，対応するsession_stateに入力値を格納する関数
def set_value_to_the_session_state(key, value):
    if key not in st.session_state:
        st.session_state[key] = None

    if value:
        st.session_state[key] = value


# keyを指定して，対応するsession_stateから入力値を取得する関数
def get_value_from_the_session_state(key):
    return st.session_state[key]


# navigationの入力欄を設置し，入力値を返す関数
def input_media():
    media = st.multiselect(
        "What's your favorite media?",
        ["Movie", "Image", "Graph", "Text"],
        ["Movie", "Image", "Graph", "Text"],
    )  # st.multiselect(label, selected, first-value)

    return media


# layoutの入力欄を設置し，入力値を返す関数
def input_navigation():
    navigation = st.radio(
        "What's your favorite navigation",
        ["Single Column", "Multi Column", "Full Screen", "Grid"],
        captions=["Single Column", "Multi Column", "Full Screen", "Grid"],
    )  # st.radio(label, selected, captions)

    return navigation


# font sizeの入力欄を設置し，入力値を返す関数
def input_font_size():
    font_size = st.slider(
        "What's your favorite font size?", 0, 100, 5
    )  # st.slider(label, min, max, step)

    return font_size


# colorの入力欄を設置し，入力値を返す関数
def input_color():
    color = st.color_picker(
        "Pick your favorite Color", "#00f900"
    )  # st.color_pecker(label, first-value)

    return color


# task_feature_setの入力欄を設置し，入力値を返す関数
def input_task_feature_set():
    task_feature_set = st.toggle("More Suggested Amount")
    return task_feature_set
