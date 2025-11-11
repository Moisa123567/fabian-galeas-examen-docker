from flask import Flask, jsonify
import os, sys

app = Flask(__name__)

@app.get("/")
def root():
    return jsonify({"mensaje": "Examen Docker", "estudiante": "Fabián Galeas"})

@app.get("/salud")
def salud():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    print(f"Aplicación iniciada en puerto {port}", file=sys.stdout, flush=True)
    app.run(host="0.0.0.0", port=port)
