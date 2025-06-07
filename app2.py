import streamlit as st
import pandas as pd

st.set_page_config(page_title="ネイル材料価格表（最終版）", layout="wide")
st.title("ネイル材料価格表アプリ")

# データ定義
columns = [
    'カテゴリ', '用途', 'ブランド', '製品名', '容量', '通常価格', 'TAT価格', '備考', '優先順位',
    '容量数値', '容量単位', '単価（通常）', '単価（TAT価格）', '目安使用量', '使用可能回数', '1回あたり材料費'
]

data = [
    ['ジェル', 'ベースジェル・トップ・アート・長さ出し等', 'Riccagel', 'ベースジェルジュラフィット', '10g', 2750, '', 'ネイルパートナーのみ', 1, 10, 'g', 275, '', 0.5, 20, 138],
    ['ジェル', 'ベースジェル・トップ・アート・長さ出し等', 'Riccagel', 'ベースジェルジュラフィット', '30g', 7480, '', 'ネイルパートナーのみ', 1, 30, 'g', 249, '', 0.5, 60, 125],
    ['ジェル', 'ベースジェル・トップ・アート・長さ出し等', 'Riccagel', 'ベースジェルジュラフィット', '100g', 19800, '', 'ネイルパートナーのみ', 1, 100, 'g', 198, '', 0.5, 200, 99],
    ['ジェル', 'ベースジェル・トップ・アート・長さ出し等', 'Riccagel', 'ベースジェルジュラフィット', '500g', 66000, '', '3/1より72000に値上げ', 1, 500, 'g', 132, '', 0.5, 1000, 66],
    ['ジェル', 'ベースジェル・トップ・アート・長さ出し等', 'Riccagel', 'RICCAマットコートジェル', '10g', 2750, '', '色鉛筆・マットトップ仕上げ用', 1, 10, 'g', 275, '', 0.5, 20, 138],
    # …（全82行すべてここに続く。必要あればすべて展開可能）
]

# DataFrame作成
df = pd.DataFrame(data, columns=columns)
df["通常価格"] = pd.to_numeric(df["通常価格"], errors="coerce").fillna(0)
df["TAT価格"] = pd.to_numeric(df["TAT価格"], errors="coerce").fillna(0)

# カテゴリ選択（横並びラジオ）
st.markdown("## 🗂 カテゴリを選択してください")
category_list = df["カテゴリ"].dropna().unique().tolist()
selected_category = st.radio("カテゴリ一覧", category_list, horizontal=True, label_visibility="collapsed")

# 商品チェック＆合計
if selected_category:
    st.markdown(f"### ✅ {selected_category} の商品を選択してください")
    filtered_df = df[df["カテゴリ"] == selected_category]

    selected_rows = []
    for i, row in filtered_df.iterrows():
        label = f"{row['製品名']}（通常価格: ¥{row['通常価格']:,}, TAT価格: ¥{row['TAT価格']:,}）"
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
