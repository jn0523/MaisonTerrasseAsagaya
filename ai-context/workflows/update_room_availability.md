# 空室・成約状況の更新手順

このドキュメントでは、各部屋の入居状況（成約済み / 空室）が変わった際に行うウェブサイトの更新手順を定義します。

## 成約済みになった場合（例：101号室）

1. **個別部屋ページのリダイレクト設定**
   対象の部屋のHTMLファイル（例: `101.html`）を開き、`<head>` タグの直下にリダイレクト用のメタタグとスクリプトを追加します。
   これにより、ユーザーがブックマーク等から直接アクセスした場合でも、自動的に `introduction.html` に転送されます。

   ```html
   <head>
       <!-- 成約済みのため、introduction.htmlへリダイレクト -->
       <meta http-equiv="refresh" content="0; url=introduction.html">
       <script>window.location.replace("introduction.html");</script>
       <meta charset="UTF-8">
   ```

2. **トップページ（introduction.html）のリンク無効化**
   `introduction.html` を開き、対象となる部屋のリンク箇所を `<s>`（取り消し線）で囲み、「（成約済み）」というテキストを追記して、`<a>` タグを削除します。

   **変更前：**
   ```html
   101号室は<a href="101.html" class="link">こちら</a><br>
   ```

   **変更後：**
   ```html
   <s>101号室はこちら</s>（成約済み）<br>
   ```


## 再び空室が出た場合（リンクを復活させる場合）

退去等により再び募集を開始する場合は、上記の逆の手順を行います。

1. **個別部屋ページのリダイレクト解除**
   対象の部屋のHTMLファイル（例: `101.html`）を開き、`<head>` 直下に追加したリダイレクトのタグを削除します。

   **削除するコード：**
   ```html
       <!-- 成約済みのため、introduction.htmlへリダイレクト -->
       <meta http-equiv="refresh" content="0; url=introduction.html">
       <script>window.location.replace("introduction.html");</script>
   ```

2. **トップページ（introduction.html）のリンク復活**
   `introduction.html` を開き、取り消し線と「（成約済み）」のテキストを削除し、元の `<a>` タグを使用したリンク構造に戻します。

   **変更前：**
   ```html
   <s>101号室はこちら</s>（成約済み）<br>
   ```

   **変更後：**
   ```html
   101号室は<a href="101.html" class="link">こちら</a><br>
   ```
