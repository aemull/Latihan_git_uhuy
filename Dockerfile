# Gunakan image Python sebagai dasar
FROM python:3.8-slim

# Menetapkan direktori kerja di dalam container
WORKDIR /app

# Menyalin file requirements.txt ke container
COPY requirements.txt .

# Menginstal dependencies dari requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Menyalin semua file dari direktori kerja host ke container
COPY . .

# Mengekspos port yang digunakan oleh Streamlit
EXPOSE 8501

# Menjalankan aplikasi Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501"]
