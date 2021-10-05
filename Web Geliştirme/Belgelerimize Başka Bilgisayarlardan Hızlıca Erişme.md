Herhangi bir bilgisayardan hızlı bir şekilde dosyalarınıza erişmek için Drive gibi araçlar kullanabilirsiniz. Ancak ben e-posta adresimi ve parolamı her yerde yazmayı güvenlik sebebiyle tercih etmiyorum. Bunun yerine geçici dosyaları (örneğin kırtasiyeden çıktı alacağım, ya da ortak kullanılan bir bilgisayarda bir dosyamı indireceğim) indirmek için sunucumda oluşturduğum ve şifrelediğim bir dizin (public_html/belgeler gibi) üzerinde tutuyorum. Aynı zamanda herhangi bir bilgisayarda acil bir şekilde kendime bir şeyler göndermek için aynı dizini kullanıyorum. 

<i>Sunucunuz üzerindeki dizini GIT ile bağlayarak bunu bilgisayarınızda da daha senkronize ve kolay bir şekilde tutabilirsiniz.</i>


Sunucunuzda bir klasör oluşturun.
<quote>public_html/belgeler</quote>

<b>Önemli Not:</b> Belgeler klasörünün izinlerini dışardan yazılabilir şekilde değiştirin.

Şimdi sadece iki dosyaya ihtiyacımız var.

<code>
websiteniz.com/belgeler/index.html
</code>
<br>
<code>
websiteniz.com/belgeler/upload.php
</code>
<br><br>

Bir de dosyaları yükleyeceğimiz bir alt dizine:<br>
<code>websiteniz.com/belgeler/yuklenenler</code>


## index.html

```html
    <!DOCTYPE html>
    <html>
        <head>
            <title>Melih Çelenk - Belgeler</title>
            <meta charset="utf-8">
        </head>
        <body>
            <center>
                <h1>Melih Çelenk - Belgeler</h1>
                <form action="upload.php" method="post" enctype="multipart/form-data">
                  Dosya yüklemek için tıkla:
                  <input type="file" name="fileToUpload" id="fileToUpload">
                  <input type="submit" value="Upload Image" name="submit">
                </form>

                <a href="http://websiteniz.com/belgeler/yuklenenler/"><h1>Dosyalar</h1></a>
            </center>

        </body>
    </html>
```

## upload.php

```html
<?php
$target_dir = "yuklenenler/";
$target_file = $target_dir . basename($_FILES<"fileToUpload"><"name">);
$uploadOk = 1;
$imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));


if(isset($_POST<"submit">)) {
 $uploadOk = 1;
}


if (file_exists($target_file)) {
  echo "Dosya zaten mevcut.";
  $uploadOk = 0;
}


if ($_FILES<"fileToUpload"><"size"> > 500000000) {
  echo "Dosya boyutu çok büyük.";
  $uploadOk = 0;
}


if ($uploadOk == 0) {
  echo "Yüklenemedi.";
} else {
  if (move_uploaded_file($_FILES<"fileToUpload"><"tmp_name">, $target_file)) {
    echo "The file ". htmlspecialchars( basename( $_FILES<"fileToUpload"><"name">)). " has been uploaded.";
  } else {
    echo "Yükleme sırasında bir hata meydana geldi.";
  }
}
?>
```
