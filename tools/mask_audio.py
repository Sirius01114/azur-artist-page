from pydub import AudioSegment
import os

def mask_audio(input_path, output_path):
    print(f"Lade Datei: {input_path}")
    audio = AudioSegment.from_wav(input_path)
    
    # 1. Tiefpass-Filter (Low-Pass) bei 500Hz
    # Das entfernt die Klarheit der Stimme (Lyrics), behält aber den Beat.
    print("Wende Tiefpass-Filter an (500Hz)...")
    masked_audio = audio.low_pass_filter(500)
    
    # 2. Leichtes Echo hinzufügen, um Fingerprinting zu verwirren
    print("Füge Verfremdung hinzu...")
    masked_audio = masked_audio.overlay(masked_audio - 10, position=50) # Minimales Delay
    
    # 3. Exportieren
    print(f"Speichere Ergebnis: {output_path}")
    masked_audio.export(output_path, format="wav")
    print("Fertig!")

if __name__ == "__main__":
    input_file = r"D:\GOOGLE ANTIGRAVITY FOLDER\AZUR\Musik\proben\coverchina_moderat.wav"
    output_file = r"D:\GOOGLE ANTIGRAVITY FOLDER\AZUR\Musik\proben\coverchina_masked_AZUR.wav"
    
    if os.path.exists(input_file):
        mask_audio(input_file, output_file)
    else:
        print("Datei nicht gefunden!")
