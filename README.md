# 🛡️ Proxy Scraper dan Validator

Proyek ini menyediakan skrip Python untuk mengumpulkan dan memvalidasi proxy HTTP dari berbagai sumber. Skrip ini mendukung penggunaan serentak dan dilengkapi dengan antarmuka baris perintah (CLI) untuk kemudahan penggunaan.

## ✨ Fitur

- 🕵️ Mengumpulkan proxy dari berbagai sumber.
- ✅ Memvalidasi proxy dengan memeriksa konektivitas mereka ke Google.
- ⚙️ Dapat dikonfigurasi melalui berkas YAML.
- 🚀 Mendukung penggunaan serentak untuk mempercepat validasi.
- 📜 Mencatat kemajuan dan kesalahan ke dalam berkas log.
- 🐳 Dockerized untuk kemudahan penyebaran.

## 🛠️ Konfigurasi

Berkas konfigurasi `config.yaml` memungkinkan Anda untuk menentukan sumber proxy, user agent, batas penggunaan serentak, dan pengaturan lainnya.

```yaml
# Berkas konfigurasi untuk proxy scraper

# Sumber proxy untuk scraping
proxy_sources:
  - "https://www.sslproxies.org/"
  - "https://free-proxy-list.net/"
  - "https://www.proxy-list.download/api/v1/get?type=http"
  - "https://www.proxynova.com/proxy-server-list/"
  - "https://www.us-proxy.org/"
  - "https://www.socks-proxy.net/"
  - "https://www.my-proxy.com/free-proxy-list.html"

# Daftar User Agent untuk permintaan berputar
user_agents:
  - "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
  - "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"
  - "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0"
  - "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
  - "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
  - "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15"
  - "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
  - "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"
  - "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0"

# Batas penggunaan serentak untuk memvalidasi proxy
concurrency_limit: 100

# Pengaturan timeout untuk permintaan (dalam detik)
request_timeout: 10
validation_timeout: 5

# Pengaturan retry
max_retries: 3
retry_backoff_factor: 2

# Berkas output untuk proxy valid
output_file: "valid_proxies.txt"

# Konfigurasi logging
log_file: "proxy_scraper.log"
log_level: "INFO"
```

## 🏃‍♂️ Penggunaan

### Menjalankan Secara Lokal

1. **Instal Dependensi:**

    ```sh
    pip install -r requirements.txt
    ```

2. **Jalankan Skrip:**

    ```sh
    python proxy_scraper.py --config config.yaml
    ```

### Menjalankan dengan Docker

1. **Bangun Gambar Docker:**

    ```sh
    docker build -t proxy-scraper .
    ```

2. **Jalankan Kontainer Docker:**

    ```sh
    docker run -v $(pwd):/app proxy-scraper
    ```

## 👥 Kontributor

Kami mengundang siapa saja yang tertarik untuk berkontribusi dalam proyek ini. Kontributor utama untuk proyek ini adalah:

- **Dekurity** - Pengembang utama dan pemelihara proyek.

Jika Anda ingin berkontribusi, silakan ajukan pull request atau buka isu di repository ini.
