from PIL import Image
import os

imagem_base = Image.open('background_site.jpg')

for _, _, arquivo in os.walk('imagens_mercado_livre'):
    print(f'Imagens encontradas: {arquivo}')
    for imagem in arquivo:
        #abre a imagem para sobrepor e redimensiona ela
        imagem_sobreposta = Image.open(f'imagens_mercado_livre/{str(imagem)}')


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
