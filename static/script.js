const URL_predict = 'https://fractal-exportprice-predictor.onrender.com/predict'
const URL_about = 'https://fractal-exportprice-predictor.onrender.com/about'

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
            results.style.color = 'rgba(0, 255, 34, 1)';
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
    results.style.color = 'rgba(251, 255, 0, 1)';
    results.innerText = data.message;
})
btn.addEventListener('click', get_payload)

// Add navigation handling
const navItems = document.querySelectorAll('.nav-item');
const mainContent = document.querySelector('main');
const defaultContent = mainContent.innerHTML;

navItems.forEach(item => {
    item.addEventListener('click', () => {
        // Remove active class from all items
        navItems.forEach(nav => nav.classList.remove('active'));
        
        // Add active class to clicked item
        item.classList.add('active');
        
        const page = item.dataset.page;
        
        if (page === 'pricing') {
            // Show default prediction page
            mainContent.innerHTML = defaultContent;
            // Reattach event listeners
            attachEventListeners();
        } else {
            // Show work in progress for other pages
            mainContent.innerHTML = `
                <div class="wip-message">
                    <h2>Work in Progress</h2>
                    <p>This feature is currently under development.</p>
                </div>
            `;
        }
    });
});

// Function to reattach event listeners
function attachEventListeners() {
    quantity = document.querySelector('.quantity_input input');
    drawback = document.querySelector('.drawback_input input');
    foreign_country = document.querySelector('.foreign_country_input select');
    category_item = document.querySelector('.category_item_input select');
    btn = document.querySelector('.predict_output');
    results = document.querySelector('.results');
    btn1 = document.querySelector('.about_output');

    btn.addEventListener('click', get_payload);
    btn1.addEventListener('click', async () => {
        // guard clause 
        let response = await fetch(URL_about)
        if (!response.ok){
            console.log('Not valid request')
            return;
        }
        
        let data = await response.json();
        results.innerText = data.message;
    });
}

// Add chat functionality
const fractalInput = document.querySelector('.fractal-input');
const analysisContent = document.querySelector('.analysis-content');

fractalInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter' && fractalInput.value.trim() !== '') {
        const message = fractalInput.value;
        const messageEl = document.createElement('div');
        messageEl.classList.add('message');
        messageEl.textContent = message;
        analysisContent.appendChild(messageEl);
        fractalInput.value = '';
        analysisContent.scrollTop = analysisContent.scrollHeight;
    }
});
