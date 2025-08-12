import pickle
import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import numpy as np

class PhonePricePredictor:
    def __init__(self, root):
        self.root = root
        self.root.title("📱 Telefon Fiyat Tahmin Uygulaması")
        self.root.geometry("900x750")
        self.root.configure(bg='#f0f0f0')
        
        # Pencereyi öne getir
        self.root.lift()
        self.root.attributes('-topmost', True)
        self.root.attributes('-topmost', False)
        
        # Model ve preprocessor'ı yükle
        try:
            with open("phone_price.pkl", "rb") as f:
                saved_data = pickle.load(f)
                self.model = saved_data["model"]
                self.preprocessor = saved_data["preprocessor"]
        except FileNotFoundError:
            messagebox.showerror("Hata", "Model dosyası bulunamadı! Lütfen phone_price.pkl dosyasının mevcut olduğundan emin olun.")
            return
        except Exception as e:
            messagebox.showerror("Hata", f"Model yüklenirken hata oluştu: {str(e)}")
            return
        
        # Veri setini yükle
        try:
            self.df = pd.read_csv("phone_data.csv")
            self.setup_ui()
        except FileNotFoundError:
            messagebox.showerror("Hata", "Veri dosyası bulunamadı! Lütfen phone_data.csv dosyasının mevcut olduğundan emin olun.")
            return
        except Exception as e:
            messagebox.showerror("Hata", f"Veri seti yüklenirken hata oluştu: {str(e)}")
            return
    
    def setup_ui(self):
        # Ana başlık
        title_frame = tk.Frame(self.root, bg='#2c3e50', height=80)
        title_frame.pack(fill='x', padx=10, pady=10)
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(title_frame, text="📱 TELEFON FİYAT TAHMİN UYGULAMASI", 
                              font=("Arial", 18, "bold"), fg='white', bg='#2c3e50')
        title_label.pack(expand=True)
        
        # Ana form frame
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Sol panel - Giriş alanları
        left_frame = tk.Frame(main_frame, bg='white', relief='raised', bd=2)
        left_frame.pack(side='left', fill='both', expand=True, padx=(0, 10))
        
        # Form başlığı
        form_title = tk.Label(left_frame, text="Telefon Özelliklerini Girin", 
                             font=("Arial", 14, "bold"), bg='white', fg='#2c3e50')
        form_title.pack(pady=20)
        
        # Depolama seçimi
        storage_frame = tk.Frame(left_frame, bg='white')
        storage_frame.pack(fill='x', padx=20, pady=10)
        
        storage_label = tk.Label(storage_frame, text="Depolama (GB):", font=("Arial", 10, "bold"), bg='white')
        storage_label.pack(anchor='w')
        
        storage_values = sorted([32, 64, 128, 256, 512, 1024])
        self.storage_var = tk.StringVar()
        storage_combo = ttk.Combobox(storage_frame, textvariable=self.storage_var, 
                                    values=storage_values, state='readonly', font=("Arial", 10))
        storage_combo.pack(fill='x', pady=5)
        storage_combo.set("Depolama seçin")
        
        # RAM seçimi
        ram_frame = tk.Frame(left_frame, bg='white')
        ram_frame.pack(fill='x', padx=20, pady=10)
        
        ram_label = tk.Label(ram_frame, text="RAM (GB):", font=("Arial", 10, "bold"), bg='white')
        ram_label.pack(anchor='w')
        
        ram_values = sorted([2, 3, 4, 6, 8, 12, 16])
        self.ram_var = tk.StringVar()
        ram_combo = ttk.Combobox(ram_frame, textvariable=self.ram_var, 
                                 values=ram_values, state='readonly', font=("Arial", 10))
        ram_combo.pack(fill='x', pady=5)
        ram_combo.set("RAM seçin")
        
        # Ekran boyutu
        screen_frame = tk.Frame(left_frame, bg='white')
        screen_frame.pack(fill='x', padx=20, pady=10)
        
        screen_label = tk.Label(screen_frame, text="Ekran Boyutu (inch):", font=("Arial", 10, "bold"), bg='white')
        screen_label.pack(anchor='w')
        
        self.screen_var = tk.StringVar()
        screen_entry = tk.Entry(screen_frame, textvariable=self.screen_var, font=("Arial", 10))
        screen_entry.pack(fill='x', pady=5)
        screen_entry.insert(0, "6.1")
        
        # Kamera sayısı
        camera_count_frame = tk.Frame(left_frame, bg='white')
        camera_count_frame.pack(fill='x', padx=20, pady=10)
        
        camera_count_label = tk.Label(camera_count_frame, text="Kamera Sayısı:", font=("Arial", 10, "bold"), bg='white')
        camera_count_label.pack(anchor='w')
        
        camera_count_values = [1, 2, 3, 4, 5]
        self.camera_count_var = tk.StringVar()
        camera_count_combo = ttk.Combobox(camera_count_frame, textvariable=self.camera_count_var, 
                                         values=camera_count_values, state='readonly', font=("Arial", 10))
        camera_count_combo.pack(fill='x', pady=5)
        camera_count_combo.set("Kamera sayısı seçin")
        
        # Toplam MP
        total_mp_frame = tk.Frame(left_frame, bg='white')
        total_mp_frame.pack(fill='x', padx=20, pady=10)
        
        total_mp_label = tk.Label(total_mp_frame, text="Toplam Kamera MP:", font=("Arial", 10, "bold"), bg='white')
        total_mp_label.pack(anchor='w')
        
        self.total_mp_var = tk.StringVar()
        total_mp_entry = tk.Entry(total_mp_frame, textvariable=self.total_mp_var, font=("Arial", 10))
        total_mp_entry.pack(fill='x', pady=5)
        total_mp_entry.insert(0, "48")
        
        # Batarya kapasitesi
        battery_frame = tk.Frame(left_frame, bg='white')
        battery_frame.pack(fill='x', padx=20, pady=10)
        
        battery_label = tk.Label(battery_frame, text="Batarya Kapasitesi (mAh):", font=("Arial", 10, "bold"), bg='white')
        battery_label.pack(anchor='w')
        
        self.battery_var = tk.StringVar()
        battery_entry = tk.Entry(battery_frame, textvariable=self.battery_var, font=("Arial", 10))
        battery_entry.pack(fill='x', pady=5)
        battery_entry.insert(0, "4500")
        
        # Tahmin butonu - Daha belirgin ve büyük
        button_frame = tk.Frame(left_frame, bg='white')
        button_frame.pack(fill='x', padx=20, pady=30)
        
        predict_button = tk.Button(button_frame, text="🚀 FİYAT TAHMİNİ YAP", 
                                  command=self.predict_price, bg='#e74c3c', fg='white',
                                  font=("Arial", 14, "bold"), relief='raised', 
                                  padx=30, pady=15, cursor='hand2')
        predict_button.pack(fill='x')
        
        # Buton hover efekti
        def on_enter(e):
            predict_button['bg'] = '#c0392b'
        def on_leave(e):
            predict_button['bg'] = '#e74c3c'
        
        predict_button.bind("<Enter>", on_enter)
        predict_button.bind("<Leave>", on_leave)
        
        # Sağ panel - Sonuçlar ve istatistikler
        right_frame = tk.Frame(main_frame, bg='white', relief='raised', bd=2)
        right_frame.pack(side='right', fill='both', expand=True, padx=(10, 0))
        
        # Sonuç başlığı
        result_title = tk.Label(right_frame, text="Tahmin Sonucu", 
                               font=("Arial", 14, "bold"), bg='white', fg='#2c3e50')
        result_title.pack(pady=20)
        
        # Sonuç alanı
        self.result_frame = tk.Frame(right_frame, bg='#ecf0f1', relief='sunken', bd=2)
        self.result_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        self.result_label = tk.Label(self.result_frame, text="Telefon özelliklerini girip\n'FİYAT TAHMİNİ YAP' butonuna tıklayın", 
                                    font=("Arial", 12), bg='#ecf0f1', fg='#7f8c8d', justify='center')
        self.result_label.pack(expand=True)
        
        # İstatistikler
        stats_frame = tk.Frame(right_frame, bg='white')
        stats_frame.pack(fill='x', padx=20, pady=20)
        
        stats_title = tk.Label(stats_frame, text="Veri Seti İstatistikleri", 
                              font=("Arial", 12, "bold"), bg='white', fg='#2c3e50')
        stats_title.pack(anchor='w', pady=(0, 10))
        
        # Fiyat aralığı
        try:
            price_range = f"Fiyat Aralığı: ${self.df['Price ($)'].str.replace('$', '').str.replace(',', '').astype(float).min():.0f} - ${self.df['Price ($)'].str.replace('$', '').str.replace(',', '').astype(float).max():.0f}"
        except:
            price_range = "Fiyat Aralığı: Bilgi mevcut değil"
        price_label = tk.Label(stats_frame, text=price_range, font=("Arial", 9), bg='white')
        price_label.pack(anchor='w')
        
        # Toplam model sayısı
        total_models = f"Toplam Model Sayısı: {len(self.df)}"
        models_label = tk.Label(stats_frame, text=total_models, font=("Arial", 9), bg='white')
        models_label.pack(anchor='w')
        
        # Marka sayısı
        brand_count = f"Marka Sayısı: {len(self.df['Brand'].unique())}"
        brands_count_label = tk.Label(stats_frame, text=brand_count, font=("Arial", 9), bg='white')
        brands_count_label.pack(anchor='w')
    
    def predict_price(self):
        try:
            # Giriş değerlerini al
            storage = self.storage_var.get()
            ram = self.ram_var.get()
            screen_size = float(self.screen_var.get())
            camera_count = self.camera_count_var.get()
            total_mp = self.total_mp_var.get()
            battery = int(self.battery_var.get())
            
            # Validasyon
            if storage == "Depolama seçin" or ram == "RAM seçin" or camera_count == "Kamera sayısı seçin":
                messagebox.showwarning("Uyarı", "Lütfen tüm alanları doldurun!")
                return
            
            # Veri hazırlama (model formatına uygun)
            input_data = pd.DataFrame({
                'Storage (GB)': [storage],
                'RAM (GB)': [ram],
                'Screen Size (inches)': [screen_size],
                'Camera Count': [camera_count],
                'Total MP': [total_mp],
                'Battery Capacity (mAh)': [battery]
            })
            
            # Preprocessor ile veriyi dönüştür
            input_transformed = self.preprocessor.transform(input_data)
            
            # Tahmin yap
            prediction = self.model.predict(input_transformed)[0]
            
            # Sonucu göster
            result_text = f"📱 Tahmin Edilen Fiyat:\n\n${prediction:,.2f}\n\n"
            result_text += f"Depolama: {storage} GB\n"
            result_text += f"RAM: {ram} GB\n"
            result_text += f"Ekran: {screen_size} inch\n"
            result_text += f"Kamera Sayısı: {camera_count}\n"
            result_text += f"Toplam MP: {total_mp}\n"
            result_text += f"Batarya: {battery} mAh"
            
            self.result_label.config(text=result_text, fg='#27ae60', font=("Arial", 11, "bold"))
            
        except ValueError as e:
            messagebox.showerror("Hata", "Lütfen geçerli sayısal değerler girin!")
        except Exception as e:
            messagebox.showerror("Hata", f"Tahmin sırasında bir hata oluştu: {str(e)}")

def main():
    root = tk.Tk()
    app = PhonePricePredictor(root)
    root.mainloop()

if __name__ == "__main__":
    main()