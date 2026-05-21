document.addEventListener("DOMContentLoaded", () => {
    // Proširivanje kartica
    const expandButtons = document.querySelectorAll(".expand-btn");

    expandButtons.forEach(button => {
        button.addEventListener("click", () => {
            const card = button.closest(".bar-card");

            // Provjera da li kartica već ima klasu "expanded"
            if (card.classList.contains("expanded")) {
                card.classList.remove("expanded"); 
                button.textContent = "Pogledaj bar";// Zatvori karticu
            } else {
                // Zatvori sve druge kartice prije nego proširiš trenutnu
                document.querySelectorAll(".bar-card").forEach(c => c.classList.remove("expanded"));
                document.querySelectorAll(".expand-btn").forEach(b => b.textContent = "Pogledaj bar"); // Resetira sve gumbe na "Pogledaj bar"

                card.classList.add("expanded"); // Proširi trenutnu karticu
                button.textContent = "Sakrij bar";// Proširi trenutnu karticu
            }
        });
    });

    // Pretraga kartica prema imenu bara i koktelima
    const searchInput = document.getElementById("search-input");
    const barCards = document.getElementById("bar-cards");

    searchInput.addEventListener("input", () => {
        const filter = searchInput.value.toLowerCase(); // Korisnički unos u malim slovima
        const barNames = barCards.getElementsByClassName("bar-name");
        const barCocktails = barCards.getElementsByClassName("barCocktails");

        Array.from(barNames).forEach((nameElement, index) => {
            const barCard = nameElement.closest(".bar-card");
            const barName = nameElement.textContent.toLowerCase(); // Ime bara u malim slovima
            const cocktailsText = barCocktails[index].textContent.toLowerCase(); // Kokteli u malim slovima

            // Ako naziv bara ili kokteli sadrže unos u pretrazi, prikaži karticu
            if (barName.includes(filter) || cocktailsText.includes(filter)) {
                barCard.style.display = "";
            } else {
                barCard.style.display = "none"; // Sakrij karticu ako ne odgovara pretrazi
            }
        });
    });
});
