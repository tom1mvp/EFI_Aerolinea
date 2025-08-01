function openModal(flightId) {
    const modal = document.getElementById("reservaModal");
    const confirmBtn = document.getElementById("confirmBtn");

    const isAuthenticated = document.body.dataset.authenticated === "true";

    if (!isAuthenticated) {
        alert("Debe loguearse para poder reservar vuelos");
        window.location.href = "/login";
        return;
    }

    confirmBtn.onclick = function () {
        window.location.href = `/reservations/reservar/${flightId}/asientos/`;
    };

    modal.style.display = "flex";
}

function closeModal() {
    const modal = document.getElementById("reservaModal");
    modal.style.display = "none";
}
document.addEventListener("DOMContentLoaded", function () {
    const isAuthenticated = document.body.dataset.authenticated === "true";

    if (!isAuthenticated) {
        alert("Debe loguearse para poder reservar vuelos");
        window.location.href = "/login";
    }
});