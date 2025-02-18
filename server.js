const express = require('express'); // Importamos Express
const app = express();
const port = 3000;

app.use(express.json()); // Permite procesar JSON en las peticiones

// Ruta de prueba para verificar que la API funciona
app.get('/', (req, res) => {
    res.send('¡La API está funcionando!');
});

// Iniciar el servidor
app.listen(port, () => {
    console.log(`API funcionando en http://localhost:${port}`);
});
