import streamlit as st
import functions.func_common as fc


# * サイドバーコンテンツ
def sidebar():
    with st.sidebar:
        st.subheader("Navigation")
        # マルチセレクト（動画・画像・逐次・全体）
        st.subheader("Layout")
        # ラジオボタン（レイアウト）
        # スライダー（フォントサイズ）
        # カラーピッカー（色）
        st.subheader("Task-Feature Set")
        # トグル（情報量最大・最小）


# main関数
def main():
    fc.setPageConfig()
    sidebar()


# 実行
if __name__ == "__main__":
    main()
