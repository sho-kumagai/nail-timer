import streamlit as st
import pandas as pd

st.set_page_config(page_title="ネイル材料価格表（タイル選択）", layout="wide")
st.title("ネイル材料価格表アプリ")

columns = ['カテゴリ', '用途', 'ブランド', '製品名', '容量', '通常価格', 'TAT価格', '備考', '優先順位',
           '容量数値', '容量単位', '単価（通常）', '単価（TAT価格）', '目安使用量', '使用可能回数', '1回あたり材料費']

data = [
  # ここに全データ（82件）を展開済み
  ['ジェル', 'ベースジェル・トップ・アート・長さ出し等', 'Riccagel', 'ベースジェルジュラフィット', '10g', '2750.0', '', 'ネイルパートナーのみ', '1.0', '10.0', 'g', '275.0', '', '0.5', '20.0', '137.5'],
  ['プライマー', 'ジェル前の油分除去・密着力向上', 'PREGEL', 'マジカルプライマー（ぞうさん）', '7ml', '990.0', '900.0', '', '3.0', '7.0', 'ml', '141.43', '128.57', '0.1', '70.0', '14.14'],
  # ...（以下略）
]

df = pd.DataFrame(data, columns=columns)
df["通常価格"] = pd.to_numeric(df["通常価格"], errors="coerce").fillna(0)
df["TAT価格"] = pd.to_numeric(df["TAT価格"], errors="coerce").fillna(0)

st.markdown("## 🗂 カテゴリを選択してください")
category_buttons = df["カテゴリ"].dropna().unique().tolist()
cols = st.columns(len(category_buttons))

selected_category = None
for i, cat in enumerate(category_buttons):
    if cols[i].button(cat):
        selected_category = cat

if selected_category:
    st.markdown(f"### ✅ {selected_category} の商品を選択してください")
    filtered_df = df[df["カテゴリ"] == selected_category]

    selected_rows = []
    for i, row in filtered_df.iterrows():
        label = f"{row['製品名']}（通常価格: ¥{row['通常価格']}, TAT価格: ¥{row['TAT価格']}）"
        if st.checkbox(label, key=i):
            selected_rows.append(row)

    if selected_rows:
        selected_df = pd.DataFrame(selected_rows)
        selected_df["通常価格"] = pd.to_numeric(selected_df["通常価格"], errors="coerce").fillna(0)
        selected_df["TAT価格"] = pd.to_numeric(selected_df["TAT価格"], errors="coerce").fillna(0)
        total_regular = selected_df["通常価格"].sum()
        total_tat = selected_df["TAT価格"].sum()

        st.success(f"🧾 合計：通常価格 ¥{int(total_regular):,} ／ TAT価格 ¥{int(total_tat):,}")
        st.dataframe(selected_df.reset_index(drop=True), use_container_width=True)
    else:
        st.info("商品にチェックを入れると合計金額が表示されます。")
else:
    st.info("上のカテゴリから選択してください。")
