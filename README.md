# Exchange Rates API

This is a FastAPI app that provides exchange rates for different currencies.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/exchange-rates-api.git
    ```

2. Navigate to the project directory:

    ```bash
    cd exchange-rates-api
    ```

3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

      ```bash
      venv\Scripts\activate
      ```

    - On macOS and Linux:

      ```bash
      source venv/bin/activate
      ```

5. Copy the `.env.template` file and rename it to `.env`:

    ```bash
    cp .env.template .env
    ```

6. Open the `.env` file and fill in the `API_KEY` value.

7. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the FastAPI app:

    ```bash
    uvicorn main:app --reload
    ```

## Example Usage

### Endpoint for Currency Conversion

- **POST** `http://127.0.0.1:8000/api/convert`

#### Request Body:

```json
{
    "input_currency": "PLN",
    "output_currencies": ["EUR", "USD", "AMD"],
    "amount": 123.45,
    "date": "2022-08-24"
}
```

#### Response:

```json
[
    {
        "currency": "EUR",
        "amount": 25.89
    },
    {
        "currency": "USD",
        "amount": 25.81
    },
    {
        "currency": "AMD",
        "amount": 10446.14
    }
]
```