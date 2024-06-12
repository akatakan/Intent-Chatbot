**Sohbet Robotu Uygulaması**
==========================

**Genel Bakış**
-----------

Bu, Streamlit, Spacy ve Scikit-learn kullanarak oluşturulmuş basit bir sohbet robotu uygulamasıdır. Uygulama, önceden eğitilmiş bir modeli kullanarak kullanıcı girişini sınıflandırır ve buna göre yanıt verir.

**Özellikler**
------------

* **Doğal Dil İşleme (NLP)**: Uygulama, kullanıcı girişini işlemek ve ilgili bilgileri çıkarmak için Spacy'nin İngilizce dil modelini kullanır.
* **İntent Sınıflandırma**: Uygulama, önceden eğitilmiş bir makine öğrenimi modelini kullanarak kullanıcı girişini farklı intent'lara sınıflandırır.
* **Yanıt Oluşturma**: Uygulama, sınıflandırılan intent'e ve kullanıcı girişine göre yanıtlar oluşturur.
* **Sohbet Arayüzü**: Uygulama, Streamlit'in sohbet arayüzünü kullanarak sohbet deneyimini simüle eder.

**Teknik Detaylar**
--------------------

* **Kullanılan Kütüphaneler**:
	+ Spacy için NLP görevleri
	+ Scikit-learn için makine öğrenimi görevleri
	+ Streamlit için sohbet arayüzü
	+ Joblib için model ve vektörleştirici yüklemek ve kaydetmek
* **Model ve Vektörleştirici**: Uygulama, `model.bin` ve `vectorizer.bin` dosyalarında saklanan önceden eğitilmiş bir model ve vektörleştiriciyi kullanır.
* **İntent Verileri**: Uygulama, `intent.json` dosyasında saklanan intent verilerini kullanır.

**Kullanım**
------------

1. Uygulamayı çalıştırmak için Python betiğini çalıştırın.
2. Sohbet robotuyla etkileşime geçmek için sohbet giriş alanına mesajlar yazın.
3. Sohbet robotu, sınıflandırılan intent'e ve kullanıcı girişine göre yanıt verir.

**Not**
----

Bu, basit bir sohbet robotu uygulamasıdır ve daha fazla özellik eklemek isteyebilirsiniz, örneğin:

* Çoklu intent'ları işlemek
* Yanıt olGeneration'ı geliştirmek
* Daha gelişmiş NLP yetenekleri eklemek

**Lisans**
---------

Bu uygulama, MIT Lisansı altında lisanslanmıştır.
