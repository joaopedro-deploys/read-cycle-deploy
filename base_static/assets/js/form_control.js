const control_form = (original_data) =>{

    function checkFormChanges(event) { // check if form is changed, to htmx send AJAX
        const form = event.target;
        const originalValues = original_data;
        const inputs = form.querySelectorAll('input, textarea, select');

        let formChanged = false;

        inputs.forEach(input => {
            if (input.value !== originalValues[input.name]) {
                formChanged = true;
            }
        });
        if (formChanged) {
            return;
        }

        event.preventDefault();
        alert('Edite alguma inforamação antes de enviar');
    }

    document.addEventListener('htmx:beforeRequest', function(event) {
        const form_element = document.querySelector('#user-edit-form')
        if (event.target.matches('#user-edit-form')) {
            checkFormChanges(event);
        }
    });                       
}

export default control_form