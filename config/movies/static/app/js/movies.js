function slider() {
    const images = document.querySelectorAll('.slider .slider_line img');
    const sliderLine = document.querySelector('.slider_line');
    let count = 0;
    let width;


    function init() {
        console.log('resize');
        width = document.querySelector('.slider').offsetWidth;
        sliderLine.style.width = width * images.length + 'px';
        images.forEach(item => {
            item.style.width = width + 'px';
            item.style.height = 'auto';
        });
        rollSlider();

    }


    window.addEventListener('resize', init);
    init();

    document.querySelector('.slider_prev').addEventListener('click', function () {
        count--;
        if (count < 0) {
            count = images.length - 1;
        }
        rollSlider();
    });

    function rollSlider() {
        sliderLine.style.transform = 'translate(-' + count * width + 'px'
    }

    document.querySelector('.slider_next').addEventListener('click', function () {
        count++;
        if (count >= images.length) {
            count = 0;
        }
        rollSlider();
    });

    function rollSlider() {
        sliderLine.style.transform = 'translate(-' + count * width + 'px'
    }

};

slider();

//! ---------------------------------------------------------------------------------------------------------------

const images = document.querySelectorAll('.slider_2 .slider_line_2 img');
const sliderLine_2 = document.querySelector('.slider_line_2');
let count = 0;
let width;

function init() {
    console.log('resize');
    width = document.querySelector('.slider_2').offsetWidth;
    sliderLine_2.style.width = width * images.length + 'px';
    images.forEach(item => {
        item.style.width = width + 'px';
        item.style.height = 'auto';
    });
    rollSlider();

}

window.addEventListener('resize', init);
init();

document.querySelector('.slider_prev_2').addEventListener('click', function () {
    count--;
    if (count < 0) {
        count = images.length - 1;
    }
    rollSlider();
});

function rollSlider() {
    sliderLine_2.style.transform = 'translate(-' + count * width + 'px'
}

document.querySelector('.slider_next_2').addEventListener('click', function () {
    count++;
    if (count >= images.length) {
        count = 0;
    }
    rollSlider();
});

function rollSlider() {
    sliderLine_2.style.transform = 'translate(-' + count * width + 'px'
}

//todo ---------------------------------------------------------------------------------------------------------------

//! When the user clicks on the button, toggle between hiding and showing the dropdown content 
function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
}

//! Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
    if (!event.target.matches('.dropbtn_users')) {
  
      var dropdowns = document.getElementsByClassName("dropdown_users_content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }