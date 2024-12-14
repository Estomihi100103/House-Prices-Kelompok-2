document.getElementById('predictionForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const formData = {
        'OverallQual': document.getElementById('overallQual').value,
        'GrLivArea': document.getElementById('grLivArea').value,
        'GarageCars': document.getElementById('garageCars').value,
        'GarageArea': document.getElementById('garageArea').value,
        'TotalBsmtSF': document.getElementById('totalBsmtSF').value,
        '1stFlrSF': document.getElementById('firstFlrSF').value,
        'FullBath': document.getElementById('fullBath').value,
        'TotRmsAbvGrd': document.getElementById('totRmsAbvGrd').value,
        'YearBuilt': document.getElementById('yearBuilt').value,
        'YearRemodAdd': document.getElementById('yearRemodAdd').value
    };

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        const priceElement = document.getElementById('priceText');
        priceElement.textContent = `$ ${data.predicted_price.toLocaleString('id-ID')}`;
    })
    .catch(error => {
        console.error('Error:', error);
        const priceElement = document.getElementById('priceText');
        priceElement.textContent = 'Gagal melakukan prediksi';
        priceElement.classList.add('text-red-500');
    });
});
