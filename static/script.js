const URL_predict = 'http://127.0.0.1:8000/predict'
const URL_about = 'http://127.0.0.1:8000/about'

let quantity = document.querySelector('.quantity_input input')
let drawback = document.querySelector('.drawback_input input')
let foreign_country = document.querySelector('.foreign_country_input select')
let category_item = document.querySelector('.category_item_input select')
let btn = document.querySelector('.predict_output')
let results = document.querySelector('.results')
let btn1 = document.querySelector('.about_output')

async function get_payload() {
    let quantity_value = quantity.value;
    let drawback_value = drawback.value;
    let foreign_country_value = foreign_country.value;
    let category_item_value = category_item.value;
    const payload = {
        "quantity": quantity_value,
        "drawback": drawback_value,
        "foreign_country": foreign_country_value,
        "categories": category_item_value
    }
    if (quantity_value == '') {
        alert('please fill the quantity value');
    } else if (drawback_value == '') {
        alert('please fill the drawback value');
    } else if (drawback_value>=314727) {
        alert('drawback value should be less than 314k');
    } else if (quantity_value>=60000) {
        alert('drawback value should be less than 60k');
    } else {
        try{
            let response_predict = await fetch(URL_predict,{
                method:'POST',
                headers:{
                    'Content-type':'application/json'
                },
                body:JSON.stringify(payload)
            })

            if(!response_predict.ok){
                console.log('invalid request');
                return;
            }

            let data_predict = await response_predict.json();
            results.innerText = data_predict.predicted_category;
        }catch(err){
            console.log(err);
        }
    }

};

btn1.addEventListener('click', async () => {
    // guard clause 
    let response = await fetch(URL_about)
    if (!response.ok){
        console.log('Not valid request')
        return;
    }
    
    let data = await response.json();
    results.innerText = data.message;
})
btn.addEventListener('click', get_payload)
