# 合計時間を再計算（メニュー描画のあと）
veteran_total = sum(vet for cat in menu_categories.values() for name, vet, _ in cat if name in st.session_state.selected)
target_total = sum(tgt for cat in menu_categories.values() for name, _, tgt in cat if name in st.session_state.selected)

# リアルタイムで上部に固定表示
header_placeholder.markdown(
    f\"\"\"
    <div style='position:fixed; top:0; left:0; right:0; background-color:#f0f0f0; padding:6px 10px; z-index:1000; border-bottom:1px solid #ccc; font-size:13px;'>
        <strong>合計時間 ▶︎ ベテラン：{veteran_total}分 ／ 新人：{target_total}分</strong>
    </div>
    <br><br><br>
    \"\"\",\n    unsafe_allow_html=True\n)
