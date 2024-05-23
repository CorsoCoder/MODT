<div align="center">
  <img src="https://web.archive.org/web/20091027075943/http://geocities.com/Heartland/7813/starbar.gif">
<br>
  <img src="https://imgur.com/X2OmvCq.gif" alt="MODT">
</div>


<p align="center">
  Aplicación de procesamiento de fotos desarrollada en PyQt5 que permite aplicar <strong>efectos</strong> a imágenes. La aplicación es altamente modular, permitiendo a los usuarios crear y agregar sus propios efectos personalizados.
</p>

<hr>
<br>

$${\color{red}Screenshots}$$

<div style="display: flex;">
    <img style="width: 200px;" src="https://imgur.com/cfGFo6z.png">
    <img style="width: 200px;" src="https://imgur.com/u4npn3I.png">
    <img style="width: 200px;" src="https://imgur.com/ICTDOQr.png">

</div>

<br>
<br>

$${\color{yellow}Características}$$


- **Interfaz de usuario muy amigable**
- **Gran variedad de efectos**: programos con opencv y numpy
- **Modularidad**: Los usuarios pueden crear sus propios efectos y agregarlos fácilmente.
- **Libertad**: tienes la libertad de editar los efectos y configurar los parametros a tu gusto


<hr>
<br>
<br>

$${\color{purple}Requisitos}$$



```bash
pip install -r requirements.txt
```

El archivo `requirements.txt` debe contener:

```txt
opencv-python==4.5.5.64
PyQt5==5.15.6
numpy==1.21.2
```

<hr>
<br>
<br>

$${\color{lightgreen}Instalación}$$


1. Clona este repositorio en tu máquina local:
    `git clone https://github.com/AlvaroVerdeguer/MODT.git`

2. Navega al directorio del proyecto:
    `cd MODT`

3. Instala las dependencias:
    `pip install -r requirements.txt`

4. Ejecuta el script de configuración de efectos:
    `python generate_effects_settings.py`

5. Disfruta:
    `python main.py`

<br>
<br>


$${\color{lightblue}Crea \space tus \space propios \space efectos❗}$$

1. Crea un archivo Python en la carpeta `effects`. Este archivo debe definir una función que aplique el efecto y si es necesario otra que envie los parametros de los QSliders y QComboBox.


2. La función debe tener la siguiente estructura:

```python
def apply_effect(image, param1, param2...):
    # Implementa tu efecto aquí
    return modified_image

def get_filter_data():
    return {
        "parameters": {
            "parametro1": {"min": valor_minimo, "max": valor_maximo, "init": valor_inicial, "interval": intervalo},
            "parametroOpcion": {"options": ["opcion1", "opcion2"], "init": "valor_inicial"},
        }
    }


```

3. Ejecuta el script `generate_effects_settings.py` para actualizar el archivo de configuración `effects_settings.py`.

<hr>
<br>
<br>

$${\color{pink}Contribuye🎉}$$

<div align="center" ><p>Las contribuciones son super bienvenidas, si creas algun efecto y quieres compartirlo con el mundo no dudes en mandarmelo!</p></div>

<br>

<div align="center">
  <img src="https://web.archive.org/web/20091027075943/http://geocities.com/Heartland/7813/starbar.gif">
</div>


