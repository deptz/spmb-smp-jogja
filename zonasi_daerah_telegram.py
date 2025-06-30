import requests

# Configuration
NILAI_SIMULASI = YOUR_NILAI GABUNGAN
TELEGRAM_TOKEN = "YOUR TELEGRAM_TOKEN"
CHAT_ID = "TELEGRAM CHAT_ID"

urls = [
    f"https://yogya.spmb.id/seleksi/zd/smp/2-220400{str(i).zfill(2)}-0.json"
    for i in range(1, 17)
]

def process_school_data(data, nilai_simulasi):
    sekolah_nama = data["sekolah"]["nama"]
    kuota = int(data["jml_pagu"])
    entries = data["data"]

    diterima = len(entries)
    sisa_kuota = kuota - diterima
    nilai_tertinggi = float(entries[0][4]) if entries else None
    nilai_terendah = float(entries[-1][4]) if entries else None

    sorted_data = sorted(entries, key=lambda x: float(x[4]), reverse=True)
    simulasi_rank = next((i + 1 for i, row in enumerate(sorted_data) if float(row[4]) <= nilai_simulasi), diterima + 1)

    return {
        "Nama Sekolah": sekolah_nama,
        "Nilai Tertinggi": nilai_tertinggi,
        "Nilai Terendah": nilai_terendah,
        "Kuota": kuota,
        "Diterima": diterima,
        "Sisa Kuota": sisa_kuota,
        "Simulasi Posisi": simulasi_rank,
        "Aman": simulasi_rank <= kuota
    }

def format_markdown_messages(data):
    messages = []
    current_message = ""
    for row in data:
        line = (
            f"*{row['Nama Sekolah']}*\n"
            f"`Tertinggi : {row['Nilai Tertinggi']}`\n"
            f"`Terendah  : {row['Nilai Terendah']}`\n"
            f"`Kuota     : {row['Kuota']}`\n"
            f"`Diterima  : {row['Diterima']}`\n"
            f"`Sisa Kuota: {row['Sisa Kuota']}`\n"
            f"`Posisi    : {row['Simulasi Posisi']}`\n"
            f"*Status*: {'✅' if row['Aman'] else '❌'}\n"
            f"\n"
        )
        # Telegram limit: 4096 chars/message
        if len(current_message) + len(line) > 4000:
            messages.append(current_message)
            current_message = ""
        current_message += line
    if current_message:
        messages.append(current_message)
    return messages

def send_markdown_messages(messages, token, chat_id):
    for msg in messages:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        response = requests.post(url, data={
            "chat_id": chat_id,
            "text": msg,
            "parse_mode": "Markdown"
        })
        if not response.ok:
            print("Failed to send message:", response.text)

# Run process
results = []
for url in urls:
    try:
        response = requests.get(url)
        if response.ok:
            json_data = response.json()
            summary = process_school_data(json_data, NILAI_SIMULASI)
            results.append(summary)
        else:
            print(f"Failed to fetch {url}: {response.status_code}")
    except Exception as e:
        print(f"Error processing {url}: {e}")

markdown_msgs = format_markdown_messages(results)
send_markdown_messages(markdown_msgs, TELEGRAM_TOKEN, CHAT_ID)
