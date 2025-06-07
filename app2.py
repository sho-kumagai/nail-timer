import streamlit as st
import pandas as pd

st.set_page_config(page_title="ネイル材料価格表", layout="wide")
st.title("ネイル材料価格表（完全版）")

# 全データ（抜粋済みだが100行以上に展開可能な構造）
columns = [
    "カテゴリ", "用途", "ブランド", "製品名", "容量", "通常価格", "TAT価格", "備考", "優先順位",
    "容量数値", "容量単位", "単価（通常）", "単価（TAT価格）", "目安使用量", "使用可能回数", "1回あたり材料費"
]

data = [
    ["ジェル", "アート", "Riccagel", "ベースジェルジュラフィット", "10g", 2750, "", "ネイルパートナーのみ", 1, 10, "g", 275, "", 0.5, 20, 138],
    ["ジェル", "アート", "Riccagel", "ベースジェルジュラフィット", "30g", 7480, "", "ネイルパートナーのみ", 1, 30, "g", 249, "", 0.5, 60, 125],
    ["ジェル", "アート", "Riccagel", "RICCAマットコートジェル", "10g", 2750, "", "色鉛筆・マットトップ仕上げ用", 1, 10, "g", 275, "", 0.5, 20, 138],
    ["ジェル", "アート", "スネークベース", "フィルイン用ベースジェル", "15g", 4400, "", "楽天／黄色くなりやすい", 3, 15, "g", 293, "", 0.5, 30, 147],
    ["ジェル", "アート", "メルティジェル", "クリアジェル", "14g", 1540, 1400, "カラー作成用", 1, 14, "g", 110, 100, 0.5, 28, 55],
    ["ジェル", "アート", "ibd", "LEDクリアジェル", "56g", 8250, 7500, "ハードジェル", 2, 56, "g", 147, 134, 0.5, 112, 74]
]

df = pd.DataFrame(data, columns=columns)
if "selected" not in st.session_state:
    st.session_state.selected = []
if "checked_ids" not in st.session_state:
    st.session_state.checked_ids = set()

with st.sidebar:
    st.header("📊 合計金額")
    if st.session_state.selected:
        sdf = pd.DataFrame(st.session_state.selected)
        st.success(f"通常: ¥{int(sdf['通常価格'].sum()):,} ／ TAT: ¥{int(sdf['TAT価格'].replace('', 0).astype(float).sum()):,}")
    else:
        st.info("商品にチェックを入れると合計金額が表示されます")
    if st.button("🧹 全リセット"):
        st.session_state.selected = []
        st.session_state.checked_ids = set()

st.markdown("### ✅ 商品選択")

for idx, row in df.iterrows():
    cid = f"chk_{idx}"
    label = f"{row['製品名']}（{row['容量']} ／ 単価: ¥{row['単価（通常）']}）"
    if row["優先順位"] and int(row["優先順位"]) == 1:
        label = f"🟥 {label}"
    elif row["優先順位"] and int(row["優先順位"]) == 2:
        label = f"🟧 {label}"
    elif row["優先順位"] and int(row["優先順位"]) == 3:
        label = f"🟨 {label}"
    checked = cid in st.session_state.checked_ids
    if st.checkbox(label, key=cid, value=checked):
        if cid not in st.session_state.checked_ids:
            st.session_state.checked_ids.add(cid)
            st.session_state.selected.append(row)
    else:
        if cid in st.session_state.checked_ids:
            st.session_state.checked_ids.remove(cid)
            st.session_state.selected = [
                r for r in st.session_state.selected
                if not (r['製品名'] == row['製品名'] and r['容量'] == row['容量'])
            ]
    if row["備考"]:
        st.caption(f"　{row['備考']}")
