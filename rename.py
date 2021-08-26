import re
import os
import shutil

#01-Aqui e a criação da pasta raiz
main_folder = r'D:\Teste03'

#05- Função para renomear arquivos e modificalos de lugar
def rename_file(file):
    #06- Dividindo o nome do arquivo da extensão do arquivo
    file_name, file_extension = os.path.splitext(file)
    
    #07- Pega os numeros do nome do arquivo e separa para renomear os arquivos
    file_name_numbers = re.findall(r'\d+', file_name)

    #08- Se não tiver numero ele retorna o nome do proprio arquivo
    if not file_name_numbers:
        return file

    #09- Adiciona a função que adiciona o zfill para colocar como padrão
    file_name_numbers = file_name_numbers[0].zfill(4)

    #10- Retorna o nome e a extansão do arquivo corretamente corrigido
    return f'{file_name_numbers}{file_extension}'

#04- Criação do For para verificar os arquivos
def file_loop(root, dirs, files):
    for file in files:
        #11- Verifica a extensão escolhida está correta e continua a ação
        if not re.search(r'\.txt$', file):
            continue

        new_file_name = rename_file(file)

        #12- Criação dos caminhos completos antigo e novo
        old_file_full_path = os.path.join(root, file)
        new_file_full_path = os.path.join(root, new_file_name)

        #13- Aqui que finaliza com a API shutil
        print(f'Movendo arquivo "{file}" para "{new_file_name}"')
        shutil.move(old_file_full_path, new_file_full_path)

#03- Criação do loop para trafego entre todas as pastas utilizando walk()
def main_loop():
    for root, dirs, files in os.walk(main_folder):
        file_loop(root, dirs, files)

#02- Criação da execução do script
if __name__ == '__main__':
    main_loop()