/* ============================
   1. LOGIN FUNCTION
   ============================ */
function login() {
    let csrf = document.getElementById('csrf').value;
    let username = document.getElementById('loginUsername').value;
    let password = document.getElementById('loginPassword').value;

    if (username == '' || password == '') {
        alert('You must enter both username and password');
        return; 
    }

    let data = {
        'username': username,
        'password': password
    };

    fetch('/api/login_api/', { 
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf
        },
        body: JSON.stringify(data)
    })
    .then(result => result.json())
    .then(response => {
        console.log("Server Response:", response);
        
        if (response.status === 200) {
            window.location.href = "/"; 
        } else {
            alert(response.message); 
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

