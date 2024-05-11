
# Social Media Insights Application
# Introduction
In today's social media-driven world, staying updated on trending topics is crucial for users seeking meaningful engagement. The Social Media Insights Application aims to address this need by providing a platform where users can compose and publish posts while also gaining insights into trending hashtags. This README file serves as a guide to understand the application's features, setup instructions, and usage guidelines.
 
# Features
1.Post Composition: Users can compose posts containing text and hashtags using the intuitive interface.

2.Post Submission: Upon clicking the "Post" button, the application sends the post content to AWS Lambda for processing.

3.AWS Lambda Integration: AWS Lambda parses the post content, extracts hashtags and post text, and stores the data in DynamoDB.

4.Trending Hashtags: Users can explore trending hashtags by clicking the "Show Trending Hashtags" button. The application analyzes the DynamoDB table to identify popular hashtags.

5.Dynamic Updates: The trending hashtags section updates in real-time as new posts are submitted and analyzed, providing users with timely insights.

6.User Interface: The application offers an intuitive and user-friendly interface, ensuring a seamless user experience for composing posts and discovering trending topics.

# Problem Scope
The Social Media Insights Application encompasses the following key aspects:

Development of a Streamlit application enabling users to compose and publish posts with text and hashtags.

Integration with AWS Lambda for post processing and storage of data in DynamoDB.

Implementation of functionality to analyze the DynamoDB table and identify trending hashtags.

Real-time updates of trending hashtags as new posts are submitted, ensuring users receive up-to-date insights.

# Success Criteria
The success of the Social Media Insights Application is measured against the following criteria:

Users can compose and publish posts using the application interface.

Posts are accurately processed by AWS Lambda and stored in DynamoDB, preserving the integrity of post text and hashtags.

The application correctly identifies and displays trending hashtags based on analysis of the DynamoDB table.

Trending hashtags update dynamically in real-time as new posts are submitted, providing users with current insights.

# Usage Instructions

To use the Social Media Insights Application, follow these steps:

Setup AWS Services: Ensure that you have an AWS account and set up AWS Lambda and DynamoDB according to the provided configuration.

Install Dependencies: Install the required dependencies.

Run the Application: Start the Streamlit application by running streamlit run app.py in your terminal.

Compose Posts: Use the provided interface to compose posts containing text and hashtags.

Submit Posts: Click the "Publish" button to submit your post. The application will trigger the backend process for post processing.

Explore Trending Hashtags: It will show top 3 trending hashtags based on analysis of the DynamoDB table.
