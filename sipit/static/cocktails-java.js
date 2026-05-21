document.querySelectorAll('.filter').forEach(filterButton => {
  filterButton.addEventListener('click', function() {
    const filterType = this.getAttribute('data-filter');
    const optionsContainer = document.getElementById(`${filterType}-options`);

    // Toggle the visibility of the corresponding options
    if (optionsContainer.style.display === 'block') {
      optionsContainer.style.display = 'none';
    } else {
      optionsContainer.style.display = 'block';
    }

    // Optionally, toggle the active class on the filter button
    this.classList.toggle('active');
  });
});

// New: Filtering Logic
document.querySelectorAll('.filter-options input').forEach(input => {
input.addEventListener('change', filterCocktails);
});

function filterCocktails() {
const cocktails = document.querySelectorAll('.cocktail-card');
const selectedFilters = {
  category: getCheckedValues('category-options'),
  ingredients: getCheckedValues('ingredients-options'),
  difficulty: getCheckedValues('difficulty-options'),
  time: getCheckedValues('time-options')
};

cocktails.forEach(cocktail => {
  const matchesCategory = matchFilter(cocktail, 'category', selectedFilters.category, true);
  const matchesIngredients = matchFilter(cocktail, 'ingredients', selectedFilters.ingredients, true);
  const matchesDifficulty = matchFilter(cocktail, 'difficulty', selectedFilters.difficulty);
  const matchesTime = matchFilter(cocktail, 'time', selectedFilters.time);

  // Show/hide based on whether all filters match
  if (matchesCategory && matchesIngredients && matchesDifficulty && matchesTime) {
    cocktail.style.display = 'block';
  } else {
    cocktail.style.display = 'none';
  }
});
}

function getCheckedValues(containerId) {
return Array.from(document.querySelectorAll(`#${containerId} input:checked`)).map(input => input.nextSibling.textContent.trim());
}

function matchFilter(cocktail, attribute, selectedValues, isMultiple = false) {
const cocktailValue = cocktail.getAttribute(`data-${attribute}`);
if (!selectedValues.length) return true; // No filter applied for this attribute

if (isMultiple || attribute === 'category') {
  const valuesArray = cocktailValue.split(', ').map(value => value.trim());;
  return selectedValues.some(value => valuesArray.includes(value));
}

return selectedValues.includes(cocktailValue);
}

// Selektiramo input za pretragu
const searchInput = document.querySelector('.search-input');

// Slušamo događaj 'input' za pretragu
searchInput.addEventListener('input', function () {
    const searchTerm = searchInput.value.toLowerCase(); // Unos korisnika (smanjen na mala slova za lakše pretraživanje)
    
    // Selektiramo sve koktele
    const cocktails = document.querySelectorAll('.cocktail-card');
    
    // Prolazimo kroz svaki koktel i provjeravamo odgovara li pretrazi
    cocktails.forEach(cocktail => {
        const cocktailName = cocktail.querySelector('h2').textContent.toLowerCase(); // Uzimamo ime koktela i pretvaramo u mala slova
        
        // Provjeravamo odgovara li ime koktela unesenom terminu
        if (cocktailName.includes(searchTerm)) {
            cocktail.style.display = 'block'; // Prikaži koktel ako odgovara pretrazi
        } else {
            cocktail.style.display = 'none'; // Sakrij koktel ako ne odgovara
        }
    });
});

document.addEventListener("DOMContentLoaded", () => {
  const buttons = document.querySelectorAll(".view-recipe-btn");

  buttons.forEach((button) => {
    button.addEventListener("click", (e) => {
      const card = e.target.closest(".cocktail-card");
      const details = card.querySelector(".card-details");

      // Početna visina kartice, uključujući samo osnovni sadržaj
      const originalWidth = card.offsetWidth;

      if (details.classList.contains("hidden")) {
        // Prikazivanje detalja
        details.classList.remove("hidden");
        
        // Spremanje visine nakon što se detalji prikazuju
        const newWidth = card.offsetWidth + details.offsetWidth;
        card.style.maxWidth = `${newWidth}px`;
        
        button.textContent = "Sakrij recept";
      } else {
        // Sakrivanje detalja
        details.classList.add("hidden");
        
        // Vraćanje kartice na početnu visinu
        card.style.maxWidth = `${originalWidth}px`;

        button.textContent = "Pogledaj recept";
      }
    });
  });
}); //ODE SVE VALJA

