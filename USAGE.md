# 📖 USAGE — MediCare Plus

Guía completa para clonar, configurar, ejecutar y usar el proyecto **MediCare Plus** de predicción de costos médicos.

---

## 📋 Requisitos Previos

- **Python 3.9 o superior** instalado en el sistema
- **Git** instalado
- Navegador web moderno (Chrome, Firefox, Edge)
- Conexión a Internet (para descargar dependencias y CDNs)

---

## 🚀 Instalación Paso a Paso

### 1. Clonar el Repositorio

```bash
git clone https://github.com/MHAlberto/MedicalCostPrediction.git
cd MedicalCostPrediction
```

### 2. Crear y Activar Entorno Virtual

**Windows (cmd/PowerShell):**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

> ✅ Verás `(venv)` al inicio de tu línea de comandos cuando esté activo.

### 3. Instalar Dependencias

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Esto instalará:
- `fastapi` + `uvicorn` — Servidor API REST
- `pandas`, `numpy` — Procesamiento de datos
- `scikit-learn` — Modelo de ML
- `joblib` — Serialización del modelo

### 4. Entrenar el Modelo

```bash
python models/train_model.py
```

Esto generará dos archivos en la carpeta `models/`:
- `model.pkl` — Modelo de Regresión Lineal entrenado
- `preprocessor.pkl` — Pipeline de preprocesamiento (OneHotEncoder + StandardScaler)

> 📊 El modelo alcanza un **R² de 0.77** sobre los datos de test.

### 5. Iniciar el Servidor Backend

```bash
uvicorn backend.main:app --host 127.0.0.1 --port 5000 --reload
```

El servidor se iniciará en `http://127.0.0.1:5000`.

**Endpoints disponibles:**

| Método | Ruta | Descripción |
|:-------|:-----|:------------|
| `GET` | `/health` | Verificar estado del servidor |
| `POST` | `/predict` | Predecir costo médico |
| `GET` | `/docs` | Documentación interactiva (Swagger UI) |

### 6. Abrir el Frontend

Abre el archivo `frontend/index.html` en tu navegador web favorito.

> ⚡ No necesitas un servidor web adicional — el frontend carga Tailwind CSS y html2pdf.js desde CDN.

---

## 🎯 Cómo Usar la Aplicación

### Usar la Interfaz Web

1. Completa el formulario **"Datos del Paciente"**:
   - **Edad**: 18 — 80 años
   - **Sexo**: Femenino / Masculino
   - **IMC (BMI)**: 10 — 60
   - **Dependientes**: 0 — 10
   - **Fumador**: Sí / No
   - **Región**: Southwest, Southeast, Northwest, Northeast

2. Haz clic en **"Estimar Costo Médico"**

3. El resultado muestra:
   - Costo médico anual estimado
   - Nivel de riesgo (Bajo / Medio / Alto)
   - Resumen de los datos ingresados
   - Botón **"Descargar Factura PDF"**

4. El historial de predicciones se guarda automáticamente en tu navegador (localStorage).

### Usar la API REST

**Ejemplo con `curl`:**

```bash
curl -X POST http://127.0.0.1:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "age": 35,
    "sex": "male",
    "bmi": 28.5,
    "children": 0,
    "smoker": "no",
    "region": "southwest"
  }'
```

**Respuesta:**

```json
{
  "predicted_charges": 4531.24
}
```

**Ejemplo con Python:**

```python
import requests

response = requests.post("http://127.0.0.1:5000/predict", json={
    "age": 45,
    "sex": "female",
    "bmi": 32.1,
    "children": 2,
    "smoker": "yes",
    "region": "northeast"
})

print(response.json())
# {'predicted_charges': 35420.87}
```

---

## 🔧 Solución de Problemas

| Problema | Causa Posible | Solución |
|:---------|:--------------|:---------|
| `pip` no se reconoce | Python no está en PATH | Usa `python -m pip install ...` |
| Puerto 5000 en uso | Otro servicio ocupando el puerto | Cambia el puerto: `--port 5001` |
| `ModuleNotFoundError` | Entorno virtual no activado | Activa venv: `venv\Scripts\activate` |
| Error en `/predict` | Modelo no entrenado | Ejecuta `python models/train_model.py` |
| Frontend no conecta | Backend no está corriendo | Inicia uvicorn en otra terminal |

---

## 🐳 Docker (opcional)

Si prefieres usar Docker:

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN python models/train_model.py
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "5000"]
```

```bash
docker build -t medicare-plus .
docker run -p 5000:5000 medicare-plus
```

---

## 📁 Scripts Útiles

```bash
# Entrenar modelo
python models/train_model.py

# Iniciar servidor con recarga automática
uvicorn backend.main:app --host 127.0.0.1 --port 5000 --reload

# Desactivar entorno virtual (cuando termines)
deactivate
```

---

## 📬 Contacto

¿Preguntas o sugerencias? Abre un [issue](https://github.com/MHAlberto/MedicalCostPrediction/issues) o contacta al autor.

---

<div align="center">
  <sub>📖 Documentación generada para MediCare Plus — Proyecto de Machine Learning para predicción de costos médicos</sub>
</div>
