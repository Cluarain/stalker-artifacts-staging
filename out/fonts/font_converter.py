import os
from fontTools.ttLib import TTFont

def convert_fonts():
    # Получаем путь к директории скрипта
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Собираем все TTF и OTF файлы в директории
    font_extensions = ['.ttf', '.otf']
    font_files = [f for f in os.listdir(script_dir) 
                  if any(f.lower().endswith(ext) for ext in font_extensions)]
    
    if not font_files:
        print("Не найдено TTF или OTF файлов в текущей директории.")
        return

    print(f"Найдено шрифтовых файлов: {len(font_files)}")
    
    for font_file in font_files:
        base_name = os.path.splitext(font_file)[0]
        input_path = os.path.join(script_dir, font_file)
        
        print(f"\nКонвертация: {font_file}")
        
        try:
            # Конвертация в WOFF
            woff_path = os.path.join(script_dir, f"{base_name}.woff")
            with TTFont(input_path) as font:
                font.flavor = 'woff'
                font.save(woff_path)
            print(f"Создан WOFF: {os.path.basename(woff_path)}")

            # Конвертация в WOFF2
            woff2_path = os.path.join(script_dir, f"{base_name}.woff2")
            with TTFont(input_path) as font:
                font.flavor = 'woff2'
                font.save(woff2_path)
            print(f"Создан WOFF2: {os.path.basename(woff2_path)}")
                
        except Exception as e:
            print(f"Ошибка при конвертации {font_file}: {str(e)}")

if __name__ == "__main__":
    convert_fonts()
    print("\nОбработка завершена!")