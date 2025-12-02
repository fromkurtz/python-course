from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import os

ROOT = "D:\estudos\python_Udemy\exercicios"
minha_foto = os.path.join(ROOT, "unhadabeta.png")

# 🔑 Coloque sua chave da API aqui
API_KEY = "AIzaSyBl_COxtbJNJ251oAe-I2IY7CHd6kWaO0w"

# Inicializa o cliente
client = genai.Client(api_key=API_KEY)

# Carrega a imagem local
with open(minha_foto, "rb") as f:
    image_data = f.read()



# Prompt de edição
prompt = "Mude a cor da unha para rosa claro, nao deixe nenhum vermelho para tras, mantenha o mais natural possivel"

image_file = types.File(path=minha_foto)

# Chamada ao modelo
response = client.models.generate_content(
    model="gemini-2.5-flash-image-preview",
    contents=[image_file, prompt],
    config=types.GenerateContentConfig(
        response_modalities=[types.Modality.IMAGE]
    )
)

# Salva e mostra as imagens geradas
for i, candidate in enumerate(response.candidates):
    for part in candidate.content.parts:
        if hasattr(part, "inline_data") and part.inline_data:
            img = Image.open(BytesIO(part.inline_data.data))
            img.show()
            img.save(f"resultado_{i}.png")
            print(f"Imagem salva como resultado_{i}.png")