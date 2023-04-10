// SUPERMARKET
document.getElementById('supermarket').addEventListener('click', function () {
    document.getElementById('supermarket_popup').style.display = 'block';
});

// RESIDENCIES
for (let i = 1; i <= 40; i++) {
    document.getElementById('house' + i).addEventListener('click', function () {
        document.getElementById('residencies_popup').style.display = 'block';
    });
}
for (let i = 1; i <= 10; i++) {
    document.getElementById('apartment' + i).addEventListener('click', function () {
        document.getElementById('residencies_popup').style.display = 'block';
    });
}

// PRAYER
for (let i = 1; i <= 3; i++) {
    document.getElementById('prayer_site' + i).addEventListener('click', function () {
        document.getElementById('prayer_popup').style.display = 'block';
    });
}

// BANK
document.getElementById('bank').addEventListener('click', function () {
    document.getElementById('bank_popup').style.display = 'block';
});

// DRUGSTORE
document.getElementById('drugstore').addEventListener('click', function () {
    document.getElementById('drugstore_popup').style.display = 'block';
});

// GYM
document.getElementById('gym').addEventListener('click', function () {
    document.getElementById('gym_popup').style.display = 'block';
});

// SCHOOL
for (let i = 1; i <= 2; i++) {
    document.getElementById('school' + i).addEventListener('click', function () {
        document.getElementById('school_popup').style.display = 'block';
    });
}
