# Sanal Kıyafet Deneme Uygulaması "Akıllı Dolabım"

Bu proje, kullanıcıların **kendi kıyafetlerini sanal ortamda deneyebileceği**, dijital bir dolap oluşturabileceği ve öneri algoritmasıyla kombinler keşfedebileceği bir mobil uygulamadır. Sistem, Flutter tabanlı mobil arayüz ile Python tabanlı sunucunun entegrasyonuyla çalışır.

---

## Özellikler

- Kullanıcı kendi fotoğrafını ve kıyafet görsellerini yükleyebilir  
- Kıyafetleri dijital dolapta organize edebilir  
- Görüntü işleme teknikleriyle sanal deneme (VITON tabanlı)  
- Kıyafet kategorilerine göre **kombin önerisi**  
- SQLite veritabanı ile yerel veri saklama  
- Karanlık mod desteği  
- Flutter + Python Flask sunucu haberleşmesi

---

## Kullanılan Teknolojiler

| Katman         | Teknoloji / Kütüphane            |
|----------------|----------------------------------|
| Mobil Geliştirme | Flutter, Dart, Provider, SQFLite |
| Backend        | Python, Flask, OpenCV, UNet, MediaPipe |
| Görüntü İşleme | Segmentasyon, Pose Estimation    |
| Depolama       | SQLite, Local File System        |

---

## Ekran Görüntüleri

| Ana Sayfa | Dolabım | Sanal Deneme |
|----------|---------|--------------|
| <img width="200" height="500" alt="image" src="https://github.com/user-attachments/assets/54dd1b3c-ef55-4926-975f-0e74e9499cd5" /> | <img width="200" height="500" alt="image" src="https://github.com/user-attachments/assets/d9683817-34eb-4b2e-821d-03164ee24e87" />| <img width="200" height="500" alt="image" src="https://github.com/user-attachments/assets/ff7a05ee-43f5-4f00-a978-9db1612faad0" />|

---

## Kurulum

```bash
git clone https://github.com/kullanici_adi/virtual-tryon-app.git
cd virtual-tryon-app
flutter pub get
flutter run
