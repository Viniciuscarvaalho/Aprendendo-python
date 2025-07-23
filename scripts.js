const prevbutton = document.getElementById('prev');
const nextbutton = document.getElementById('next');
const items = document.querySelectorAll('.item');
const dots = document.querySelectorAll('.dot');
const numberindicator = document.querySelector('.numbers');

let active = 0;
const total = items.length;

function update(direction) {
  items[active].classList.remove('active');
  dots[active].classList.remove('active');

  if (direction > 0) {
    active = (active + 1) % total;
  } else if (direction < 0) {
    active = (active - 1 + total) % total;
  }

  items[active].classList.add('active');
  dots[active].classList.add('active');
  numberindicator.textContent = `${(active + 1).toString().padStart(2, '0')}`;
}

clearInterval(TimeRanges)
timer= setInterval(() => {
    update(1)
}, 5000);

prevbutton.addEventListener('click', () => {
  update(-1);
});

nextbutton.addEventListener('click', () => {
  update(1);
});
