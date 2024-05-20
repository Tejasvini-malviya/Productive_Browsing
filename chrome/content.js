function fetchDataFromBackend() {
    fetch('http://localhost:8000/all_urls_data/', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            // Add any necessary headers, such as authentication tokens
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log('Data from backend:', data);
        // Process the data as needed
    })
    .catch(error => console.error('Error fetching data:', error));
}

// Call the function to fetch data when needed
fetchDataFromBackend();
