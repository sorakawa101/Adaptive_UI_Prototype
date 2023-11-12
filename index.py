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
        st.radio(
            "What's your favorite layout",
            ["Single Column", "Multi Column", "Full Screen", "Grid"],
            captions=["Single Column", "Multi Column", "Full Screen", "Grid"],
        )  # st.radio(label, selected, captions)

        # スライダー（フォントサイズ）
        st.slider(
            "What's your favorite font size?", 0, 100, 5
        )  # st.slider(label, min, max, step)

        # カラーピッカー（色）
        st.color_picker(
            "Pick your favorite Color", "#00f900"
        )  # st.color_pecker(label, first-value)

        st.header("Task-Feature Set")
        # トグル（情報量最大・最小）
        st.toggle("More Suggested Amount")


def container():
    st.write(fs.get_value_from_the_session_state("navigation"))


# main関数
def main():
    fc.setPageConfig()
    sidebar()
    container()


# 実行
if __name__ == "__main__":
    main()
