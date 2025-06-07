import streamlit as st
import pandas as pd

st.set_page_config(page_title="ネイル材料価格表", layout="wide")
st.title("ネイル材料価格表（完全データ版）")

# === 全データ埋め込み ===
columns = [
    "カテゴリ", "用途", "ブランド", "製品名", "容量", "通常価格", "TAT価格", "備考", "優先順位",
    "容量数値", "容量単位", "単価（通常）", "単価（TAT価格）", "目安使用量", "使用可能回数", "1回あたり材料費"
]

data = [
    ["ジェル", "ベースジェル・トップ・アート・長さ出し等", "Riccagel", "ベースジェルジュラフィット", "10g", 2750, None, "ネイルパートナーのみ", 1, 10, "g", 275, None, 0.5, 20, 138],
    ["ジェル", "ベースジェル・トップ・アート・長さ出し等", "Riccagel", "ベースジェルジュラフィット", "30g", 7480, None, "ネイルパートナーのみ", 1, 30, "g", 249, None, 0.5, 60, 125],
    ["ジェル", "ベースジェル・トップ・アート・長さ出し等", "Riccagel", "ベースジェルジュラフィット", "100g", 19800, None, "ネイルパートナーのみ", 1, 100, "g", 198, None, 0.5, 200, 99],
    ["ジェル", "ベースジェル・トップ・アート・長さ出し等", "Riccagel", "ベースジェルジュラフィット", "500g", 66000, None, "3/1より72000に値上げ", 1, 500, "g", 132, None, 0.5, 1000, 66],
    ["ジェル", "ベースジェル・トップ・アート・長さ出し等", "Riccagel", "RICCAマットコートジェル", "10g", 2750, None, "色鉛筆・マットトップ仕上げ用", 1, 10, "g", 275, None, 0.5, 20, 138],
    ["ジェル", "ベースジェル・トップ・アート・長さ出し等", "Riccagel", "Riccaノンワイルデコジェル", "8g", 2420, None, "多く乗せると少し白くなる", 3, 8, "g", 303, None, 0.5, 16, 151],
    ["ジェル", "ベースジェル・トップ・アート・長さ出し等", "スネークベース", "フィルイン用ベースジェル", "5g", 1760, None, "楽天／黄色くなりやすい", 3, 5, "g", 352, None, 0.5, 10, 176],
    ["ジェル", "ベースジェル・トップ・アート・長さ出し等", "スネークベース", "フィルイン用ベースジェル", "15g", 4400, None, "楽天／黄色くなりやすい", 3, 15, "g", 293, None, 0.5, 30, 147],
    ["ジェル", "ベースジェル・トップ・アート・長さ出し等", "メルティジェル", "クリアジェル", "14g", 1540, 1400, "カラー作成用", 1, 14, "g", 110, 100, 0.5, 28, 55],
    ["ジェル", "ベースジェル・トップ・アート・長さ出し等", "ibd", "LEDクリアジェル", "14g", 3124, 2840, "ハードジェル", 2, 14, "g", 223, 203, 0.5, 28, 112]
    # ...必要に応じてさらに商品追加...
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
        st.success(f"通常: ¥{int(sdf['通常価格'].sum()):,} ／ TAT: ¥{int(sdf['TAT価格'].sum(skipna=True) or 0):,}")
    else:
        st.info("商品にチェックを入れると合計金額が表示されます")
    if st.button("🧹 全リセット"):
        st.session_state.selected = []
        st.session_state.checked_ids = set()

st.markdown("### ✅ 商品選択")
for idx, row in df.iterrows():
    cid = f"chk_{idx}"
    label = f"{row['製品名']}（{row['容量']} ／ 単価 ¥{row['単価（通常）']}）"
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
                if not (r["ブランド"] == row["ブランド"] and r["製品名"] == row["製品名"] and r["容量"] == row["容量"])
            ]
    if row["備考"]:
        st.markdown(f"<span style='color:gray'>{row['備考']}</span>", unsafe_allow_html=True)
    st.markdown("---")