// document.addEventListener("DOMContentLoaded", () => {
//   const buttons = document.querySelectorAll(".view-recipe-btn");

//   buttons.forEach((button) => {
//     button.addEventListener("click", (e) => {
//       const card = e.target.closest(".cocktail-card");
//       const details = card.querySelector(".card-details");

//       // Početna širina kartice
//       const originalWidth = card.offsetWidth;

//       if (details.classList.contains("hidden")) {
//         // Prikazivanje detalja
//         details.classList.remove("hidden");

//         // Širina kartice kad se detalji prikazuju (zauzima cijeli red)
//         card.style.width = '100%';
        
//         button.textContent = "Sakrij recept";
//       } else {
//         // Sakrivanje detalja
//         details.classList.add("hidden");

//         // Vraćanje kartice na početnu širinu
//         card.style.width = ${originalWidth}px;

//         button.textContent = "Pogledaj recept";
//       }
//     });
//   });
// });




function postFavourites(cocktails) {
  // Create the payload
  const payload = {
    //user: user,
    cocktails: cocktails
  };

  // Send the POST request
  fetch('/api/favourites/post', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json' // Specify the content type
    },
    body: JSON.stringify(payload) // Convert the payload to JSON
  })
    .then(response => response.json()) // Parse the JSON response
    .then(data => {
      // Handle the server response
      console.log('Server Response:', data);

      if (data.success) {
        //alert('Favourites successfully saved!');

      } else {
        alert('Failed to save favourites: ' + data.error);
      }
    })
    .catch(error => {
      // Handle any errors
      console.error('Error:', error);
      alert('An error occurred while saving favourites.');
    });
}




document.addEventListener("DOMContentLoaded", () => {
  const cocktailCards = document.querySelectorAll(".cocktail-card");
  const favourites = []; // Array to store favourites dynamically
  // Fetch the user's favourites from the server

  var dataUser;

  fetch("/api/favourites/get", { method: "GET" })
    .then(response => response.json())
    .then(data => {
      
      dataUser = data.username;
      if (!data.success) {
        
        console.error(data.error);
        return;
      }

      


      const serverFavourites = data.favourites; // Array of favourite cocktails

      // Iterate through each cocktail card and mark favourites from the server
      cocktailCards.forEach(card => {
        const cocktailName = card.querySelector("h2").textContent;

        // Check if the cocktail is in the server's favourites list
        if (serverFavourites.includes(cocktailName)) {
          let heartButton = card.querySelector(".heart-btn");
          if (!heartButton) {
            // Create heart button if it doesn't exist
            heartButton = document.createElement("button");
            heartButton.classList.add("heart-btn");
            heartButton.innerHTML = "&#9825;"; // Empty heart symbol
            card.appendChild(heartButton);
          }

          // Mark the heart button as liked
          heartButton.classList.add("liked");
          heartButton.innerHTML = "&#9829;"; // Filled heart
          favourites.push(cocktailName); // Sync with local favourites
        }
      });
    })
    .catch(error => console.error("Error fetching favourites:", error));

  // Add heart buttons dynamically and toggle favourites locally
  cocktailCards.forEach(card => {
    const cocktailName = card.querySelector("h2").textContent;

    let heartButton = card.querySelector(".heart-btn");
    if (!heartButton) {
      // Create the heart button if it doesn't exist
      heartButton = document.createElement("button");
      heartButton.classList.add("heart-btn");
      heartButton.innerHTML = "&#9825;"; // Empty heart symbol
      card.appendChild(heartButton);
    }

    // Add event listener for toggling favourites
    heartButton.addEventListener("click", () => {
        
      if (heartButton.classList.contains("liked")) {
        // Unmark as favourite
        heartButton.classList.remove("liked");
        heartButton.innerHTML = "&#9825;"; // Empty heart
        const index = favourites.indexOf(cocktailName);
        if (index > -1) {
          favourites.splice(index, 1); // Remove from the local favourites array
        }
      } else {
        // Mark as favourite
        if (dataUser !== "Guest"){
          heartButton.classList.add("liked");
          heartButton.innerHTML = "&#9829;"; // Filled heart
          favourites.push(cocktailName); // Add to the local favourites array
        }
        else{
          alert("Can't add to favourite cocktails, you are guest");

        }
      }

      // Optionally: Sync favourites with the server
      if (dataUser !== "Guest")
        postFavourites(favourites);
    });
  });
});
