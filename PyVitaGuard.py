import customtkinter as ctk
import psutil
import os
import sys

# Get icon.ico path
if getattr(sys, 'frozen', False):
    icon_path = os.path.join(sys._MEIPASS, "images", "icon.ico")
else:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    icon_path = os.path.join(script_dir, "images", "icon.ico")

ctk.set_appearance_mode("light")

class PyVitaGuard(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("PyVitaGuard")
        self.geometry("600x475")
        self.resizable(False, False)
        self.iconbitmap(icon_path)
        self.configure(fg_color=("#f3f3f3", "#1a1a1a"))

        # Var for theme of app
        self.dark_mode = False

        # GRID CONFIG
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure((1, 2), weight=0)
        self.grid_rowconfigure(3, weight=1)

        # Actually create all the UI
        self.create_header()
        self.create_hardware()
        self.create_processes()
        self.start_update_loop()

    # Dark mode core logic function!
    def toggle_mode(self):
        if self.dark_mode:
            ctk.set_appearance_mode("light")
            self.mode_btn.configure(text="🌙")
            self.dark_mode = False
        else:
            ctk.set_appearance_mode("dark")
            self.mode_btn.configure(text="☀️")
            self.dark_mode = True

    # Title + dark/light mode btn switch :))
    def create_header(self):
        header_frame = ctk.CTkFrame(
            self,
            height=50,
            width=200,
            fg_color="transparent"
        )
        header_frame.grid(row=1, column=0, columnspan=3, padx=7, pady=(4, 0), sticky="new")
        header_frame.pack_propagate(False)

        self.mode_btn = ctk.CTkButton(
            header_frame,
            height=36,
            width=36,
            fg_color="transparent",
            hover_color=("#e8e8e8", "#3a3a3a"),
            corner_radius=18,
            border_width=2,
            border_color="#6f6e73",
            text="🌙",
            font=("Segoe UI Emoji", 15),
            text_color="#6f6e73",
            command=self.toggle_mode,
            border_spacing=0
        )
        self.mode_btn.pack(side="right", pady=4, padx=2)

        vitaguard_text = ctk.CTkLabel(
            header_frame,
            text="PyVitaGuard",
            text_color=("#05070d", "#f0f0f0"),
            fg_color="transparent",
            font=("Segoe UI", 18, "bold")
        )
        vitaguard_text.pack(anchor="w", pady=(4, 0), padx=3)

        dashboard_text = ctk.CTkLabel(
            header_frame,
            text="DASHBOARD",
            text_color="#6f6e73",
            fg_color="transparent",
            font=("Segoe UI", 12, "bold")
        )
        dashboard_text.pack(anchor="w", pady=(0, 0), padx=3)

    # Hardware stat section
    def create_hardware(self):
        # Hardware frame config
        hardware_fconfig = {
            "fg_color": ("#ffffff", "#2b2b2b"),
            "height": 120,
            "width": 200,
            "corner_radius": 10
        }

        # Hardware percent % frame creation
        cpu_frame = ctk.CTkFrame(self, **hardware_fconfig)
        cpu_frame.grid(row=2, column=0, padx=7, pady=15, sticky="new")
        cpu_frame.pack_propagate(False)

        ram_frame = ctk.CTkFrame(self, **hardware_fconfig)
        ram_frame.grid(row=2, column=1, padx=7, pady=15, sticky="new")
        ram_frame.pack_propagate(False)

        disk_frame = ctk.CTkFrame(self, **hardware_fconfig)
        disk_frame.grid(row=2, column=2, padx=7, pady=15, sticky="new")
        disk_frame.pack_propagate(False)

        # CPU labels
        self.cpu_label = ctk.CTkLabel(
            cpu_frame,
            text="CPU",
            text_color="#6f6e73",
            fg_color="transparent",
            font=("Segoe UI", 14, "bold")
        )
        self.cpu_label.pack(anchor="w", padx=10, pady=(7, 5))

        self.cpu_per_label = ctk.CTkLabel(
            cpu_frame,
            text="68%",
            text_color=("#05070d", "#f0f0f0"),
            fg_color="transparent",
            font=("Segoe UI", 23, "bold"),
            height=28
        )
        self.cpu_per_label.pack(anchor="w", pady=(4, 0), padx=9)

        self.cpu_ghz_label = ctk.CTkLabel(
            cpu_frame,
            text="3.5GHz",
            text_color=("#555557", "#a0a0a0"),
            fg_color="transparent",
            font=("Segoe UI", 12),
            height=16
        )
        self.cpu_ghz_label.pack(anchor="w", pady=(0, 7), padx=13)

        self.cpu_progbar = ctk.CTkProgressBar(
            cpu_frame,
            orientation="horizontal",
            fg_color="#eceefb",
            progress_color="#0b439f",
            height=8
        )
        self.cpu_progbar.pack(fill="x", padx=12, pady=(0, 12))
        self.cpu_progbar.set(0.29)

        # RAM labels
        self.ram_label = ctk.CTkLabel(
            ram_frame,
            text="RAM",
            text_color="#6f6e73",
            fg_color="transparent",
            font=("Segoe UI", 14, "bold")
        )
        self.ram_label.pack(anchor="w", padx=10, pady=(7, 5))

        self.ram_per_label = ctk.CTkLabel(
            ram_frame,
            text="59%",
            text_color=("#05070d", "#f0f0f0"),
            fg_color="transparent",
            font=("Segoe UI", 23, "bold"),
            height=28
        )
        self.ram_per_label.pack(anchor="w", pady=(4, 0), padx=11)

        self.ram_mbusage_label = ctk.CTkLabel(
            ram_frame,
            text="5.35 / 16 GB",
            text_color=("#555557", "#a0a0a0"),
            fg_color="transparent",
            font=("Segoe UI", 12),
            height=16
        )
        self.ram_mbusage_label.pack(anchor="w", pady=(0, 7), padx=12)

        self.ram_progbar = ctk.CTkProgressBar(
            ram_frame,
            orientation="horizontal",
            fg_color="#e8f4f2",
            progress_color="#31acab",
            height=8
        )
        self.ram_progbar.pack(fill="x", padx=12, pady=(0, 12))
        self.ram_progbar.set(0.59)

        # Disk labels
        self.disk_label = ctk.CTkLabel(
            disk_frame,
            text="DISK",
            text_color="#6f6e73",
            fg_color="transparent",
            font=("Segoe UI", 14, "bold")
        )
        self.disk_label.pack(anchor="w", padx=10, pady=(7, 5))

        self.disk_per_label = ctk.CTkLabel(
            disk_frame,
            text="87%",
            text_color=("#05070d", "#f0f0f0"),
            fg_color="transparent",
            font=("Segoe UI", 23, "bold"),
            height=28
        )
        self.disk_per_label.pack(anchor="w", pady=(4, 0), padx=11)

        self.disk_gb_label = ctk.CTkLabel(
            disk_frame,
            text="124 / 953 GB",
            text_color=("#555557", "#a0a0a0"),
            fg_color="transparent",
            font=("Segoe UI", 12),
            height=16
        )
        self.disk_gb_label.pack(anchor="w", pady=(0, 7), padx=12)

        self.disk_progbar = ctk.CTkProgressBar(
            disk_frame,
            orientation="horizontal",
            fg_color="#eaf7f0",
            progress_color="#15a064",
            height=8
        )
        self.disk_progbar.pack(fill="x", padx=12, pady=(0, 12))
        self.disk_progbar.set(0.87)

    # Processes section
    def create_processes(self):
        process_frame = ctk.CTkFrame(
            self,
            fg_color=("#ffffff", "#2b2b2b"),
            height=250,
            width=600,
            corner_radius=10
        )
        process_frame.grid(row=3, column=0, columnspan=3, padx=5, pady=5, sticky="new")
        process_frame.pack_propagate(False)

        process_text_label = ctk.CTkLabel(
            process_frame,
            text="PROCESS LIST",
            text_color=("#5b5a5e", "#a0a0a0"),
            fg_color="transparent",
            font=("Segoe UI", 15, "bold")
        )
        process_text_label.pack(anchor="w", padx=12, pady=(10, 0))

        self.scrollable_processes = ctk.CTkScrollableFrame(
            process_frame,
            fg_color="transparent",
            scrollbar_button_color=("#f0f0f0", "#3a3a3a"),
            scrollbar_button_hover_color=("#e0e0e0", "#4a4a4a"),
            scrollbar_fg_color=("#ffffff", "#2b2b2b")
        )
        self.scrollable_processes.pack(fill="both", expand=True, padx=5, pady=1)

    # Update stat labels with the actual sys info
    def updatestats(self):
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory()
        disk = psutil.disk_usage('/')

        freq = psutil.cpu_freq()
        ghz = freq.current / 1000

        ram_used = ram.used / (1024**3)
        ram_total = ram.total / (1024**3)

        disk_used = disk.used / (1024**3)
        disk_total = disk.total / (1024**3)

        self.cpu_per_label.configure(text=f"{cpu}%")
        self.cpu_progbar.set(cpu / 100)
        self.cpu_ghz_label.configure(text=f"{ghz:.1f}Ghz")

        self.ram_per_label.configure(text=f"{ram.percent}%")
        self.ram_progbar.set(ram.percent / 100)
        self.ram_mbusage_label.configure(text=f"{ram_used:.1f} / {ram_total:.1f} GB")

        self.disk_per_label.configure(text=f"{disk.percent}%")
        self.disk_progbar.set(disk.percent / 100)
        self.disk_gb_label.configure(text=f"{disk_used:.1f} / {disk_total:.1f} GB")

        # Build process list
        process_names = []
        for process in psutil.process_iter():
            try:
                name = process.name()
                memory = process.memory_info().rss
                process_names.append((name, memory))
            except:
                pass

        process_names.sort(key=lambda x: x[1], reverse=True)
        self.update_processes(process_names)

    # Create UI based on array
    def update_processes(self, process_names):
        for widget in self.scrollable_processes.winfo_children():
            widget.destroy()

        for name, memory in process_names[:10]:
            row = ctk.CTkFrame(
                self.scrollable_processes,
                fg_color="transparent",
                border_width=1,
                border_color=("#e0e0e0", "#3a3a3a"),
                height=35
            )
            row.pack(fill="x", pady=2)
            row.pack_propagate(False)

            ctk.CTkLabel(
                row,
                text=name,
                font=("Segoe UI", 13),
                text_color=("#555557", "#a0a0a0")
            ).pack(side="left", padx=10, pady=8)

            ctk.CTkLabel(
                row,
                text=f"{memory / 1024 / 1024:.1f} MB",
                font=("Segoe UI", 13),
                text_color=("#555557", "#a0a0a0")
            ).pack(side="right", padx=10, pady=8)

    # Threading, so UI stays responsive while updating stats. (IMPORTANT!!!)
    def start_update_loop(self):
        import threading
        thread = threading.Thread(target=self.update_loop, daemon=True)
        thread.start()

    def update_loop(self):
        import time
        while True:
            self.updatestats()
            time.sleep(2)


# RUN THE GOSH DARN THING!!
app = PyVitaGuard()
app.mainloop()