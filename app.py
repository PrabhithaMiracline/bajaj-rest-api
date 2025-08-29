from flask import Flask, request, jsonify

app = Flask(__name__)

# Replace with your details
FULL_NAME = "Prabhitha Miracline M"
DOB = "09-08-2004"
EMAIL = "mprabhy@gmail.com"
ROLL_NUMBER = "22BCB0006"

@app.route("/bfhl", methods=["POST"])
def process_data():
    try:
        data = request.json.get("data", [])

        even_numbers = []
        odd_numbers = []
        alphabets = []
        special_characters = []
        concat_chars = []
        total_sum = 0

        for item in data:
            if item.isdigit():
                num = int(item)
                if num % 2 == 0:
                    even_numbers.append(item)
                else:
                    odd_numbers.append(item)
                total_sum += num
            elif item.isalpha():
                alphabets.append(item.upper())
                concat_chars.append(item)
            else:
                special_characters.append(item)

        concat_string = ""
        for i, ch in enumerate("".join(concat_chars)[::-1]):
            concat_string += ch.upper() if i % 2 == 0 else ch.lower()

        response = {
            "is_success": True,
            "user_id": f"{FULL_NAME}_{DOB}",
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(total_sum),
            "concat_string": concat_string
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
