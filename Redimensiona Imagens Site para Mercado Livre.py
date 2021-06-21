from PIL import Image
import os



try:
    os.mkdir('imagens_mercado_livre')
    os.mkdir('imagens_site')
except:
    pass
imagem_base = Image.open('background_mercado_livre.jpg')

for _, _, arquivo in os.walk('imagens_site'):
    print(f'Imagens encontradas: {arquivo}')
    for imagem in arquivo:
        #abre a imagem para sobrepor e redimensiona ela
        imagem_sobreposta = Image.open(f'imagens_site/{str(imagem)}')
        imagem_redimensionada = imagem_sobreposta.resize((1136,1458), Image.ANTIALIAS)
        #une as imagens
        imagem_base.paste(imagem_redimensionada, (0, -150))
        #imagem_base.show()
        if  '1200x1200' in imagem:
            renomeia_imagem = imagem.split("site_1497x1920_")[0]
            imagem_renomeada = f'{renomeia_imagem}.jpg'
            imagem_base.save(f"imagens_mercado_livre/mercado_livre_1200_1200_{imagem_renomeada}")
        else:
            imagem_base.save(f"imagens_mercado_livre/mercado_livre_1200_1200_{imagem}")
