window.onload = () => {
    const error_elem = document.getElementById('err-elem');
    document.getElementById('loginform').addEventListener('submit', (e) => {
        e.preventDefault();
        const form = new FormData(e.target);
        fetch('/auth/signin', {
            method: 'POST',
            redirect: "follow",
            headers: { "Content-Type": "application/json", "Accept": "application/json" },
            body: JSON.stringify({ 'email': form.get('email'), 'password': form.get('password') })
        }).then(response => response.json())
            .then(data => {
                if (data['status'] == 200) {
                    window.location.href = '/';
                } else if (data['status'] == 304) {
                    error_elem.innerHTML = '<p class="text-center fw-bold mx-3 mb-4 text-danger" id="disp-error">Incorrect Username/Password!</p>'
                } else {
                    console.log('Failure')
                }
            })
    })
}