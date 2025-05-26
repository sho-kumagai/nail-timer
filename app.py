import streamlit as st

menu_data = [
    ("ワンカラー", 40, 60),
    ("グラデーション", 50, 70),
    ("フレンチ", 60, 90),
    ("マグネット", 45, 65),
    ("ニュアンス", 75, 105),
]

st.title("ネイル施術時間シミュレーター")

if "selected" not in st.session_state:
    st.session_state.selected = []

cols = st.columns(3)
for idx, (name, _, _) in enumerate(menu_data):
    with cols[idx % 3]:
        checked = name in st.session_state.selected
        if st.checkbox(name, value=checked, key=name):
            if name not in st.session_state.selected:
                st.session_state.selected.append(name)
        else:
            if name in st.session_state.selected:
                st.session_state.selected.remove(name)

veteran_total = 0
target_total = 0

for name, vet, tgt in menu_data:
    if name in st.session_state.selected:
        veteran_total += vet
        target_total += tgt

if st.session_state.selected:
    st.write(f"🧑‍🏫 ベテランの合計時間：{veteran_total}分")
    st.write(f"👶 新人の目標時間：{target_total}分")
else:
    st.info("上からメニューを選んでください")
