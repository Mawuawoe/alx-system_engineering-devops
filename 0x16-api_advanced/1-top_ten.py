import requests

def top_ten(subreddit):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        try:
            r_json = r.json()
            posts = r_json.get('data', {}).get('children', [])
            
            if not posts:
                print("No posts found.")
            
            for post in posts:
                post_data = post.get('data', {})
                title = post_data.get('title', 'No Title')
                print("Post Data: {}".format(post_data))  # Debug: Print the entire post data
                print("Title: {}".format(title))  # Print the title
        except ValueError as e:
            print('Error parsing JSON: {}'.format(e))
    else:
        print('Failed to retrieve data. Status code: {}'.format(r.status_code))
        print('Response Text: {}'.format(r.text))  # Print the response text for debugging
