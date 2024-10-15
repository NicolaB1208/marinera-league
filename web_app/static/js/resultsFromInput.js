let nameInput = document.getElementById('nameInput');

    nameInput.addEventListener('input', async function() {
        console.log(nameInput.value)
        let response = await fetch('/searchname?name=' + nameInput.value);
        let person_results = await response.json();
        console.log(typeof person_results);
        console.log(person_results)
        let html = '';
        
        // Assuming person_results is your main object
        for (let key in person_results) {
            // Check if the first-level key ends with '_couples'
            if (key.endsWith('_couples')) {
                console.log(`Found key: ${key}`);
                
                // Access the array inside the matching key
                let couplesArray = person_results[key][0]; 
                let fase = '';

                // Loop through the objects inside the array
                for (let i = 0; i < couplesArray.length; i++) {
                    if (key.startsWith('eliminatoria')) {
                        fase = 'eliminatoria'
                    }
                    else if (key.startsWith('semifinal')) {
                        fase = 'semifinal'
                    } else {
                        fase = 'final'
                    }
                    let category = couplesArray[i].category.replace('<', '&lt;').replace('&', '&amp;').replace('alma_de_marinera', 'alma de marinera');
                    let names = couplesArray[i].names.replace('<', '&lt;').replace('&', '&amp;');
                    let total_score = couplesArray[i].total_score.replace('<', '&lt;').replace('&', '&amp;');
                    let qualified = couplesArray[i].qualified.replace('<', '&lt;').replace('&', '&amp;').replace('11', 'PRIMERO').replace('12', 'SEGUNDO').replace('13', 'TERCERO').replace('1', 'CALIFICADO').replace('0', 'NO CALIFICADO').replace('2','NO PRESENTADO');
                    html +=                         
                                '<tr>' +
                                '<td>' + fase + '</td>' +
                                '<td>' + category + '</td>' +
                                '<td>' + names + '</td>' +                            
                                '<td>' + total_score + '</td>' +
                                '<td>' + qualified + '</td>'+
                                '</tr>';                
                }                          
            } else {
                let singleArray = person_results[key][0]; 
                let fase = '';
                for (let i = 0; i < singleArray.length; i++) {
                    if (key.startsWith('eliminatoria')) {
                        fase = 'eliminatoria'
                    }
                    else if (key.startsWith('semifinal')) {
                        fase = 'semifinal'
                    } else {
                        fase = 'final'
                    }
                    let category = singleArray[i].category.replace('<', '&lt;').replace('&', '&amp;').replace('alma_de_marinera', 'alma de marinera');
                    let name = singleArray[i].name.replace('<', '&lt;').replace('&', '&amp;');
                    let total_score = singleArray[i].total_score.replace('<', '&lt;').replace('&', '&amp;');
                    let qualified = singleArray[i].qualified.replace('<', '&lt;').replace('&', '&amp;').replace('11', 'PRIMERO').replace('12', 'SEGUNDO').replace('13', 'TERCERO').replace('1', 'CALIFICADO').replace('0', 'NO CALIFICADO').replace('2','NO PRESENTADO');
                    html +=                         
                                '<tr>' +
                                '<td>' + fase + '</td>' +
                                '<td>' + category + '</td>' +
                                '<td>' + name + '</td>' +                            
                                '<td>' + total_score + '</td>' +
                                '<td>' + qualified + '</td>'+
                                '</tr>';                
                }  

            }
        }
        document.querySelector('#tablenamesearch tbody').innerHTML = html;

    });