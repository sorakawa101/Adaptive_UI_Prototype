import streamlit as st
import functions.func_common as fc
import functions.func_sidebar as fs


# * サイドバーコンテンツ
def sidebar():
    with st.sidebar:
        st.header("Navigation")
        # マルチセレクト（動画・画像・逐次・全体）
        navigation = fs.input_navigation()
        fs.set_value_to_the_session_state("navigation", navigation)

        st.header("Layout")
        # ラジオボタン（レイアウト）
        layout = fs.input_layout()
        fs.set_value_to_the_session_state("layout", layout)

        # スライダー（フォントサイズ）
        font_size = fs.input_font_size()
        fs.set_value_to_the_session_state("font_size", font_size)

        # カラーピッカー（色）
        color = fs.input_color()
        fs.set_value_to_the_session_state("color", color)

        st.header("Task-Feature Set")
        # トグル（情報量最大・最小）
        task_feature_set = fs.input_task_feature_set()
        fs.set_value_to_the_session_state("task_feature_set", task_feature_set)


def container():
    st.write(fs.get_value_from_the_session_state("navigation"))
    st.write(fs.get_value_from_the_session_state("layout"))
    st.write(fs.get_value_from_the_session_state("font_size"))
    st.write(fs.get_value_from_the_session_state("color"))
    st.write(fs.get_value_from_the_session_state("task_feature_set"))


# main関数
def main():
    fc.set_page_config()
    sidebar()
    container()


# 実行
if __name__ == "__main__":
    main()
