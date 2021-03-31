# Programa para fazer otimização de fotos de alta resolução do unplash
import time
import concurrent.futures
from PIL import Image, ImageFilter # Inicializando a biblioteca pillow 

img_names = [ # Váriével que recebe a lista de urls das imagens
    'photo-1516117172878-fd2c41f4a759.jpg',
    'photo-1532009324734-20a7a5813719.jpg',
    'photo-1524429656589-6633a470097c.jpg',
    'photo-1530224264768-7ff8c1789d79.jpg',
    'photo-1564135624576-c5c88640f235.jpg',
    'photo-1541698444083-023c97d3f4b6.jpg',
    'photo-1522364723953-452d3431c267.jpg',
    'photo-1513938709626-033611b8cc03.jpg',
    'photo-1507143550189-fed454f93097.jpg',
    'photo-1493976040374-85c8e12f0c0e.jpg',
    'photo-1504198453319-5ce911bafcde.jpg',
    'photo-1530122037265-a5f1f91d3b99.jpg',
    'photo-1516972810927-80185027ca84.jpg',
    'photo-1550439062-609e1531270e.jpg',
    'photo-1549692520-acc6669e2f0c.jpg'
]

t1 = time.perf_counter() # Variável que recebe o tempo de início do processamento do script 

size = (1200, 1200) # Atribuindo uma resolução de 1200 pixels para as imagens 


def process_image(img_name): # Função que recebe por argumento a lista de imagens e faz a otimização delas
    img = Image.open(img_name) # Abrindo uma imagem por vez

    img = img.filter(ImageFilter.GaussianBlur(15)) # Aplicando filtro Glaussian Blur a imagem 

    img.thumbnail(size) # Passando por argumento os pixels da imagem 
    img.save(f'processed/{img_name}') # Salvando cada imagem com respectivo nome em uma pasta denominada 'processed'
    print(f'{img_name} was processed...') # Exibindo na tela o nome da imagem que foi processada 


with concurrent.futures.ProcessPoolExecutor() as executor: # Implementando os processos como gerentes. Nesta etapa que é implementado o multiprocessamento 
    executor.map(process_image, img_names) # Recebendo a função 'process_image' e a lista 'img_names' como argumentos. Assim, mapeará o processo para cada imagem e realizará a otimização delas

t2 = time.perf_counter() # Variável que recebe o tempo final de processamento do script

print(f'Finished in {t2-t1} seconds') # Imprimindo o tempo de execução dos processos