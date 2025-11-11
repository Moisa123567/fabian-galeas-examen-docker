const express = require("express");
const app = express();
const PORT = process.env.PORT || 3000;

app.get("/", (req, res) => {
  res.json({
    mensaje: "API funcionando",
    db: process.env.DB_HOST || "desconocido",
    nombre_db: process.env.DB_NAME || "sin_nombre"
  });
});

app.get("/salud", (req, res) => res.json({ status: "ok" }));

app.listen(PORT, () => console.log(`API iniciada en puerto ${PORT}`));
