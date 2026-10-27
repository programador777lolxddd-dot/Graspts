# Cómo contribuir a Graspts

¡Gracias por querer mejorar Graspts! 💚

## Antes de empezar

1. Revisa el README y los problemas abiertos.
2. Crea una rama para tu cambio.
3. Haz cambios pequeños y fáciles de revisar.
4. Comprueba la aplicación en móvil y escritorio.
5. Abre un Pull Request explicando qué cambiaste y por qué.

## Guía de estilo

- Mantén la interfaz en español claro.
- Prioriza accesibilidad, legibilidad y diseño responsive.
- No añadas dependencias si una solución nativa sencilla basta.
- No subas contraseñas, tokens, claves API ni datos personales.
- No afirmes que una función está probada si no la has probado.

## Comprobaciones

Ejecuta la prueba de humo:

```bash
python3 tests/smoke_test.py
```

Después, abre la aplicación en un navegador y prueba el flujo afectado.

## Commits

Usa mensajes breves y descriptivos, por ejemplo:

- `feat: añadir filtro por categoría`
- `fix: corregir total de gastos`
- `docs: actualizar instrucciones`

## Pull Requests

Incluye un resumen, los pasos para probar el cambio y capturas cuando modifiques la interfaz.
