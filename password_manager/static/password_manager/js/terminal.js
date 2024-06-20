function handleKeyPress(event) {
    if (event.key === 'Enter') {
        event.preventDefault();
        executeCommand();
    }
}

// Function to execute command and send it to the server
function executeCommand() {
    const inputField = document.getElementById('input-field');
    const command = inputField.value.trim();
    inputField.value = '';

    if (command) {
        // Display the user's command in the terminal
        const terminal = document.getElementById('terminal');
        const userCommandDiv = document.createElement('div');
        userCommandDiv.textContent = `$ ${command}`;
        terminal.appendChild(userCommandDiv);

        // Send the command to the server
        fetch('/password-manager/execute-command/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCsrfToken()
            },
            body: JSON.stringify({ command: command })
        })
        .then(response => response.json())
        .then(data => {
            displayOutput(data.output);
            // Automatically scroll to the bottom after displaying new output
            terminal.scrollTop = terminal.scrollHeight;
        })
        .catch(error => console.error('Error:', error));
    }
}

// Function to display server response
function displayOutput(output) {
    const outputContainer = document.getElementById('output-container');
    const newOutput = document.createElement('div');
    newOutput.textContent = output;
    newOutput.style.whiteSpace = 'pre'; // Preserve newlines
    outputContainer.appendChild(newOutput);
    // Automatically scroll to the bottom after displaying new output
    outputContainer.scrollTop = outputContainer.scrollHeight;
}

// Function to get the CSRF token
function getCsrfToken() {
    return document.querySelector('input[name=csrfmiddlewaretoken]').value;
}

// Function to initialize the terminal with the welcome message
function initializeTerminal() {
    fetch('/password-manager/execute-command/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCsrfToken()
        },
        body: JSON.stringify({ command: '' }) // Send an empty command to get the welcome message
    })
    .then(response => response.json())
    .then(data => {
        displayOutput(data.output);
    })
    .catch(error => console.error('Error:', error));

    // Initially focus the input field
    document.getElementById('input-field').focus();
}

// Initialize terminal on page load
initializeTerminal();
