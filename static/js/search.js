const searchField = document.getElementById('searchField')

const tableOutput = document.getElementById('table-output')
const appTable = document.getElementById('app-table')
const paginationContainer = document.getElementById('pagination-container')

tableOutput.style.display = 'none'
const noResults = document.getElementById('no-results')
const tbody = document.getElementById('table-body')

searchField.addEventListener('keyup', (e) => {
  const searchValue = e.target.value

  if (searchValue.trim().length > 0) {
    paginationContainer.style.display = 'none'
    tbody.innerHTML = ''
    fetch('search-data/', {
      body: JSON.stringify({ searchText: searchValue }),
      method: 'POST',
    })
      .then((res) => res.json())
      .then((data) => {
        appTable.style.display = 'none'
        tableOutput.style.display = 'block'
        console.log(data)

        if (data.length === 0) {
          noResults.style.display = 'block'
          tableOutput.style.display = 'none'
        } else {
          noResults.style.display = 'none'
          data.forEach((item) => {
            date = new Date(item.created_date).toDateString()
            tbody.innerHTML += `
                <tr>
                <td>${item.location}</td>
                <td>${item.temperature}</td>
                <td>${item.humidity}</td>
                <td>${item.wind}</td>
                <td>${item.description}</td>
                <td>${date}</td>
                </tr>`
          })
        }
      })
  } else {
    tableOutput.style.display = 'none'
    appTable.style.display = 'block'
    paginationContainer.style.display = 'block'
  }
})
