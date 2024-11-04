# Unit (methods or functions) test.

import flet as ft
from random import choice

# App settings.
file = open('assets/settings.txt')
content = file.read().splitlines()
file.close()

dark_theme_on = bool(int(content[2][16:].strip()))
language = content[3][11:].strip()

# Load the theme:
def load_theme():
    """Load the theme preference from the settings file."""
    global font_color, bgcolor, btn_color, btn_bgcolor, label_style, \
           field_border_color, field_bgcolor, field_label_style

    if dark_theme_on:
        font_color = 'white'
        bgcolor = '#111418'
        btn_color = 'black'
        btn_bgcolor = '#7ce7ff'
        label_style = ft.TextStyle(color='white')
        field_border_color = 'white'
        field_bgcolor = '#1b263f'
        field_label_style = ft.TextStyle(color='white')
    else:
        font_color = 'black'
        bgcolor = 'white'
        btn_color = 'white'
        btn_bgcolor = '#0076d1'
        label_style = ft.TextStyle(color='black')
        field_border_color = 'black'
        field_bgcolor = '#dfeffc'
        field_label_style = ft.TextStyle(color='black')


def load_language():
    """Load the language preference."""
    global rtl, alignment, lang, hints
    if language == 'english':
        rtl = False
        alignment = 'start'
        lang =    {'Another Ayah': 'Another Ayah',
                   'Settings': 'Settings',
                   'Dark theme.': 'Dark theme.',
                   'Language': 'Language',
                   'Hint!': 'Hint!',
                   'About': 'About',
                   'Copyright © 2024 Didouna Mohyeddine': 'Copyright © 2024 Didouna Mohyeddine',
                   }
        hints = ['When you feel sad or upset, try to read Quran.',
                 ]

    elif language == 'العربية':
        rtl = True
        alignment = 'end'
        lang =    {'Another Ayah': 'آية أخرى',
                   'Settings': 'الإعدادات',
                   'Dark theme.': 'الوضع المظلم.',
                   'Language': 'اللغة',
                   'Hint!': 'نصيحة',
                   'About': 'حول التطبيق',
                   'Copyright © 2024 Didouna Mohyeddine': 'جميع الحقوق محفوظة © 2024 - ديدونه محيي الدين',
                   }
        hints = ['في حالة حزنك أو تضايقك، حاول قراءة بعض من كتاب الله.',
                 ]


# Import & Organize the Quran ayah_txt file.
BASMALA = 'بِسْمِ اللَّهِ الرَّحْمَـٰنِ الرَّحِيمِ'

file = open('assets/Quran.txt')
QURAN = file.read()
QURAN = QURAN.splitlines()[:-30]
file.close()

for line in QURAN[:]:
    line = line.strip()
    if not line:
        QURAN.remove(line)
    elif line == BASMALA:
        QURAN.remove(line)
    elif BASMALA in line:
        index = QURAN.index(line)
        new_line = line.replace(BASMALA, '').strip()
        QURAN[index] = new_line


