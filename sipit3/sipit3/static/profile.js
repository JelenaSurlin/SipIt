document.addEventListener("DOMContentLoaded", () => {

    // Fetch the user's favourites from the server
    fetch("/api/favourites/get", { method: "GET" })
      .then(response => response.json())
      .then(data => {
        if (!data.success) {
          console.error(data.error);
          return;
        }

        console.log(data.username);
  
      const container = document.getElementById("info-div");

      // Create and display the username
      const userDiv = document.createElement("p");
      userDiv.classList.add("username-style");
      userDiv.innerHTML = `<span class = "user-style">Korisnik: </span> ${data.username}`;
      container.appendChild(userDiv);

      // Create and display the favorites heading
      const favouritesHeading = document.createElement("p");
      favouritesHeading.classList.add("username-style");
      favouritesHeading.innerHTML = `<span class = "user-style">Omiljeni kokteli:</span>`;
      container.appendChild(favouritesHeading);

      // Create and display the list of favorite cocktails
      const favouritesList = document.createElement("ul"); // Use an unordered list for neat display
      favouritesList.classList.add("list-style");
      data.favourites.forEach(cocktail => {
          const listItem = document.createElement("li");
          listItem.textContent = cocktail;
          favouritesList.appendChild(listItem);
      });

      favouritesHeading.appendChild(favouritesList);

    // Append the list to the container

    //     // Iterate through each cocktail card and mark favourites
    //     cocktailCards.forEach(card => {
    //       const cocktailName = card.querySelector("h2").textContent.toLowerCase(); // Normalize card name
    //       if (favourites.includes(cocktailName)) {
    //         // If the cocktail is in favourites, display it
    //         card.style.display = "block";
    //         console.log(`Showing favourite: ${cocktailName}`);
    //       } else {
    //         // Hide the card if it's not a favourite
    //         card.style.display = "none";
    //       }
    //     });
    //   })
    })
      .catch(error => console.error("Error fetching favourites:", error));
  });
  



