
$(document).ready(function() {
    alert('Welcome on ready, user.');
    
    $('a').addClass('bold');
    $('a').click(function(event) {
        event.preventDefault();
        $(this).hide('slow');

        // Note: an arrow function (() => {}) preserves enclosing scope, e.g., 'this' is preserved here.
        setTimeout(() => {
            $(this).show('slow');
        }, 2000);
    });
});

// Runs when all images and things are finished downloading.
window.onload = function() {
    alert('Welcome, user.');
}