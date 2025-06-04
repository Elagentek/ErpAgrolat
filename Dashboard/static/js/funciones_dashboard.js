function actualizarReloj() {
    const ahora = new Date();
    const horas = ahora.getHours().toString().padStart(2, '0');
    const minutos = ahora.getMinutes().toString().padStart(2, '0');
    const segundos = ahora.getSeconds().toString().padStart(2, '0');
    const reloj = document.getElementById('reloj');
    if (reloj) {
        reloj.textContent = `${horas}:${minutos}:${segundos}`;
    }
}

document.addEventListener("DOMContentLoaded", function () {
    const fechaSpan = document.getElementById("fecha-actual");

    if (fechaSpan) {
        const hoy = new Date();
        const opcionesFecha = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
        fechaSpan.textContent = hoy.toLocaleDateString('es-CL', opcionesFecha);

        fetch("https://worldtimeapi.org/api/timezone/America/Santiago")
            .then(response => response.json())
            .then(data => {
                const datetime = new Date(data.datetime);
                fechaSpan.textContent = datetime.toLocaleDateString('es-CL', opcionesFecha);
            })
            .catch(error => {
                console.error("Error al obtener la fecha desde la API:", error);
            });
    }

    actualizarReloj();
    setInterval(actualizarReloj, 1000);
});
