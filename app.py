import streamlit as st

menu_data = [
    ("ワンカラー", 40, 60),
    ("グラデーション", 50, 70),
    ("フレンチ", 60, 90),
    ("マグネット", 45, 65),
    ("ニュアンス", 75, 105),
]

st.title("ネイル施術時間シミュレーター")

selected = st.multiselect("メニューを選んでください", [m[0] for m in menu_data])

veteran_total = 0
target_total = 0

for name, vet, tgt in menu_data:
    if name in selected:
        veteran_total += vet
        target_total += tgt

if selected:
    st.write(f"🧑‍🏫 ベテランの合計時間：{veteran_total}分")
    st.write(f"👶 新人の目標時間：{target_total}分")
else:
    st.info("上からメニューを選んでください")
