import os
import json
import platform
import webbrowser
import zipfile
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

CONFIG_FILE = os.path.join(os.path.expanduser("~"), ".sims4_manager.json")
KRISTINA_MEDIAFIRE = "https://www.mediafire.com/folder/3sc6iawzv7ysu/TS4+Resources"
YOUTUBE_LINK = "https://www.youtube.com/@KristinaPlaysTheSims"
LEUANS_SERVER = "https://discord.gg/G7eMu58YAK"
MELON_ARCHIVE = "https://gofile.io/d/VqC3pX"

_SYS = platform.system()
FONT = "Helvetica Neue" if _SYS == "Darwin" else ("Segoe UI" if _SYS == "Windows" else "DejaVu Sans")

C = {
    "bg":           "#ffd6ea",
    "fg":           "#000000",
    "accent":       "#ff4daf",
    "accent_h":     "#ff63ac",
    "error":        "#fc728d",
    "success":      "#8fffa3",
    "warning":      "#fcc46f",
    "card":         "#ff91ca",
    "border":       "#e84a9e",
    "muted":        "#050505",
    "desc":         "#050505",
}

PAD = 28   # horizontal page padding

# ==================== TRANSLATIONS ====================
T = {
    "es": {
        "title": "The Sims 4 - Content Manager (Original by Leuan)",
        "language": "Idioma",
        "select_folder": "Seleccionar carpeta",
        "path_label": "Ruta del juego:",
        "start": "Iniciar instalación",
        "mode_select": "Modo de instalación",
        "mode_single": "Instalar un archivo",
        "mode_all": "Instalar todos los DLCs",
        "mode_offline": "Modo Offline (backup)",
        "step_1": "Paso 1 — Descarga el archivo",
        "step_1_desc": "Haz clic en el botón de abajo para abrir el enlace de descarga y descargar el archivo .zip.",
        "step_2": "Paso 2 — Selecciona el archivo .zip",
        "step_2_desc": "Una vez descargado, haz clic en el botón y elige el archivo .zip.",
        "step_3": "Paso 3 — Selecciona la carpeta del juego",
        "step_3_desc": "Haz clic en el botón y elige la carpeta donde está instalado The Sims 4.",
        "dlc_steps_1": "Paso 1 — Descarga todos los DLCs",
        "dlc_steps_1_desc": "Haz clic en el botón y descarga TODOS los archivos .zip de DLC.",
        "dlc_steps_2": "Paso 2 — Guárdalos en una sola carpeta",
        "dlc_steps_2_desc": "Guarda TODOS los archivos .zip descargados dentro de UNA SOLA CARPETA en tu computadora.",
        "dlc_steps_3": "Paso 3 — Selecciona la carpeta de DLCs",
        "dlc_steps_3_desc": "Haz clic en el botón y elige la carpeta donde guardaste todos los .zip.",
        "dlc_steps_4": "Paso 4 — Selecciona la carpeta del juego",
        "dlc_steps_4_desc": "Haz clic en el botón y elige la carpeta donde está instalado The Sims 4.",
        "offline_title": "Modo Offline",
        "offline_desc": "Instala directamente desde tu backup local. No necesitas internet ni enlaces de descarga.",
        "offline_step_1": "Paso 1 — Selecciona la carpeta de backup",
        "offline_step_1_desc": "Elige la carpeta donde guardaste todos tus archivos .zip de backup.",
        "offline_step_2": "Paso 2 — Selecciona la carpeta del juego",
        "offline_step_2_desc": "Elige la carpeta donde está instalado The Sims 4.",
        "zip_label": "Archivo .zip seleccionado:",
        "dlc_folder_label": "Carpeta de DLCs:",
        "backup_label": "Carpeta de backup:",
        "zip_ph": "Ningún archivo seleccionado",
        "path_ph": "Ninguna ruta seleccionada",
        "folder_ph": "Ninguna carpeta seleccionada",
        "backup_ph": "No configurado aún",
        "open_link": "🌐  Abrir enlace de descarga",
        "browse_dlcs": "📁  Explorar carpeta DLC",
        "browse_game": "📂  Seleccionar carpeta del juego",
        "browse_zip": "📄  Seleccionar archivo .zip",
        "browse_backup": "📦  Seleccionar carpeta de backup",
        "install_all": "⚙️  Instalar todos los DLCs",
        "install_from_backup": "⚙️  Instalar desde backup",
        "error": "Error",
        "success": "Éxito",
        "invalid_path": "❌ Ruta inválida.\n\nVe a la carpeta de The Sims 4 y selecciónala.",
        "no_zip": "❌ No seleccionaste ningún archivo .zip.\n\nDescarga el archivo y luego selecciónalo.",
        "invalid_zip": "❌ El archivo está corrupto o no es un .zip válido.\n\nVuelve a descargarlo.",
        "success_msg": "✓ Contenido instalado correctamente.",
        "no_path": "❌ No seleccionaste la carpeta del juego.",
        "no_dlc_folder": "❌ No seleccionaste la carpeta de DLCs.\n\nElige la carpeta donde guardaste los archivos .zip.",
        "no_zips_found": "❌ No se encontraron archivos .zip en esa carpeta.\n\nAsegúrate de haber puesto los archivos ahí.",
        "no_backup_path": "❌ No tienes un backup configurado.\n\nPrimero selecciona la carpeta de backup.",
        "backup_empty": "❌ La carpeta de backup no contiene archivos .zip.",
        "installed_msg": "✓ {count} DLC(s) instalado(s) correctamente.",
        "failed_msg": "⚠ {count} archivo(s) con error.",
        "ask_backup_title": "¿Crear backup offline?",
        "ask_backup_msg": (
            "El contenido se instaló correctamente.\n\n"
            "¿Quieres configurar un backup offline permanente?\n\n"
            "Con esto nunca necesitarás volver a descargar los DLCs. "
            "Podrás reinstalar todo en cualquier momento, sin internet."
        ),
        "backup_win_title": "Configurar Backup Offline",
        "backup_what_title": "¿Qué es el Backup Offline?",
        "backup_what_text": (
            "El Backup Offline es una copia permanente de todos tus DLCs guardada en un lugar "
            "seguro que TÚ controlas: un disco externo, un USB, Google Drive, etc.\n\n"
            "Una vez configurado, esta aplicación NUNCA más necesitará los enlaces de descarga. "
            "Todo el proceso será 100% local y offline.\n\n"
            "Solo necesitas descargar los archivos UNA VEZ. Si cuidas bien tu backup, "
            "tienes los DLCs garantizados para siempre."
        ),
        "backup_how_title": "¿Cómo funciona?",
        "backup_how_text": (
            "1.  Guardas todos los archivos .zip que descargaste en una carpeta dedicada "
            "(disco externo, USB, Google Drive, Dropbox, etc.).\n\n"
            "2.  Le indicas a esta app dónde está esa carpeta.\n\n"
            "3.  La próxima vez que necesites instalar, usas el Modo Offline y la app "
            "lee directamente de tu backup. Sin internet, sin links, sin esperas."
        ),
        "backup_storage_title": "Espacio necesario",
        "backup_storage_text": (
            "Necesitarás aproximadamente 50 GB de espacio libre. Puedes guardarlo en:\n\n"
            "  •  USB de 64 GB o más\n"
            "  •  Disco duro o SSD externo\n"
            "  •  Google Drive / Dropbox / OneDrive\n"
            "  •  Una carpeta en un segundo disco interno\n"
            "  •  Cualquier lugar accesible desde este computador"
        ),
        "backup_warning_title": "⚠  ADVERTENCIA IMPORTANTE",
        "backup_warning_text": (
            "NO pierdas, borres ni muevas la carpeta de backup sin actualizar la app.\n\n"
            "Si pierdes tu USB o disco de backup, tendrás que descargar TODOS los DLCs "
            "desde cero (~50 GB). Los links de descarga pueden caducar o desaparecer, "
            "así que tu backup puede ser tu ÚNICA forma de recuperar los archivos.\n\n"
            "Guárdalo en un lugar seguro. Considera tener una copia en 2 lugares distintos."
        ),
        "backup_setup_title": "Selecciona la ubicación del backup",
        "backup_setup_desc": (
            "Elige la carpeta donde tienes (o tendrás) todos los archivos .zip. "
            "Asegúrate de que la carpeta contenga TODOS los archivos antes de continuar."
        ),
        "backup_current_label": "Carpeta seleccionada:",
        "save_backup": "✓  Guardar y activar Modo Offline",
        "backup_saved_msg": "✓ Backup configurado correctamente.\nYa puedes usar el Modo Offline.",
        "backup_cancel": "Cancelar",
    },
    "en": {
        "title": "The Sims 4 - Content Manager (Original by Leuan)",
        "language": "Language",
        "select_folder": "Select folder",
        "path_label": "Game Path:",
        "start": "Start Installation",
        "mode_select": "Installation Mode",
        "mode_single": "Install single file",
        "mode_all": "Install all DLCs",
        "mode_offline": "Offline Mode (backup)",
        "step_1": "Step 1 — Download the file",
        "step_1_desc": "Click the button below to open the download link and get the .zip file.",
        "step_2": "Step 2 — Select the .zip file",
        "step_2_desc": "Once downloaded, click the button and choose your .zip file.",
        "step_3": "Step 3 — Select the game folder",
        "step_3_desc": "Click the button and choose the folder where The Sims 4 is installed.",
        "dlc_steps_1": "Step 1 — Download all DLCs",
        "dlc_steps_1_desc": "Click the button below to open the download page and get ALL the DLC .zip files.",
        "dlc_steps_2": "Step 2 — Save them in one folder",
        "dlc_steps_2_desc": "Put ALL the downloaded .zip files inside ONE SINGLE FOLDER on your computer.",
        "dlc_steps_3": "Step 3 — Select the DLC folder",
        "dlc_steps_3_desc": "Click the button and choose the folder where you saved all the .zip files.",
        "dlc_steps_4": "Step 4 — Select the game folder",
        "dlc_steps_4_desc": "Click the button and choose the folder where The Sims 4 is installed.",
        "offline_title": "Offline Mode",
        "offline_desc": "Install directly from your local backup. No internet or download links needed.",
        "offline_step_1": "Step 1 — Select your backup folder",
        "offline_step_1_desc": "Choose the folder where you saved all your backup .zip files.",
        "offline_step_2": "Step 2 — Select the game folder",
        "offline_step_2_desc": "Choose the folder where The Sims 4 is installed.",
        "zip_label": "Selected .zip file:",
        "dlc_folder_label": "DLC Folder:",
        "backup_label": "Backup folder:",
        "zip_ph": "No file selected",
        "path_ph": "No path selected",
        "folder_ph": "No folder selected",
        "backup_ph": "Not configured yet",
        "open_link": "🌐  Open download link",
        "browse_dlcs": "📁  Browse DLC Folder",
        "browse_game": "📂  Select game folder",
        "browse_zip": "📄  Select .zip file",
        "browse_backup": "📦  Select backup folder",
        "install_all": "⚙️  Install all DLCs",
        "install_from_backup": "⚙️  Install from Backup",
        "error": "Error",
        "success": "Success",
        "invalid_path": "❌ Invalid path.\n\nGo to The Sims 4 folder and select it.",
        "no_zip": "❌ No .zip file selected.\n\nDownload the file first, then select it.",
        "invalid_zip": "❌ File is corrupted or not a valid .zip.\n\nPlease re-download it.",
        "success_msg": "✓ Content installed successfully.",
        "no_path": "❌ No game folder selected.",
        "no_dlc_folder": "❌ No DLC folder selected.\n\nChoose the folder containing your .zip files.",
        "no_zips_found": "❌ No .zip files found in that folder.\n\nMake sure you placed the files there.",
        "no_backup_path": "❌ No backup configured.\n\nFirst select a backup folder.",
        "backup_empty": "❌ The backup folder contains no .zip files.",
        "installed_msg": "✓ {count} DLC(s) installed successfully.",
        "failed_msg": "⚠ {count} file(s) failed.",
        "ask_backup_title": "Create Offline Backup?",
        "ask_backup_msg": (
            "Content installed successfully!\n\n"
            "Would you like to set up a permanent offline backup?\n\n"
            "With this you will NEVER need to download the DLCs again. "
            "You can reinstall everything at any time, with no internet required."
        ),
        "backup_win_title": "Set Up Offline Backup",
        "backup_what_title": "What is Offline Backup?",
        "backup_what_text": (
            "The Offline Backup is a permanent copy of all your DLCs stored in a safe place "
            "that YOU control: an external drive, USB stick, Google Drive, etc.\n\n"
            "Once configured, this app will NEVER need download links again. "
            "The entire process becomes 100% local and offline.\n\n"
            "You only need to download the files ONCE. As long as you keep your backup safe, "
            "your DLCs are guaranteed forever."
        ),
        "backup_how_title": "How does it work?",
        "backup_how_text": (
            "1.  You save all the .zip files you downloaded into a dedicated folder "
            "(external drive, USB stick, Google Drive, Dropbox, etc.).\n\n"
            "2.  You tell this app where that folder is.\n\n"
            "3.  Next time you need to install, use Offline Mode and the app reads "
            "directly from your backup. No internet, no links, no waiting."
        ),
        "backup_storage_title": "Storage Requirements",
        "backup_storage_text": (
            "You will need approximately 50 GB of free space. You can store it on:\n\n"
            "  •  USB stick (64 GB or larger)\n"
            "  •  External hard drive or SSD\n"
            "  •  Google Drive / Dropbox / OneDrive\n"
            "  •  A folder on a second internal drive\n"
            "  •  Any location accessible from this computer"
        ),
        "backup_warning_title": "⚠  IMPORTANT WARNING",
        "backup_warning_text": (
            "Do NOT lose, delete, or move the backup folder without updating this app.\n\n"
            "If you lose your USB drive or backup folder, you will have to re-download "
            "ALL DLCs from scratch (~50 GB). Download links may expire or disappear over time, "
            "making your backup your ONLY way to recover the files.\n\n"
            "Keep it somewhere safe. Consider keeping a copy in 2 different locations."
        ),
        "backup_setup_title": "Select backup location",
        "backup_setup_desc": (
            "Choose the folder where you have (or will have) all the .zip files saved. "
            "Make sure the folder contains ALL the files before continuing."
        ),
        "backup_current_label": "Selected folder:",
        "save_backup": "✓  Save & Enable Offline Mode",
        "backup_saved_msg": "✓ Backup configured.\nYou can now use Offline Mode anytime.",
        "backup_cancel": "Cancel",
    },
}

