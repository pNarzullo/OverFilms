let offset = 0;  // смещение от левого края
const sliderLine = document.querySelector('.slider_line');

document.querySelector('.slider_next').addEventListener('click', function () {
    offset = offset + 512; // offset += 512
    if (offset > 1536) {
        offset = 0;
    }

    sliderLine.style.left = -offset + 'px';
});

document.querySelector('.slider_prev').addEventListener('click', function () {
    offset = offset - 512; // offset -= 512
    if (offset < 0) {
        offset = 1536;
    }
    sliderLine.style.left = -offset + 'px';
});

//! ---------------------------------------------------------------------------------------------------------------

const images = document.querySelectorAll('.slider_2 .slider_line_2 img');
const sliderLine_2 = document.querySelector('.slider_line_2');
let count = 0;
let width;

function init(){
    console.log('resize');
    width = document.querySelector('.slider_2').offsetWidth;
    sliderLine_2.style.width = width*images.length + 'px';
    images.forEach( item => {
        item.style.width = width + 'px';
        item.style.height = 'auto';
    });
    rollSlider();

}

window.addEventListener('resize', init);
init();

document.querySelector('.slider_prev_2').addEventListener('click', function(){
    count--;
    if (count < 0) {
        count = images.length -1;
    }
    rollSlider();
});

function rollSlider(){
    sliderLine_2.style.transform = 'translate(-'+count*width+'px'
}

document.querySelector('.slider_next_2').addEventListener('click', function(){
    count++;
    if (count >= images.length) {
        count = 0;
    }
    rollSlider();
});

function rollSlider(){
    sliderLine_2.style.transform = 'translate(-'+count*width+'px'
}
