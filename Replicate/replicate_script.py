import os
import replicate
import requests

# -----------------------------------------
# 1. CONFIGURAR TOKEN DE REPLICATE
# -----------------------------------------
api_token = os.getenv("REPLICATE_API_TOKEN")
if not api_token:
    raise RuntimeError("Falta la variable de entorno REPLICATE_API_TOKEN")


# -----------------------------------------
# 2. ID DEL MODELO - SIN VERSIONES INVÁLIDAS
# -----------------------------------------
MODEL_ID = "black-forest-labs/flux-kontext-pro"


# -----------------------------------------
# 3. FUNCIÓN PARA EDITAR IMAGEN USANDO FLUX
# -----------------------------------------
def editar_imagen(input_image_path, output_path):
    print("Procesando imagen...")

    with open(input_image_path, "rb") as image:
        output = replicate.run(
            MODEL_ID,
            input={
                "prompt": "Make this a 90s cartoon",
                "input_image": image,
                "aspect_ratio": "match_input_image",
                "output_format": "jpg",          # corrige 'ipg' → 'jpg'
                "safety_tolerance": 2,
                "prompt_upsampling": False
            }
        )

    print("Respuesta de la IA:", output)


    if isinstance(output, list):
        image_url = str(output[0])
    else:
        image_url = str(output)

    print("URL generada:", image_url)

    # Descargar la imagen
    img_data = requests.get(image_url).content

    os.makedirs("outputs", exist_ok=True)
    with open(output_path, "wb") as f:
        f.write(img_data)

    print("Imagen generada y guardada en:", output_path)


# -----------------------------------------
# 4. EJECUCIÓN PRINCIPAL
# -----------------------------------------
if __name__ == "__main__":
    input_img = "CHLOE.jpg"
    output_img = "outputs/flux_CHLOE_90s.jpg"

    editar_imagen(input_img, output_img)

