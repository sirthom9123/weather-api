const historyButton = document.getElementById('history-button')
const historyData = document.getElementById('history-data')

    historyButton.addEventListener('click', function (e) {
        e.preventDefault()
        if (historyData.style.display == 'none') {
            historyData.style.display = 'block';
           } else {
            historyData.style.display = 'none';
         }
    })