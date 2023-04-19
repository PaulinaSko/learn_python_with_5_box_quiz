document.addEventListener("DOMContentLoaded", function (event) {
    // hamburger-menu
    const hamburgerMenu = document.querySelector('.hamburger-menu');
    const menu = document.querySelector('.menu');

    hamburgerMenu.addEventListener('click', () => {
        menu.classList.toggle('active');
    });

    // flashcard
    const knowButton = document.querySelectorAll('.i-know');

    if ( knowButton.length > 0 ) {
        [...knowButton].forEach((btn)=>{
            btn.addEventListener( 'click', function(e) {
                e.preventDefault()
                btn.closest('.flashcard').classList.add('to-back');
            });
        });
    }

    const nextButton = document.querySelectorAll('.next');

    if ( nextButton.length > 0 ) {
        [...nextButton].forEach((btn)=>{
            btn.addEventListener( 'click', function(e) {
                e.preventDefault()
                btn.closest('.flashcard').classList.remove('active');
                btn.closest('.flashcard').classList.add('not-active');

                if( btn.closest('.flashcard').nextElementSibling !== null ) {
                    btn.closest('.flashcard').nextElementSibling.classList.add('active');
                }
            });
        });
    }
});