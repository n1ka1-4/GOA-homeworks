const bill = document.getElementById('bill');
const custom = document.querySelectorAll('.custom');
const people = document.getElementById('people');
const totalPerPerson = document.getElementById('total-per-person');
const tipPerPerson = document.getElementById('tip-per-person');

let tip;

custom.forEach((button) => {
    button.addEventListener('click', () => {
        if (button.textContent.includes("%")) {
            tip = parseInt(button.textContent.replace("%", ""));
        } else {
            tip = parseInt(button.value);
        }
    });
});
bill.addEventListener('input', () => {
    totalPerPerson.textContent = `${((Number(bill.value) + (Number(bill.value) * tip / 100)) / Number(people.value)).toFixed(2)}`;
    tipPerPerson.textContent = `${((Number(bill.value) + (Number(bill.value) * tip / 100)) / Number(people.value) * tip / 100).toFixed(2)}`;
});
people.addEventListener('input', () => {
    totalPerPerson.textContent = `${((Number(bill.value) + (Number(bill.value) * tip / 100)) / Number(people.value)).toFixed(2)}`;
    tipPerPerson.textContent = `${((Number(bill.value) + (Number(bill.value) * tip / 100)) / Number(people.value) * tip / 100).toFixed(2)}`;
    console.log(tip)
});

setInterval(() => {
  if (bill.value === '' || people.value === '') {
    totalPerPerson.textContent = '0.00';
    tipPerPerson.textContent = '0.00';
  }
}, 0);
