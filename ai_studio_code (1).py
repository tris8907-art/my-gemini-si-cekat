import requests
import json

class SiCekatClient:
    def __init__(self, base_url):
        """
        Inisialisasi client dengan URL dasar aplikasi SI-CEKAT.
        """
        self.base_url = base_url

    def get_readiness_report(self):
        """
        Mengambil data laporan kesiapan armada dari API.
        """
        try:
            # Endpoint simulasi API (sesuaikan dengan endpoint backend Anda)
            response = requests.get(f"{self.base_url}/api/reports")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error: Gagal terhubung ke server SI-CEKAT. {e}")
            return None

def display_dashboard(reports):
    """
    Menampilkan data dalam format dashboard sederhana di terminal.
    """
    if not reports:
        print("Data tidak tersedia.")
        return

    print("\n" + "="*50)
    print("   DASHBOARD MONITORING ARMADA DAMKAR SELUMA")
    print("="*50)
    
    for unit in reports:
        status = unit.get('status', 'UNKNOWN')
        icon = "✅" if status == "SIAGA" else "⚠️" if status == "SIAGA TERBATAS" else "❌"
        
        print(f"{icon} Unit: {unit['unitNumber']:<10} | Status: {status:<15}")
        if unit.get('notes'):
            print(f"   Catatan: {unit['notes']}")
    
    print("="*50 + "\n")

if __name__ == "__main__":
    # Ganti dengan URL preview atau URL produksi SI-CEKAT Anda
    BASE_URL = "https://si-cekat.seluma.go.id" 
    
    client = SiCekatClient(BASE_URL)
    data = client.get_readiness_report()
    
    if data:
        display_dashboard(data)