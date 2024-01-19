function generate4DigitNumber() {
    // Generate the random number
    const randomNumber = Math.floor(Math.random() * 9000) + 1000;

    // Ensure 4-digit string with leading zeros

    let numbafield = document.getElementById("numberField")
    numbafield.value = randomNumber
}