SIMS4_DLCS = [
    "Life of the Party Digital Content", "Up All Night Digital Content",
    "Digital Deluxe Upgrade", "The Sims™ 4 Holiday Celebration Pack",
    "The Sims™ 4 Outdoor Retreat", "The Sims™ 4 Get to Work",
    "The Sims™ 4 Luxury Party Stuff", "The Sims™ 4 Perfect Patio Stuff",
    "The Sims™ 4 Spa Day", "The Sims™ 4 Cool Kitchen Stuff",
    "The Sims™ 4 Spooky Stuff", "The Sims™ 4 Get Together",
    "The Sims™ 4 Movie Hangout Stuff", "The Sims™ 4 Romantic Garden Stuff",
    "The Sims™ 4 Dine Out", "The Sims™ 4 Kids Room Stuff",
    "The Sims™ 4 Backyard Stuff", "The Sims™ 4 City Living",
    "The Sims™ 4 Vintage Glamour Stuff", "The Sims™ 4 Vampires",
    "The Sims™ 4 Bowling Night Stuff", "The Sims™ 4 Parenthood",
    "The Sims™ 4 Fitness Stuff", "The Sims™ 4 Toddler Stuff",
    "The Sims™ 4 Cats & Dogs", "The Sims™ 4 Laundry Day Stuff",
    "The Sims™ 4 Jungle Adventure", "The Sims™ 4 My First Pet Stuff",
    "The Sims™ 4 Seasons", "The Sims™ 4 Get Famous",
    "The Sims™ 4 StrangerVille", "The Sims™ 4 Island Living",
    "The Sims™ 4 Moschino Stuff Pack", "The Sims™ 4 Realm of Magic",
    "The Sims™ 4 Discover University", "The Sims™ 4 Tiny Living",
    "The Sims™ 4 Eco Lifestyle", "The Sims™ 4 Nifty Knitting Stuff Pack",
    "The Sims™ 4 STAR WARS™: Journey to Batuu Game Pack", "The Sims™ 4 Snowy Escape",
    "The Sims™ 4 Paranormal Stuff Pack", "The Sims™ 4 Throwback Fit Kit",
    "The Sims™ 4 Country Kitchen Kit", "The Sims™ 4 Bust the Dust Kit",
    "The Sims™ 4 Courtyard Oasis Kit", "The Sims™ 4 Dream Home Decorator",
    "The Sims™ 4 Cottage Living", "The Sims™ 4 Industrial Loft Kit",
    "The Sims™ 4 Fashion Street Kit", "The Sims™ 4 Incheon Arrivals Kit",
    "The Sims™ 4 Blooming Rooms Kit", "The Sims™ 4 Modern Menswear Kit",
    "The Sims™ 4 Carnaval Streetwear Kit", "The Sims™ 4 My Wedding Stories",
    "The Sims™ 4 Décor to the Max Kit", "The Sims™ 4 Moonlight Chic Kit",
    "The Sims™ 4 Little Campers Kit", "The Sims™ 4 Werewolves",
    "The Sims™ 4 High School Years", "The Sims™ 4 First Fits Kit",
    "The Sims™ 4 Desert Luxe Kit", "The Sims™ 4 Pastel Pop Kit",
    "The Sims™ 4 Everyday Clutter Kit", "The Sims™ 4 Simtimates Collection Kit",
    "The Sims™ 4 Bathroom Clutter Kit", "The Sims™ 4 Growing Together",
    "The Sims™ 4 Greenhouse Haven Kit", "The Sims™ 4 Basement Treasures Kit",
    "The Sims™ 4 Grunge Revival Kit", "The Sims™ 4 Book Nook Kit",
    "The Sims™ 4 Horse Ranch", "The Sims™ 4 Poolside Splash Kit",
    "The Sims™ 4 Modern Luxe Kit", "The Sims™ 4 Home Chef Hustle Stuff Pack",
    "The Sims™ 4 For Rent", "The Sims™ 4 Castle Estate Kit",
    "The Sims™ 4 Goth Galore Kit", "The Sims™ 4 Crystal Creations Stuff Pack",
    "The Sims™ 4 Urban Homage Kit", "The Sims™ 4 Party Essentials Kit",
    "The Sims™ 4 Riviera Retreat Kit", "The Sims™ 4 Cozy Bistro Kit",
    "The Sims™ 4 Lovestruck", "The Sims™ 4 Artist Studio Kit",
    "The Sims™ 4 Storybook Nursery Kit", "The Sims™ 4 Life & Death",
    "The Sims™ 4 Sweet Slumber Party Kit", "The Sims™ 4 Cozy Kitsch Kit",
    "The Sims™ 4 Comfy Gamer Kit", "The Sims™ 4 Secret Sanctuary Kit",
    "The Sims™ 4 Casanova Cave Kit", "The Sims™ 4 Refined Living Room Kit",
    "The Sims™ 4 Business Chic Kit", "The Sims™ 4 Businesses & Hobbies",
    "The Sims™ 4 Sleek Bathroom Kit", "The Sims™ 4 Sweet Allure Kit",
    "The Sims™ 4 Restoration Workshop Kit", "The Sims™ 4 Kitchen Clutter Kit",
    "The Sims™ 4 Golden Years Kit", "The Sims™ 4 Enchanted by Nature Expansion Pack",
    "The Sims™ 4 Essential Glam Kit", "The Sims™ 4 Grange Mudroom Kit",
    "The Sims™ 4 Adventure Awaits Expansion Pack", "The Sims™ 4 Autumn Apparel Kit",
    "The Sims™ 4 Modern Retreat Kit", "The Sims™ 4 Garden to Table Kit",
    "The Sims™ 4 SpongeBob's House Kit", "The Sims™ 4 SpongeBob Kid's Room Kit",
    "The Sims™ 4 Prairie Dreams Kit", "The Sims™ 4 Royalty & Legacy Grand Bundle",
    "The Sims™ 4 Silver Screen Style Kit", "The Sims™ 4 Tea Time Solarium Kit",
    "The Sims™ 4 Wonderland Playroom Kit", "The Sims™ 4 Yard Charm (Creator) Kit",
    "Readers Nook", "The Sims™ 4 Lady Bridgerton's Masquerade Ballroom Kit",
    "The Sims™ 4 Lady Bridgerton's Masquerade Ball Fashion Kit",
]


