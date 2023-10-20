# YouTube Comment Search API

## Overview

The YouTube Comment Search API is designed to help you find and filter comments from YouTube videos efficiently. It allows you to perform searches based on various criteria such as author name, date range, likes, replies, and specific text within comments. This API simplifies the process of retrieving comments for analysis, research, or any application that requires access to YouTube comments.

## Table of Contents

- [Getting Started](#getting-started)
- [Features](#features)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Examples](#examples)
- [Contributing](#contributing)


## Getting Started

Follow these steps to get started with the YouTube Comment Search API:

### Installation

1. Clone this repository.
2. Install the required dependencies using `npm install`.
3. Start the API server with `npm start`.

### Configuration

To configure your API, set environment variables as needed. This may include specifying API keys or other credentials.

## Features

The YouTube Comment Search API offers several features that make it stand out:

- **Search by Author**: Find comments by a specific author.
- **Date Range**: Search for comments within a specific date range.
- **Like and Reply Filtering**: Filter comments based on likes and replies.
- **Text Search**: Search for comments containing specific text.
- **Multiple Filters**: Combine filters within a single request.

## Usage

The API is straightforward to use. Here are some examples of how to interact with it:

## API Endpoints

The API provides several endpoints to serve your needs. Each endpoint has a specific purpose and accepts certain parameters.

### `GET /search`

This endpoint is used for searching comments. It allows you to search comments based on author name, date range, like count range, reply count range, and specific text.

- **Parameters**:
  - `search_author`: Search comments by author name.
  - `at_from` / `at_to`: Filter comments within a date range.
  - `like_from` / `like_to`: Filter comments within a like range.
  - `reply_from` / `reply_to`: Filter comments within a reply range.
  - `search_text`: Search comments containing specific text.
- **Response**: JSON array of matching comments.

## Examples

Here are some example requests to the API:

### Searching for Comments by Author
```http
GET /search?search_author=JohnDoe
```
## Contributing

If you would like to contribute to this project, we welcome your contributions! Please follow our contributing guidelines for instructions.
