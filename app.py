import streamlit as st

menu_items = [
    ("ファイリング", 5, 10, "10分以内を目標に。まずは1本1分で整える練習から。"),
    ("甘皮処理", 5, 10, "押し上げ＋ニッパーで片手5分を目安。丁寧さ優先。"),
    ("サンディング", 5, 10, "片手2分半ずつ。全体をまんべんなく削れるか意識。"),
    ("ベース塗布＋硬化", 10, 15, "厚みを均一に塗って10分以内。はみ出し確認も忘れずに。"),
    ("カラー2度塗＋硬化", 10, 20, "1度塗り10分＋2度目10分が理想。ムラをなくす練習を。"),
    ("フレンチ／グラデ", 15, 20, "通常カラーに追加10分。ライン取りに集中して練習。"),
    ("軽めアート2本", 15, 15, "ストーンや簡単なラメなら片手7〜8分。左右差に注意。"),
    ("複雑アート", 30, 45, "手描き・埋め込みなどは30分以上もOK。正確さ重視で。"),
    ("ストーン配置", 5, 10, "バランス・配置ミス防止を意識して丁寧に。"),
    ("トップ塗布＋硬化", 10, 20, "凹凸を覆う意識で塗って10分以内。流れやすいので注意。"),
    ("拭き取り仕上げ", 3, 3, "未硬化ジェルの拭き残しがないか丁寧に。"),
    ("オイル＋マッサージ", 1, 3, "1本10秒×10本で2分＋全体仕上げ3分が目安。"),
    ("オフ（自店）", 10, 15, "フィルインなので1本1分目安。パーツ込み。全体では30〜35分。"),
    ("オフ（他店）", 40, 45, "厚みのあるジェルや強いベースには余裕を持って対応。")
]

if "selected_items" not in st.session_state:
    st.session_state.selected_items = []

st.title("ネイル施術 練習用タイム目安リスト（新人向け）")

cols = st.columns(2)
for idx, (name, min_time, max_time, comment) in enumerate(menu_items):
    with cols[idx % 2]:
        checked = st.checkbox(name, key=name)
        if checked and name not in st.session_state.selected_items:
            st.session_state.selected_items.append(name)
        elif not checked and name in st.session_state.selected_items:
            st.session_state.selected_items.remove(name)

v_total = sum(min_time for name, min_time, _, _ in menu_items if name in st.session_state.selected_items)
t_total = sum(max_time for name, _, max_time, _ in menu_items if name in st.session_state.selected_items)

st.markdown("---")
st.subheader("🧮 合計時間")
st.markdown(f"ベテラン：**{v_total}分**　／　新人：**{t_total}分**")

if st.session_state.selected_items:
    st.markdown("### 📝 選択されたメニューと時間")
    for name, v, t, _ in menu_items:
        if name in st.session_state.selected_items:
            st.markdown(f"{name:<30}（べ）{v:>2}分　（新）{t:>2}分")