# ==================== APP ====================
class App:
    def __init__(self, root):
        self.root = root
        self.lang = "en"
        self.mode = "single"
        self.zip_path = None
        self.game_path = None
        self.dlc_folder = None
        self.backup_path = None

        self.lang_var = tk.StringVar(value="en")
        self.mode_var = tk.StringVar(value="single")

        self._load_config()
        self._setup_window()
        self._setup_styles()
        self._setup_scroll()
        self._build()

    # ── Config ──────────────────────────────────────────────────────
    def _load_config(self):
        try:
            with open(CONFIG_FILE, encoding="utf-8") as f:
                self.backup_path = json.load(f).get("backup_path")
        except Exception:
            pass

    def _save_config(self):
        try:
            with open(CONFIG_FILE, "w", encoding="utf-8") as f:
                json.dump({"backup_path": self.backup_path}, f, ensure_ascii=False)
        except Exception:
            pass

    # ── Window ──────────────────────────────────────────────────────
    def _setup_window(self):
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        w = max(min(int(sw * 0.52), 960), 720)
        h = max(min(int(sh * 0.80), 820), 560)
        x = (sw - w) // 2
        y = (sh - h) // 2
        self.root.geometry(f"{w}x{h}+{x}+{y}")
        self.root.minsize(580, 500)
        self.root.title(T[self.lang]["title"])
        self.root.configure(bg=C["bg"])

    # ── Styles ──────────────────────────────────────────────────────
    def _setup_styles(self):
        s = ttk.Style()
        s.theme_use("clam")
        s.configure("TFrame",      background=C["bg"])
        s.configure("Card.TFrame", background=C["card"])
        s.configure("TLabel",      background=C["bg"], foreground=C["fg"], font=(FONT, 10))
        s.configure("TRadiobutton",background=C["bg"], foreground=C["fg"], font=(FONT, 10))
        s.configure("TScrollbar",  background=C["card"], troughcolor=C["bg"], borderwidth=0)
        s.configure("TButton",
                    background=C["card"], foreground=C["fg"],
                    font=(FONT, 10), padding=(12, 9), borderwidth=1,
                    relief="flat")
        s.map("TButton",
              background=[("active", C["accent"])],
              foreground=[("active", "#ffffff")])
        s.configure("Accent.TButton",
                    background=C["accent"], foreground="#ffffff",
                    font=(FONT, 11, "bold"), padding=(12, 11))
        s.map("Accent.TButton",
              background=[("active", C["accent_h"])])

    # ── Scroll area ─────────────────────────────────────────────────
    def _setup_scroll(self):
        self._canvas = tk.Canvas(self.root, bg=C["bg"], highlightthickness=0)
        self._sb = ttk.Scrollbar(self.root, orient="vertical", command=self._canvas.yview)
        self._canvas.configure(yscrollcommand=self._sb.set)

        # inner page — plain tk.Frame so bg works correctly
        self._page = tk.Frame(self._canvas, bg=C["bg"])
        self._win_id = self._canvas.create_window((0, 0), window=self._page, anchor="nw")

        # keep inner frame width == canvas width
        self._canvas.bind("<Configure>",
                          lambda e: self._canvas.itemconfigure(self._win_id, width=e.width))
        # update scroll region when content grows/shrinks
        self._page.bind("<Configure>",
                        lambda *_: self._canvas.configure(scrollregion=self._canvas.bbox("all")))

        # mousewheel — cross-platform
        def _scroll(e):
            if _SYS == "Darwin":
                self._canvas.yview_scroll(-1 * int(e.delta), "units")
            elif _SYS == "Windows":
                self._canvas.yview_scroll(-1 * int(e.delta / 120), "units")
            else:
                self._canvas.yview_scroll(-1 if e.num == 4 else 1, "units")

        if _SYS in ("Windows", "Darwin"):
            self._canvas.bind_all("<MouseWheel>", _scroll)
        else:
            self._canvas.bind_all("<Button-4>", _scroll)
            self._canvas.bind_all("<Button-5>", _scroll)

        self._sb.pack(side=tk.RIGHT, fill=tk.Y)
        self._canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # ── Rebuild ──────────────────────────────────────────────────────
    def _rebuild(self):
        for w in self._page.winfo_children():
            w.destroy()
        self._canvas.yview_moveto(0)
        self._build()

    # ── Primitive widgets ─────────────────────────────────────────────
    def t(self, k):
        return T[self.lang][k]

    def _label(self, text, fg=None, size=10, bold=False, pady=(0, 0)):
        """Single-line label, left-aligned."""
        font = (FONT, size, "bold") if bold else (FONT, size)
        lbl = tk.Label(self._page, text=text, bg=C["bg"],
                       fg=fg or C["fg"], font=font, anchor="w")
        lbl.pack(fill=tk.X, padx=PAD, pady=pady)
        return lbl

    def _desc(self, text, pady=(0, 14)):
        """Multi-line description that wraps to available width."""
        lbl = tk.Label(self._page, text=text, bg=C["bg"], fg=C["desc"],
                       font=(FONT, 10), justify=tk.LEFT, anchor="nw")
        lbl.pack(fill=tk.X, padx=PAD + 4, pady=pady)
        lbl.bind("<Configure>",
                 lambda e, l=lbl: l.configure(wraplength=max(100, e.width - 2)))
        return lbl

    def _section(self, title):
        """Bold section heading + underline."""
        tk.Label(self._page, text=title, bg=C["bg"], fg=C["fg"],
                 font=(FONT, 11, "bold"), anchor="w").pack(
            fill=tk.X, padx=PAD, pady=(20, 4))
        tk.Frame(self._page, height=1, bg=C["border"]).pack(
            fill=tk.X, padx=PAD, pady=(0, 8))

    def _divider(self):
        tk.Frame(self._page, height=1, bg=C["border"]).pack(
            fill=tk.X, padx=PAD, pady=16)

    def _btn(self, text, cmd, accent=False, pady=(0, 8)):
        style = "Accent.TButton" if accent else "TButton"
        ttk.Button(self._page, text=text, command=cmd, style=style).pack(
            fill=tk.X, padx=PAD, pady=pady)

    def _path_box(self, placeholder, pady=(0, 8)):
        """Displays a selected path; returns the label so caller can update it."""
        lbl = tk.Label(self._page, text=placeholder,
                       bg=C["card"], fg=C["muted"],
                       font=(FONT, 9), anchor="w",
                       padx=12, pady=10)
        lbl.pack(fill=tk.X, padx=PAD, pady=pady)
        lbl.bind("<Configure>",
                 lambda e, l=lbl: l.configure(wraplength=max(100, e.width - 24)))
        return lbl

    # ── Main build ────────────────────────────────────────────────────
    def _build(self):
        p = self._page

        # ── Header ──
        tk.Label(p, text="The Sims 4", bg=C["bg"], fg=C["accent"],
                 font=(FONT, 22, "bold")).pack(pady=(28, 2))
        tk.Label(p, text="Source Code by Leuan. Translations by Leuan. Modified by thelinuxsimmer/Melon The Goblin. Made for KristinaPlaysTheSims", bg=C["bg"], fg=C["muted"],
                 font=(FONT, 11)).pack(pady=(0, 20))

        # ── Language ──
        row = tk.Frame(p, bg=C["bg"])
        row.pack(fill=tk.X, padx=PAD, pady=(0, 4))
        tk.Label(row, text=self.t("language") + ":", bg=C["bg"], fg=C["fg"],
                 font=(FONT, 10, "bold")).pack(side=tk.LEFT)
        ttk.Radiobutton(row, text="English", variable=self.lang_var, value="en",
                        command=lambda: self._set_lang("en")).pack(side=tk.LEFT, padx=(16, 0))
        ttk.Radiobutton(row, text="Español", variable=self.lang_var, value="es",
                        command=lambda: self._set_lang("es")).pack(side=tk.LEFT, padx=(10, 0))

        self._divider()

        # ── Mode selector ──
        tk.Label(p, text=self.t("mode_select"), bg=C["bg"], fg=C["fg"],
                 font=(FONT, 11, "bold")).pack(fill=tk.X, padx=PAD, pady=(0, 10))

        modes = [
            ("single",  "▶   " + self.t("mode_single")),
            ("all",     "📦  " + self.t("mode_all")),
            ("offline", "💾  " + self.t("mode_offline")),
        ]
        for val, label in modes:
            ttk.Radiobutton(p, text=label, variable=self.mode_var, value=val,
                            command=lambda v=val: self._set_mode(v)).pack(
                anchor=tk.W, padx=PAD + 8, pady=3)

        self._divider()

        # ── Mode content ──
        if self.mode == "all":
            self._build_all()
        elif self.mode == "offline":
            self._build_offline()
        else:
            self._build_single()

        # bottom breathing room
        tk.Frame(p, bg=C["bg"], height=32).pack()

    # ── Single file ───────────────────────────────────────────────────
    def _build_single(self):
        self._section(self.t("step_1"))
        self._desc(self.t("step_1_desc"))
        self._btn(self.t("open_link"), self._open_link)

        self._section(self.t("step_2"))
        self._desc(self.t("step_2_desc"))
        self._label(self.t("zip_label"), fg=C["muted"], size=9, pady=(0, 4))
        self.zip_lbl = self._path_box(self.t("zip_ph"))
        if self.zip_path:
            self.zip_lbl.config(text=f"✓  {self.zip_path}", fg=C["success"])
        self._btn(self.t("browse_zip"), self._pick_zip)

        self._section(self.t("step_3"))
        self._desc(self.t("step_3_desc"))
        self._label(self.t("path_label"), fg=C["muted"], size=9, pady=(0, 4))
        self.game_lbl = self._path_box(self.t("path_ph"))
        if self.game_path:
            self.game_lbl.config(text=f"✓  {self.game_path}", fg=C["success"])
        self._btn(self.t("browse_game"), self._pick_game_single)

        self._divider()
        self._btn("▶   " + self.t("start"), self._install_single, accent=True, pady=(0, 0))

    # ── All DLCs ──────────────────────────────────────────────────────
    def _build_all(self):
        self._section(self.t("dlc_steps_1"))
        self._desc(self.t("dlc_steps_1_desc"))
        self._btn(self.t("open_link"), self._open_link)

        self._section(self.t("dlc_steps_2"))
        self._desc(self.t("dlc_steps_2_desc"))

        self._section(self.t("dlc_steps_3"))
        self._desc(self.t("dlc_steps_3_desc"))
        self._label(self.t("dlc_folder_label"), fg=C["muted"], size=9, pady=(0, 4))
        self.dlc_lbl = self._path_box(self.t("folder_ph"))
        if self.dlc_folder:
            n = sum(1 for f in os.listdir(self.dlc_folder) if f.endswith(".zip"))
            self.dlc_lbl.config(text=f"✓  {self.dlc_folder}  ({n} .zip files)", fg=C["success"])
        self._btn(self.t("browse_dlcs"), self._pick_dlc_folder)

        self._section(self.t("dlc_steps_4"))
        self._desc(self.t("dlc_steps_4_desc"))
        self._label(self.t("path_label"), fg=C["muted"], size=9, pady=(0, 4))
        self.game_lbl2 = self._path_box(self.t("path_ph"))
        if self.game_path:
            self.game_lbl2.config(text=f"✓  {self.game_path}", fg=C["success"])
        self._btn(self.t("browse_game"), self._pick_game_all)

        self._divider()
        self._btn(self.t("install_all"), self._install_all, accent=True, pady=(0, 0))

    # ── Offline ───────────────────────────────────────────────────────
    def _build_offline(self):
        self._section(self.t("offline_title"))
        self._desc(self.t("offline_desc"))

        self._section(self.t("offline_step_1"))
        self._desc(self.t("offline_step_1_desc"))
        self._label(self.t("backup_label"), fg=C["muted"], size=9, pady=(0, 4))
        self.bk_lbl = self._path_box(self.t("backup_ph"))
        if self.backup_path and os.path.isdir(self.backup_path):
            n = sum(1 for f in os.listdir(self.backup_path) if f.endswith(".zip"))
            self.bk_lbl.config(text=f"✓  {self.backup_path}  ({n} .zip files)", fg=C["success"])
        self._btn(self.t("browse_backup"), self._pick_backup)

        self._section(self.t("offline_step_2"))
        self._desc(self.t("offline_step_2_desc"))
        self._label(self.t("path_label"), fg=C["muted"], size=9, pady=(0, 4))
        self.game_lbl3 = self._path_box(self.t("path_ph"))
        if self.game_path:
            self.game_lbl3.config(text=f"✓  {self.game_path}", fg=C["success"])
        self._btn(self.t("browse_game"), self._pick_game_offline)

        self._divider()
        self._btn(self.t("install_from_backup"), self._install_offline, accent=True, pady=(0, 0))

    # ── Language / mode ───────────────────────────────────────────────
    def _set_lang(self, lang):
        self.lang = lang
        self.root.title(T[lang]["title"])
        self._rebuild()

    def _set_mode(self, mode):
        self.mode = mode
        self._rebuild()

    # ── Browse actions ────────────────────────────────────────────────
    def _pick_zip(self):
        p = filedialog.askopenfilename(filetypes=[("ZIP", "*.zip"), ("All", "*.*")])
        if p:
            self.zip_path = p
            self.zip_lbl.config(text=f"✓  {p}", fg=C["success"])

    def _pick_game_single(self):
        p = filedialog.askdirectory()
        if p:
            self.game_path = p
            self.game_lbl.config(text=f"✓  {p}", fg=C["success"])

    def _pick_game_all(self):
        p = filedialog.askdirectory()
        if p:
            self.game_path = p
            self.game_lbl2.config(text=f"✓  {p}", fg=C["success"])

    def _pick_game_offline(self):
        p = filedialog.askdirectory()
        if p:
            self.game_path = p
            self.game_lbl3.config(text=f"✓  {p}", fg=C["success"])

    def _pick_dlc_folder(self):
        p = filedialog.askdirectory()
        if p:
            self.dlc_folder = p
            n = sum(1 for f in os.listdir(p) if f.endswith(".zip"))
            color = C["success"] if n else C["error"]
            self.dlc_lbl.config(
                text=f"{'✓' if n else '⚠'}  {p}  ({n} .zip files found)", fg=color)

    def _pick_backup(self):
        p = filedialog.askdirectory()
        if p:
            self.backup_path = p
            self._save_config()
            n = sum(1 for f in os.listdir(p) if f.endswith(".zip"))
            color = C["success"] if n else C["warning"]
            self.bk_lbl.config(
                text=f"✓  {p}  ({n} .zip files)", fg=color)

    def _open_link(self):
        webbrowser.open(KRISTINA_MEDIAFIRE)
        webbrowser.open(YOUTUBE_LINK)
        webbrowser.open(LEUANS_SERVER)
        webbrowser.open(MELON_ARCHIVE)

    # ── Error helper ──────────────────────────────────────────────────
    def _err(self, key):
        messagebox.showerror(self.t("error"), self.t(key))

    # ── Install ───────────────────────────────────────────────────────
    def _install_single(self):
        if not self.zip_path:
            return self._err("no_zip")
        if not self.game_path or not os.path.isdir(self.game_path):
            return self._err("no_path" if not self.game_path else "invalid_path")
        if not zipfile.is_zipfile(self.zip_path):
            return self._err("invalid_zip")
        try:
            with zipfile.ZipFile(self.zip_path) as zf:
                zf.extractall(self.game_path)
            messagebox.showinfo(self.t("success"), self.t("success_msg"))
            self._offer_backup()
        except Exception as e:
            messagebox.showerror(self.t("error"), str(e))

    def _install_all(self):
        if not self.dlc_folder:
            return self._err("no_dlc_folder")
        if not self.game_path or not os.path.isdir(self.game_path):
            return self._err("no_path" if not self.game_path else "invalid_path")
        zips = [f for f in os.listdir(self.dlc_folder) if f.endswith(".zip")]
        if not zips:
            return self._err("no_zips_found")
        ok = fail = 0
        for name in zips:
            fp = os.path.join(self.dlc_folder, name)
            try:
                if zipfile.is_zipfile(fp):
                    with zipfile.ZipFile(fp) as zf:
                        zf.extractall(self.game_path)
                    ok += 1
                else:
                    fail += 1
            except Exception:
                fail += 1
        msg = self.t("installed_msg").format(count=ok)
        if fail:
            msg += "\n" + self.t("failed_msg").format(count=fail)
        messagebox.showinfo(self.t("success"), msg)
        self._offer_backup()

    def _install_offline(self):
        if not self.backup_path or not os.path.isdir(self.backup_path):
            return self._err("no_backup_path")
        if not self.game_path or not os.path.isdir(self.game_path):
            return self._err("no_path" if not self.game_path else "invalid_path")
        zips = [f for f in os.listdir(self.backup_path) if f.endswith(".zip")]
        if not zips:
            return self._err("backup_empty")
        ok = fail = 0
        for name in zips:
            fp = os.path.join(self.backup_path, name)
            try:
                if zipfile.is_zipfile(fp):
                    with zipfile.ZipFile(fp) as zf:
                        zf.extractall(self.game_path)
                    ok += 1
                else:
                    fail += 1
            except Exception:
                fail += 1
        msg = self.t("installed_msg").format(count=ok)
        if fail:
            msg += "\n" + self.t("failed_msg").format(count=fail)
        messagebox.showinfo(self.t("success"), msg)

    # ── Offline backup offer ──────────────────────────────────────────
    def _offer_backup(self):
        if self.backup_path and os.path.isdir(self.backup_path):
            return
        if messagebox.askyesno(self.t("ask_backup_title"), self.t("ask_backup_msg")):
            self._backup_window()

    # ── Backup setup window ───────────────────────────────────────────
    def _backup_window(self):
        win = tk.Toplevel(self.root)
        win.title(self.t("backup_win_title"))
        sw = win.winfo_screenwidth()
        sh = win.winfo_screenheight()
        w = max(min(int(sw * 0.48), 860), 620)
        h = max(min(int(sh * 0.78), 760), 520)
        win.geometry(f"{w}x{h}+{(sw-w)//2}+{(sh-h)//2}")
        win.minsize(520, 460)
        win.configure(bg=C["bg"])
        win.grab_set()

        # Canvas + scrollbar
        canvas = tk.Canvas(win, bg=C["bg"], highlightthickness=0)
        sb = ttk.Scrollbar(win, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=sb.set)
        page = tk.Frame(canvas, bg=C["bg"])
        wid = canvas.create_window((0, 0), window=page, anchor="nw")
        canvas.bind("<Configure>", lambda e: canvas.itemconfigure(wid, width=e.width))
        page.bind("<Configure>",   lambda *_: canvas.configure(scrollregion=canvas.bbox("all")))
        sb.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        BP = 28  # backup window padding

        def heading(text):
            tk.Label(page, text=text, bg=C["bg"], fg=C["fg"],
                     font=(FONT, 11, "bold"), anchor="w").pack(
                fill=tk.X, padx=BP, pady=(20, 4))
            tk.Frame(page, height=1, bg=C["border"]).pack(fill=tk.X, padx=BP, pady=(0, 8))

        def body(text, fg=None):
            lbl = tk.Label(page, text=text, bg=C["bg"], fg=fg or C["desc"],
                           font=(FONT, 10), justify=tk.LEFT, anchor="nw")
            lbl.pack(fill=tk.X, padx=BP + 4, pady=(0, 10))
            lbl.bind("<Configure>", lambda e, l=lbl: l.configure(wraplength=max(100, e.width - 2)))

        # Title
        tk.Label(page, text="📦  " + self.t("backup_win_title"),
                 bg=C["bg"], fg=C["accent"],
                 font=(FONT, 18, "bold")).pack(pady=(28, 4))
        tk.Frame(page, height=2, bg=C["accent"]).pack(fill=tk.X, padx=BP, pady=(0, 6))

        heading(self.t("backup_what_title"))
        body(self.t("backup_what_text"))

        heading(self.t("backup_how_title"))
        body(self.t("backup_how_text"))

        heading(self.t("backup_storage_title"))
        body(self.t("backup_storage_text"))

        # Warning card
        card = tk.Frame(page, bg="#1e1200", bd=0)
        card.pack(fill=tk.X, padx=BP, pady=(16, 6))
        tk.Label(card, text=self.t("backup_warning_title"),
                 bg="#1e1200", fg=C["warning"],
                 font=(FONT, 10, "bold"), anchor="w").pack(
            fill=tk.X, padx=14, pady=(12, 4))
        wlbl = tk.Label(card, text=self.t("backup_warning_text"),
                        bg="#1e1200", fg="#e0c080",
                        font=(FONT, 10), justify=tk.LEFT, anchor="nw")
        wlbl.pack(fill=tk.X, padx=18, pady=(0, 14))
        wlbl.bind("<Configure>", lambda e, l=wlbl: l.configure(wraplength=max(100, e.width - 2)))

        # Setup section
        heading(self.t("backup_setup_title"))
        lbl_d = tk.Label(page, text=self.t("backup_setup_desc"),
                         bg=C["bg"], fg=C["desc"],
                         font=(FONT, 10), justify=tk.LEFT, anchor="nw")
        lbl_d.pack(fill=tk.X, padx=BP + 4, pady=(0, 10))
        lbl_d.bind("<Configure>", lambda e, l=lbl_d: l.configure(wraplength=max(100, e.width - 2)))

        tk.Label(page, text=self.t("backup_current_label"),
                 bg=C["bg"], fg=C["muted"],
                 font=(FONT, 9), anchor="w").pack(fill=tk.X, padx=BP, pady=(4, 2))

        path_lbl = tk.Label(page,
                            text=self.backup_path or self.t("backup_ph"),
                            bg=C["card"],
                            fg=C["success"] if self.backup_path else C["muted"],
                            font=(FONT, 9), anchor="w", padx=12, pady=10)
        path_lbl.pack(fill=tk.X, padx=BP, pady=(0, 8))
        path_lbl.bind("<Configure>",
                      lambda e, l=path_lbl: l.configure(wraplength=max(100, e.width - 24)))

        def pick():
            p = filedialog.askdirectory()
            if p:
                self.backup_path = p
                self._save_config()
                n = sum(1 for f in os.listdir(p) if f.endswith(".zip"))
                path_lbl.config(text=f"✓  {p}  ({n} .zip files found)", fg=C["success"])

        def save_close():
            if not self.backup_path:
                messagebox.showwarning(self.t("backup_win_title"), self.t("no_backup_path"))
                return
            self._save_config()
            messagebox.showinfo(self.t("success"), self.t("backup_saved_msg"))
            win.destroy()

        ttk.Button(page, text=self.t("browse_backup"), command=pick).pack(
            fill=tk.X, padx=BP, pady=(0, 8))
        ttk.Button(page, text=self.t("save_backup"), command=save_close,
                   style="Accent.TButton").pack(fill=tk.X, padx=BP, pady=(0, 6))
        ttk.Button(page, text=self.t("backup_cancel"), command=win.destroy).pack(
            fill=tk.X, padx=BP, pady=(0, 24))


def main():
    root = tk.Tk()
    _app = App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
