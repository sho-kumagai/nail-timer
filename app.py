import streamlit as st

menu_items = [
    ("ファイリング", 5, 10, "10分以内を目標に。まずは1本1分で整える練習から。"),
    ("甘皮処理", 5, 10, "押し上げ＋ニッパーで片手5分を目安。丁寧さ優先。"),
    ("サンディング", 5, 10, "片手2分半ずつ。全体をまんべんなく削れるか意識。"),
    ("ベース塗布＋硬化", 10, 15, "厚みを均一に塗って10分以内。はみ出し確認も忘れずに。"),
    ("カラー2度塗＋硬化", 10, 20, "1度塗り10分＋2度目10分が理想。ムラをなくす練習を。"),
    ("フレンチ／グラデ", 15, 20, "通常カラーに追加10分。ライン取りに集中して練習。"),
    ("軽めアート2本", 15, 15, "ストーンや簡単なラメなら片手7〜8分。左右差に注意。"),
    ("複雑アート", 30, 40, "手描き・埋め込みなどは30分以上もOK。正確さ重視で。"),
    ("ストーン配置", 5, 10, "バランス・配置ミス防止を意識して丁寧に。"),
    ("トップ塗布＋硬化", 10, 20, "凹凸を覆う意識で塗って10分以内。流れやすいので注意。"),
    ("拭き取り仕上げ", 3, 3, "未硬化ジェルの拭き残しがないか丁寧に。"),
    ("オイル＋マッサージ", 1, 3, "1本10秒×10本で2分＋全体仕上げ3分が目安。"),
    ("オフ（自店）", 10, 15, "フィルインなので１本1分目安、待ち時間不要なのでパーツオフとかも込みで目標。"),
    ("オフ（他店）", 40, 40, "厚みのあるジェルや強いベースには余裕を持って対応。")
]

st.title("ネイル施術 練習用タイム目安リスト")

if "selected" not in st.session_state:
    st.session_state.selected = []

col1, col2 = st.columns(2)

for idx, (name, min_time, max_time, note) in enumerate(menu_items):
    col = col1 if idx % 2 == 0 else col2
    with col:
        checked = st.checkbox(name, key=name, value=name in st.session_state.selected)
        if checked and name not in st.session_state.selected:
            st.session_state.selected.append(name)
        elif not checked and name in st.session_state.selected:
            st.session_state.selected.remove(name)
        st.caption(note)

if st.button("選択をリセット"):
    st.session_state.selected = []

st.markdown("---")

selected_items = [item for item in menu_items if item[0] in st.session_state.selected]
if selected_items:
    st.subheader("🧮 合計時間")
    min_total = sum(item[1] for item in selected_items)
    max_total = sum(item[2] for item in selected_items)
    st.markdown(f"**{min_total}〜{max_total}分**")

    st.markdown("### 選択されたメニュー：")
    for name, min_time, max_time, _ in selected_items:
        st.markdown(f"{name.ljust(20)} {'（新）'+str(max_time)+'分'.rjust(6)} {'（べ）'+str(min_time)+'分'.rjust(6)}")
