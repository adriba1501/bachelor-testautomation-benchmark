import threading
import time
import csv
import subprocess
import sys
import psutil

N = 100

#Hardware Monitoring
class HardwareMonitorThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.running = True
        self.max_cpu = 0.0
        self.max_ram_mb = 0.0

    def run(self):
        # während TEst läuft, wird alle 0.1 Sekunden gemessen
        while self.running:
            #CPU-Auslastung in %
            cpu = psutil.cpu_percent(interval=None)
            #Arbeitsspeicher (RAM) in Megabyte
            ram = psutil.virtual_memory().used / (1024 * 1024)

            # Nur der Höchswert wird gespeichert
            if cpu > self.max_cpu:
                self.max_cpu = cpu
            if ram > self.max_ram_mb:
                self.max_ram_mb = ram

            time.sleep(0.1)

    def stop(self):
        self.running = False


print(f"Starte das Bachelor_Experiment mit {N} Durchläufen pro Framework..")

with open('benchmark_result.csv', mode='w', newline='') as file:
    writer = csv.writer(file,delimiter='|')
    writer.writerow(['Framework', 'Durchlauf', 'Dauer_Sekunden', 'Max_CPU_%', 'Max_RAM_MB', 'Status'])
    # 1. Messung von Playwright
    print("\n--- Starte Playwright Messungen ---")
    for i in range(1, N + 1):
        #Monitoring starten
        monitor = HardwareMonitorThread()
        monitor.start()

        start_zeit = time.time()
        result = subprocess.run([sys.executable, "-m", "pytest", "tests/test_playwright.py"], capture_output=True)
        end_zeit = time.time()

        # Monitor stoppen
        monitor.stop()
        monitor.join()

        # Zeit ausrechnen und auf 2 Nachkommastellen runden
        dauer = round(end_zeit - start_zeit, 2)
        # Prüfen, ob der Test grün (0) oder rot (Fehler) war
        status = "Pass" if result.returncode == 0 else "Fail"
        cpu_wert = round(monitor.max_cpu, 2)
        ram_wert = round(monitor.max_ram_mb, 2)

        if status == "Fail":
            print(f"  -> Fehler: {result.stderr.decode('utf-8', errors='ignore')}")

        # Ergebnis in die CSV-Datei schreiben
        writer.writerow(['Playwright', i, dauer, cpu_wert, ram_wert, status])
        print(f"Playwright Lauf {i}/{N}: {dauer}s | CPU: {cpu_wert}% | RAM: {ram_wert} MB")
    # 2. Messung von Selenium

    print("\n--- Starte Selenium Messung ---")
    for i in range(1, N + 1):
        monitor = HardwareMonitorThread()
        monitor.start()

        start_zeit = time.time()
        result = subprocess.run(["pytest", "tests/test_selenium.py"], capture_output=True)
        end_zeit = time.time()

        monitor.stop()
        monitor.join()

        dauer = round(end_zeit - start_zeit, 2)
        status = "Pass" if result.returncode == 0 else "Fail"
        cpu_wert = round(monitor.max_cpu, 2)
        ram_wert = round(monitor.max_ram_mb, 2)

        if status == "Fail":
            print(f"  -> Fehler: {result.stderr.decode('utf-8', errors='ignore')}")

        writer.writerow(['Selenium', i, dauer, cpu_wert, ram_wert, status])
        print(f"Selenium Lauf {i}/{N}: {dauer}s | CPU: {cpu_wert}% | RAM: {ram_wert} MB")
    print("\n🎉 Experiment erfolgreich beendet! Die Ergebnisse liegen in der Datei 'benchmark_results.csv'.")
