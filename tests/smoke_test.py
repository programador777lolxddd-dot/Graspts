#!/usr/bin/env python3
"""Pruebas de humo sencillas para los archivos estáticos de Graspts."""

from pathlib import Path
import json
import unittest

ROOT = Path(__file__).resolve().parents[1]


class GrasptsSmokeTests(unittest.TestCase):
    def test_main_html_exists_and_has_basic_document_structure(self):
        html = (ROOT / "Graspts.html").read_text(encoding="utf-8")
        self.assertIn("<!DOCTYPE html>", html.upper())
        self.assertIn('<html lang="es">', html)
        self.assertIn("<meta charset=", html.lower())
        self.assertIn("Graspts", html)

    def test_main_html_has_responsive_viewport(self):
        html = (ROOT / "Graspts.html").read_text(encoding="utf-8").lower()
        self.assertIn('name="viewport"', html)
        self.assertIn("width=device-width", html)

    def test_custom_404_exists(self):
        html = (ROOT / "404.html").read_text(encoding="utf-8")
        self.assertIn("404", html)
        self.assertIn("Volver a Graspts", html)

    def test_vercel_configuration_is_valid_json(self):
        config = json.loads((ROOT / "vercel.json").read_text(encoding="utf-8"))
        self.assertIn("rewrites", config)
        self.assertEqual(config["rewrites"][0]["destination"], "/Graspts.html")


if __name__ == "__main__":
    unittest.main(verbosity=2)
