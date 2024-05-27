import streamlit as st
import boto3
import uuid

# Initialize DynamoDB client with AWS credentials
aws_access_key_id = 'Aws_access_key'
aws_secret_access_key = 'Aws_secret_key'
region_name = 'ap-south-1'

dynamodb = boto3.resource(
    'dynamodb',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

# Get reference to the DynamoDB table
table = dynamodb.Table('Trend')

# Streamlit UI components
st.title('Post Composer')

# Input field for text content
post_content = st.text_area('Compose your post:', height=100)

# Input field for hashtags
hashtags = st.text_input('Add hashtags (comma-separated):')

# Button to submit the post
if st.button('Publish'):
    # Process the post and hashtags
    post_data = {
        'post_id': str(uuid.uuid4()), 
        'content': post_content,
        'hashtags': [tag.strip() for tag in hashtags.split(',')]
    }
    
    # Store the post in DynamoDB
    table.put_item(Item=post_data)
    
    # Clear input fields after submission
    post_content = ''
    hashtags = ''

    # Display success message
    st.success('Post published successfully!')

st.title('Trending Hashtags')

# Query DynamoDB table to fetch trending hashtags
response = table.scan()

# Extract hashtags from items and count occurrences
hashtags_count = {}
for item in response['Items']:
    for hashtag in item['hashtags']:
        hashtags_count[hashtag] = hashtags_count.get(hashtag, 0) + 1

# Sort hashtags by count in descending order
sorted_hashtags = sorted(hashtags_count.items(), key=lambda x: x[1], reverse=True)

# Display top 3 trending hashtags
st.write("Top 3 Trending Hashtags:")
for hashtag, count in sorted_hashtags[:3]:
    st.write(f"{hashtag}: {count} posts")
