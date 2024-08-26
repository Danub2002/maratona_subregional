import re

def extract_styles(html_file, css_file, output_html_file):
    # Ler o conteúdo do arquivo HTML
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Usar uma expressão regular para encontrar o conteúdo das tags <style>
    style_content = re.findall(r'<style[^>]*>(.*?)</style>', html_content, re.DOTALL)

    # Se houver conteúdo CSS encontrado, gravá-lo em um arquivo .css
    if style_content:
        with open(css_file, 'w', encoding='utf-8') as css_output:
            for style in style_content:
                css_output.write(style.strip() + '\n')

    # Remover as tags <style> do conteúdo HTML
    cleaned_html_content = re.sub(r'<style[^>]*>.*?</style>', '', html_content, flags=re.DOTALL)

    # Salvar o HTML limpo em um novo arquivo
    with open(output_html_file, 'w', encoding='utf-8') as output_file:
        output_file.write(cleaned_html_content)

    print(f"Estilos extraídos para {css_file} e HTML limpo salvo em {output_html_file}")

# Exemplo de uso
html_file = 'teste.html'
css_file = 'teste.css'
output_html_file = 'html_sem_estilos.html'

extract_styles(html_file, css_file, output_html_file)
