window.onload = () => {
    document.getElementById('reg_form').addEventListener('submit', (e) => {
        e.preventDefault();

        form_data = new FormData(e.target);
        const password = form_data.get('reg-cpassword');
        const error_elem = document.getElementById('disp-error');


        if (form_data.get('reg-password') != password) {
            error_elem.innerHTML = '<p class="text-center fw-bold mx-3 mb-4 text-danger" id="disp-error">Passwords not same!</p>'
        } else if (password.length != 8) {
            error_elem.innerHTML = '<p class="text-center fw-bold mx-3 mb-4 text-danger" id="disp-error">Password Must contain 8 letters!</p>'
        }
        else {
            fetch('/auth/signup', {
                method: "POST",
                redirect: "follow",
                headers: { "Content-Type": "application/json", "Accept": "application/json" },
                body: JSON.stringify({ 'name': form_data.get('reg-username'), 'email': form_data.get('reg-email'), 'password': password })
            }).then(response => response.json())
                .then(data => {
                    if (data['status'] == 200) {
                        window.location.href = '/';
                    } else if (data['status'] == 300) {
                        error_elem.innerHTML = '<p class="text-center fw-bold mx-3 mb-4 text-danger" id="disp-error">Existing User!</p>'
                    } else {
                        console.log('Failure')
                    }
                });

        }

    });
};


