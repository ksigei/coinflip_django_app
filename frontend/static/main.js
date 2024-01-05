// coinflip_project/coinflip_app/static/coinflip_app/js/main.js
document.addEventListener('DOMContentLoaded', function () {
    const coinContainer = document.getElementById('coin-container');
    const resultDisplay = document.getElementById('result-display');
    const flipButton = document.getElementById('coin-flip-button');

    flipButton.addEventListener('click', function () {
        const flipCount = getRandomInt(1, 10); // Adjust the range as needed

        flipCoin(flipCount);
    });

    function getRandomInt(min, max) {
        return Math.floor(Math.random() * (max - min + 1)) + min;
    }

    function flipCoin(flipCount) {
        let flipsRemaining = flipCount;

        function performFlip() {
            coinContainer.classList.add('flip'); // Add the flip class
            setTimeout(() => {
                fetch('/flip-coin/')
                    .then(response => response.json())
                    .then(data => {
                        resultDisplay.textContent = `Result: ${data.result}`;
                        flipsRemaining--;

                        if (flipsRemaining > 0) {
                            setTimeout(() => {
                                coinContainer.classList.remove('flip'); // Remove the flip class after the animation
                                performFlip(); // Perform the next flip after a delay
                            }, 500); // Adjust this delay based on your flip animation duration
                        } else {
                            coinContainer.classList.remove('flip'); // Remove the flip class after the last flip
                        }
                    })
                    .catch(error => {
                        console.error('Error:', error);
                    });
            }, 300); // Adjust this timeout based on your flip animation duration
        }

        performFlip(); // Start the first flip
    }
});
