# Değişken İsimleri İçin Bir Yöntem
Android Studio üzerinde programlama yaparken ID'lerin çakışmaması ve daha kolay ulaşılabilir olması amacıyla <b>Pascal Case</b>, <b>Snake Case</b> ve <b>Camel Case</b> yazım şekillerinin bir kombinasyonunu kullanıyorum. Özellikle XML'ler ile çalışırken farklı layoutlarda dahi olsa aynı isimde değişkenler verildiğinde karışıklık oluşuyor. Bunu çözmek için şöyle bir yazım şekli kullanılabilir:

<b>AktiviteAdi_degiskenAdi</b>

veya

<b>AktiviteAdi_AltBolum_degiskenAdi</b>

## Örnek:

<b>Main Activity</b> içindeki <b>zaman</b>ı gösteren Text View için:

<code>MainActivity_zamanTV</code>

<b>Main Activity</b> üzerinde çalışan <b>Bilgiler</b> Recycler View'ı içindeki <b>Başlık</b> Edit Text'i için:

<code>MainActivity_BilgilerRV_baslikET</code>
