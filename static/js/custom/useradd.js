document.getElementById('useradd').addEventListener('submit', async function(e){
    e.preventDefault();
    let error = document.getElementById('error');
    const form = new FormData(e.target);
    if (Number(form.get('phone').length) != 10){
        error.innerHTML = `<div class="alert alert-danger opacity-75 alert-dismissible fade show" id="alert" role="alert">
        Check Phone no!  <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>`
        return;
    } else if (form.get('password') != form.get('cpassword')) {
        error.innerHTML = `<div class="alert alert-danger opacity-75 alert-dismissible fade show" id="alert" role="alert">
        Password not same!  <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>`
        return;
    } else if (!!!(/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()-_=+{};:'",.<>\/?[\]`|])(?!.*\s).{8,}$/).test(form.get('password')) && form.get('password') != null){
        error.innerHTML = `<div class="alert alert-danger opacity-75 alert-dismissible fade show" id="alert" role="alert">
        Password must be strong!  <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>`
        return;
    };
    const data = {'id': form.get('id'), 'emp_no' : form.get('emp_no'),'name' : form.get('name'),'email' : form.get('email'),
                  'phone' : form.get('phone'),'password' : form.get('password')};
    await fetch('/users/add', {
        method: 'POST',
        headers: { "Content-Type": "application/json", 'Accept': 'application/json', 'X-CSRFToken': csrfToken },
        body : JSON.stringify(data)
    }).then(response => response.json())
    .then(data => {if (data['status'] == 200) {successToastText.innerHTML = data['text'];successToast.show();} 
                   else if (data['status'] == 300) {warningToastText.innerHTML = data['text'];warningToast.show();} 
                   else if (data['status'] == 400) {unsuccessToastText.innerHTML = data['text'];unsuccessToast.show();}
                   else if (data['status'] == 303) { window.location.href = '/users/list'}});
    e.target.reset();
    error.innerHTML = '';
});