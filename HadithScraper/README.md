
# Hadith Scraper

This is a Python-based Hadith Scraper that allows you to fetch and verify Hadiths from [Sunnah.com](https://sunnah.com/). It fetches the Hadith content, including Arabic text, English translation, reference details, and more. The script is designed to extract Hadith details from specific books like Sahih Bukhari, Sahih Muslim, Musnad Ahmad, and others.

## Features

- Fetches Hadith details (Arabic and English translation) from [Sunnah.com](https://sunnah.com/)
- Supports popular Hadith collections like **Sahih Bukhari**, **Sahih Muslim**, **Musnad Ahmad**, etc.
- Retrieves additional Hadith information like references and annotations.
- Handles errors gracefully, providing feedback when the Hadith number or input format is incorrect.

## Installation

To get started, clone this repository to your local machine:

```bash
git clone https://github.com/abdulmuizz0903/Hadith-Verification-TG-Bot.git
```

### Dependencies

The script relies on the following Python libraries:

- `requests`
- `beautifulsoup4`

You can install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### Usage

The scraper is designed to extract Hadith details from a specified book and Hadith number. You can use the `verify_hadith()` function to get the details.

#### Example

```python
from scraper import verify_hadith

# Example: Verify a Hadith from Sahih Bukhari, Hadith 1035
result = verify_hadith('bukhari', '1035')
print(result)
```

### Function: `verify_hadith(book, hadith)`

- `book`: The name of the book (e.g., 'bukhari', 'muslim', 'ahmad').
- `hadith`: The Hadith number to be verified (e.g., '1035').

This function returns the Hadith details, including references, Arabic text, English translation, and more. If the Hadith does not exist or there is an error, it will return an error message.

### Error Handling

The scraper includes error handling for the following scenarios:
- Incorrect Hadith number
- Invalid input format
- Missing Hadith data for specific books (e.g., Sahih Muslim not available for Hadith numbers above 3033)

## Contributing

If you'd like to contribute to this project, feel free to fork the repository, submit a pull request, or report any issues you encounter.

## License

This project is open-source and available under the MIT License.

## Contact

For support or inquiries, feel free to reach out to me at [saeedabdulmuizz@gmail.com](mailto:saeedabdulmuizz@gmail.com)
