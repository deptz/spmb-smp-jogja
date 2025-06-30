# Zonasi Daerah SPMB Yogyakarta

A Python tool for monitoring and analyzing junior high school (SMP) admission data in Yogyakarta's regional zoning system (Zonasi Daerah). This tool helps students and parents track admission statistics, quotas, and simulate admission chances based on their scores.

## Features

- **Real-time Data Fetching**: Automatically retrieves admission data from the official SPMB Yogyakarta website
- **Score Analysis**: Analyzes highest and lowest accepted scores for each school
- **Quota Monitoring**: Tracks available slots and remaining quotas
- **Position Simulation**: Simulates where your score would rank among accepted students
- **Safety Assessment**: Determines if your score provides a "safe" chance of admission
- **Multiple Output Formats**: Console table display and Telegram bot integration

## Files Overview

- `zonasi_daerah.py`: Console version that displays results in a markdown table format
- `zonasi_daerah_telegram.py`: Enhanced version that sends formatted results to a Telegram bot/channel

## Requirements

- Python 3.6+
- `requests` library

Install dependencies:
```bash
pip install requests
```

## Configuration

### For Console Version (`zonasi_daerah.py`)

1. Open `zonasi_daerah.py`
2. Replace `YOUR_NILAI_GABUNGAN` with your actual combined score:
   ```python
   NILAI_SIMULASI = 255.5  # Replace with your actual score
   ```

### For Telegram Version (`zonasi_daerah_telegram.py`)

1. Open `zonasi_daerah_telegram.py`
2. Configure the following variables:
   ```python
   NILAI_SIMULASI = 255.5  # Replace with your actual score
   TELEGRAM_TOKEN = "your_bot_token_here"  # Get from @BotFather
   CHAT_ID = "your_chat_id_here"  # Your chat/channel ID
   ```

#### Setting up Telegram Bot

1. Create a new bot by messaging [@BotFather](https://t.me/botfather) on Telegram
2. Use `/newbot` command and follow the instructions
3. Copy the bot token provided by BotFather
4. Get your chat ID by messaging [@userinfobot](https://t.me/userinfobot) or use your channel ID

## Usage

### Console Version
```bash
python zonasi_daerah.py
```

This will display a formatted table showing:
- School names
- Highest and lowest accepted scores
- Quota information
- Your simulated position
- Safety status

### Telegram Version
```bash
python zonasi_daerah_telegram.py
```

This will send formatted messages to your configured Telegram chat/channel with the same information in a mobile-friendly format.

## Output Information

For each school, the tool provides:

| Field | Description |
|-------|-------------|
| **Nama Sekolah** | School name |
| **Nilai Tertinggi** | Highest accepted score |
| **Nilai Terendah** | Lowest accepted score |
| **Kuota** | Total quota/slots available |
| **Diterima** | Number of students already accepted |
| **Sisa Kuota** | Remaining available slots |
| **Simulasi Posisi** | Your simulated ranking position |
| **Aman** | Safety status (✅ safe / ❌ risky) |

## Data Source

The tool fetches data from the official SPMB Yogyakarta website:
- Base URL: `https://yogya.spmb.id/seleksi/zd/smp/`
- Covers schools with codes from 2-22040001-0 to 2-22040016-0

## How It Works

1. **Data Retrieval**: Fetches JSON data from each school's endpoint
2. **Score Analysis**: Processes admission data and calculates statistics
3. **Position Simulation**: Sorts all accepted students by score and finds where your score would rank
4. **Safety Assessment**: Determines if your simulated position is within the quota (safe) or beyond it (risky)
5. **Output Generation**: Formats results for console display or Telegram delivery

## Limitations

- Data availability depends on the SPMB website being accessible
- Only covers junior high schools (SMP) in Yogyakarta's regional zoning system
- Simulation is based on current accepted students and may not reflect final admission results
- Real-time data may change as more students are accepted

## Contributing

Feel free to submit issues and pull requests to improve this tool.

## Disclaimer

This tool is for informational purposes only. Official admission decisions should always be confirmed through the official SPMB Yogyakarta channels. 