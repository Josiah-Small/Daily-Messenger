# Daily AffirmationText Message Scheduler

## Description

This project is a Python-based application that fetches daily affirmations from an API and sends them as text messages using Twilio's messaging services. The application schedules the sending of daily affirmations at a specified time.

## Features

- **Fetch Daily Affirmations**: Retrieves daily affirmations from the `affirmations.dev` API.
- **Send Text Messages**: Uses Twilio to send the fetched affirmation as a text message to a specified phone number.
- **Scheduled Messaging**: Schedules the sending of daily affirmations at a specified time.

## Requirements

- Python 3.x
- `requests` library
- `twilio` library
- `schedule` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

2. Install the required libraries:
    ```sh
    pip install requests twilio schedule
    ```

## Usage

1. Replace the placeholder credentials in the script with your actual Twilio account SID, auth token, Twilio phone number, and client phone number:
    ```python
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    twilio_phone_number = 'your_twilio_phone_number'
    client_phone_number = 'your_client_phone_number'
    ```

2. Run the script:
    ```sh
    python affirmation_scheduler.py
    ```

3. The script will fetch daily affirmations and send them as text messages to the specified phone number at the scheduled time.

## File Structure

- `affirmation_scheduler.py`: The main script for fetching affirmations and sending them as text messages.

## Code Explanation

### `get_affirmation()`
- Fetches daily affirmations from the `affirmations.dev` API.
- Returns the affirmation if the API call is successful, otherwise returns an error message.

### `send_message()`
- Retrieves the daily affirmation using `get_affirmation()`.
- Sends the affirmation as a text message using Twilio's messaging service.
- Prints the message SID to confirm that the message was sent.

### Schedule Setup
- Schedules the `send_message()` function to run daily at 13:10.
- Continuously checks for pending scheduled tasks and executes them.

## License

This project is licensed under the MIT License.