def main(page: ft.page):
    """Style the app."""
    # Page settings.
    page.settings_txt = 'ayah'
    page.adaptive = True
    page.padding = ft.padding.only(15, 50, 15, 15)
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.fonts = {'Amiri': 'assets/fonts/Amiri-Quran-Regular.ttf'}

    def home_page(event=None):
        """Customize the home/main page."""
        global another_ayah_btn, basmala_txt, ayah_txt

        # Organize elements.
        ayah = choice(QURAN) + ' ' * 250
        settings_btn = ft.IconButton(icon=ft.icons.SETTINGS, scale=2.5, on_click=settings)
        another_ayah_btn = ft.ElevatedButton(text=lang['Another Ayah'], on_click=show_ayah, height=45, scale=1.5,
                                             bgcolor=btn_bgcolor, color=btn_color)
        basmala_txt = ft.Text(font_family='Amiri', value=BASMALA, size=25, weight=ft.FontWeight.W_100,
                              theme_style=ft.TextThemeStyle.LABEL_SMALL)
        ayah_txt = ft.Text(font_family='Amiri', value=ayah, size=25, weight=ft.FontWeight.W_100,
                           theme_style=ft.TextThemeStyle.LABEL_SMALL, rtl=False)

        row_1 = ft.Row([another_ayah_btn], alignment='center', height=100, spacing=200)
        row_2 = ft.Row([basmala_txt], alignment='right', rtl=True)
        row_3 = ft.Row([ayah_txt], alignment='right', wrap=True, rtl=True)

        # Display.
        page.clean()
        page.add(settings_btn, row_1, row_2, row_3)
        set_theme()
        page.update()

    def settings(event):
        """Customize the settings page."""
        global settings_txt, dark_theme_check, language_menu, hint_txt, hint_title_txt, \
               about_title_txt, about_txt
        page.clean()

        # Create elements.
        go_back_btn = ft.IconButton(icon=ft.icons.ARROW_BACK_SHARP, scale=2.5, on_click=home_page)
        settings_txt = ft.Text(lang['Settings'], size=20)
        dark_theme_check = ft.Checkbox(label=lang['Dark theme.'], value=dark_theme_on, on_change=change_theme,
                                       label_style=label_style)
        options = [ft.dropdown.Option('English'), ft.dropdown.Option('العربية')]
        language_menu = ft.Dropdown(label=lang['Language'], options=options,
                                    on_change=change_language)

        hint = choice(hints)
        hint_title_txt = ft.Text(value=lang['Hint!'], size=20)
        hint_txt = ft.Text(value=hint)

        about_title_txt = ft.Text(lang['About'], size=20)
        about_txt = ft.Text(lang['Copyright © 2024 Didouna Mohyeddine'])

        # Organize elements in rows.
        s = ft.Text('')     # Separator.
        row_1 = ft.Row([settings_txt], alignment=alignment)
        row_2 = ft.Row([dark_theme_check], rtl=rtl)
        row_2_1 = ft.Row([language_menu], rtl=rtl)
        row_3 = ft.Row([hint_title_txt], alignment=alignment)
        row_4 = ft.Row([hint_txt], rtl=rtl)
        row_5 = ft.Row([about_title_txt], alignment=alignment)
        row_6 = ft.Row([about_txt], alignment=alignment)

        # Display.
        page.add(go_back_btn, s, row_1, row_2, row_2_1, s, s,
                 row_3, row_4, s, s, row_5, row_6)

        if event != "startup":
            set_theme()
            page.update()

    def show_ayah(event):
        """Display a new random Ayah when clicking."""
        ayah_txt.value = choice(QURAN)  + ' ' * 250
        page.update()

    def set_theme():
        """Set the theme at the startup of the app."""
        load_theme()

        # General theme.
        page.bgcolor = bgcolor

        # Home page theme.
        another_ayah_btn.color = btn_color
        another_ayah_btn.bgcolor = btn_bgcolor
        basmala_txt.color = font_color
        ayah_txt.color = font_color

        # Settings page theme.
        settings_txt.color = font_color
        dark_theme_check.label_style = label_style
        language_menu.border_color = field_border_color
        language_menu.color = font_color
        language_menu.bgcolor = field_bgcolor
        language_menu.label_style = field_label_style
        language_menu.icon_enabled_color = font_color
        hint_txt.color = font_color
        hint_title_txt.color = font_color
        about_title_txt.color = font_color
        about_txt.color = font_color

    def change_theme(event):
        """Change the theme when requested."""
        global dark_theme_on

        value = dark_theme_check.value
        dark_theme_on = value
        set_theme()

        # Save the changes.
        page.update()

        old_value = 0 if value else 1
        new_value = 1 if value else 0

        file = open('assets/settings.txt', 'r')
        content = file.read().replace(f'dark_theme_on = {old_value}', f'dark_theme_on = {new_value}')
        file = open('assets/settings.txt', 'w')
        file.write(content)
        file.close()

    def change_language(event):
        """Switch the language."""
        global language
        value = language_menu.value.lower()

        # Save the changes.
        file = open('assets/settings.txt', 'r')
        content = file.read()
        content = content.replace(language, value)
        file = open('assets/settings.txt', 'w')
        file.write(content)
        file.close()

        language = value

        # Reload.
        load_language()
        settings('reload')


    # Display.
    load_theme()
    load_language()
    settings('startup')
    home_page()


ft.app(target=main, assets_dir='assets')
