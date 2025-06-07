import streamlit as st
import pandas as pd

st.set_page_config(page_title="ネイル材料価格表", layout="wide")
st.title("ネイル材料価格一覧")

@st.cache_data
def load_data():
    return pd.DataFrame([
        ["ジェル", "アート", "ブランドA", "商品A", "10g", 2000, 1800, "", 1, 10, "g", 200, 180, 0.5, 20, 100],
        ["ジェル", "アート", "ブランドB", "商品B", "30g", 6000, 5500, "人気商品", 3, 30, "g", 200, 183, 0.5, 60, 90],
        ["トップ", "仕上げ", "ブランドC", "商品C", "14g", 1500, 1400, "在庫限り", 2, 14, "g", 107, 100, 0.5, 28, 50]
    ], columns=["カテゴリ", "用途", "ブランド", "製品名", "容量", "通常価格", "TAT価格", "備考", "優先順位",
                "容量数値", "容量単位", "単価（通常）", "単価（TAT価格）", "目安使用量", "使用可能回数", "1回あたり材料費"])

df = load_data()
for col in ["通常価格", "TAT価格", "単価（通常）", "単価（TAT価格）", "使用可能回数", "1回あたり材料費"]:
    df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

if "selected" not in st.session_state:
    st.session_state.selected = []
if "checked_ids" not in st.session_state:
    st.session_state.checked_ids = set()

with st.sidebar:
    st.header("🔍 フィルター")
    keyword = st.text_input("キーワード")
    min_price = st.number_input("単価下限", 0, 10000, 0)
    max_price = st.number_input("単価上限", 0, 10000, 10000)
    min_uses = st.number_input("使用可能回数下限", 0, 10000, 0)
    if st.button("🧹 チェック全解除"):
        st.session_state.selected = []
        st.session_state.checked_ids = set()
    if st.session_state.selected:
        sdf = pd.DataFrame(st.session_state.selected)
        st.markdown("### 💰 合計")
        st.success(f"通常: ¥{int(sdf['通常価格'].sum()):,}／TAT: ¥{int(sdf['TAT価格'].sum()):,}／材料費平均: ¥{int(sdf['1回あたり材料費'].mean())}")

filtered = df.drop_duplicates(subset=["ブランド", "製品名"]).copy()
if keyword:
    keyword = keyword.lower()
    filtered = filtered[
        filtered["製品名"].str.lower().str.contains(keyword) |
        filtered["ブランド"].str.lower().str.contains(keyword) |
        filtered["用途"].str.lower().str.contains(keyword)
    ]
filtered = filtered[
    (filtered["単価（通常）"] >= min_price) &
    (filtered["単価（通常）"] <= max_price) &
    (filtered["使用可能回数"] >= min_uses)
]

st.markdown(f"### 📦 一致商品数: {len(filtered)} 件")

for idx, row in filtered.iterrows():
    cid = f"chk_{row['ブランド']}_{row['製品名']}_{idx}"
    label = f"{row['製品名']}（{row['容量']}・¥{int(row['単価（通常）'])}）"
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
                if not (r["ブランド"] == row["ブランド"] and r["製品名"] == row["製品名"])
            ]
    if row["備考"]:
        st.markdown(f"<span style='color:gray'>{row['備考']}</span>", unsafe_allow_html=True)
    st.markdown("---")
