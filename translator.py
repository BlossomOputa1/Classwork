import flet as ft
import speech_recognition as sr
import os


def main(page: ft.Page):
    page.title = "Audio Translator"
    # page.scroll = "auto"
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = "Center"
    # page.window.minimized = False
    page.window.height = 600
    page.window.width = 450
    page.window.center()
    page.window.maximized = False
    page.window.resizable = False
    page.bgcolor = "lightblue"
    page.padding = 20


    # Display area
    output_text = ft.Text(
        value="Upload an audio file (.wav) to begin.",
        color=ft.Colors.BLACK,
    )

    transcribe_text = ""

    # Pickers
    file_picker = ft.FilePicker()
    save_dialog = ft.FilePicker()
    page.overlay.append(file_picker)
    page.overlay.append(save_dialog)

    #AUDIO TRANSCRIPTION
    def transcribe_audio(file_path):
        nonlocal transcribe_text
        r = sr.Recognizer()
        try:
            with sr.AudioFile(file_path) as source:
                audio = r.record(source)
                text = r.recognize_google(audio)
                transcribe_text = text
                output_text.value = f"✅ Transcription Completed:\n\n{text}"
        except sr.UnknownValueError:
            output_text.value = "⚠️ Could not understand audio."
        except sr.RequestError:
            output_text.value = "⚠️ Could not connect to Google Speech Recognition API."
        except FileNotFoundError:
            output_text.value = f"⚠️ File not found: {file_path}"
        page.update()

    #WHEN AUDIO IS PICKED
    def file_picked(e: ft.FilePickerResultEvent):
        if e.files:
            file_path = e.files[0].path
            output_text.value = f"🎧 Transcribing: {os.path.basename(file_path)}..."
            page.update()
            transcribe_audio(file_path)
        else:
            output_text.value = "⚠️ No file selected."
            page.update()

    file_picker.on_result = file_picked

    #SAVE HANDLERS
    def save_text(_):
        # Triggered when user clicks "Save Transcription"
        nonlocal transcribe_text
        if transcribe_text.strip() == "":
            output_text.value = "⚠️ No transcription to save."
            page.update()
            return
        save_dialog.save_file()  # Opens the save dialog

    def on_save_result(e: ft.FilePickerResultEvent):
        # Triggered after user selects where to save
        save_path = getattr(e, "path", None)
        if not save_path:
            output_text.value = "⚠️ Save cancelled or no path selected."
            page.update()
            return
        with open(save_path, "w", encoding="utf-8") as f:
            f.write(transcribe_text)
        output_text.value = f"💾 Transcription saved to:\n{save_path}"
        page.update()

    save_dialog.on_result = on_save_result

    # -------------------- BUTTONS --------------------
    transcribe_button = ft.ElevatedButton(
        "Upload Audio File",
        icon=ft.Icons.UPLOAD_FILE,
        on_click=lambda _: file_picker.pick_files(
            allow_multiple=False, allowed_extensions=["wav"]
        ),
        bgcolor=ft.Colors.BLUE,
        color=ft.Colors.WHITE,
    )

    save_button = ft.ElevatedButton(
        "Save Transcription",
        icon=ft.Icons.SAVE,
        on_click=save_text,
        bgcolor=ft.Colors.GREEN,
        color=ft.Colors.BLACK,
    )

    page.add(
        ft.Column(
            [
                ft.Container(
                    content=ft.Text(
                        "Speech to Text Converter",
                        size=24,
                        weight="bold",
                        color="blue",
                    ),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.Colors.WHITE,
                    width=500,
                    height=120,
                    border_radius=10,
                ),
                ft.Container(
                    content=output_text,
                    height=120,
                    width=500,
                    margin=10,
                    padding=10,
                    bgcolor=ft.Colors.WHITE,
                ),
                ft.Row(
                    [transcribe_button, save_button],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
    # -------------------- PAGE LAYOUT --------------------


ft.app(target=main)
