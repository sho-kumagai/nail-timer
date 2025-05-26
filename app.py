import streamlit as st

menu_categories = {
    "ケア": [
        ("プレパレーション（基本ケア）", 15, 25),
        ("ウォーターケア", 20, 30),
        ("ドライケア", 15, 25),
        ("ハンドスパ", 20, 30),
    ],
    "デザイン": [
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
    ],
    "スカルプ・補強": [
        ("ジェルスカルプ（1本）", 7, 10),
        ("フォームスカルプ（1本）", 10, 15),
        ("チップオーバーレイ", 60, 90),
        ("リペア（亀裂補強・1本）", 10, 15),
        ("亀裂補修＋補強（セット）", 15, 20),
    ],
    "オフ": [
        ("当店付け替えオフ", 20, 30),
        ("他店オフ", 30, 45),
        ("ハードジェルオフ", 45, 60),
        ("ポリッシュオフ", 10, 15),
    ],
    "その他オプション": [
        ("ネイルチップ作成（オーダー）", 90, 120),
        ("カラー追加（1色ごと）", 5, 10),
        ("パーツ追加（個数ごと）", 3, 5),
        ("コーティング（艶あり・マット）", 5, 10),
    ]
}

exclusive_groups = [
    {"ワンカラー（2色まで）", "ワンカラー（3色以上）", "グラデーション（縦）", "グラデーション（横）", "ラメグラ", "マグネットネイル（アートなし）", "マグネットネイル（アート込み）"},
    {"フレンチネイル（クリアベース）", "変形フレンチ"},
    {"当店付け替えオフ", "他店オフ", "ハードジェルオフ", "ポリッシュオフ"}
]

veteran_total = 0
target_total = 0

if "selected" not in st.session_state:
    st.session_state.selected = []

# 合計時間エリアをリアルタイム更新用にプレースホルダー化
header_placeholder = st.empty()

st.title("ネイル施術時間シミュレーター")

for category, items in menu_categories.items():
    with st.expander(f"【{category}】", expanded=True):
        cols = st.columns(3)
        for idx, (name, vet, tgt) in enumerate(items):
            with cols[idx % 3]:
                is_checked = name in st.session_state.selected
                disabled = any(
                    name in group and any(
                        other in st.session_state.selected and other != name
                        for other in group
                    ) for group in exclusive_groups
                )
                checked = st.checkbox(name, value=is_checked, key=name, disabled=disabled)
                if checked and name not in st.session_state.selected:
                    st.session_state.selected.append(name)
                elif not checked and name in st.session_state.selected:
                    st.session_state.selected.remove(name)

# 合計時間を再計算（メニュー描画のあと）
veteran_total = sum(vet for cat in menu_categories.values() for name, vet, _ in cat if name in st.session_state.selected)
target_total = sum(tgt for cat in menu_categories.values() for name, _, tgt in cat if name in st.session_state.selected)

# 上部にリアルタイムで固定表示
header_placeholder.markdown(f"ベテラン：{veteran_total}分 ／ 新人：{target_total}分", unsafe_allow_html=True)
