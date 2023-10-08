import requests
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search_comments():
    # Get query parameters from the request URL
    search_author = request.args.get('search_author')
    at_from = request.args.get('at_from')
    at_to = request.args.get('at_to')
    like_from = request.args.get('like_from')
    like_to = request.args.get('like_to')
    reply_from = request.args.get('reply_from')
    reply_to = request.args.get('reply_to')
    search_text = request.args.get('search_text')

    # Define the base URL of the existing API
    base_url = 'https://app.ylytic.com/ylytic/test'

    # Build the request URL with query parameters
    params = {
        'search_author': search_author,
        'at_from': at_from,
        'at_to': at_to,
        'like_from': like_from,
        'like_to': like_to,
        'reply_from': reply_from,
        'reply_to': reply_to,
        'search_text': search_text
    }

    try:
        # Send a GET request to the existing API
        response = requests.get(base_url, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response if the API returns JSON data
            data = response.json()

            # Apply filters to the response based on search criteria
            filtered_data = []
            # return jsonify(data["comments"])

            for comment in data["comments"]:
                # Filter by author name
                # print("comment",data)
                if search_author and search_author.lower() not in comment['author'].lower():
                    continue

                # Filter by date range
                comment_date_str = comment['at']
                comment_date = datetime.strptime(comment_date_str, '%a, %d %b %Y %H:%M:%S GMT')
                formatted_date = comment_date.strftime('%d-%m-%Y')
                # print(formatted_date)

                # Filter by date range
                if at_from and at_to:
                    from_date = datetime.strptime(at_from, '%d-%m-%Y')
                    to_date = datetime.strptime(at_to, '%d-%m-%Y')
                    if not (from_date <= comment_date <= to_date):
                        continue

                # Filter by like count range
                if like_from and like_to:
                    like_count = int(comment['like'])
                    if not (int(like_from) <= like_count <= int(like_to)):
                        continue

                elif like_from:
                    like_count = int(comment['like'])
                    if not (int(like_from) <= like_count):
                        continue

                elif like_to:
                    like_count = int(comment['like'])
                    if not (like_count <= int(like_to)):
                        continue


                # Filter by reply count range
                if reply_from and reply_to:
                    reply_count = int(comment['reply'])
                    if not (int(reply_from) <= reply_count <= int(reply_to)):
                        continue

                elif reply_from:
                    reply_count = int(comment['reply'])
                    if not (int(reply_from) <= reply_count):
                        continue

                elif reply_to:
                    reply_count = int(comment['reply'])
                    if not (reply_count <= int(reply_to)):
                        continue


                # Filter by search text
                if search_text and search_text.lower() not in comment['text'].lower():
                    continue

                # If the comment passed all filters, add it to the filtered_data list
                filtered_data.append(comment)

            return jsonify(filtered_data)

        else:
            return jsonify({'error': 'API request failed'})


    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/')
def hello_world():
    return 'This is my first API call!'