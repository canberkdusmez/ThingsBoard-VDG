English

This code generates random voltage number datas to use in thingsboard. Voltage number is limited between 190-300 it can be adjusted to wanted numbers. After first random number next random number will be in +-10% range so there will not be big changes to voltage.
To be able to use this code you should write your domain and your token for thingsboard. Voltage data is created for 100 times with 1 second delays.
This code also uses json to send the voltage data and store the timestamp of each voltage data sent.

Türkçe

Bu kod thingsboard'da kullanmak için rastgele voltaj değeri üretir. Volt 190-300 arasında sınırlıdır istediğiniz gibi değiştirebilirsiniz. İlk random sayıdan sonraki sayı +-%10 aralığında olucaktır bu sayede voltaj değerleri arasında çok büyük değişiklikler olmayacaktır.
Bu kodu çalıştırabilmek için thingsboard'daki kendi domain adresinizi ve token'ınızı kullanmanız gerekmektedir. Voltaj verileri 1'er saniye ara ile 100 defa oluşturulur.
Bu kod ayrıca voltaj verisini göndermek ve verilerin gönderilme zamanını tutmak için json kullanır.
