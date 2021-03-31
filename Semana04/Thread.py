# Programa para fazer downloads de fotos de alta resolução do unplash
import requests
import time
import concurrent.futures

# Váriével que recebe a lista de urls das imagens
img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]

t1 = time.perf_counter() # Variável que recebe o tempo de início do processamento do script


def download_image(img_url): # Passando a lista de urls por argumento para a função realizar o download de uma imagem por vez
    img_bytes = requests.get(img_url).content # Nesta linha a variável recebe o número de bytes do conteúdo
    img_name = img_url.split('/')[3] 
    img_name = f'{img_name}.jpg' # Passando o nome da imagem por meio de uma string e colocando em formato .jpg
    with open(img_name, 'wb') as img_file: # Abrindo o arquivo expresso em bytes
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded...') # Imprimindo a mensagem que o download foi concluído 


with concurrent.futures.ThreadPoolExecutor() as executor: # Implementando as threads como gerentes. Nesta etapa que são implementadas as threads
    executor.map(download_image, img_urls) # Recebendo a função 'download_image' e a lista 'img_urls' como argumentos. Assim, mapeará a thread para cada url e realizará o download delas


t2 = time.perf_counter() # Variável que recebe o tempo final de processamento do script

print(f'Finished in {t2-t1} seconds') # Imprimindo o tempo de execução dos downloads 