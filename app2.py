<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <title>ネイル材料価格検索アプリ</title>
  <style>
    body {
      font-family: sans-serif;
      padding: 20px;
      background: #f9f9f9;
    }
    h1 {
      text-align: center;
      margin-bottom: 20px;
    }
    input[type="text"] {
      width: 100%;
      padding: 10px;
      font-size: 16px;
      margin-bottom: 20px;
      border-radius: 8px;
      border: 1px solid #ccc;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      background: white;
    }
    th, td {
      border: 1px solid #ddd;
      padding: 8px;
      font-size: 14px;
      text-align: left;
    }
    th {
      background-color: #f0f0f0;
    }
    tr:nth-child(even) {
      background-color: #f9f9f9;
    }
    tr:hover {
      background-color: #eef;
    }
  </style>
</head>
<body>
  <h1>ネイル材料価格検索</h1>
  <input type="text" id="searchBox" placeholder="キーワードで絞り込み（例：Riccagel、トップ、¥100 など）">

  <table id="materialsTable">
    <thead>
      <tr>
        <th>カテゴリ</th>
        <th>用途</th>
        <th>ブランド</th>
        <th>製品名</th>
        <th>容量</th>
        <th>価格</th>
        <th>単価</th>
        <th>使用量</th>
        <th>回数</th>
        <th>1回材料費</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>ジェル</td>
        <td>ベースジェル</td>
        <td>Riccagel</td>
        <td>ベースジェルジュラフィット</td>
        <td>10g</td>
        <td>¥2,750</td>
        <td>¥275</td>
        <td>0.5g</td>
        <td>20</td>
        <td>¥138</td>
      </tr>
      <tr>
        <td>トップコート</td>
        <td>ミラーネイル</td>
        <td>PREGEL</td>
        <td>ノンワイプクリアキャンジェル</td>
        <td>14g</td>
        <td>¥2,178</td>
        <td>¥156</td>
        <td>0.5g</td>
        <td>28</td>
        <td>¥78</td>
      </tr>
    </tbody>
  </table>

  <script>
    document.getElementById('searchBox').addEventListener('input', function () {
      const keyword = this.value.toLowerCase();
      const rows = document.querySelectorAll('#materialsTable tbody tr');

      rows.forEach(row => {
        const text = row.textContent.toLowerCase();
        row.style.display = text.includes(keyword) ? '' : 'none';
      });
    });
  </script>
</body>
</html>
