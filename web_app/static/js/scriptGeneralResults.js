let categoryDropdown = document.getElementById('categorySelect');
let phaseDropdown = document.getElementById('phaseSelect');

// Function to handle changes from either dropdown
function handleDropdownChange() {
    let selectedCategory = categoryDropdown.value;
    let selectedPhase = phaseDropdown.value;

    // Make sure both dropdowns have a value selected
    if (selectedCategory && selectedPhase) {
        fetchResults(selectedCategory, selectedPhase);
    }
}

async function fetchResults(category, phase) {
    let response = await fetch(`/search?q=${category}&phase=${phase}`);
    let competition_results = await response.json();
    let html = '';
    if (category.startsWith('single')){
        for (let person_id in competition_results) {
                let couple_number = competition_results[person_id].couple_number.replace('<', '&lt;').replace('&', '&amp;');
                let category = competition_results[person_id].category.replace('<', '&lt;').replace('&', '&amp;').replace('alma_de_marinera', 'alma de marinera');
                let name = competition_results[person_id].name.replace('<', '&lt;').replace('&', '&amp;');
                let total_score = competition_results[person_id].total_score.replace('<', '&lt;').replace('&', '&amp;');
                let qualified = competition_results[person_id].qualified.replace('<', '&lt;').replace('&', '&amp;').replace('11', 'PRIMERO').replace('12', 'SEGUNDO').replace('13', 'TERCERO');
                html +=                         
                            '<tr>' +
                            '<td>' + category + '</td>' +
                            '<td>' + name + '</td>' +
                            '<td>' + couple_number + '</td>' +
                            '<td>' + total_score + '</td>' +
                            '<td>' + qualified + '</td>'+
                            '</tr>';
        }                    
    } else {
        for (let couple_id in competition_results) {
            let couple_number = competition_results[couple_id].couple_number.replace('<', '&lt;').replace('&', '&amp;');
            let category = competition_results[couple_id].category.replace('<', '&lt;').replace('&', '&amp;').replace('alma_de_marinera', 'alma de marinera');
            let names = competition_results[couple_id].names.replace('<', '&lt;').replace('&', '&amp;');
            let total_score = competition_results[couple_id].total_score.replace('<', '&lt;').replace('&', '&amp;');
            let qualified = competition_results[couple_id].qualified.replace('<', '&lt;').replace('&', '&amp;').replace('11', 'PRIMERO').replace('12', 'SEGUNDO').replace('13', 'TERCERO');
            html +=                         
                        '<tr>' +
                        '<td>' + category + '</td>' +
                        '<td>' + names + '</td>' +
                        '<td>' + couple_number + '</td>' +
                        '<td>' + total_score + '</td>' +
                        '<td>' + qualified + '</td>' +
                        '</tr>';    
        }
    }
    document.querySelector('tbody').innerHTML = html;
};

// Add event listeners to both dropdowns
categoryDropdown.addEventListener('change', handleDropdownChange);
phaseDropdown.addEventListener('change', handleDropdownChange);