import requests

# Simulated score for ranking
NILAI_SIMULASI = YOUR_NILAI_GABUNGAN

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

    # Sort descending by score
    sorted_data = sorted(entries, key=lambda x: float(x[4]), reverse=True)

    # Simulasi rank
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

# Collect results
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

# Print Markdown-style table
header = ["Nama Sekolah", "Nilai Tertinggi", "Nilai Terendah", "Kuota", "Diterima", "Sisa Kuota", "Simulasi Posisi", "Aman"]
print(f"| {' | '.join(header)} |")
print(f"|{'|'.join(['-' * (len(h) + 2) for h in header])}|")
for row in results:
    print(f"| {row['Nama Sekolah']} | {row['Nilai Tertinggi']} | {row['Nilai Terendah']} | {row['Kuota']} | {row['Diterima']} | {row['Sisa Kuota']} | {row['Simulasi Posisi']} | {row['Aman']} ")
