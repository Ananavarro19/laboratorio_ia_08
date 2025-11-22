import os
import time
import replicate

# Asegúrate de tener REPLICATE_API_TOKEN configurado en tu entorno
api_token = os.getenv("REPLICATE_API_TOKEN")
if not api_token:
    raise ValueError("Falta la variable de entorno REPLICATE_API_TOKEN")

# Ejemplo 1: modelo de imagen (Stable Diffusion)
def generar_imagen(prompt: str, output_path: str):
    start = time.time()

    output = replicate.run(
        "stability-ai/stable-diffusion:latest",
        input={"prompt": prompt}
    )

    end = time.time()
    duracion = end - start
    print(f"Imagen generada en {duracion:.2f} segundos")

    # 'output' suele ser una lista de URLs de imágenes
    # Descargamos la primera imagen
    import requests
    img_url = output[0]
    img_data = requests.get(img_url).content
    with open(output_path, "wb") as f:
        f.write(img_data)

    return duracion, img_url

# Ejemplo 2: modelo de texto (chat)
def generar_texto(prompt: str):
    start = time.time()

    output = replicate.run(
        "meta/llama-2-7b-chat:latest",
        input={
            "prompt": prompt,
            "max_tokens": 256
        }
    )

    end = time.time()
    duracion = end - start
    print(f"Texto generado en {duracion:.2f} segundos")

    # 'output' puede ser un string o lista según el modelo
    texto = "".join(output) if isinstance(output, list) else str(output)
    return duracion, texto


if __name__ == "__main__":
    os.makedirs("outputs", exist_ok=True)

    # Prueba imagen
    prompt_img = "a student studying with a laptop in a futuristic classroom, digital art"
    t_img, url_img = generar_imagen(prompt_img, "outputs/imagen_sd_01.png")
    print("Imagen guardada en outputs/imagen_sd_01.png")
    print("URL de la imagen:", url_img)

    # Prueba texto
    prompt_txt = "Explica en términos sencillos qué es un modelo generativo de IA."
    t_txt, texto_generado = generar_texto(prompt_txt)

    with open("outputs/texto_llama2_01.txt", "w", encoding="utf-8") as f:
        f.write(texto_generado)

    print("Texto guardado en outputs/texto_llama2_01.txt")
    print(f"Latencias: imagen={t_img:.2f}s, texto={t_txt:.2f}s")
