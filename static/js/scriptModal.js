function openModal() {
    const modal = document.getElementById("reservaModal");
    modal.style.display = "flex"; // flex para que mantenga el flexbox centrado
}

function closeModal() {
    const modal = document.getElementById("reservaModal");
    modal.style.display = "none";
}

function confirmarReserva() {
    setTimeout(() => {
        window.location.href = "login";
    }, 100)
    
    alert("Debe loguearse para poder reservar vuelos")

}