from PIL import Image
import os
import shutil



for _, _, arquivo in os.walk('imagens_mercado_livre'):
    print(f'Imagens encontradas: {arquivo}')
    for imagem in arquivo:
        #abre a imagem para sobrepor e redimensiona ela
        imagem_base = Image.open('background.jpg')
        imagem_sobreposta = Image.open(f'imagens_mercado_livre/{str(imagem)}')
        tamanho_imagem = imagem_sobreposta.size

        #se a imagem for quadradada (com medidas iguais):
        if tamanho_imagem[0] == tamanho_imagem[1]:
            imagem_redimensionada = imagem_sobreposta.resize((1497, 1497), Image.ANTIALIAS)
            #une as imagens
            imagem_base.paste(imagem_redimensionada, (0, 250))
            #imagem_base.show()
            if  '1200x1200' in imagem:
                renomeia_imagem = imagem.split("1200x1200")[0]
                imagem_renomeada = f'{renomeia_imagem}.jpg'
                imagem_base.save(f"imagens_site/site_1497x1920_{imagem_renomeada}")
            else:
                imagem_base.save(f"imagens_site/site_1497x1920_{imagem}")

        if tamanho_imagem[0] != tamanho_imagem[1]:
            print('imagem de tamanho diferente')

            tamanho_base = 1497
            wpercent = (tamanho_base / float(imagem_sobreposta.size[0]))
            hsize = int((float(imagem_sobreposta.size[1]) * float(wpercent)))
            imagem_redimensionada = imagem_sobreposta.resize((tamanho_base, hsize), Image.ANTIALIAS)

            # une as imagens
            imagem_base.paste(imagem_redimensionada, (0, 250))
            imagem_base.save(f"imagens_site/site_1497x1920_{imagem}")

