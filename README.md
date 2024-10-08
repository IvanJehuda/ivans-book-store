# README
Nama : Ivan Jehuda Angi

NPM : 2306162222

Kelas : PBP E

## Website Link
https://ivan-jehuda-ivansbookstore.pbp.cs.ui.ac.id/

## Markdown
- [Tugas 2](#tugas-2)

- [Tugas 3](#tugas-3)

- [Tugas 4](#tugas-4)

- [Tugas 5](#Tugas-5)

- [Tugas 6](#Tugas-6)

# Tugas-2
### Step by step pembuatan Ivan's Book Store

1. Membuat direktori baru dengan nama `ivans-book-store`.

2. Membuat dan mengaktifkan virtual environment pada direktori tersebut dengan:
    ```
    python -m venv env
    env\Scripts\activate
    ```

3. Membuat berkas reqirements berisikan :
    ```
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```
    dan menginstal dependencies tersebut dengan perintah `pip install -r requirements.txt`
4. Menginisiasi proyek django baru dengan perintah
`django-admin startproject ivans-book-store .`

5. Membuat aplikasi baru bernama main dengan perintah :
`python manage.py startapp main`

6. Membuat berkas template dalam main dan mengisinya dengan :
    ```
    <h1>Ivan's Book Store</h1>
    <h5>NPM: </h5>
    <p>{{ npm }}<p>
    <h5>Name: </h5>
    <p>{{ name }}<p>
    <h5>Class: </h5>
    <p>{{ class }}<p>
    ```
7. Membuat model product dengan memodifikasi berkas models.py dengan :
    ```
    from django.db import models

    class Product(models.Model):
        name = models.CharField(max_length=255)
        price = models.DateField(auto_now_add=True)
        description = models.TextField()
        genre = models.CharField(max_length=255)
    ```
8. Menambahkan routing untuk menghubungkan `views.py` di `main` pada `urls.py`:
    ```python
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [ path('', show_main, name='show_main'),]
    ```
9. Mengkofigurasi routing url proyeng dengan memodifikasi berkas urls.py dalam direktori ivans_book_store dengan :
    ```
    urlpatterns = [
    ...
    path('', include('main.urls')),
    ...
    ```
10. Melakukan deployment pada PWS (Pacil Web Service).



### Diagram cara kerja Django

![Django Flow Chart](django_chart.png)


### Fungsi git dalam pengembangan perangkat lunak
1. Memungkinkan suatu tim mengerjakan suatu proyek secara bersamaan tanpa mengganggu bagian yang lain.

2. Mencatat riwayat perubahan kode serta menyimpan berbagai informasi detail seperti : waktu perubahan dan siapa yang melakukan perubahan.

3. Menjadi tempat penyimpanan file atau product management, memudahkan penggunaan backup file.

4. Memudahkan deployment dengan adanya fungsi pull serta push.


### Alasan Django dijadikan sebagai framework pembelajaran
1. Menyediakan banyak fitur bawaan yang memudahkan pengembangan aplikasi web.
2. Memiliki fitur keamanan yang baik.
3. Memiliki fitur MVT sehingga mengajarkan bagaimana pengembangan web terorganisir.

### Alasan model Django disebut sebagai ORM
 Model pada Django disebut ORM (Object Relational Mapping) karena berfungsi sebagai penghubung antara model (objek) dalam kode Python dengan  database relasional. ORM membantu aplikasi lebih portabel dan mendukung berbagai jenis relasi antar tabel.



### Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data sangat penting dalam sebuah platform karena beberapa alasan kunci:

1. **Efisiensi dan Kinerja**: Data yang tepat waktu dan efisien memastikan bahwa pengguna dapat mengakses dan memanfaatkan platform tanpa delay yang signifikan. Ini mempengaruhi kinerja keseluruhan platform, kepuasan pengguna, dan skalabilitas, terutama dalam aplikasi waktu nyata seperti layanan streaming atau cloud computing.

2. **Pengalaman Pengguna**: Data delivery yang cepat dan dapat diandalkan secara langsung mempengaruhi pengalaman pengguna. Misalnya, di platform e-commerce, pengiriman data yang lambat dapat menyebabkan navigasi yang buruk dan membuat pengguna frustrasi, yang mungkin membuat mereka pergi.

3. **Pengambilan Keputusan Berdasarkan Data**: Banyak platform bergantung pada data delivery secara real-time untuk memberikan wawasan, dasbor, dan analitik yang memungkinkan pengambilan keputusan berdasarkan data. Keterlambatan dalam pengiriman data dapat menyebabkan wawasan yang usang atau tidak akurat.

4. **Keamanan**: Mekanisme data delivery yang efisien memastikan bahwa data sensitif ditransmisikan dengan aman dan mematuhi persyaratan kepatuhan, seperti GDPR atau HIPAA, terutama untuk platform yang menangani data pribadi pengguna.

5. **Kolaborasi dan Integrasi**: Banyak platform perlu mengirimkan data ke sistem lain, API, atau pengguna untuk tujuan integrasi dan kolaborasi. Pengiriman data yang efisien mendukung integrasi yang mulus antara layanan dan memastikan bahwa platform dapat berinteraksi dengan sistem eksternal secara real-time.




# Tugas-3

### Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya, dalam hal format data delivery yang umum digunakan, saya memilih JSON untuk digunakan. Banyak aspek yang memengaruhi JSON lebih populer dari XML, seperti:

1. **Kesederhanaan**:
   - JSON lebih ringan dan lebih mudah dibaca serta ditulis. Strukturnya lebih sederhana, menggunakan pasangan key-value.

2. **Keterbacaan**:
   - Format JSON lebih ringkas dan lebih mudah dibaca, terutama bagi para pengembang. Ini terintegrasi secara alami dengan JavaScript, yang menjadikannya ideal untuk aplikasi web.

3. **Kinerja**:
   - JSON memiliki ukuran yang lebih kecil dibandingkan XML karena tidak memiliki tag penutup, sehingga lebih cepat untuk diparse dan ditransmisikan melalui jaringan.

4. **Tipe Data**:
   - JSON mendukung tipe data bawaan seperti angka, string, array, dan boolean, sehingga memudahkan untuk bekerja dengan data secara langsung dalam bahasa pemrograman.

5. **Integrasi dengan JavaScript**:  
   - JSON berasal dari JavaScript, sehingga secara alami kompatibel dengan pengembangan web modern. JavaScript dapat dengan mudah mem-parsing JSON menggunakan `JSON.parse()` dan mengonversi objek menjadi JSON dengan `JSON.stringify()`.



### Fungsi dari method `is_valid()` pada form Django
Dalam Django, `is_valid()` adalah metode yang digunakan untuk memvalidasi data dalam formulir atau serializer. Ini memeriksa apakah data yang diberikan ke formulir atau serializer memenuhi aturan validasi yang ditetapkan untuk bidang yang sesuai. Metode ini mengembalikan True jika data valid dan False jika tidak. Selain itu, ketika `is_valid()` dipanggil, Django mengisi atribut errors dengan semua kesalahan validasi yang terjadi.

### Pentingnya `crsf_token` dan bahaya penyerang
Token Cross-Site Request Forgery melindungi aplikasi dari serangan Cross-Site Request Forgery. Dengan memiliki `csrf_token`, mereka dapat memastikan bahwa request POST berasal dari situs yang sah dan mencegah modifikasi data yang tidak sah melalui request palsu. Tanpa `csrf_token`, penyerang dapat membuat request palsu menggunakan nama pengguna yang sudah terotentikasi, mengubah data sensitif, atau mengakses informasi pribadi pengguna.

Jika `csrf_token` tidak ada, penyerang akan membuat situs web berbahaya atau memodifikasi situs web yang sudah ada. Saat pengguna masuk ke aplikasi Django, mereka akan tanpa disadari mengakses situs berbahaya tersebut. Selanjutnya, situs berbahaya akan memuat form tersembunyi yang meminta aplikasi Django.

## Step by Step Week 3
1. Membuat berkas `base.html` dan emngisinya dengan
    ```python
    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            {% block meta %} {% endblock meta %}
        </head>
        <body>
            {% block content %} {% endblock content %}
        </body>
    </html>
    ```

    2. Menambahkan `BASE_DIR` pada `settings.py` agar project mengenali html yang akan menjadi template utama
    ```python
    'DIRS': [BASE_DIR / 'templates'],
    ```

    3. Menambahkan atribut `time` dan `id` pada model product
    ```python
    from django.db import models
    import uuid


    class Product(models.Model):
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
        name = models.CharField(max_length=255)
        price = models.IntegerField()
        description = models.TextField()
        genre = models.CharField(max_length=255)
        author = models.CharField(max_length=255, default='-')

    ```

    4. Membuat `forms.py` untuk mendeklarasikan atribut-atribut dari model yang membutuhkan input dari user
    ```python
    from django.forms import ModelForm
    from .models import ProductEntry

    class ProductEntryForm(ModelForm):
        class Meta:
            model = ProductEntry
            fields=['name','price', 'genre', 'description', 'author']
    ```

    5. Membuat method `create_product_entry` untuk mengambil input user sesuai dengan `forms.py`
    ```python
    def create_product_entry(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
    ```

    6. Membuat method `show_main` untuk menampilkannya di `main.html`
    ```python
    def show_main(request):
    product_entries = Product.objects.all()

    context = {
        'appname' : 'ivans book store',
        'npm' : '2306123456',
        'name': 'Pak Bepe',
        'class': 'PBP E',
        'product_entries': product_entries

    }

    return render(request, "main.html", context)
    ```

    

    8. Membuat `show_xml`, `show_json`, `show_xml_by_id`, `show_json_by_id` untuk menampilkan response back dari input user
    ```python
    def show_xml(request):
        data = ProductEntry.objects.all()
        return HttpResponse(serializers.serialize("xml",data),content_type='application/xml')

    def show_json(request):
        data = ProductEntry.objects.all()
        return HttpResponse(serializers.serialize("json",data),content_type='application/json')

    def show_xml_by_id(request, id):
        data = ProductEntry.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json_by_id(request, id):
        data = ProductEntry.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```

    9. Melakukan routing di dari method yang sudah dibuat di `urls.py`
    ```python
    from django.urls import path
    from main.views import show_main,create_name_entry,show_xml,show_json,show_xml_by_id,show_json_by_id,delete_product_entry

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
        path('create-name-entry', create_name_entry, name='create_name_entry'),
        path('xml/',show_xml,name='show_xml'),
        path('json/',show_json,name='show_json'),
        path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
        path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
        ]
    ```

    10. Membuat `create_product_entry.html` untuk tampilan ketika web ingin meminta input dari pengguna
    ```python
    {% extends 'base.html' %} 
    {% block content %}
    <h1>Add New Product Entry</h1>

    <form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
        <td></td>
        <td>
            <input type="submit" value="Add Product " />
        </td>
        </tr>
    </table>
    </form>

    {% endblock %}
    ```
    
    11. Membuat `main.html` untuk menampilkan product dari hasil input pengguna
    ```python
        {% extends 'base.html' %}
        {% block content %}
        <h1>Ivan's Book Store</h1>

        <h5>NPM: </h5>
        <p>{{ npm }}<p>

        <h5>Name:</h5>
        <p>{{ name }}</p>

        <h5>Class:</h5>
        <p>{{ class }}</p>
        {% if not product_entries %}
        <p>Belum ada data produk pada ivan's book store.</p>
        {% else %}
        <table>
        <tr>
            <th>Product Name</th>
            <th>Price</th>
            <th>Genre</th>
            <th>Description</th>
            <th>Author</th>
        </tr>

        {% comment %} Berikut cara memperlihatkan data prduk di bawah baris ini 
        {% endcomment %} 
        {% for product_entry in product_entries %}
        <tr>
            <td>{{product_entry.name}}</td>
            <td>{{product_entry.price}}</td>
            <td>{{product_entry.genre}}</td>
            <td>{{product_entry.description}}</td>
            <td>{{product_entry.author}}</td>
        </tr>
        {% endfor %}
        </table>
        {% endif %}

        <br />

        <a href="{% url 'main:create_product_entry' %}">
        <button>Add New Product Entry</button>
        </a>
        {% endblock content %}
    ```

# Postman Screenshots
## a.  XML
![Postman](postmanXML.png)

## b. JSON
![Postman](postmanJSON.png)

## c. XML by id
![Postman](postmanXMLbyID.png)

## d. JSON by id
![Postman](postmanJSONbyID.png)

# Tugas-4

##  Menghubungkan `product` dengan  `user`
 Dalam Django, model `Product` biasanya dihubungkan dengan model `User` menggunakan Foreign Key. Dengan adanya Foreign Key, setiap `Product` dapat terhubung ke pengguna tertentu yang telah login.

Contoh model `Product`:
```python
from django.db import models
import uuid
from django.contrib.auth.models import User

class ProductEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True,default = uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
```

Cara kerja dalam menghubungkannya adalah dengan setiap kali pengguna membuat entry product, entry tersebut akan dikaitkan dengan `user` yang login. Lalu ForeignKey akan bermanfaat untuk membuat relasi many-to-one antara `Product` dengan `User`. Many-to-one memiliki arti bahwa setiap `user` dapat memiliki lebih dari satu entry `Product`. Lalu parameter `on_delete=models.Cascade` memiliki arti apabila `user` dihapus, maka semua entri `Product` yang berkaitan dengan `user` akan dihapus.
## Cara Django mengingat pengguna yang login
Django menggunakan kombinasi session dan cookies untuk mengingat pengguna yang telah login. Ketika pengguna berhasil login, Django akan membuat sebuah session unik dan menyimpan ID session ini dalam sebuah cookie di browser pengguna. Pada setiap permintaan selanjutnya, browser akan mengirimkan cookie ini kembali ke server, dan Django akan menggunakan ID session untuk mencari data pengguna yang sesuai di server. Selain untuk mengingat pengguna, cookies juga digunakan untuk personalisasi, pelacakan, dan otentikasi.

## Authentication dan authorization
**Authentication** adalah proses memverifikasi identitas pengguna , sedangkan **authorization** adalah proses menentukan hak akses pengguna.

Implementasi di Django:

- **Authentication**: Django menyediakan sistem authentication bawaan yang sangat fleksibel. Anda dapat menggunakan model User bawaan atau membuat model User custom untuk menyimpan informasi pengguna. Django juga menyediakan berbagai backend authentication untuk mendukung berbagai metode otentikasi seperti username/password, otentikasi sosial, dan lain-lain.

- **Authorization**: Django mendukung konsep permission dan group untuk mengelola otorisasi. Permission adalah izin untuk melakukan tindakan tertentu (misalnya, menambahkan pengguna, mengubah postingan), sedangkan group adalah kumpulan pengguna yang memiliki permission yang sama. Anda dapat memberikan permission kepada group, dan kemudian menambahkan pengguna ke dalam group tersebut.


## Perbedaan `HttpResponseRedirect()` and `redirect()`
HttpResponseRedirect() dan redirect() adalah dua fungsi yang digunakan untuk mengalihkan pengguna ke URL yang berbeda di Django, tetapi keduanya memiliki cara yang sedikit berbeda dalam mencapainya:

- `HttpResponseRedirect()` :Secara langsung membuat objek HttpResponse dengan kode status 302 (Ditemukan) dan header Lokasi yang menentukan URL baru.
Lebih fleksibel karena memungkinkan Anda untuk menyesuaikan header respons dan atribut lain dari objek HttpResponse.
- `redirect()` : Sebuah fungsi shortcut yang menyederhanakan proses pembuatan objek HttpResponseRedirect.
Fungsi ini mengambil URL baru sebagai argumen dan secara otomatis membuat objek HttpResponse dengan kode status yang benar dan header Lokasi.

## Step by step tugas 4
1. Menambahkan import di `views.py` untuk keperluan register, login, dan logout.
```python
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
```
2. Membuat fitur register, login, dan logout
```python
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('main:show_main')

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('main:login')
```
3. Membuat template baru sebagai tempat login bernama `login.html`, yang berisi :
```python
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
  <h1>Login</h1>

  <form method="POST" action="">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input class="btn login_btn" type="submit" value="Login" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %} Don't have an account yet?
  <a href="{% url 'main:register' %}">Register Now</a>
</div>

{% endblock content %}
```
4. Membuat template baru sebagai tempat register bernama `register.html`, yang berisi :
```python
{% extends 'base.html' %}

{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}

<div class="login">
  <h1>Register</h1>

  <form method="POST">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input type="submit" name="submit" value="Daftar" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %}
</div>

{% endblock content %}
```

5. Menambahkan fuction untuk keperluan login, logout, dan register pada `views.py`
```py
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('main:show_main')

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('main:login')
```
6. Melakukan routing pada `urls.py`
```python
from main.views import register, login_user, logout_user
```

```python
urlpatterns = [
...
path('register/', register, name='register'),
path('login/', login_user, name='login'),
path('logout/', logout_user, name='logout'),
]

```
7. Menghubungkan model `Product` dengan `User`.
```python
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
```

8. Selanjutnya, pada `views.py`, saya melakukan perubahan pada fungsi `create_product()` dan `show_main()`
```python
@login_required(login_url='/login')
def show_main(request):
    product = Product.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
        ...
    }

def create_product_entry(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)
```

9.  Mengimpor hal-hal penting pada `views.py` untuk menampilkan detail informasi pengguna yang sedang _logged in_ seperti _username_ dan _last login_
```python
    import datetime
    from django.http import HttpResponseRedirect
    from django.urls import reverse
```

9. Menambahkan fungsionalitas _cookie_ pada fungsi `login_user`
```python
if form.is_valid():
    user = form.get_user()
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main"))
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
```

10. Tambahkan `'last_login': request.COOKIES['last_login'],` pada fungsi `show_main`

11.  Ubah fungsi `logout_user`
```python
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```

12 Modifikasi `main.html` untuk menambahkan informasi last login serta tombol logout.

# Tugas-5
## Prioritas CSS Selector 
Prioritas selector CSS menentukan gaya mana yang diterapkan ketika beberapa aturan menargetkan elemen yang sama. Berikut urutan prioritas dari yang terendah hingga tertinggi:

1. **Selector element** (misalnya, `div`, `p`)  
   - Prioritas terendah.  
   ```css
   p { color: red; }
   ```

2. **Selector class** (misalnya, `.nama-kelas`)  
   - Lebih tinggi dari selector elemen.  
   ```css
   .alert { color: blue; }
   ```

3. **Selector ID** (misalnya, `#id`)  
   - Lebih diprioritskan dari selector class.  
   ```css
   #header { color: green; }
   ```

4. **inline style** (ditambahkan langsung dalam HTML, misalnya, `style="color: yellow;"`)  
   - Lebih diprioritaskan dari selector ID.  
   ```html
   <p style="color: yellow;">Hello</p>
   ```

5. **Selector atribute**, **pseudo-class** (misalnya, `[type="text"]`, `:hover`)  
   - Sama kuat dengan selector kelas.  
   ```css
   input[type="text"] { border: 1px solid black; }
   ```


Jika terjadi konflik prioritas, aturan yang terakhir ditulis di file CSS yang akan digunakan.

## Mengapa responsive design penting

1. **Pengalaman Pengguna yang Lebih Baik**: Ini memastikan bahwa situs web Anda terlihat dan berfungsi dengan baik di semua perangkat, dari desktop hingga smartphone, memberikan pengalaman yang mulus bagi pengguna.

2. **Peningkatan Lalu Lintas Seluler**: Dengan semakin banyaknya pengguna seluler, memiliki situs web yang ramah seluler adalah hal yang penting. Desain responsif membantu menarik dan mempertahankan audiens ini.

3. **SEO yang Lebih Baik**: Mesin pencari seperti Google memprioritaskan situs web yang ramah seluler dalam peringkat mereka. Desain responsif dapat meningkatkan visibilitas situs Anda dan peringkat di mesin pencari.

4. **Hemat Biaya**: Alih-alih membuat situs web terpisah untuk perangkat yang berbeda, desain responsif memungkinkan Anda untuk mempertahankan satu situs yang dapat menyesuaikan dengan berbagai ukuran layar, menghemat waktu dan sumber daya.

5. **Future Proofing**: Seiring dengan dirilisnya perangkat baru dengan ukuran dan resolusi layar yang berbeda, desain responsif memastikan situs web Anda tetap dapat diakses dan berfungsi.


Contoh aplikasi yang sudah menerapkan responsive design:
- Google
- Youtube

Contoh aplikasi yang belum menerapkan responsive design:
- SiakNG

## Margin, Padding, dan Border

1. **Margin**:
   - **Definisi**: Ruang di luar batas suatu elemen.
   - **Tujuan**: Ini menciptakan space antara elemen dan elemen lain di sekitarnya.


2. **Padding**:
   - **Definisi**: Space antara konten suatu elemen dan batasnya.
   - **Tujuan**: Ini menciptakan space di dalam elemen, antara konten dan border.
   

3. **Border**:
   - **Definisi**: Garis yang mengelilingi padding dan konten dari sebuah elemen.
   - **Tujuan**: Ini mendefinisikan batas elemen tersebut.

## Grid Box and Flex Box

### Flexbox (Flexible Box Layout)
Flexbox dirancang untuk **tata letak satu dimensi**. Ini unggul dalam mendistribusikan ruang sepanjang satu sumbu (baik secara horizontal maupun vertikal) dan menyelaraskan item di dalam sebuah wadah.

#### Komponen:
1. **Flex Container**: Elemen induk yang menampung item-item fleksibel.
   ```css
   .container {
     display: flex;
   }
   ```
2. **Flex Items**: Elemen anak di dalam kontainer fleksibel.
3. **Main Axis and Cross Axis**: Tata letak Flexbox didasarkan pada main axis (secara default adalah horizontal) dan cross axis. .
4. **Properti Flex**:
   - `flex-direction`: Menentukan arah main axis (row, row-reverse, column, column-reverse).
   - `justify-content`: Menyelaraskan item di sepanjang main axis (flex-start, flex-end, center, space-between, space-around).
   - `align-items`: Menyelaraskan item di sepanjang cross axis (flex-start, flex-end, center, stretch).


### Grid (CSS Grid Layout)
Grid dirancang untuk **tata letak dua dimensi**. Ini memungkinkan Anda untuk membuat tata letak yang kompleks dengan baris dan kolom.

#### Komponen:
1. **Kontainer Grid**: Elemen induk yang menampung item grid.
   ```css
   .grid-container {
     display: grid;
     grid-template-columns: ulangi(3, 1fr);
     grid-template-rows: otomatis;
   }
    ```
2. **Item Grid**: Elemen anak di dalam  grid.

3. **Grid lines**: Garis-garis yang membagi grid menjadi cells.
4. **Properti Grid**:
   - `grid-template-columns` dan `grid-template-rows`: Menentukan struktur dari grid.
   - `grid-gap`: Mengatur jarak antara item grid.
   - `grid-area`: Menentukan posisi dan ukuran item grid dalam grid.


### Kapan Menggunakan Flexbox vs. Grid
- **Flexbox**: Lebih baik untuk tata letak dalam satu arah (e.g., navigation bars, aligning items dalam row and column).
- **Grid**: Ideal untuk tata letak dua dimensi yang kompleks (e.g.,  web pages, dashboards).

Baik Flexbox maupun Grid dapat digunakan bersama untuk menciptakan desain yang sangat responsif dan fleksibel.

## Step by step Tugas 5
1. Menambahkan dua function di `views.py`, yaitu `delete_product` dan `edit_product` yang bisa diterapkan pada setiap productnya.
    ```python
    
    def edit_product(request, id):
        # Get mood entry berdasarkan id
        product = Product.objects.get(pk = id)

        # Set mood entry sebagai instance dari form
        form =ProductForm(request.POST or None, instance=product)

        if form.is_valid() and request.method == "POST":
            # Simpan form dan kembali ke halaman awal
            form.save()
            return HttpResponseRedirect(reverse('main:show_main'))

        context = {'form': form}
        return render(request, "edit_product.html", context)

    def delete_product(request, id):
        # Get mood berdasarkan id
        product = Product.objects.get(pk = id)
        # Hapus mood
        product.delete()
        # Kembali ke halaman awal
        return HttpResponseRedirect(reverse('main:show_main
    ```
2. Melakukan routing dari kedua function ini ke `urls.py`
    ```python
        path('delete/<uuid:id>', delete_product, name='delete_product'),
        path('edit-product/<uuid:id>', edit_product, name='edit_product'),
    ```
 3. Memodifikasi `base.html` untuk tampilan responsive web design and tailwind css
    ```python
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <script src="https://cdn.tailwindcss.com"></script>
    ```
4. Membuat `global.css` untuk mengatur tampilan general dari web
    ```css
        .form-style form input, form textarea, form select {
        font-family: 'Roboto', sans-serif;
        width: 100%;
        padding: 0.5rem;
        border: 2px solid #bcbcbc;
        border-radius: 0.375rem;
        }
        .form-style form input:focus, form textarea:focus, form select:focus {
            outline: none;
            border-color: #674ea7;
            box-shadow: 0 0 0 3px #674ea7;
        }


        @keyframes gradient-animation {
            0% {
                background-position: 0% 50%;
            }
            50% {
                background-position: 100% 50%;
            }
            100% {
                background-position: 0% 50%;
            }
        }

        .animate-gradient {
            background: linear-gradient(270deg, #4f46e1, #ec4899, #4f46e1); /* Adjust colors as needed */
            background-size: 300% 300%; /* Adjust to change the speed */
            animation: gradient-animation 5s ease infinite; /* Duration and easing */
        }

        ```
5. Membuat `navbar.html` sebagai navigation bar, untuk 2 versi( desktop dan mobile viewing)
6. Menambahkan path untuk ke static folder pada `settings.py`
    ```python
    STATIC_URL = '/static/'
    if DEBUG:
    STATICFILES_DIRS = [
        BASE_DIR / 'static'
    ]
    else:
    STATIC_ROOT = BASE_DIR / 'static' 
    ```
8. Membuat `card_info.html` dan `card_product.html` sebagai wadah informasi di `main.html`
7. Mengubah tampilan pada `login.html`, `edit_product.html` , `create_product_entry.html`, `register.html`, dan mengimplementasikan  `card_info.html` dan `card_product.html` pada `main.html` agar terlihat modern dan menjadi responsive terhadap berbagai device.

# Tugas-6
## Manfaat Javascript
JavaScript memungkinkan developer membuat halaman web yang interaktif dan dinamis. JavaScript berjalan di browser pengguna (client-side), yang artinya pemrosesan dan interaksi dapat dilakukan langsung di perangkat pengguna tanpa perlu mengirim data ke server setiap saat. JavaScript juga memungkinkan pengiriman dan penerimaan data dari server tanpa memuat ulang halaman secara keseluruhan. Hal ini memungkingkan Javascript untuk membuat aplikasi yang lebih ringan.

## Fungs `await` saat menggunakan `fetch()`
 `await` dalam JavaScript digunakan di dalam fungsi `async` untuk menangani operasi asynchronous, seperti mengambil data dari API menggunakan fungsi `fetch()`. Dengan menggunakan `await`, kita dapat menghentikan eksekusi kode hingga promise yang dikembalikan oleh `fetch()` terpenuhi, memungkinkan struktur kode yang lebih mudah dibaca. Approach ini menyederhanakan penanganan kesalahan dengan `try...catch`, meningkatkan kejelasan kode secara keseluruhan dibandingkan dengan menggunakan `.then()` dan `.catch()` untuk pengelolaan promise.

 Jika kita tidak menggunakan `await` atau metode lain untuk menangani promise (seperti `.then()`), JavaScript akan melanjutkan eksekusi kode berikutnya sebelum permintaan selesai. Ini berarti kode yang bergantung pada hasil dari `fetch()` (seperti data yang diambil dari server) bisa jadi dijalankan sebelum data yang diperlukan tersedia.


## Alasan digunakannya decorator `crsf_exempt`
 Django secara default memerlukan CSRF token untuk setiap permintaan POST. Namun, dalam kasus AJAX, Django tidak dapat membuat CSRF token secara otomatis, jadi kita harus menonaktifkan CSRF protection untuk tampilan tersebut.

Dengan menggunakan decorator csrf_exempt, kami meminta Django untuk menghindari memeriksa CSRF token pada permintaan POST yang dikirimkan ke view tersebut. Ini memungkinkan kami untuk mengirimkan permintaan POST dari AJAX tanpa masalah.

## Alasan validasi di back-end
Pembersihan data di frontend hanya bersifat client-side dan dapat dengan mudah diubah dan di-bypass oleh penyerang. Pembersihan data di backend memastikan bahwa data yang diterima adalah valid dan aman untuk diproses, karena tidak bisa diubah oleh pengguna.

Pembersihan data di backend memastikan bahwa semua data yang diterima oleh aplikasi telah melalui proses pembersihan yang sama, sehingga mengurangi kesalahan dan inkonsistensi.

Pembersihan data di backend dapat digabungkan dengan validasi data untuk memastikan bahwa data yang diterima sesuai dengan aturan dan keamanan aplikasi.

## Step by step tugas 6
1. Membuat fungsi `add_product_entry_ajax` di `views.py`
```python
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

...
@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    if not request.user.is_authenticated:
        return HttpResponse(b"UNAUTHORIZED", status=401)

    name = strip_tags(request.POST.get("name"))
    price = request.POST.get("price")
    description = strip_tags(request.POST.get("description"))  
    genre = strip_tags(request.POST.get("genre"))
    author = strip_tags(request.POST.get("author"))
    user = request.user

    new_product = Product(
        name=name, 
        price=price,
        description=description,
        genre=genre, 
        author=author,
        user=user  
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)
```
2. Melakukan routing terhadap fungsi `add_product_entry_ajax` di `urls.py`
```python
from main.views import ..., add_mood_entry_ajax

...

path('add-product-ajax/', add_product_entry_ajax, name='add_product_entry_ajax'),
```
3. Modifikasi fungsi `show_main` pada `views.py`
```python
def show_main(request):
    context = {
        'appname' : 'ivans book store',
        'npm' : '2306123456',
        'name': request.user.username,
        'class': 'PBP E',
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "main.html", context)
```
4. Modifikasi fungsi `show_json` dan `show_xml` pada `views.py`
```python
def show_xml(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

5. Memodfikasi `forms.py` agar dapat membersihkan data dengan `strip_tags`
```python
from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "genre", "author"]
    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_genre(self):
        genre = self.cleaned_data["genre"]
        return strip_tags(genre)
    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)
    def clean_author(self):
        author = self.cleaned_data["author"]
        return strip_tags(author)
```
6. Menambahkan script javascript baru pada `main.html` untuk menampilakn data produk, merefresh data produk, menambah data produk, serta melakukan pembersihan data.
7. Tambahkan kode untuk mengaplikasikan tailwind pada aplikasi `Ivans-Book-Store` di `main.htnl`
7. Mengganti bagian conditionals `main.html` untuk menampilkan data produk menjadi
```py
...
<div id="mood_entry_cards"></div>
...
```
8. Tambahkan tombol untuk menambahkan produk menggunakan AJAX
```html
...

<button data-modal-target="crudModal" data-modal-toggle="crudModal" class="btn bg-indigo-700 hover:bg-indigo-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105" onclick="showModal();">
    Add New Product Entry by AJAX
</button>
...
```
9. Terakhir menambahkan error masage pada `login_user` di `views.py`
```py
...
if form.is_valid():
    user = form.get_user()
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main"))
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
else:
    messages.error(request, "Invalid username or password. Please try again.")
...
```











