// change simple dropdown  "contry code" to researchable dropdown
$(document).ready(function () {
    $('#id_country_code').select2({
        placeholder: "Select or search a country code",
        allowClear: true,
    });
});

//  enable the eye icon to toggle password visibility.
// document.addEventListener('DOMContentLoaded', function() {
//     const passwordInputs = document.querySelectorAll('.password-input');
    
//     passwordInputs.forEach(input => {
//         // Create wrapper div
//         const wrapper = document.createElement('div');
//         wrapper.className = 'password-toggle';
        
//         // Create eye icon
//         const icon = document.createElement('i');
//         icon.className = 'fas fa-eye';
        
//         // Insert wrapper and icon
//         input.parentNode.insertBefore(wrapper, input);
//         wrapper.appendChild(input);
//         wrapper.appendChild(icon);
        
//         // Toggle password visibility
//         icon.addEventListener('click', function() {
//             if (input.type === 'password') {
//                 input.type = 'text';
//                 icon.className = 'fas fa-eye-slash';
//             } else {
//                 input.type = 'password';
//                 icon.className = 'fas fa-eye';
//             }
//         });
//     });
// });

document.addEventListener('DOMContentLoaded', function () {
    const passwordFields = document.querySelectorAll('.password-input');
    passwordFields.forEach(field => {
        const wrapper = document.createElement('div');
        wrapper.style.position = 'relative';
        field.parentNode.insertBefore(wrapper, field);
        wrapper.appendChild(field);
        const toggle = document.createElement('span');
        toggle.innerHTML = '<i class="fa fa-eye"></i>'; // Eye icon
        toggle.style.position = 'absolute';
        toggle.style.right = '5px';
        toggle.style.top = '50%';
        toggle.style.transform = 'translateY(-50%)';
        toggle.style.cursor = 'pointer';
        toggle.addEventListener('click', () => {
            if (field.type === 'password') {
                field.type = 'text';
                toggle.innerHTML = '<i class="fa fa-eye-slash"></i>'
            } else {
                field.type = 'password';
                toggle.innerHTML = '<i class="fa fa-eye"></i>'
            }
        });
        
        wrapper.appendChild(toggle);
    });
});
