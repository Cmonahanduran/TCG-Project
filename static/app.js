const searchInput = document.querySelector("#search");
let allCardsData = null;

searchInput.addEventListener("input", (e) => {
    const value = e.target.value;
    
    const div = document.getElementById('filter_results');
    const filteredCards = [];
    
    for (let i = 0; i < allCardsData.length; i++) {
        //console.log(allCardsData[i].name);
        if (allCardsData[i].name.includes(value)) {
          filteredCards.push(allCardsData[i]);
        }
        // const html = createHTMLForm(data, i);
        // console.log(html);
        // div.insertAdjacentHTML('beforeend', html);
        //console.log(filteredCards[i].name);
    }


    //const filteredCards = Array.from(allCardsData).filter(checkName);
    //console.log(filteredCards);
    for (let i = 0; i < filteredCards.length; i++) {
        // const html = createHTMLForm(data, i);
        // console.log(html);
        // div.insertAdjacentHTML('beforeend', html);
        console.log(filteredCards[i].name);
    }
});




fetch("/all_cards", {
    headers: {
        'Accept': 'application/json',
        'Content-type': 'application/json',
    },
})
    .then(response => {
        //console.log(response);
        return response.json();
    })
    .then(data => {
        allCardsData = data.cards;
        //console.log(allCardsData);
    });



    // When making DOM divs give class so they can be removed and replaced
    // Replace with new filter results
    // possibly replace innerHTML each time
    //