# Converting from Arabic numerals or "decimals" to Roman numerals

## Requirements
- **Req-1:** When starting the system, a welcome message should be displayed on the screen. 
- **Req-2:** The system should request to press **enter** after presenting the welcome message.
- **Req-3:** The system must allow the entry of Arabic or decimal numbers up to 5000.50.
- **Req-4:** The system will validate decimal numbers using a period (.).
- **Req-5:** When entering a text or character input with the exception of the dot (.), the system should display an **Invalid Input** message.
- **Req-6:** The system must avoid sending empty fields.
- **Req-7:** The system must convert Arabic or decimal numbers to Roman numerals.
    ![Romans Numbers](https://espaciociencia.com//wp-content/uploads/numeros-romanos-origen.jpg) \
    - **key symbols** \
     "M", "MM", "MMM", "I!V", "!V" \
     "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM" \
     "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC" \
     "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"
- **Req-8:** At the end of the conversion, the system should ask if you want to continue making conversions or exit.
- **Req-9:** The system must validate that the response input of the requirement: **Req-8** is **S** to continue making conversions or **Any key** to exit.
- **Req-10:** Upon completion, the system should display the following message: **See you later**
- **Req-11** The system must validate the NO entry of negative numbers.
## Criteria of acceptance
- **Cri-1-1:** The system should display a welcome message.
- **Cri-2-1:** After the welcome message, the system must request to press **enter** and clear the screen.
- **Cri-2-2:** The system must stabilize while waiting for the acceptance criterion number : **Cri-2-1** to start the data entry process.
- **Cri-3-1:** The system must allow the entry of Arabic or decimal numbers up to 5000.50.
- **Cri-3-2:** If the number entered in the input is greater than 5000.50, it should display the following message: **The number entered is out of range**
- **Cri-4-1:** The system must validate the decimal numbers by means of a point (.), otherwise when sending the entry it will throw an **Invalid Entry** message.
- **Cri-5-1:** When entering a text or character input with the exception of the dot (.), the system will display an **Invalid Input** message.
- **Cri-6-1:** When submitting an empty entry, the system will display a **You must fill in the field to perform the conversion** message.
- **Cri-7-1:** The system must convert decimal numbers to natural or Arabic numbers using a rounding function.
- **Cri-7-2:** The system must convert natural numbers to Roman numerals.
- **Cri-7-3:** The system must validate that a negative number or zero (0) is not sent, otherwise it must display the following message: **Invalid input:** **The number entered is out of range**.
- **Cri-8-1:** When presenting the result of the conversion, the system should ask if you want to continue making conversions or exit.
- **Cri-9-1:** The answer to criterion number: **Cri-8-1** must be **S** or  **Any key**.
- **Cri-9-2:** If the answer to criterion number: **Cri-9-1** is  **Any key**, the system must end.
- **Cri-9-3:** If the answer to criterion number: **Cri-9-1** is **S**, the screen must be cleared and a number requested for conversion again.
- **Cri-10-1:** The system should display the message: **See you later** at the end.
- **Cri-11-1:** When sending a negative number, the system should display the following message: **Invalid Entry**.

## Test cases
### End-To-End (From the UI)
- **CP-01:** Verify that the text is aligned to the left.
- **CP-02:** Verify that there is a space between the text and the data input.
- **CP-03:** Verify that the screen after the welcome message or the answer to the question asking if you want to continue making conversions is cleared.
### Unit Tests
- **UT-01:** Input of texts and characters with the exception of the dot (.) in the number input field for conversion. 
  - **Response:** Invalid Input 
- **UT-02:** Entry of Arabic numbers greater than 5000.50. 
  - **Response:** The number entered is out of range
- **UT-03:** Leave the data entry field empty. 
  - **Response:** You must fill in the field to perform the conversion
- **UT-04:** Entering  numbers in the data entry field: **Continue making conversions**. 
  - **Response:** Invalid Entry
- **UT-05:** Input of negative numbers. 
  - **Response:** Invalid Entry
