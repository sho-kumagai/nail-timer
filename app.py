import streamlit as st

# メニュー項目（名前, 時間, メモ）
menu_items = [
    ("ファイリング", 10, "10分以内を目標に。まずは1本1分で整える練習から。"),
    ("甘皮処理", 10, "押し上げ＋ニッパーで片手5分を目安。丁寧さ優先。"),
    ("サンディング", 10, "片手2分半ずつ。全体をまんべんなく削れるか意識。"),
    ("ベース塗布＋硬化", 15, "厚みを均一に塗って10分以内。はみ出し確認も忘れずに。"),
    ("カラー2度塗＋硬化", 20, "1度塗り10分＋2度目10分が理想。ムラをなくす練習を。"),
    ("フレンチ／グラデ", 20, "通常カラーに追加10分。ライン取りに集中して練習。"),
    ("軽めアート2本", 15, "ストーンや簡単なラメなら片手7〜8分。左右差に注意。"),
    ("複雑アート", 30, "手描き・埋め込みなどは30分以上もOK。正確さ重視で。"),
    ("ストーン配置", 10, "バランス・配置ミス防止を意識して丁寧に。"),
    ("トップ塗布＋硬化", 20, "凹凸を覆う意識で塗って10分以内。流れやすいので注意。"),
    ("拭き取り仕上げ", 3, "未硬化ジェルの拭き残しがないか丁寧に。"),
    ("オイル＋マッサージ", 3, "1本10秒×10本で2分＋全体仕上げ3分が目安。"),
    ("オフ（自店）", 15, "フィルインなので１本1分目安、待ち時間不要なのでパーツオフ込みで。"),
    ("オフ（他店）", 40, "厚みのあるジェルや強いベースには余裕を持って対応。")
]

# タイトル（メニューと同じサイズに調整）
st.markdown("##### ネイル施術 練習用タイム目安リスト")

# 合計用変数
total_time = 0

# 2列に分けてチェックボックスを表示
cols = st.columns(2)
checked_states = {}

for idx, (menu, minutes, note) in enumerate(menu_items):
    with cols[idx % 2]:
        key = f"menu_{idx}"
        # チェックボックス表示
        checked = st.checkbox(f"{menu}（目標：{minutes}分）", key=key)
        checked_states[key] = checked
        # 合計に加算
        if checked:
            total_time += minutes
        st.caption(note)

# 合計表示
st.markdown("---")
st.markdown(f"**合計目標時間：{total_time}分**")

# リセット処理（session_state の該当キーを False に）
if st.button("リセット"):
    for idx in range(len(menu_items)):
        key = f"menu_{idx}"
        if key in st.session_state:
            st.session_state[key] = False
    st.experimental_rerun()
