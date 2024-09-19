import control_form from "../../js/form_control.js";

document.addEventListener('DOMContentLoaded', function() {
    const inputs = document.querySelectorAll('input, textarea, select');
    let original_data = {}
    inputs.forEach(input => {
        original_data[input.name] = input.value;
    });
    control_form(original_data)

})

