import streamlit as st

menu_data = [
    ("プレパレーション（基本ケア）", 15, 25),
    ("ウォーターケア", 20, 30),
    ("ドライケア", 15, 25),
    ("ハンドスパ", 20, 30),
    ("ワンカラー（2色まで）", 40, 60),
    ("ワンカラー（3色以上）", 50, 70),
    ("グラデーション（縦）", 50, 70),
    ("グラデーション（横）", 50, 70),
    ("ラメグラ", 40, 60),
    ("マグネットネイル（アートなし）", 45, 65),
    ("マグネットネイル（アート込み）", 55, 75),
    ("フレンチネイル（クリアベース）", 60, 90),
    ("変形フレンチ", 65, 95),
    ("ミラーネイル", 45, 65),
    ("ニュアンス（アート2本）", 60, 90),
    ("ニュアンス（アート4〜6本）", 75, 105),
    ("手描きアート（1本）", 15, 25),
    ("水彩アート・インクアート", 30, 45),
    ("パーツアート（3D）", 20, 30),
    ("フィルム／ホイルアート", 20, 30),
    ("ジェルスカルプ（1本）", 7, 10),
    ("フォームスカルプ（1本）", 10, 15),
    ("チップオーバーレイ", 60, 90),
    ("リペア（亀裂補強・1本）", 10, 15),
    ("当店付け替えオフ", 20, 30),
    ("他店オフ", 30, 45),
    ("ハードジェルオフ", 45, 60),
    ("ポリッシュオフ", 10, 15),
    ("ネイルチップ作成（オーダー）", 90, 120),
    ("カラー追加（1色ごと）", 5, 10),
    ("パーツ追加（個数ごと）", 3, 5),
    ("コーティング（艶あり・マット）", 5, 10),
    ("亀裂補修＋補強（セット）", 15, 20),
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
