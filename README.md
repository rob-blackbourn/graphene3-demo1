# graphene3-demo1

A demo of query, mutation, and subscription in Graphene v3 using twitter.

## Prerequisites

You will need Python 3.8, and probably a Linux box (I haven't tried this with windows).

You will need [poetry](https://python-poetry.org/) installed.

You will need a Twitter developer account.

In the Twitter developer portal create a new project and generate the authentication tokens.

Grant your project full access to everything and make a note of the tokens and secrets.

## Installation

Clone the project from github then install the project and dependencies.

```bash
~ $ git clone https://github.com/rob-blackbourn/graphene3-demo1.git
~ $ cd graphene3-demo1
~/graphene3-demo1 $ python3.8 -m venv .venv
~/graphene3-demo1 $ . .venv/bin/activate
(.venv) ~/graphene3-demo1 $ poetry install
```

## Usage

Set up the environment variables from your twitter development account and run the server.

```bash
(.venv) ~/graphene3-demo1 $ APP_KEY="*******************",
(.venv) ~/graphene3-demo1 $ APP_KEY_SECRET="*************************************************",
(.venv) ~/graphene3-demo1 $ ACCESS_TOKEN="**************************************************",
(.venv) ~/graphene3-demo1 $ ACCESS_TOKEN_SECRET="**********************************************"
(.venv) ~/graphene3-demo1 $ start-server
```

Use the Chrome [altair](https://altair.sirmuel.design/) extension to explore the GraphQL api. The
query/mutation endpoint is `http://0.0.0.0:10001/graphql` and the subscription endpoint is
`ws://0.0.0.0:10001/subscriptions`.

Try this query to search tweets containing the word `"python"`:

```graphql
query {
  searchTweets(q: "python") {
    statuses {
      createdAt
      id
      text
      user {
        name
        screenName
      }
    }
    searchMetadata {
      completedIn
      query
      count
    }
  } 
}
```

Try this mutation to update your status.

```graphql
mutation {
  updateStatus(status: "This is not a tst") {
    createdAt
    id
    idStr
    text
    source
    truncated
    inReplyToStatusId
    inReplyToStatusIdStr
    inReplyToUserId
    inReplyToUserIdStr
    inReplyToScreenName
    user {
      name
      createdAt
    }
  } 
}
```

Try this subscription to monitor tweets about python:

```graphql
subscription {
  filter (track: ["python"]) {
    text
    user {
      name
      screenName
    }
  } 
}
```
