# Grafical-Match-Matrix
iki diilimin eşleşen noktalarını gösteren bir tablo oluştuturur.
<h2>Süreç</h2>
• Ödevi yapacağım dil olarak Python programlama dilini seçtim. <br>
• Görsel programlama için ise PyQt5 modülünü kullanmaya karar verdir. <br>
• PyQt5 modülünde Qt Designer aracı ile form tasarımı yapılabiliyor. Bende biri kullanıcıdan değerleri alacak olan pencere, diğeri tablo penceresi olmak üzere 2 pencere(widget) oluşturdum. Bunları _window ve _table olarak isimlendirdim. <br>
• _window ve _table dosyaları üzerinde de düzenlemeler yaptım. Qt Designer ile 
oluşturduğum yapıyı iskelet olarak kullandım. <br>
• Sonrasında işlemlerimi yürüteceğim process.py dosyasında _window ve 
_table’ı import ettim.<br>
• İşlemlerimi daha kolay yürütebilmek için, process.py’da bir sınıf oluşturdum ve isim 
olarak “Match” ismini verdim. Bütün süreci bu sınıf üzerinden yönettim.<br>
• Pythonda __init__ metodu yapılandırıcı metot(constructor) olarak kullanılıyor. Match 
sınıfını oluştururken QtWidget sınıfından miras aldım. __init__ metodunda super() ile 
miras aldığım QtWidget’a gerekli değerleri gönderdim. <br>
• Yine __init__ metodunda, ui isminde bir nesne oluşturdum ve bu nesneyi 
pencerelerimi yönetmek için kullandım. İlk pencereyi ve sonrasında açılan 
tabloyu bu nesne ile yönettim.<br>
• Son olarak da __init__ metodunda kullanıcıdan dizilimleri ve keymer değerini 
alacağım pencerenin kurulumunu yaptım ve pencereyi açtım.
<br>

![form](https://user-images.githubusercontent.com/77548038/157219386-8ab607e7-eb44-491a-b6bd-3f1c68a42d14.png)
<br>
• Bu pencerede kullanıcıdan alınacak olan, first sequence değeri ve second sequence 
değeri düzgün bir değer olduğu varsayılmıştır. Kullanıcının gireceği 
keymer değeri(n-value) de bir tamsayı olarak varsayılmıştır. .<br>
• Kod tarafında kullanıcıdan gelen değerleri almak için getSequence() metodunu ve 
gelen sekansı keymerlerine ayırmak için de divideSequence() metodunu kullandım. 
Ardından getSequence() metodu içerisinde kullanıcından değerleri alan pencereyi 
kapattım.<br>
• Tabloyu oluşturması için createTable() isimli bir metot tanımladım ve bu metoda 
getSequence() metoduyla kullanıcıdan alınmış ve divideSequence() metoduyla 
keymerlerine ayrılmış liste tipindeki first ve second sekanslarını verdim.<br>
• Sekansların uzunluklarını bulup, bu uzunluklara göre tablomu 
oluşturdum. Tabloda first sekansını sütun başlıklarına, second sekansını satır 
başlıklarına verdim.<br>
• Tablodaki bütün satır ve sütunların genişliklerini ayarlayan bir metot bulamadım, 
setColumnWidth() ve setRowHeight() metotları sadece belli bir satır veya sütunun 
genişliğini ayarlayabiliyordu bu yüzden, döngü kullanıp bütün satır-sütunların 
genişliklerini ayarladım.<br>
• Ardından tabloda eşleşen keymerleri bulma, sayma ve renklendirme işlemine geçtim. 
Bu işlemi en verimli nasıl yaparım diye üzerinde düşündükten sonra, çözüm olarak 
sırasıyla tablodaki diagonelleri gezmeye karar verdim. Algoritmayı anlatması biraz 
zor, özet olarak; first sekans uzunluğu + second sekans uzunluğu – 1 adet olan 
digonalleri gezmek için biri ortadaki diagonal, diğer biri ortadaki diagonalin üst 
kısmındaki diagonaller, sonuncusu da ortadaki diagonalin alt kısmındaki diagonaller 
için olmak üzere 3 döngü sistemi kurdum. Bu döngüler, eşleşme bulduğunda countı 
arttırıp, renklendirir ve count sayısını o hücreye yazar. Eşleşme bulamadığı yerde de 
countı sıfırlayıp oluşturduğum newColor() metodundan farklı bir renk alır. Bu şekilde 
bütün diagonalleri gezip, eşleşen yerleri renklendirir. Son olarak da tabloyu gösterir.<br>

![tablex](https://user-images.githubusercontent.com/77548038/157219401-05df3de2-2265-4907-ac0c-7e7a64636782.png)
<br>
<h2>Sonuç</h2>
Sonuç olarak, kullanıcıdan sekansları ve n değerini alan, sekansları 
keymerlerine ayıran, bir tablo oluşturup burada keymerleri eşleştiren, eşleşen 
keymerleri sayıp renklendiren ve son olarak da bu tabloyu bize gösteren bir 
program yazmış oldum.
Ödev sırasında birçok hata aldım, çözmek için saatlerce uğraştım. PyQt5 
ile ilgili birçok dökümana baktım. Python’daki OOP mantığı Java’dan çok farklı. 
Bu noktada biraz zorlandım. Ancak, benim açımdan gayet verimliydi. Güzel bir 
ödevdi.
