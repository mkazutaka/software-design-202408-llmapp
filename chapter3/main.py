# main.py
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

st.title("翻訳アプリ")
source_languages = ["英語", "日本語", "丁寧な日本語", "2ちゃんまとめ風"]


def translate(source: str, target: str, input: str) -> str:
    model = ChatOpenAI(model="gpt-4o-2024-05-13")
    parser = StrOutputParser()
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "次の{source_language}を{target_language}に翻訳してください",
            ),
            ("user", "{user_input}"),
        ]
    )
    chain = prompt | model | parser
    return chain.invoke(
        {
            "source_language": source,
            "target_language": target,
            "user_input": input,
        }
    )


row1_left, row1_center, row1_right = st.columns((4, 0.5, 4))
row2_left, row2_right = st.columns(2)

with row1_left:
    source = st.selectbox(
        "ソース言語",
        source_languages,
        label_visibility="collapsed",
        key="source",
    )

with row1_right:
    target_languages = [l for l in source_languages if l != source]
    index = 0
    if "target" in st.session_state and st.session_state.target != source:
        index = target_languages.index(st.session_state.target)
    target = st.selectbox(
        "ターゲット言語",
        target_languages,
        label_visibility="collapsed",
        key="target",
        index=index,
    )


def swap_selectbox_value():
    st.session_state.target, st.session_state.source = (
        st.session_state.source,
        st.session_state.target,
    )
    if "output" in st.session_state and st.session_state.output != "":
        st.session_state.input = st.session_state.output


with row1_center:
    st.button(
        "⇔",
        type="secondary",
        use_container_width=True,
        on_click=swap_selectbox_value,
    )

with row2_left:
    input = st.text_area(
        "入力テキスト",
        label_visibility="collapsed",
        height=200,
        placeholder="翻訳したい文章を入力してください",
        key="input",
    )

with row2_right:
    if input != "":
        with st.spinner("翻訳中..."):
            output = translate(source, target, input)
            st.session_state.output = output
            st.write(output)
