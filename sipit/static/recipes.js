
document.querySelectorAll('.filter-checkbox').forEach(checkbox => {

    checkbox.addEventListener('change', HandleCheckboxChange);
});

function HandleCheckboxChange(){

    const data = {
        ingredients: [],
        time: [],
        category:[],
        difficulty:[]
    };
    
    // Collect selected ingredients
    document.querySelectorAll('#ingredients-options .filter-checkbox:checked').forEach(checkbox => {
        data.ingredients.push(checkbox.name);
    });


    // Collect selected time
    document.querySelectorAll('#time-options .filter-checkbox:checked').forEach(checkbox => {
        data.time.push(checkbox.name);
    });

    document.querySelectorAll('#category-options .filter-checkbox:checked').forEach(checkbox => {
        data.category.push(checkbox.name);
    });

    // Collect selected time
    document.querySelectorAll('#difficulty-options .filter-checkbox:checked').forEach(checkbox => {
        data.difficulty.push(checkbox.name);
    });


    APIQuery(data,"all_filter_cocktail.php", APIreturnStatusCocktail);



}


function clearCocktailResults() {
    const parentDiv = document.getElementById('cocktails-list-div'); // Replace with your parent div ID
    while (parentDiv.firstChild) {
        parentDiv.removeChild(parentDiv.firstChild);
    }
}

function APIreturnStatusCocktail(jobj){

    clearCocktailResults();
    //alert(jobj);
    objRet={};
    objRet=JSON.parse(jobj);
    

    for(let counter = 0; counter < objRet.all.length; counter++){
        //alert(objRet.all[counter].naziv);
        const parentDiv = document.getElementById('cocktails-list-div');
        parentDiv.className = `dynamic-div-parent`;
        const newDiv = document.createElement('div');
        newDiv.id = `div-${counter}`;
        newDiv.className = `dynamic-div`;
        parentDiv.appendChild(newDiv);
        createCocktailHTML(newDiv.id, objRet.all[counter]);

  }

}

function createCocktailHTML(divName, cocktail) {
    const container = document.getElementById(divName);

    if (!container) {
        console.error(`Div with id '${divName}' not found.`);
        return;
    }

    // Clear any existing content in the container
    container.innerHTML = '';

    // Main card container
    const card = document.createElement('div');
    card.className = 'cocktail-card';

    // Cocktail Name
    const nameElement = document.createElement('h2');
    nameElement.textContent = cocktail.naziv;
    card.appendChild(nameElement);

    
    // Preparation Time and Difficulty
    const timeDifficulty = document.createElement('p');
    timeDifficulty.innerHTML = `<strong>Vrijeme pripreme:</strong> ${cocktail.duljina_pripreme} <br> <strong>Težina:</strong> ${cocktail.tezina}`;
    details.appendChild(timeDifficulty);

    // Special Features
    if (cocktail.posebnosti && cocktail.posebnosti.length > 0) {
        const specialFeatures = document.createElement('p');
        specialFeatures.innerHTML = `<strong>Posebnosti:</strong> ${cocktail.posebnosti.join(', ')}`;
        details.appendChild(specialFeatures);
    }

    // Ingredients
    const ingredients = document.createElement('ul');
    ingredients.innerHTML = '<strong>Sastojci:</strong>';
    cocktail.sastojci.forEach(sastojak => {
        const li = document.createElement('li');
        li.textContent = sastojak;
        ingredients.appendChild(li);
    });
    details.appendChild(ingredients);

    // Preparation Instructions
    const preparation = document.createElement('p');
    preparation.innerHTML = `<strong>Priprema:</strong> ${cocktail.priprema}`;
    details.appendChild(preparation);

    // Toggle Button
    const toggleButton = document.createElement('button');
    toggleButton.textContent = 'Prikaži detalje';
    toggleButton.className = 'toggle-details';

    const extraContent = document.createElement('div');
    extraContent.className = 'extra-content';
    extraContent.style.display = 'none';

    extraContent.appendChild(details);

    toggleButton.addEventListener('click', () => {
        if (extraContent.style.display === 'none') {
            extraContent.style.display = 'block';
            toggleButton.textContent = 'Sakrij detalje';
        } else {
            extraContent.style.display = 'none';
            toggleButton.textContent = 'Prikaži detalje';
        }
    });

    card.appendChild(toggleButton);
    card.appendChild(extraContent);

    // Append the card to the container
    container.appendChild(card);
}

document.addEventListener("DOMContentLoaded", () => {
    // Proširivanje kartica
    const expandButtons = document.querySelectorAll(".expand-btn");

    expandButtons.forEach(button => {
        button.addEventListener("click", () => {
            const card = button.closest(".cocktail-card");

            // Provjera da li kartica već ima klasu "expanded"
            if (card.classList.contains("expanded")) {
                card.classList.remove("expanded"); 
                button.textContent = "Pogledaj recept";// Zatvori karticu
            } else {
                // Zatvori sve druge kartice prije nego proširiš trenutnu
                document.querySelectorAll(".cocktail-card").forEach(c => c.classList.remove("expanded"));
                document.querySelectorAll(".expand-btn").forEach(b => b.textContent = "Pogledaj recept"); // Resetira sve gumbe na "Pogledaj bar"

                card.classList.add("expanded"); // Proširi trenutnu karticu
                button.textContent = "Sakrij";// Proširi trenutnu karticu
            }
        });
    });
});

