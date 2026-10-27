<!--
  Graspts · README principal
  App web de control de gastos, ligera y centrada en la privacidad.
-->

<div align="center">

# 💸 Graspts

### Tus gastos, bajo control. Sin complicarte la vida.

**Una webapp ligera para registrar gastos y ver cuánto llevas gastado, con una interfaz moderna y modo claro/oscuro.**

<img width="64" height="64" alt="686901312-b4feb138-2b7a-4ecb-9ebd-401df67c23c6" src="https://github.com/user-attachments/assets/b7aabe23-dc0c-4ac3-b76a-e46221d68423" />

<p>
  <a href="https://graspts.vercel.app/"><img src="https://img.shields.io/badge/🌐-Abrir%20Graspts-16c79a?style=for-the-badge" alt="Abrir Graspts"></a>
  <img src="https://img.shields.io/badge/Estado-BETA-1e88e5?style=for-the-badge" alt="Estado beta">
  <img src="https://img.shields.io/badge/Idioma-Español-0f9b77?style=for-the-badge" alt="Idioma español">
  <img src="https://img.shields.io/badge/Hecho%20con-HTML%20%7C%20CSS%20%7C%20JS-f7df1e?style=for-the-badge" alt="HTML CSS y JavaScript">
</p>

<p><i>Pequeño, directo y pensado para ayudarte a tener tus gastos a la vista.</i></p>

</div>

---

## ✨ ¿Qué es Graspts?

**Graspts** es una aplicación web de control de gastos diseñada para registrar movimientos cotidianos de forma sencilla. Puedes añadir una descripción, indicar el importe, elegir una categoría y consultar el total acumulado desde una misma pantalla.

La aplicación está construida como una web estática: no requiere instalar una app de escritorio ni configurar un servidor para empezar a usarla.

> 🚧 **Estado: BETA.** Algunas funciones avanzadas, como cuentas de usuario, sincronización en la nube y exportación de datos, no forman parte de la versión actual.

## 🚀 Pruébala

**[👉 Abrir Graspts en producción](https://graspts.vercel.app/)**

También puedes descargar o clonar el repositorio para ejecutarla localmente.

## 🌟 Características

| Función | Descripción |
| --- | --- |
| 🧾 Registro de gastos | Añade una descripción, un importe y una categoría. |
| 🧮 Total automático | Consulta el total de los movimientos registrados. |
| 🌗 Tema claro y oscuro | Cambia la apariencia para adaptarla a tus preferencias. |
| 💾 Guardado local | Los datos se guardan en el navegador mediante almacenamiento local. |
| 📱 Diseño adaptable | Interfaz preparada para pantallas de móvil y escritorio. |
| 🎨 Identidad visual | Icono SVG integrado en el HTML mediante una Data URL. |
| 🧭 Página 404 | Página personalizada para rutas que no existen. |
| 🪶 Sin instalación | No necesita un proceso de compilación para la app estática. |

## 🖥️ Captura rápida

La interfaz incluye un encabezado con el total, un formulario para registrar gastos y una lista de movimientos. La apariencia exacta puede cambiar a medida que avance la beta.

## ⚡ Ejecutar en local

### Opción 1: abrir el archivo

1. Descarga o clona el repositorio.
2. Abre `Graspts.html` en tu navegador.

### Opción 2: usar un servidor local

Desde la carpeta del proyecto, ejecuta:

```bash
python3 -m http.server 8000
```

Abre después [http://localhost:8000/Graspts.html](http://localhost:8000/Graspts.html).

## 🧪 Comprobar los archivos del proyecto

Se incluye una prueba de humo básica para verificar la estructura HTML, la página 404 y la configuración de Vercel.

```bash
python3 tests/smoke_test.py
```

Estas comprobaciones son básicas: no sustituyen las pruebas manuales en navegadores reales ni una auditoría de accesibilidad o seguridad.

## 🗂️ Estructura del repositorio

```text
Graspts/
├── Graspts.html          # Aplicación web principal
├── 404.html              # Página de ruta no encontrada
├── README.md             # Documentación principal
├── LICENSE               # Licencia del proyecto
├── .gitignore            # Archivos que Git debe ignorar
├── vercel.json           # Configuración de rutas para Vercel
├── CHANGELOG.md          # Registro de cambios
├── CONTRIBUTING.md       # Guía para contribuir
├── SECURITY.md           # Política de seguridad y privacidad
├── docs/
│   ├── USAGE.md          # Guía de uso
│   └── ROADMAP.md        # Ideas y hoja de ruta
└── tests/
    └── smoke_test.py     # Pruebas de humo básicas
```

## 🔐 Privacidad y almacenamiento

Graspts utiliza almacenamiento local del navegador para conservar los movimientos y preferencias compatibles con la implementación actual.

- **Los gastos no se sincronizan automáticamente** entre navegadores o dispositivos.
- La versión actual **no incluye inicio de sesión ni una base de datos remota**.
- Borrar los datos del sitio desde el navegador puede eliminar los movimientos guardados.
- No introduzcas contraseñas, números de tarjeta ni información sensible en las descripciones.
- Si tus datos son importantes, conserva una copia por separado.

Lee también la [política de seguridad](SECURITY.md).

## 🧭 Hoja de ruta

Las ideas futuras incluyen edición de movimientos, búsqueda y filtros, exportación e importación de datos, resúmenes por periodo y mejoras adicionales de accesibilidad. Son propuestas, no promesas de funciones ya disponibles.

Consulta [docs/ROADMAP.md](docs/ROADMAP.md).

## 🤝 Contribuir

¡Las mejoras son bienvenidas! Lee la [guía de contribución](CONTRIBUTING.md), explica el cambio que propones y, cuando sea posible, incluye pasos para probarlo.

Si encuentras un problema, informa con detalles suficientes para reproducirlo, sin compartir información personal.

## 📦 Tecnologías

- **HTML5** — estructura.
- **CSS** — diseño adaptable y temas visuales.
- **JavaScript** — interacciones y lógica del cliente.
- **Web Storage** — persistencia local en el navegador.
- **Vercel** — despliegue de la web estática.

## 📄 Licencia

Este proyecto incluye el archivo [LICENSE](LICENSE). Consulta ese archivo para conocer los términos aplicables.

---

<div align="center">

**Graspts** · Menos lío con los gastos. Más claridad con tu dinero. 💚

[Web](https://graspts.vercel.app/) · [Repositorio](https://github.com/programador777lolxddd-dot/Graspts)

</div>
