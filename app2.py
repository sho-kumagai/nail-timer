import streamlit as st
import pandas as pd

# アプリのタイトル
st.title("ネイル材料価格表アプリ")

# サンプルデータ（本当はもっと行を増やせます）
data = [
    ["ジェル", "ベース", "Riccagel", "ベースジェルジュラフィット", "10g", 2750, "¥275/g", "0.5g", 20, "¥138"],
    ["ジェル", "カラー", "メルティジェル", "クリアジェル", "200g", 15400, "¥77/g", "0.5g", 400, "¥39"],
    ["プライマー", "前処理", "PREGEL", "マジカルプライマー", "7ml", 990, "¥141/ml", "0.1ml", 70, "¥14"],
    ["アクリル", "リキッド", "フルーリア", "アクリルリキッド", "480ml", 8250, "¥17/ml", "0.5ml", 960, "¥9"]
]

# 列の名前
columns = [
    "カテゴリ", "用途", "ブランド", "製品名", "容量",
    "価格", "単価", "使用量", "回数", "1回材料費"
]

# 表に変換
df = pd.DataFrame(data, columns=columns)

# 検索ボックス
keyword = st.text_input("キーワードで検索（例：Riccagel, ベース, 100以下 など）")

# フィルター処理（ざっくり検索）
if keyword:
    df = df[df.astype(str).apply(lambda row: keyword.lower() in row.str.lower().to_string(), axis=1)]

# 表示
st.dataframe(df, use_container_width=True)
