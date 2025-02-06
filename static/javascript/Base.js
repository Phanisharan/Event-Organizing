document.addEventListener('DOMContentLoaded', function () {
  
    var backToTop = document.getElementById('back-to-top');
    var imageArrow = document.getElementById('image-arrow');


    window.addEventListener('scroll', function () {
        if (window.scrollY > window.innerHeight) {
            backToTop.style.display = 'block';
        } else {
            backToTop.style.display = 'none';
        }
    });


    if (imageArrow) {
        imageArrow.addEventListener('click', function () {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    } else {
        console.error("Element with ID 'image-arrow' not found.");
    }


  });
  